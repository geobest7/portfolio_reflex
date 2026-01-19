from pydantic import BaseModel
from typing import List


class Proyecto(BaseModel):
    id: int
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    descripcion_es: str
    descripcion_en: str
    descripcion_it: str
    descripcion_ca: str
    tecnologias: List[str]
    github_url: str = ""  
    demo_url: str = "" 
    imagen_url: str = ""     
    video_url: str = ""
    destacado: bool
    activo: bool
    orden: int


class Curso(BaseModel):
    id: int
    tipo: str
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    institucion_es: str
    institucion_en: str
    institucion_it: str
    institucion_ca: str
    fecha_inicio: str
    fecha_fin: str = ""  
    certificado_url: str = ""  
    diploma_pdf: str = ""
    activo: bool
    orden: int


class Experiencia(BaseModel):
    id: int
    tipo: str
    empresa: str
    cargo_es: str
    cargo_en: str
    cargo_it: str
    cargo_ca: str
    fecha_inicio: str
    fecha_fin: str = ""
    actual: bool
    descripcion_es: str = ""
    descripcion_en: str = ""
    descripcion_it: str = ""
    descripcion_ca: str = ""
    tecnologias: List[str]
    video_url: str = ""
    orden: int
    activo: bool
    mostrar_en_web: bool


class GitHubRepo(BaseModel):
    """Modelo para repositorio de GitHub"""
    id: int
    repo_id: int
    name: str
    full_name: str
    description: str = ""
    html_url: str
    homepage: str = ""
    language: str = ""
    stargazers_count: int = 0
    forks_count: int = 0
    topics: list[str] = []
    created_at: str = ""
    updated_at: str = ""
    pushed_at: str = ""
