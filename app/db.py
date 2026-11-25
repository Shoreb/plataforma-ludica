"""Configuración y dependencias de acceso a la base de datos."""

import os
from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app import modelos  # noqa: F401

URL_BASE_DATOS = os.getenv("DATABASE_URL", "sqlite:///./plataforma.db")
ARGUMENTOS_CONEXION = {"check_same_thread": False} if URL_BASE_DATOS.startswith("sqlite") else {}

motor = create_engine(URL_BASE_DATOS, connect_args=ARGUMENTOS_CONEXION)


def crear_tablas() -> None:
    """Crea las tablas declaradas en los modelos."""

    SQLModel.metadata.create_all(motor)


def obtener_sesion() -> Generator[Session, None, None]:
    """Entrega una sesión de base de datos y la cierra al finalizar la petición."""

    with Session(motor) as sesion:
        yield sesion
