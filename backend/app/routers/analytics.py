from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import datetime, timedelta
from ..database import get_db
from ..models.visita import Visita
from ..utils.auth import get_current_admin_user

router = APIRouter()


@router.get("/resumen")
def resumen_analytics(
    dias: int = 30,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    """Resumen general de analíticas"""
    fecha_desde = datetime.utcnow() - timedelta(days=dias)
    
    total = db.query(func.count(Visita.id)).filter(
        Visita.timestamp >= fecha_desde
    ).scalar()
    
    ips_unicas = db.query(func.count(func.distinct(Visita.ip))).filter(
        Visita.timestamp >= fecha_desde
    ).scalar()
    
    return {
        "total_visitas": total,
        "visitantes_unicos": ips_unicas,
        "periodo_dias": dias,
    }


@router.get("/paginas")
def paginas_mas_visitadas(
    dias: int = 30,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    """Top páginas más visitadas"""
    fecha_desde = datetime.utcnow() - timedelta(days=dias)
    
    resultados = db.query(
        Visita.pagina,
        func.count(Visita.id).label("visitas")
    ).filter(
        Visita.timestamp >= fecha_desde
    ).group_by(Visita.pagina).order_by(desc("visitas")).limit(limit).all()
    
    return [{"pagina": r[0], "visitas": r[1]} for r in resultados]


@router.get("/dispositivos")
def distribucion_dispositivos(
    dias: int = 30,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    """Distribución por tipo de dispositivo"""
    fecha_desde = datetime.utcnow() - timedelta(days=dias)
    
    resultados = db.query(
        Visita.dispositivo,
        func.count(Visita.id).label("total")
    ).filter(
        Visita.timestamp >= fecha_desde
    ).group_by(Visita.dispositivo).order_by(desc("total")).all()
    
    return [{"dispositivo": r[0], "total": r[1]} for r in resultados]


@router.get("/navegadores")
def distribucion_navegadores(
    dias: int = 30,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    """Distribución por navegador"""
    fecha_desde = datetime.utcnow() - timedelta(days=dias)
    
    resultados = db.query(
        Visita.navegador,
        func.count(Visita.id).label("total")
    ).filter(
        Visita.timestamp >= fecha_desde
    ).group_by(Visita.navegador).order_by(desc("total")).all()
    
    return [{"navegador": r[0], "total": r[1]} for r in resultados]


@router.get("/visitas-por-dia")
def visitas_por_dia(
    dias: int = 30,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    """Visitas agrupadas por día"""
    fecha_desde = datetime.utcnow() - timedelta(days=dias)
    
    resultados = db.query(
        func.date(Visita.timestamp).label("fecha"),
        func.count(Visita.id).label("visitas")
    ).filter(
        Visita.timestamp >= fecha_desde
    ).group_by(func.date(Visita.timestamp)).order_by("fecha").all()
    
    return [{"fecha": str(r[0]), "visitas": r[1]} for r in resultados]


@router.get("/recientes")
def visitas_recientes(
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    """Últimas visitas registradas"""
    visitas = db.query(Visita).order_by(desc(Visita.timestamp)).limit(limit).all()
    
    return [
        {
            "id": v.id,
            "ip": v.ip,
            "pagina": v.pagina,
            "dispositivo": v.dispositivo,
            "navegador": v.navegador,
            "timestamp": v.timestamp.isoformat() if v.timestamp else "",
        }
        for v in visitas
    ]
