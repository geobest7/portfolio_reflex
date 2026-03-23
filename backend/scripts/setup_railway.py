"""
Setup Railway PostgreSQL: create tables and insert seed data.
Usage:
    set DATABASE_URL=postgresql://...
    python -m scripts.setup_railway
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ["DATABASE_URL"] = os.environ.get("DATABASE_URL", "")

from app.database import engine, Base
from app.models import proyecto, curso, experiencia, github_repo, user, visita
from sqlalchemy import text
from sqlalchemy.orm import Session

# 1. Create all tables
Base.metadata.create_all(bind=engine)
print("✓ Tablas creadas")

# 2. List tables
with engine.connect() as conn:
    tables = conn.execute(text("SELECT tablename FROM pg_tables WHERE schemaname='public'")).fetchall()
    print(f"  Tablas: {[t[0] for t in tables]}")

# 3. Create admin user if not exists
from app.models.user import User
from app.utils.auth import get_password_hash

with Session(engine) as db:
    admin = db.query(User).filter(User.username == "ginetto").first()
    if not admin:
        admin = User(
            username="ginetto",
            email="admin@portfolio.com",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
            is_admin=True,
        )
        db.add(admin)
        db.commit()
        print("✓ Admin 'ginetto' creado")
    else:
        print("  Admin 'ginetto' ya existe")

# 4. Insert Diploma if not exists
from app.models.curso import Curso
from datetime import date

with Session(engine) as db:
    diploma = db.query(Curso).filter(Curso.tipo == "diploma").first()
    if not diploma:
        diploma = Curso(
            tipo="diploma",
            titulo_es="Diploma de Maturidad – Técnico en Industrias Eléctricas",
            titulo_en="High School Diploma – Electrical Industries Technician",
            titulo_it="Diploma di Maturità – Tecnico delle Industrie Elettriche",
            titulo_ca="Diploma de Maduresa – Tècnic en Indústries Elèctriques",
            institucion_es="ITIS Galileo Galilei, Bolzano",
            institucion_en="ITIS Galileo Galilei, Bolzano",
            institucion_it="ITIS Galileo Galilei, Bolzano",
            institucion_ca="ITIS Galileo Galilei, Bolzano",
            fecha_inicio=date(2013, 9, 1),
            fecha_fin=date(2019, 6, 30),
            descripcion_es="Formación técnica en electrónica, electricidad y automatización industrial.",
            descripcion_en="Technical training in electronics, electricity and industrial automation.",
            descripcion_it="Formazione tecnica in elettronica, elettricità e automazione industriale.",
            descripcion_ca="Formació tècnica en electrònica, electricitat i automatització industrial.",
            orden=1,
            activo=True,
        )
        db.add(diploma)
        db.commit()
        print("✓ Diploma insertado")
    else:
        print("  Diploma ya existe")

# 5. Summary
with Session(engine) as db:
    for table_name in ["users", "cursos", "proyectos", "experiencias", "github_repos", "visitas"]:
        count = db.execute(text(f'SELECT COUNT(*) FROM "{table_name}"')).scalar()
        print(f"  {table_name}: {count}")

print("\n✓ Railway PostgreSQL listo")
