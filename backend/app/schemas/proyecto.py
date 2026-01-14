from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProyectoBase(BaseModel):
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    descripcion_es: str
    descripcion_en: str
    descripcion_it: str
    descripcion_ca: str
    tecnologias: Optional[List[str]] = []
    url_github: Optional[str] = None
    url_demo: Optional[str] = None
    imagen_url: Optional[str] = None
    destacado: bool = False
    orden: int = 0
    activo: bool = True


class ProyectoCreate(ProyectoBase):
    pass


class ProyectoUpdate(ProyectoBase):
    pass


class Proyecto(ProyectoBase):
    id: int
    
    class Config:
        from_attributes = True