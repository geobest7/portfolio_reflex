from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    app_name: str = "Portfolio API"
    debug: bool = True
    
    database_url: str = "postgresql://postgres:postgres@localhost:5432/portfolio"
    
    # Seguridad JWT
    secret_key: str = "cambiar-en-produccion-clave-secreta-muy-larga-y-segura"
    access_token_expire_minutes: int = 60 * 24  # 24 horas
    
    cors_origins: list = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    cors_allow_all: bool = False
    
    github_token: Optional[str] = None
    github_username: str = "geobest7"
    
    # Resend API para formulario de contacto
    resend_api_key: str = ""
    contact_email_to: str = "febbrai.alessandro@libero.it"
    
    # Cloudinary para upload de archivos
    cloudinary_cloud_name: str = ""
    cloudinary_api_key: str = ""
    cloudinary_api_secret: str = ""
    
    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()