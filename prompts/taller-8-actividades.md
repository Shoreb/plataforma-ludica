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