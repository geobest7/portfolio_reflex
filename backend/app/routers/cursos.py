from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.curso import Curso as CursoModel
from ..schemas.curso import Curso, CursoCreate, CursoUpdate

router = APIRouter()


@router.get("/", response_model=List[Curso])
def get_cursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener lista de cursos"""
    cursos = db.query(CursoModel).filter(CursoModel.activo == True).order_by(CursoModel.orden).offset(skip).limit(limit).all()
    return cursos


@router.get("/{curso_id}", response_model=Curso)
def get_curso(curso_id: int, db: Session = Depends(get_db)):
    """Obtener un curso por ID"""
    curso = db.query(CursoModel).filter(CursoModel.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


@router.post("/", response_model=Curso)
def create_curso(curso: CursoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo curso"""
    db_curso = CursoModel(**curso.dict())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso


@router.put("/{curso_id}", response_model=Curso)
def update_curso(
    curso_id: int,
    curso: CursoUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar un curso"""
    db_curso = db.query(CursoModel).filter(CursoModel.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    for key, value in curso.dict().items():
        setattr(db_curso, key, value)
    
    db.commit()
    db.refresh(db_curso)
    return db_curso


@router.delete("/{curso_id}")
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    """Eliminar un curso (soft delete)"""
    db_curso = db.query(CursoModel).filter(CursoModel.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    db_curso.activo = False
    db.commit()
    return {"message": "Curso eliminado"}