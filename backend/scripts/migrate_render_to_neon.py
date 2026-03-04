"""
Migración directa Render PostgreSQL → Neon PostgreSQL via Python/SQLAlchemy.
No requiere pg_dump/psql.

Uso:
    cd backend
    python -m scripts.migrate_render_to_neon

Lee todas las tablas de Render, crea la estructura en Neon, e inserta los datos.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text, inspect, MetaData
from sqlalchemy.orm import sessionmaker

# ============ CONFIGURACIÓN ============
RENDER_URL = "postgresql://portfolio_db_yn9o_user:LsGcC9dHANi8uNg6V5C5nMjvn0SkjwtO@dpg-d6360lsoud1c73ckddj0-a.oregon-postgres.render.com/portfolio_db_yn9o"
NEON_URL = "postgresql://neondb_owner:npg_WHiNTD3XEMO6@ep-little-field-alveteyb-pooler.c-3.eu-central-1.aws.neon.tech/neondb?sslmode=require"
# =======================================


def migrate():
    print(f"\n{'='*60}")
    print(f"  MIGRACIÓN RENDER → NEON")
    print(f"{'='*60}")

    # 1. Conectar a Render (source)
    print(f"\n--- 1. Conectando a Render (source) ---")
    try:
        src_engine = create_engine(RENDER_URL, pool_pre_ping=True)
        with src_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(f"  ✓ Render conectado")
    except Exception as e:
        print(f"  ✗ ERROR conectando a Render: {e}")
        sys.exit(1)

    # 2. Conectar a Neon (destination)
    print(f"\n--- 2. Conectando a Neon (destination) ---")
    try:
        dst_engine = create_engine(NEON_URL, pool_pre_ping=True)
        with dst_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(f"  ✓ Neon conectado")
    except Exception as e:
        print(f"  ✗ ERROR conectando a Neon: {e}")
        sys.exit(1)

    # 3. Reflejar estructura de Render
    print(f"\n--- 3. Leyendo estructura de Render ---")
    src_meta = MetaData()
    src_meta.reflect(bind=src_engine)
    tables = list(src_meta.tables.keys())
    print(f"  Tablas encontradas: {', '.join(tables)}")

    if not tables:
        print(f"  ⚠ No hay tablas. Nada que migrar.")
        return

    # 4. Contar registros en source
    print(f"\n--- 4. Registros en Render ---")
    src_counts = {}
    with src_engine.connect() as conn:
        for table_name in tables:
            count = conn.execute(text(f'SELECT COUNT(*) FROM "{table_name}"')).scalar()
            src_counts[table_name] = count
            print(f"  {table_name}: {count}")

    # 5. Limpiar y crear tablas en Neon
    print(f"\n--- 5. Creando estructura en Neon ---")
    dst_meta_existing = MetaData()
    dst_meta_existing.reflect(bind=dst_engine)
    existing_tables = list(dst_meta_existing.tables.keys())

    if existing_tables:
        print(f"  Tablas existentes en Neon: {', '.join(existing_tables)}")
        print(f"  Eliminando tablas existentes...")
        with dst_engine.connect() as conn:
            for t in reversed(list(dst_meta_existing.sorted_tables)):
                conn.execute(text(f'DROP TABLE IF EXISTS "{t.name}" CASCADE'))
                print(f"    Dropped: {t.name}")
            conn.commit()

    src_meta.create_all(bind=dst_engine)
    print(f"  ✓ Tablas creadas en Neon")

    # 6. Copiar datos tabla por tabla
    print(f"\n--- 6. Copiando datos ---")
    BATCH_SIZE = 500

    # Insertion order: tables without FK first, then tables with FK
    src_inspector = inspect(src_engine)
    tables_no_fk = []
    tables_with_fk = []
    for table_name in tables:
        fks = src_inspector.get_foreign_keys(table_name)
        if fks:
            tables_with_fk.append(table_name)
        else:
            tables_no_fk.append(table_name)

    ordered_tables = tables_no_fk + tables_with_fk
    print(f"  Orden de inserción: {', '.join(ordered_tables)}")

    for table_name in ordered_tables:
        table = src_meta.tables[table_name]
        col_names = [c.name for c in table.columns]

        with src_engine.connect() as src_conn:
            rows = src_conn.execute(table.select()).fetchall()

        if not rows:
            print(f"  {table_name}: 0 registros (vacía)")
            continue

        with dst_engine.connect() as dst_conn:
            # Disable triggers on this table (handles FK without needing superuser)
            dst_conn.execute(text(f'ALTER TABLE "{table_name}" DISABLE TRIGGER ALL'))

            total = len(rows)
            inserted = 0
            for i in range(0, total, BATCH_SIZE):
                batch = rows[i:i + BATCH_SIZE]
                data = [dict(zip(col_names, row)) for row in batch]
                dst_conn.execute(table.insert(), data)
                inserted += len(batch)

            # Re-enable triggers
            dst_conn.execute(text(f'ALTER TABLE "{table_name}" ENABLE TRIGGER ALL'))

            # Reset sequence for auto-increment PK
            for col in table.columns:
                if col.primary_key and col.autoincrement:
                    try:
                        max_id = dst_conn.execute(
                            text(f'SELECT COALESCE(MAX("{col.name}"), 0) FROM "{table_name}"')
                        ).scalar()
                        dst_conn.execute(text(
                            f"SELECT setval(pg_get_serial_sequence('{table_name}', '{col.name}'), {max_id}, true)"
                        ))
                    except Exception:
                        pass  # Not all PKs have sequences

            dst_conn.commit()
            print(f"  ✓ {table_name}: {inserted} registros copiados")

    # 7. Verificar
    print(f"\n--- 7. Verificación ---")
    all_ok = True
    with dst_engine.connect() as conn:
        for table_name in tables:
            dst_count = conn.execute(text(f'SELECT COUNT(*) FROM "{table_name}"')).scalar()
            src_count = src_counts[table_name]
            match = "✓" if dst_count == src_count else "✗ MISMATCH"
            if dst_count != src_count:
                all_ok = False
            print(f"  {table_name}: Render={src_count} → Neon={dst_count} {match}")

    print(f"\n{'='*60}")
    if all_ok:
        print(f"  ✓ MIGRACIÓN COMPLETADA EXITOSAMENTE")
        print(f"\n  Próximo paso:")
        print(f"  1. Actualizar DATABASE_URL en Render (Environment Variables)")
        print(f"     Nuevo valor: {NEON_URL}")
        print(f"  2. Render hará redeploy automático")
        print(f"  3. Verificar: curl https://portfolio-reflex-pwdv.onrender.com/health")
    else:
        print(f"  ⚠ MIGRACIÓN CON ERRORES — revisar conteos arriba")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    migrate()
