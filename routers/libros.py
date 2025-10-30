from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/libros", tags=["Libros"])


# Crear libro
@router.post("/", response_model=schemas.Libro)
def crear_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    return crud.create_libro(db, libro)


# Listar libros
@router.get("/", response_model=list[schemas.Libro])
def listar_libros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_libros(db, skip=skip, limit=limit)


# Obtener libro por ID
@router.get("/{libro_id}", response_model=schemas.Libro)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


# Eliminar libro
@router.delete("/{libro_id}")
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.delete_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado correctamente"}


# Actualizar libro
@router.put("/{libro_id}", response_model=schemas.Libro)
def actualizar_libro(libro_id: int, libro_actualizado: schemas.LibroCreate, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    libro.titulo = libro_actualizado.titulo
    libro.isbn = libro_actualizado.isbn
    libro.anio_publicacion = libro_actualizado.anio_publicacion
    libro.copias_disponibles = libro_actualizado.copias_disponibles
    libro.autor_id = libro_actualizado.autor_id

    db.commit()
    db.refresh(libro)
    return libro
