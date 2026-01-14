from sqlalchemy import Column, Integer, String, Text, Boolean, Date
from ..database import Base


class Curso(Base):
    __tablename__ = "cursos"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False)
    
    titulo_es = Column(String(200), nullable=False)
    titulo_en = Column(String(200), nullable=False)
    titulo_it = Column(String(200), nullable=False)
    titulo_ca = Column(String(200), nullable=False)
    
    institucion = Column(String(200), nullable=False)
    
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    
    descripcion_es = Column(Text)
    descripcion_en = Column(Text)
    descripcion_it = Column(Text)
    descripcion_ca = Column(Text)
    
    certificado_url = Column(String(500))
    
    orden = Column(Integer, default=0)
    activo = Column(Boolean, default=True)