from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    app_name: str = "Portfolio API"
    debug: bool = True
    
    database_url: str = "sqlite:///./portfolio.db"
    
    # Seguridad JWT
    secret_key: str = "cambiar-en-produccion-clave-secreta-muy-larga-y-segura"
    access_token_expire_minutes: int = 60 * 24  # 24 horas
    
    cors_origins: list = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    github_token: Optional[str] = None
    github_username: str = "geobest7"
    
    # SMTP para formulario de contacto
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    contact_email_to: str = ""
    
    class Config:
        env_file = "../.env"


settings = Settings()