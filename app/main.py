"""Punto de entrada de la aplicación FastAPI."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import proyecto
from app.db import crear_tablas
from app.rutas import api, paginas

CARPETA_APP = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Inicializa la base de datos al iniciar la aplicación."""

    crear_tablas()
    yield


app = FastAPI(
    title="Plataforma lúdica de cursos para niños",
    description=f"Proyecto de {proyecto.APRENDIZ}: {proyecto.CURSO} con {proyecto.MECANICA}.",
    version=proyecto.VERSION,
    lifespan=lifespan,
)

app.mount("/static", StaticFiles(directory=CARPETA_APP / "static"), name="static")
app.include_router(paginas.router)
app.include_router(api.router)
