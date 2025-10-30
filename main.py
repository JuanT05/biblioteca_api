from fastapi import FastAPI
from database import Base, engine
from routers import autores, libros

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Inicializar app
app = FastAPI(title="Sistema de Gestión de Biblioteca")

# Incluir routers
app.include_router(autores.router)
app.include_router(libros.router)


@app.get("/")
def root():
    return {"mensaje": "Bienvenido al sistema de gestión de biblioteca 📚"}
