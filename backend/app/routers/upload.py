from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from ..config import settings
from ..utils.auth import get_current_admin_user
from ..models.user import User
import cloudinary
import cloudinary.uploader

router = APIRouter()


def configure_cloudinary():
    """Configura Cloudinary con las credenciales"""
    if not settings.cloudinary_cloud_name:
        raise HTTPException(status_code=500, detail="Cloudinary no configurado")
    cloudinary.config(
        cloud_name=settings.cloudinary_cloud_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True,
    )


@router.post("/")
async def upload_file(
    file: UploadFile = File(...),
    current_admin: User = Depends(get_current_admin_user),
):
    """Subir archivo (PDF, imagen) a Cloudinary. Requiere autenticación admin."""
    allowed_types = [
        "application/pdf",
        "image/jpeg",
        "image/png",
        "image/webp",
        "image/gif",
    ]
    
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo de archivo no permitido: {file.content_type}. Permitidos: PDF, JPEG, PNG, WebP, GIF",
        )
    
    max_size = 10 * 1024 * 1024  # 10MB
    contents = await file.read()
    if len(contents) > max_size:
        raise HTTPException(status_code=400, detail="Archivo demasiado grande (máximo 10MB)")
    
    configure_cloudinary()
    
    try:
        resource_type = "raw" if file.content_type == "application/pdf" else "image"
        result = cloudinary.uploader.upload(
            contents,
            folder="portfolio",
            resource_type=resource_type,
            public_id=file.filename.rsplit(".", 1)[0] if file.filename else None,
        )
        return {
            "url": result["secure_url"],
            "public_id": result["public_id"],
            "format": result.get("format", ""),
            "size": result.get("bytes", 0),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir archivo: {str(e)}")
