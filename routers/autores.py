from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", response_model=schemas.Autor)
def crear_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    return crud.create_autor(db, autor)


@router.get("/", response_model=list[schemas.Autor])
def listar_autores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_autores(db, skip=skip, limit=limit)


@router.get("/{autor_id}", response_model=schemas.Autor)
def obtener_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor


@router.delete("/{autor_id}")
def eliminar_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = crud.delete_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return {"mensaje": "Autor eliminado correctamente"}


# Actualizar un autor
@router.put("/autores/{autor_id}", response_model=schemas.AutorRead)
def actualizar_autor(autor_id: int, autor_actualizado: schemas.AutorCreate, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    autor.nombre = autor_actualizado.nombre
    autor.nacionalidad = autor_actualizado.nacionalidad
    db.commit()
    db.refresh(autor)
    return autor
