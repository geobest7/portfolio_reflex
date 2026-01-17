from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.proyecto import Proyecto as ProyectoModel
from ..schemas.proyecto import Proyecto, ProyectoCreate, ProyectoUpdate
from ..utils.auth import get_current_admin_user
from ..models.user import User

router = APIRouter()


@router.get("/", response_model=List[Proyecto])
def get_proyectos(
    skip: int = 0,
    limit: int = 100,
    destacados: bool = None,
    db: Session = Depends(get_db)
):
    """Obtener lista de proyectos"""
    query = db.query(ProyectoModel).filter(ProyectoModel.activo == True)
    
    if destacados is not None:
        query = query.filter(ProyectoModel.destacado == destacados)
    
    proyectos = query.order_by(ProyectoModel.orden).offset(skip).limit(limit).all()
    return proyectos


@router.get("/{proyecto_id}", response_model=Proyecto)
def get_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    """Obtener un proyecto por ID"""
    proyecto = db.query(ProyectoModel).filter(ProyectoModel.id == proyecto_id).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


@router.post("/", response_model=Proyecto)
def create_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin_user)):
    """Crear un nuevo proyecto"""
    db_proyecto = ProyectoModel(**proyecto.dict())
    db.add(db_proyecto)
    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto


@router.put("/{proyecto_id}", response_model=Proyecto)
def update_proyecto(
    proyecto_id: int,
    proyecto: ProyectoUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
):
    """Actualizar un proyecto"""
    db_proyecto = db.query(ProyectoModel).filter(ProyectoModel.id == proyecto_id).first()
    if not db_proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    
    for key, value in proyecto.dict().items():
        setattr(db_proyecto, key, value)
    
    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto


@router.delete("/{proyecto_id}")
def delete_proyecto(proyecto_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin_user)):
    """Eliminar un proyecto (soft delete)"""
    db_proyecto = db.query(ProyectoModel).filter(ProyectoModel.id == proyecto_id).first()
    if not db_proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    
    db_proyecto.activo = False
    db.commit()
    return {"message": "Proyecto eliminado"}