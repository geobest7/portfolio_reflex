from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database import Base


class Visita(Base):
    __tablename__ = "visitas"
    
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String(45))
    pagina = Column(String(500))
    metodo = Column(String(10))
    user_agent = Column(String(500))
    referer = Column(String(500))
    pais = Column(String(100))
    ciudad = Column(String(100))
    dispositivo = Column(String(50))
    navegador = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
