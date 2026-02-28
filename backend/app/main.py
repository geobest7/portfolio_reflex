from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import engine, Base, SessionLocal
from .routers import proyectos, cursos, experiencias, github, auth, contacto, analytics, upload
from .models import proyecto, curso, experiencia, github_repo, user, visita
from .models.user import User
from .utils.auth import get_password_hash

Base.metadata.create_all(bind=engine)


def migrar_columnas_visitas():
    """Añadir columnas nuevas a la tabla visitas si no existen"""
    from sqlalchemy import text
    db = SessionLocal()
    try:
        for col, tipo in [
            ("screen_width", "INTEGER"),
            ("screen_height", "INTEGER"),
            ("idioma", "VARCHAR(10)"),
            ("plataforma", "VARCHAR(100)"),
        ]:
            try:
                db.execute(text(f"ALTER TABLE visitas ADD COLUMN {col} {tipo}"))
                db.commit()
            except Exception:
                db.rollback()
    finally:
        db.close()


migrar_columnas_visitas()


def crear_admin_si_no_existe():
    """Crear usuario admin automaticamente si no existe (necesario porque SQLite se pierde en cada redeploy de Render)"""
    db = SessionLocal()
    try:
        existing = db.query(User).filter(User.username == "admin").first()
        if not existing:
            admin_user = User(
                username="admin",
                email="admin@portfolio.com",
                hashed_password=get_password_hash("admin123"),
                is_active=True,
                is_admin=True
            )
            db.add(admin_user)
            db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()


crear_admin_si_no_existe()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.cors_allow_all else settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(proyectos.router, prefix="/api/proyectos", tags=["proyectos"])
app.include_router(cursos.router, prefix="/api/cursos", tags=["cursos"])
app.include_router(experiencias.router, prefix="/api/experiencias", tags=["experiencias"])
app.include_router(github.router, prefix="/api/github", tags=["github"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(contacto.router, prefix="/api/contacto", tags=["contacto"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
app.include_router(upload.router, prefix="/api/upload", tags=["upload"])


@app.get("/")
def root():
    return {"message": "Portfolio API", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}