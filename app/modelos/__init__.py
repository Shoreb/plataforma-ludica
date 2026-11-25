"""Modelos de datos de la plataforma."""

from datetime import datetime

from sqlalchemy import JSON, CheckConstraint, Column
from sqlmodel import Field, SQLModel


class Clase(SQLModel, table=True):
    """Grupo identificado por un código de acceso."""

    __table_args__ = (CheckConstraint("length(codigo) = 6", name="ck_clase_codigo_longitud"),)

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    codigo: str = Field(min_length=6, max_length=6, unique=True, index=True)


class Nino(SQLModel, table=True):
    """Niño asociado a una clase."""

    id: int | None = Field(default=None, primary_key=True)
    alias: str
    avatar: str
    clase_id: int = Field(foreign_key="clase.id")


class Actividad(SQLModel, table=True):
    """Actividad del curso."""

    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str | None = Field(default="", nullable=True)
    orden: int


class Pregunta(SQLModel, table=True):
    """Pregunta de una actividad con opciones de respuesta."""

    id: int | None = Field(default=None, primary_key=True)
    enunciado: str
    opciones: list[str] = Field(sa_column=Column(JSON, nullable=False))
    respuesta_correcta: str
    actividad_id: int = Field(foreign_key="actividad.id")


class Intento(SQLModel, table=True):
    """Resultado de un niño al completar una actividad."""

    id: int | None = Field(default=None, primary_key=True)
    nino_id: int = Field(foreign_key="nino.id")
    actividad_id: int = Field(foreign_key="actividad.id")
    aciertos: int
    total: int
    duracion_segundos: int
    fecha: datetime
