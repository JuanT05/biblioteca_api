from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    pais_origen = Column(String, nullable=True)
    anio_nacimiento = Column(Integer, nullable=True)

    libros = relationship("Libro", back_populates="autor", cascade="all, delete")


class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    anio_publicacion = Column(Integer)
    copias_disponibles = Column(Integer, default=1)
    autor_id = Column(Integer, ForeignKey("autores.id"))

    autor = relationship("Autor", back_populates="libros")
