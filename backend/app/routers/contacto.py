import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
    """Enviar email desde el formulario de contacto"""
    
    if not form.nombre.strip():
        raise HTTPException(status_code=400, detail="El nombre es obligatorio")
    if not form.mensaje.strip():
        raise HTTPException(status_code=400, detail="El mensaje es obligatorio")
    
    if not settings.smtp_user or not settings.smtp_password or not settings.contact_email_to:
        raise HTTPException(
            status_code=500,
            detail="El servicio de email no está configurado"
        )
    
    try:
        msg = MIMEMultipart()
        msg["From"] = settings.smtp_user
        msg["To"] = settings.contact_email_to
        msg["Subject"] = f"Portfolio - Nuevo mensaje de {form.nombre}"
        
        body = f"""
Nuevo mensaje desde el formulario de contacto del Portfolio:

Nombre: {form.nombre}
Email: {form.email}

Mensaje:
{form.mensaje}

---
Enviado desde el formulario de contacto del portfolio.
"""
        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=15) as server:
            server.starttls()
            server.login(settings.smtp_user, settings.smtp_password)
            server.send_message(msg)
        
        return {"status": "ok", "message": "Mensaje enviado correctamente"}
    
    except smtplib.SMTPAuthenticationError:
        raise HTTPException(
            status_code=500,
            detail="Error de autenticación del servidor de email"
        )
    except (TimeoutError, OSError) as e:
        raise HTTPException(
            status_code=504,
            detail="No se pudo conectar al servidor de email. Inténtalo más tarde."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al enviar el mensaje: {str(e)}"
        )
