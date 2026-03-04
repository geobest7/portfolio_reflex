"""
Script de verificación de base de datos.
Uso: python -m scripts.verify_db

Verifica:
1. Conexión a la base de datos
2. Tablas existentes
3. Conteo de registros por tabla
4. Integridad de relaciones básicas

Ejecutar desde backend/:
    python -m scripts.verify_db
    
O con URL explícita:
    DATABASE_URL="postgresql://user:pass@host/db" python -m scripts.verify_db
"""
import os
import sys

# Añadir backend/ al path para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text, inspect


def get_database_url():
    """Obtener URL de la base de datos desde env o config"""
    url = os.environ.get("DATABASE_URL", "")
    if not url:
        try:
            from app.config import settings
            url = settings.database_url
        except Exception:
            print("ERROR: No se pudo obtener DATABASE_URL")
            print("Usa: DATABASE_URL='postgresql://...' python -m scripts.verify_db")
            sys.exit(1)
    
    # Fix postgres:// → postgresql://
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    
    # Neon SSL
    if "neon.tech" in url and "sslmode" not in url:
        separator = "&" if "?" in url else "?"
        url = url + separator + "sslmode=require"
    
    return url


def verify():
    url = get_database_url()
    
    # Ocultar password en output
    display_url = url
    if "@" in url:
        parts = url.split("@")
        pre = parts[0]
        if ":" in pre:
            # mask password
            scheme_user = pre.rsplit(":", 1)[0]
            display_url = scheme_user + ":****@" + parts[1]
    
    print(f"\n{'='*60}")
    print(f"  VERIFICACIÓN DE BASE DE DATOS")
    print(f"{'='*60}")
    print(f"\nURL: {display_url}")
    
    # 1. Test conexión
    print(f"\n--- 1. Conexión ---")
    try:
        engine = create_engine(url, pool_pre_ping=True)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print(f"  ✓ Conexión exitosa")
    except Exception as e:
        print(f"  ✗ ERROR de conexión: {e}")
        sys.exit(1)
    
    # 2. Listar tablas
    print(f"\n--- 2. Tablas ---")
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    if not tables:
        print(f"  ⚠ No se encontraron tablas")
        return
    
    for table in sorted(tables):
        print(f"  ✓ {table}")
    
    # 3. Conteo de registros
    print(f"\n--- 3. Registros por tabla ---")
    with engine.connect() as conn:
        for table in sorted(tables):
            try:
                result = conn.execute(text(f'SELECT COUNT(*) FROM "{table}"'))
                count = result.scalar()
                print(f"  {table}: {count} registros")
            except Exception as e:
                print(f"  {table}: ERROR - {str(e)[:80]}")
    
    # 4. Verificar columnas de tablas principales
    print(f"\n--- 4. Estructura de tablas principales ---")
    expected_tables = ["users", "proyectos", "cursos", "experiencias", "visitas", "github_repos"]
    for table in expected_tables:
        if table in tables:
            columns = inspector.get_columns(table)
            col_names = [c["name"] for c in columns]
            print(f"  {table} ({len(columns)} cols): {', '.join(col_names)}")
        else:
            print(f"  ⚠ Tabla '{table}' NO encontrada")
    
    # 5. Verificar usuario admin
    print(f"\n--- 5. Usuario admin ---")
    with engine.connect() as conn:
        try:
            result = conn.execute(text("SELECT id, username, email, is_admin FROM users WHERE username = 'admin'"))
            row = result.fetchone()
            if row:
                print(f"  ✓ Admin encontrado: id={row[0]}, username={row[1]}, email={row[2]}, is_admin={row[3]}")
            else:
                print(f"  ⚠ No hay usuario admin (se creará automáticamente al iniciar el backend)")
        except Exception as e:
            print(f"  ✗ Error: {str(e)[:80]}")
    
    print(f"\n{'='*60}")
    print(f"  VERIFICACIÓN COMPLETADA")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    verify()
