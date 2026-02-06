from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import engine, Base, get_db
from .routers import proyectos, cursos, experiencias, github, auth, contacto, analytics
from .models import proyecto, curso, experiencia, github_repo, user, visita
from .middleware.analytics import AnalyticsMiddleware

Base.metadata.create_all(bind=engine)

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

app.add_middleware(AnalyticsMiddleware)


@app.get("/")
def root():
    return {"message": "Portfolio API", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/setup-admin")
def setup_admin(secret: str, db=Depends(get_db)):
    if secret != settings.secret_key:
        raise HTTPException(status_code=403, detail="Forbidden")
    from .models.user import User
    from .utils.auth import get_password_hash
    db.query(User).filter(User.username == "admin").delete()
    db.commit()
    admin_user = User(
        username="admin",
        email="admin@portfolio.com",
        hashed_password=get_password_hash("admin123"),
        is_active=True,
        is_admin=True
    )
    db.add(admin_user)
    db.commit()
    return {"message": "Admin recreado con bcrypt directo. Usuario: admin, Password: admin123"}