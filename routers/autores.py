from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", response_model=schemas.AutorRead)
def crear_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    return crud.create_autor(db, autor)


@router.get("/", response_model=list[schemas.AutorRead])
def listar_autores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_autores(db, skip=skip, limit=limit)


@router.get("/{autor_id}", response_model=schemas.AutorRead)
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


# ✅ Endpoint para actualizar un autor
@router.put("/{autor_id}", response_model=schemas.AutorRead)
def actualizar_autor(autor_id: int, autor_actualizado: schemas.AutorCreate, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    autor.nombre = autor_actualizado.nombre
    autor.pais_origen = autor_actualizado.pais_origen
    autor.anio_nacimiento = autor_actualizado.anio_nacimiento

    db.commit()
    db.refresh(autor)
    return autor
