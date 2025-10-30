from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", response_model=schemas.AutorRead)
def crear_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    return crud.create_autor(db, autor)


@router.get("/", response_model=list[schemas.AutorRead])
def listar_autores(pais: str | None = None, db: Session = Depends(get_db)):
    autores = crud.get_autores(db)
    if pais:
        autores = [a for a in autores if a.nacionalidad and a.nacionalidad.lower() == pais.lower()]
    return autores


@router.get("/{autor_id}", response_model=schemas.AutorRead)
def obtener_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor


@router.put("/{autor_id}", response_model=schemas.AutorRead)
def actualizar_autor(autor_id: int, autor_actualizado: schemas.AutorCreate, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    autor.nombre = autor_actualizado.nombre
    autor.nacionalidad = autor_actualizado.nacionalidad
    autor.anio_nacimiento = autor_actualizado.anio_nacimiento
    db.commit()
    db.refresh(autor)
    return autor


@router.delete("/{autor_id}")
def eliminar_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    if autor.libros:
        raise HTTPException(status_code=400, detail="No se puede eliminar un autor con libros registrados")

    crud.delete_autor(db, autor_id)
    return {"mensaje": "Autor eliminado correctamente"}
