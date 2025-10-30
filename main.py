from fastapi import FastAPI
from database import init_db
from routers import autores, libros

app = FastAPI(title="Sistema de Gestión de Biblioteca")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(autores.router)
app.include_router(libros.router)
