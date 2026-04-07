import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from ..config import settings

router = APIRouter()


class ContactForm(BaseModel):
    nombre: str
    email: EmailStr
    mensaje: str


@router.post("/")
async def enviar_contacto(form: ContactForm):
    """Enviar email desde el formulario de contacto usando Resend API"""
    
    if not form.nombre.strip():
        raise HTTPException(status_code=400, detail="El nombre es obligatorio")
    if not form.mensaje.strip():
        raise HTTPException(status_code=400, detail="El mensaje es obligatorio")
    
    if not settings.resend_api_key:
        raise HTTPException(
            status_code=500,
            detail="El servicio de email no está configurado"
        )
    
    # Debug temporal: ver los primeros/últimos chars de la key
    key = settings.resend_api_key
    print(f"[DEBUG RESEND] key length={len(key)}, starts='{key[:6]}...', ends='...{key[-4:]}', repr='{repr(key[:20])}'")
    print(f"[DEBUG RESEND] contact_email_to='{settings.contact_email_to}'")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {settings.resend_api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "from": "Portfolio Contact <onboarding@resend.dev>",
                    "to": [settings.contact_email_to],
                    "subject": f"Portfolio - Nuevo mensaje de {form.nombre}",
                    "reply_to": form.email,
                    "text": f"""Nuevo mensaje desde el formulario de contacto del Portfolio:

Nombre: {form.nombre}
Email: {form.email}

Mensaje:
{form.mensaje}

---
Enviado desde el formulario de contacto del portfolio.""",
                },
                timeout=15.0,
            )
        
        if response.status_code == 200:
            return {"status": "ok", "message": "Mensaje enviado correctamente"}
        else:
            detail = response.json().get("message", "Error al enviar")
            raise HTTPException(status_code=500, detail=detail)
    
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="No se pudo conectar al servidor de email. Inténtalo más tarde."
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al enviar el mensaje: {str(e)}"
        )
