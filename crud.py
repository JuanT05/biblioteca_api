from sqlalchemy.orm import Session
import models, schemas


# --- AUTORES ---

def get_autores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Autor).offset(skip).limit(limit).all()


def get_autor(db: Session, autor_id: int):
    return db.query(models.Autor).filter(models.Autor.id == autor_id).first()



def create_autor(db: Session, autor: schemas.AutorCreate):
    db_autor = models.Autor(**autor.dict())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor


def delete_autor(db: Session, autor_id: int):
    autor = db.query(models.Autor).filter(models.Autor.id == autor_id).first()
    if autor:
        db.delete(autor)
        db.commit()
    return autor


# --- LIBROS ---

def get_libros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Libro).offset(skip).limit(limit).all()


def get_libro(db: Session, libro_id: int):
    return db.query(models.Libro).filter(models.Libro.id == libro_id).first()


def create_libro(db: Session, libro: schemas.LibroCreate):
    db_libro = models.Libro(**libro.dict())
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro


def delete_libro(db: Session, libro_id: int):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if libro:
        db.delete(libro)
        db.commit()
    return libro
