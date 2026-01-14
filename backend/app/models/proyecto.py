from sqlalchemy import Column, Integer, String, Text, Boolean, JSON
from ..database import Base


class Proyecto(Base):
    __tablename__ = "proyectos"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo_es = Column(String(200), nullable=False)
    titulo_en = Column(String(200), nullable=False)
    titulo_it = Column(String(200), nullable=False)
    titulo_ca = Column(String(200), nullable=False)
    
    descripcion_es = Column(Text, nullable=False)
    descripcion_en = Column(Text, nullable=False)
    descripcion_it = Column(Text, nullable=False)
    descripcion_ca = Column(Text, nullable=False)
    
    tecnologias = Column(JSON)
    url_github = Column(String(500))
    url_demo = Column(String(500))
    imagen_url = Column(String(500))
    
    destacado = Column(Boolean, default=False)
    orden = Column(Integer, default=0)
    activo = Column(Boolean, default=True)