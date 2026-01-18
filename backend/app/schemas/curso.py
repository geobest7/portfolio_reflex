from pydantic import BaseModel
from typing import Optional
from datetime import date


class CursoBase(BaseModel):
    tipo: str
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    institucion_es: str
    institucion_en: str
    institucion_it: str
    institucion_ca: str
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    descripcion_es: Optional[str] = None
    descripcion_en: Optional[str] = None
    descripcion_it: Optional[str] = None
    descripcion_ca: Optional[str] = None
    certificado_url: Optional[str] = None
    diploma_pdf: Optional[str] = None
    orden: int = 0
    activo: bool = True


class CursoCreate(CursoBase):
    pass


class CursoUpdate(CursoBase):
    pass


class Curso(CursoBase):
    id: int
    
    class Config:
        from_attributes = True