from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    app_name: str = "Portfolio API"
    debug: bool = True
    
    database_url: str = "sqlite:///./portfolio.db"
    
    cors_origins: list = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    github_token: Optional[str] = None
    github_username: str = "geobest7"
    
    class Config:
        env_file = ".env"


settings = Settings()