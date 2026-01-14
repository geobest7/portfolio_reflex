from sqlalchemy import Column, Integer, String, Text, Boolean, Date, JSON
from ..database import Base


class Experiencia(Base):
    __tablename__ = "experiencias"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False)
    empresa = Column(String(200), nullable=False)
    
    cargo_es = Column(String(200), nullable=False)
    cargo_en = Column(String(200), nullable=False)
    cargo_it = Column(String(200), nullable=False)
    cargo_ca = Column(String(200), nullable=False)
    
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)
    actual = Column(Boolean, default=False)
    
    descripcion_es = Column(Text)
    descripcion_en = Column(Text)
    descripcion_it = Column(Text)
    descripcion_ca = Column(Text)
    
    tecnologias = Column(JSON)
    
    orden = Column(Integer, default=0)
    activo = Column(Boolean, default=True)
    mostrar_en_web = Column(Boolean, default=True)