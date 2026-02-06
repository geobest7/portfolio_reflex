from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from ..database import SessionLocal
from ..models.visita import Visita
import re


# Rutas que NO se deben trackear
RUTAS_EXCLUIDAS = [
    r"^/api/",
    r"^/docs",
    r"^/openapi",
    r"^/health",
    r"^/_next/",
    r"^/favicon",
    r"\.\w+$",
]


def detectar_dispositivo(user_agent: str) -> str:
    ua = user_agent.lower()
    if any(m in ua for m in ["mobile", "android", "iphone", "ipad"]):
        if "ipad" in ua or "tablet" in ua:
            return "tablet"
        return "movil"
    return "desktop"


def detectar_navegador(user_agent: str) -> str:
    ua = user_agent.lower()
    if "edg" in ua:
        return "Edge"
    if "chrome" in ua:
        return "Chrome"
    if "firefox" in ua:
        return "Firefox"
    if "safari" in ua:
        return "Safari"
    if "opera" in ua or "opr" in ua:
        return "Opera"
    return "Otro"


def anonimizar_ip(ip: str) -> str:
    """Anonimizar último octeto de la IP para privacidad"""
    if not ip:
        return ""
    partes = ip.split(".")
    if len(partes) == 4:
        partes[-1] = "0"
        return ".".join(partes)
    return ip


class AnalyticsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        path = request.url.path
        
        # No trackear rutas excluidas
        if any(re.match(patron, path) for patron in RUTAS_EXCLUIDAS):
            return response
        
        # Solo trackear GET exitosos (páginas)
        if request.method != "GET" or response.status_code != 200:
            return response
        
        try:
            user_agent = request.headers.get("user-agent", "")
            ip_raw = request.client.host if request.client else ""
            
            db = SessionLocal()
            try:
                visita = Visita(
                    ip=anonimizar_ip(ip_raw),
                    pagina=path,
                    metodo=request.method,
                    user_agent=user_agent[:500],
                    referer=request.headers.get("referer", "")[:500],
                    pais="",
                    ciudad="",
                    dispositivo=detectar_dispositivo(user_agent),
                    navegador=detectar_navegador(user_agent),
                )
                db.add(visita)
                db.commit()
            finally:
                db.close()
        except Exception:
            pass
        
        return response
