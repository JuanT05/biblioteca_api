from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/libros", tags=["Libros"])


@router.post("/", response_model=schemas.Libro)
def crear_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    return crud.create_libro(db, libro)


@router.get("/", response_model=list[schemas.Libro])
def listar_libros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_libros(db, skip=skip, limit=limit)


@router.get("/{libro_id}", response_model=schemas.Libro)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


@router.delete("/{libro_id}")
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.delete_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado correctamente"}
