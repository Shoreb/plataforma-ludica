# Taller 8: especificación, modelo de datos y actividades

Curso: Lectura. Mecánica: Racha Diaria.

## Especificación

**Objetivo:** redactar specs/spec.md con las seis historias del MVP.
**Herramienta y modelo:** Copilot con el modelo mai-code-2-flash
**Prompt:** 

## Rol
Actúa como analista de requisitos de software.

## Objetivo
Redactar en `specs/spec.md` la especificación del MVP de la plataforma, con la estructura que ya tiene ese archivo.

## Contexto
Lee `AGENTS.md`, `specs/encargo.md`, `specs/ficha-mecanica.md`, `specs/dudas-encargo.md` y `specs/respuestas-cliente.md`. Cuando una respuesta del cliente contradiga un supuesto de `dudas-encargo.md`, prevalece la respuesta del cliente.

## Restricciones
- Incluye exactamente estas seis historias de usuario:
  - H1. El docente gestiona las actividades del curso.
  - H2. La plataforma inicia con contenido del curso.
  - H3. El niño entra con el código de la clase, su alias y un avatar.
  - H4. El niño resuelve una actividad y sabe de inmediato si acertó.
  - H5. La plataforma aplica la regla de la mecánica.
  - H6. El docente consulta el progreso de cada niño.
- Cada historia tiene al menos dos criterios Dado/Cuando/Entonces, con los valores exactos de `specs/respuestas-cliente.md`.
- Todas las actividades son preguntas con 3 o 4 opciones y una respuesta correcta. Los demás tipos de actividad del encargo van en la sección Fuera de alcance.
- Las dudas que no responde el cliente van en Dudas abiertas, con el supuesto de `dudas-encargo.md`.
- No agregues funcionalidades que no estén en los documentos.
- En la tabla de Dudas abiertas, la columna Respuesta del cliente se renombra como Supuesto, porque esas dudas no tienen respuesta del cliente.
- Modifica solo `specs/spec.md`.

## Formato de salida
Antes de escribir, muestra la lista de historias con sus criterios resumidos en una línea cada uno y espera mi aprobación.

## Ejemplo
H5. Como niño, quiero acumular una racha diaria al terminar actividades, para ganar más puntos y motivarme a practicar todos los días.
- Dado que el niño jugó ayer y tiene una racha actual de 2 días, cuando termina su primera actividad del día de hoy (fecha de Colombia), entonces su racha aumenta a 3 días y recibe 20 puntos.
- Dado que el niño ya terminó una actividad hoy, cuando completa una segunda actividad el mismo día, entonces su racha se mantiene igual y no suma puntos adicionales.

## Criterio de éxito
Las seis historias tienen al menos dos criterios cada una y ningún criterio usa términos vagos como rápido, fácil o adecuado.

**Resultado:** [qué produjo y qué criterios hubo que corregir]

## Modelo de datos

**Objetivo:** crear los modelos, app/db.py y el diagrama entidad-relación.
**Herramienta y modelo:** Copilot con el modelo gpt-6-luna.
**Prompt:** 
Rol
Actúa como desarrollador backend con experiencia en FastAPI y SQLModel.

Objetivo
Crear el modelo de datos del MVP y la conexión con la base de datos:

En app/modelos/init.py, los modelos de tabla Clase, Nino, Actividad, Pregunta e Intento, con los campos del contrato.

En app/db.py, la variable motor, la función crear_tablas() y la dependencia obtener_sesion(), que entrega una sesión por petición.

En app/main.py, un ciclo de vida (lifespan) que llame a crear_tablas() al iniciar la aplicación.

En specs/plan.md, el diagrama entidad-relación en Mermaid, dentro de la sección Modelo de datos.

Contexto
Lee AGENTS.md, specs/spec.md, specs/plan.md y app/main.py.

Contrato de datos:

Clase: id, nombre, codigo (texto de 6 caracteres, único).

Nino: id, alias, avatar, clase_id (clave foránea a Clase).

Actividad: id, titulo, descripcion (texto opcional, vacío por defecto), orden (entero).

Pregunta: id, enunciado, opciones (lista de textos), respuesta_correcta, actividad_id (clave foránea a Actividad).

Intento: id, nino_id, actividad_id, aciertos, total, duracion_segundos, fecha (fecha y hora).

Restricciones
Usa exactamente los nombres de clases y campos del contrato.

Guarda opciones en una columna JSON.

La URL de la base de datos se lee de la variable de entorno DATABASE_URL, con el valor por defecto sqlite:///./plataforma.db.

No agregues dependencias: sqlmodel ya está en requirements.txt.

No crees endpoints ni modifiques las pruebas.

Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos y espera mi aprobación.

Ejemplo
Pregunta(enunciado="En la oración «El perro corre en el parque», ¿qué hace el perro?", opciones=["Duerme", "Corre", "Come"], respuesta_correcta="Corre", actividad_id=1)

Criterio de éxito
python -m pytest -v pasa todas las pruebas existentes, ruff check . no reporta errores y el comando python -c "import app.main" termina sin errores. No dejes ningún servidor en ejecución. Si después de 3 intentos no se cumple, detente y explica el problema.
**Resultado:** [qué produjo y qué hubo que corregir]