# AGENTS.md

Contexto del proyecto para los agentes de IA. Léalo antes de cualquier cambio.

## Proyecto

Plataforma web lúdica de cursos para niños. Curso: Lectura. Mecánica: Racha diaria.
Roles: docente y Niño. Entra con código de clase y avatar, sin correo.

## Stack

- Python 3.11 o superior, FastAPI, plantillas Jinja2
- SQLModel: SQLite en desarrollo, PostgreSQL al publicar
- pytest con TestClient, Ruff
- GitHub Actions (CI) y Render (despliegue)

## Comandos

- Instalar: `pip install -r requirements-dev.txt`
- Ejecutar: `uvicorn app.main:app --reload`
- Probar: `pytest -v`
- Estilo: `ruff check .`

## Estructura

- `app/rutas/api.py`: endpoints REST (documentación en /docs)
- `app/rutas/paginas.py`: páginas HTML con Jinja2 (raíz /)
- `app/servicios/`: regla de negocio
- `app/modelos/`: tablas SQLModel
- `app/proyecto.py`: APRENDIZ, CURSO, MECANICA, VERSION (no modificar valores sensibles)
- `tests/`: unitarias; `tests/aceptacion/`: criterios de especificación

## Convenciones

- Al iniciar cada sesión, leer STATE.md.
- Nombres en español, claros y completos.
- Una tarea por rama; escribir prueba antes del código.
- Leer `app/proyecto.py` para datos del proyecto.

## Qué no hacer

- No escribir claves ni contraseñas en el código: se leen de variables de entorno (.env).
- No instalar dependencias sin verificar que existen en pypi.org.
- No modificar ni borrar pruebas para que pasen.
- No usar datos personales reales.
- No hacer commit ni push: los hace el desarrollador.

## Lecciones aprendidas

- Revisar que la app arranca el CI (`/salud` endpoint) antes de fusionar.
- Los fixtures del TestClient usan `app.main:app`.
