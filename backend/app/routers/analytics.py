from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import datetime, timedelta
from io import BytesIO
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


@router.get("/export")
def exportar_excel(
    dias: int = 30,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    """Exportar analíticas a Excel"""
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    
    fecha_desde = datetime.utcnow() - timedelta(days=dias)
    
    wb = openpyxl.Workbook()
    
    # Estilos
    header_font = Font(bold=True, color="FFFFFF", size=11)
    header_fill = PatternFill(start_color="1a1a1a", end_color="1a1a1a", fill_type="solid")
    header_align = Alignment(horizontal="center", vertical="center")
    thin_border = Border(
        left=Side(style="thin", color="333333"),
        right=Side(style="thin", color="333333"),
        top=Side(style="thin", color="333333"),
        bottom=Side(style="thin", color="333333"),
    )
    
    def style_header(ws, row=1):
        for cell in ws[row]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_align
            cell.border = thin_border
    
    # === Hoja 1: Resumen ===
    ws_resumen = wb.active
    ws_resumen.title = "Resumen"
    
    total = db.query(func.count(Visita.id)).filter(Visita.timestamp >= fecha_desde).scalar()
    unicos = db.query(func.count(func.distinct(Visita.ip))).filter(Visita.timestamp >= fecha_desde).scalar()
    
    ws_resumen.append(["Métrica", "Valor"])
    style_header(ws_resumen)
    ws_resumen.append(["Periodo", f"Últimos {dias} días"])
    ws_resumen.append(["Total Visitas", total])
    ws_resumen.append(["Visitantes Únicos", unicos])
    ws_resumen.column_dimensions["A"].width = 25
    ws_resumen.column_dimensions["B"].width = 20
    
    # === Hoja 2: Visitas por día ===
    ws_dias = wb.create_sheet("Visitas por Día")
    ws_dias.append(["Fecha", "Visitas"])
    style_header(ws_dias)
    
    por_dia = db.query(
        func.date(Visita.timestamp).label("fecha"),
        func.count(Visita.id).label("visitas")
    ).filter(Visita.timestamp >= fecha_desde).group_by(
        func.date(Visita.timestamp)
    ).order_by("fecha").all()
    
    for r in por_dia:
        ws_dias.append([str(r[0]), r[1]])
    ws_dias.column_dimensions["A"].width = 15
    ws_dias.column_dimensions["B"].width = 12
    
    # === Hoja 3: Páginas ===
    ws_paginas = wb.create_sheet("Páginas")
    ws_paginas.append(["Página", "Visitas"])
    style_header(ws_paginas)
    
    paginas = db.query(
        Visita.pagina, func.count(Visita.id).label("visitas")
    ).filter(Visita.timestamp >= fecha_desde).group_by(
        Visita.pagina
    ).order_by(desc("visitas")).all()
    
    for r in paginas:
        ws_paginas.append([r[0], r[1]])
    ws_paginas.column_dimensions["A"].width = 40
    ws_paginas.column_dimensions["B"].width = 12
    
    # === Hoja 4: Dispositivos ===
    ws_disp = wb.create_sheet("Dispositivos")
    ws_disp.append(["Dispositivo", "Total"])
    style_header(ws_disp)
    
    dispositivos = db.query(
        Visita.dispositivo, func.count(Visita.id).label("total")
    ).filter(Visita.timestamp >= fecha_desde).group_by(
        Visita.dispositivo
    ).order_by(desc("total")).all()
    
    for r in dispositivos:
        ws_disp.append([r[0], r[1]])
    ws_disp.column_dimensions["A"].width = 20
    ws_disp.column_dimensions["B"].width = 12
    
    # === Hoja 5: Navegadores ===
    ws_nav = wb.create_sheet("Navegadores")
    ws_nav.append(["Navegador", "Total"])
    style_header(ws_nav)
    
    navegadores = db.query(
        Visita.navegador, func.count(Visita.id).label("total")
    ).filter(Visita.timestamp >= fecha_desde).group_by(
        Visita.navegador
    ).order_by(desc("total")).all()
    
    for r in navegadores:
        ws_nav.append([r[0], r[1]])
    ws_nav.column_dimensions["A"].width = 20
    ws_nav.column_dimensions["B"].width = 12
    
    # === Hoja 6: Todas las visitas ===
    ws_todas = wb.create_sheet("Todas las Visitas")
    ws_todas.append(["Fecha/Hora", "Página", "Dispositivo", "Navegador", "IP", "País", "Ciudad"])
    style_header(ws_todas)
    
    visitas = db.query(Visita).filter(
        Visita.timestamp >= fecha_desde
    ).order_by(desc(Visita.timestamp)).all()
    
    for v in visitas:
        ws_todas.append([
            v.timestamp.strftime("%Y-%m-%d %H:%M") if v.timestamp else "",
            v.pagina or "",
            v.dispositivo or "",
            v.navegador or "",
            v.ip or "",
            v.pais or "",
            v.ciudad or "",
        ])
    ws_todas.column_dimensions["A"].width = 18
    ws_todas.column_dimensions["B"].width = 30
    ws_todas.column_dimensions["C"].width = 15
    ws_todas.column_dimensions["D"].width = 15
    ws_todas.column_dimensions["E"].width = 18
    ws_todas.column_dimensions["F"].width = 15
    ws_todas.column_dimensions["G"].width = 15
    
    # Guardar en buffer
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    
    fecha_str = datetime.utcnow().strftime("%Y%m%d")
    filename = f"analytics_{fecha_str}.xlsx"
    
    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
