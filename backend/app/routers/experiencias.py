from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.experiencia import Experiencia as ExperienciaModel
from ..schemas.experiencia import Experiencia, ExperienciaCreate, ExperienciaUpdate
from ..utils.auth import get_current_admin_user
from ..models.user import User

router = APIRouter()


@router.get("/", response_model=List[Experiencia])
def get_experiencias(
    skip: int = 0,
    limit: int = 100,
    mostrar_en_web: bool = None,
    db: Session = Depends(get_db)
):
    """Obtener lista de experiencias"""
    query = db.query(ExperienciaModel).filter(ExperienciaModel.activo == True)
    
    if mostrar_en_web is not None:
        query = query.filter(ExperienciaModel.mostrar_en_web == mostrar_en_web)
    
    experiencias = query.order_by(ExperienciaModel.orden).offset(skip).limit(limit).all()
    return experiencias


@router.get("/{experiencia_id}", response_model=Experiencia)
def get_experiencia(experiencia_id: int, db: Session = Depends(get_db)):
    """Obtener una experiencia por ID"""
    experiencia = db.query(ExperienciaModel).filter(ExperienciaModel.id == experiencia_id).first()
    if not experiencia:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    return experiencia


@router.post("/", response_model=Experiencia)
def create_experiencia(experiencia: ExperienciaCreate, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin_user)):
    """Crear una nueva experiencia"""
    db_experiencia = ExperienciaModel(**experiencia.dict())
    db.add(db_experiencia)
    db.commit()
    db.refresh(db_experiencia)
    return db_experiencia


@router.put("/{experiencia_id}", response_model=Experiencia)
def update_experiencia(
    experiencia_id: int,
    experiencia: ExperienciaUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
):
    """Actualizar una experiencia"""
    db_experiencia = db.query(ExperienciaModel).filter(ExperienciaModel.id == experiencia_id).first()
    if not db_experiencia:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    
    for key, value in experiencia.dict().items():
        setattr(db_experiencia, key, value)
    
    db.commit()
    db.refresh(db_experiencia)
    return db_experiencia


@router.delete("/{experiencia_id}")
def delete_experiencia(experiencia_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin_user)):
    """Eliminar una experiencia (soft delete)"""
    db_experiencia = db.query(ExperienciaModel).filter(ExperienciaModel.id == experiencia_id).first()
    if not db_experiencia:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    
    db_experiencia.activo = False
    db.commit()
    return {"message": "Experiencia eliminada"}