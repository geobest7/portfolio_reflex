import io
import logging
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from ..config import settings
from ..utils.auth import get_current_admin_user
from ..models.user import User
import cloudinary
import cloudinary.uploader

logger = logging.getLogger(__name__)

router = APIRouter()

ALLOWED_TYPES = {
    "application/pdf": "raw",
    "image/jpeg": "image",
    "image/png": "image",
    "image/webp": "image",
    "image/gif": "image",
    "video/mp4": "video",
    "video/webm": "video",
    "video/quicktime": "video",
}

MAX_SIZE_PDF_IMG = 10 * 1024 * 1024   # 10MB
MAX_SIZE_VIDEO = 100 * 1024 * 1024    # 100MB


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
    """Subir archivo (PDF, imagen, video) a Cloudinary. Requiere autenticación admin."""
    resource_type = ALLOWED_TYPES.get(file.content_type)
    if not resource_type:
        allowed = ", ".join(ALLOWED_TYPES.keys())
        raise HTTPException(
            status_code=400,
            detail=f"Tipo no permitido: {file.content_type}. Permitidos: {allowed}",
        )
    
    contents = await file.read()
    size_mb = len(contents) / (1024 * 1024)
    logger.info(f"Upload: {file.filename} ({file.content_type}) {size_mb:.1f}MB resource_type={resource_type}")
    
    max_size = MAX_SIZE_VIDEO if resource_type == "video" else MAX_SIZE_PDF_IMG
    if len(contents) > max_size:
        limit_mb = max_size // (1024 * 1024)
        raise HTTPException(status_code=400, detail=f"Archivo demasiado grande ({size_mb:.1f}MB, máximo {limit_mb}MB)")
    
    configure_cloudinary()
    
    try:
        public_id = file.filename.rsplit(".", 1)[0] if file.filename else None
        
        if resource_type == "video":
            # upload_large usa chunked upload — más fiable para videos grandes
            result = cloudinary.uploader.upload_large(
                io.BytesIO(contents),
                folder="portfolio",
                resource_type="video",
                public_id=public_id,
                chunk_size=6_000_000,  # 6MB chunks
                timeout=300,
            )
        else:
            result = cloudinary.uploader.upload(
                contents,
                folder="portfolio",
                resource_type=resource_type,
                public_id=public_id,
            )
        
        logger.info(f"Upload OK: {result.get('secure_url', '')[:80]}")
        return {
            "url": result["secure_url"],
            "public_id": result["public_id"],
            "resource_type": resource_type,
            "format": result.get("format", ""),
            "size": result.get("bytes", 0),
        }
    except Exception as e:
        logger.error(f"Upload FAILED: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al subir archivo: {str(e)}")
