from pydantic import BaseModel
from typing import List, Optional


class LibroBase(BaseModel):
    titulo: str
    isbn: str
    anio_publicacion: Optional[int]
    copias_disponibles: Optional[int] = 1


class LibroCreate(LibroBase):
    autor_id: int


class Libro(LibroBase):
    id: int
    autor_id: int

    class Config:
        orm_mode = True


class AutorBase(BaseModel):
    nombre: str
    pais_origen: Optional[str]
    anio_nacimiento: Optional[int]


class AutorCreate(AutorBase):
    pass


class Autor(AutorBase):
    id: int
    libros: List[Libro] = []

    class Config:
        orm_mode = True


class AutorCreate(AutorBase):
    pass

class AutorRead(AutorBase):
    id: int

    class Config:
        orm_mode = True