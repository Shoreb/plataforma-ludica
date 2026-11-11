# STATE.md

Estado del proyecto. Léalo al iniciar cada sesión de trabajo y actualícelo al cerrarla.

## Estado actual

Repositorio publicado en GitHub con el CI en verde.
Página de inicio, /salud y /docs funcionando en https://plataforma-ludica-dfuw.onrender.com/
Endpoint GET /api/version implementado e integrado en main; responde con la versión definida en app.proyecto.VERSION y tiene una prueba con TestClient.

## Decisiones

| Fecha | Decisión | Motivo |
| --- | --- | --- |
| 2026-11-08 | Usar la plantilla del curso con FastAPI | Es el stack definido para el proyecto |
| 2026-11-10 | Completar AGENTS.md y STATE.md
| 2026-11-11 | Exponer GET /api/version con respuesta {"version": ...} | Permite consultar la versión desde la constante central app.proyecto.VERSION; el contrato se verifica con TestClient. |

## Siguiente paso

Documentar GET /api/version en el contrato de API de specs/plan.md y definir la siguiente tarea.
