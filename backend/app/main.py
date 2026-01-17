from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import engine, Base
from .routers import proyectos, cursos, experiencias, github
from .models import proyecto, curso, experiencia, github_repo


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(proyectos.router, prefix="/api/proyectos", tags=["proyectos"])
app.include_router(cursos.router, prefix="/api/cursos", tags=["cursos"])
app.include_router(experiencias.router, prefix="/api/experiencias", tags=["experiencias"])
app.include_router(github.router, prefix="/api/github", tags=["github"])


@app.get("/")
def root():
    return {"message": "Portfolio API", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}