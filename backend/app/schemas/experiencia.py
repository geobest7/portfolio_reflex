from pydantic import BaseModel
from typing import Optional, List

class ExperienciaBase(BaseModel):
    tipo: str
    empresa: str
    cargo_es: str
    cargo_en: str
    cargo_it: str
    cargo_ca: str
    fecha_inicio: str
    fecha_fin: Optional[str] = None
    actual: bool = False
    descripcion_es: Optional[str] = None
    descripcion_en: Optional[str] = None
    descripcion_it: Optional[str] = None
    descripcion_ca: Optional[str] = None
    tecnologias: Optional[List[str]] = []
    imagen_url: Optional[str] = None
    video_url: Optional[str] = None
    documento_url: Optional[str] = None
    orden: int = 0
    activo: bool = True

class ExperienciaCreate(ExperienciaBase):
    pass

class ExperienciaUpdate(ExperienciaBase):
    pass


class Experiencia(ExperienciaBase):
    id: int
    
    class Config:
        from_attributes = True