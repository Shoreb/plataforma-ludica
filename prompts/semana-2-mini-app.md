# Mini-aplicación de práctica: Generador de contraseñas

## Versión A
**Objetivo:** construir la mini-aplicación con un prompt de una línea.
**Herramienta y modelo:** Copilot con el modelo GPT-6 luna.
**Prompt:** 
```text
Haz una app web que genere contraseñas con FastAPI.
```
**Resultado:** Aplicación web para generar contraseñas aleatorias con FastAPI., pruebas aprobadas: 0 de 7 y errores de Ruff: Estructura del proyecto

## Versión B
**Objetivo:** construir la misma aplicación con un prompt estructurado, AGENTS.md y
pruebas de aceptación.
**Herramienta y modelo:** Copilot con el modelo GPT-6 luna.
**Prompt:** 
```text
## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con
pytest.

## Objetivo
Construir la mini-aplicación web Generador de contraseñas con estos requisitos:

1. GET / muestra un formulario para elegir la longitud y si se incluyen números y
símbolos, un botón para generar y un botón para copiar la contraseña.
2. GET /api/contrasena recibe los parámetros longitud, numeros y simbolos, y devuelve
{"contrasena": texto, "longitud": número}. Valores por defecto: longitud 12, numeros
true y simbolos false.
3. La contraseña siempre incluye letras minúsculas y mayúsculas. Si numeros es true,
incluye al menos un número; si es false, no incluye ninguno. Si simbolos es true,
incluye al menos un símbolo de este grupo: !@#$%&*?-_ ; si es false, no incluye
ninguno.
4. La longitud debe estar entre 8 y 64; fuera de ese rango responde con el código
422.
5. La contraseña se genera con el módulo secrets de Python, no con random.

## Contexto
Lee AGENTS.md. El contrato de la API está en tests/test_aceptacion.py: las rutas, los
nombres de los campos y los códigos de estado deben coincidir con esas pruebas.

## Restricciones
- Usa solo las dependencias de requirements.txt.
- Define las rutas en app/main.py y la lógica en app/servicios.py, sin importar
FastAPI en servicios.
- Guarda los datos en memoria, sin base de datos ni archivos.
- No modifiques tests/test_aceptacion.py.
- La página usa HTML, CSS y JavaScript sin librerías externas.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que
vas a crear y espera mi aprobación. Al terminar, resume en una línea qué hace cada
archivo.

## Ejemplo
GET /api/contrasena?longitud=16&numeros=true&simbolos=true devuelve:
{"contrasena": "q7G!mR2-xW9a#Lp4", "longitud": 16}

## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check . no reporta errores. Si
después de 3 intentos las pruebas no pasan, detente y explica el problema.
```
**Resultado:** mini-aplicación web Generador de contraseñas,  cuántos intentos necesitó: ninguno, pruebas aprobadas: 7 de 7 y
errores de Ruff: Ninguno.

## Mejora
**Objetivo:** La mejora añade un indicador visual de fuerza clasificado en tres niveles de color (rojo para débil, amarillo para media y verde para fuerte) según la longitud y complejidad de los caracteres.
**Herramienta y modelo:** Copilot con el modelo GPT-6 luna.
**Prompt:** 
```text
## 1. Rol
Actúa como un desarrollador backend y frontend con experiencia en FastAPI, Jinja2, HTML, CSS, JavaScript y pruebas automatizadas con pytest. Tu responsabilidad es implementar la mejora solicitada respetando la arquitectura y el funcionamiento actual del proyecto.

## 2. Objetivo
Implementar un indicador de fuerza de contraseña en la mini-aplicación web Generador de contraseñas.

La mejora debe cumplir las siguientes condiciones:

**Backend:**

- Modificar la respuesta de `GET /api/contrasena` para incluir un nuevo campo llamado `fuerza`.
- El campo `fuerza` debe calcularse de acuerdo con estas reglas:
- **Fuerte:** cuando la contraseña tenga una longitud de 16 caracteres o más e incluya números y símbolos.
- **Débil:** cuando la contraseña tenga menos de 12 caracteres o no incluya números ni símbolos (es decir, que no incluya ninguno de los dos).
- **Media:** en todos los demás casos.
- La respuesta JSON debe conservar los campos originales `contrasena` y `longitud`, agregando `fuerza` sin cambiar sus nombres ni eliminar información.

**Frontend:**

- La página principal debe mostrar la fuerza de la contraseña generada.
- El indicador debe actualizarse cada vez que se genere una nueva contraseña.
- Mostrar el indicador con los siguientes colores:
- Rojo para fuerza débil.
- Amarillo para fuerza media.
- Verde para fuerza fuerte.
- El indicador debe ser fácil de identificar y comprender para el usuario.

## 3. Contexto
La aplicación existente se encuentra en la carpeta `mini-app-b`.

Antes de realizar cualquier cambio:

- Lee el archivo `AGENTS.md`.
- Revisa la estructura y el funcionamiento actual del proyecto.
- Examina `app/main.py`, `app/servicios.py` y los archivos de la interfaz.
- Revisa `tests/test_aceptacion.py` para conocer el contrato original de la API.

La mejora debe integrarse sobre la aplicación existente, conservando sus funcionalidades y respetando los requisitos originales.

## 4. Restricciones
- Utiliza únicamente las dependencias declaradas en `requirements.txt`.
- Mantén las rutas de FastAPI en `app/main.py`.
- Mantén la lógica de generación y cálculo de fuerza en `app/servicios.py`, sin importar FastAPI en este archivo.
- No utilices bases de datos ni almacenamiento externo.
- No modifiques, elimines ni reemplaces `tests/test_aceptacion.py`.
- Crea una nueva prueba en `tests/test_mejora.py` para comprobar la funcionalidad solicitada.
- No elimines ni alteres las funcionalidades originales del generador de contraseñas.
- La interfaz debe utilizar HTML, CSS y JavaScript sin librerías externas.
- No realices cambios innecesarios en archivos que no estén relacionados con la mejora.

## 5. Formato de salida
Antes de escribir o modificar cualquier código, debes presentar un plan de implementación.

El plan debe incluir:

1. Una explicación de cómo implementarás el cálculo de la fuerza en el backend.
2. Cómo mostrarás y actualizarás el indicador de fuerza en la página principal.
3. Los archivos que crearás o modificarás, indicando sus rutas absolutas y completas.
4. La función específica que cumplirá cada archivo.
5. Las pruebas que ejecutarás para comprobar la mejora.

Después de presentar el plan, detente y espera mi aprobación explícita. No debes crear, modificar ni eliminar archivos antes de recibirla.

Una vez aprobada la implementación, realiza los cambios y, al finalizar, presenta un resumen de una línea por cada archivo creado o modificado, explicando su función.

## 6. Ejemplo
Una petición a la API:

`GET /api/contrasena?longitud=16&numeros=true&simbolos=true`

Debe devolver una respuesta con esta estructura:

`{"contrasena": "q7G!mR2-xW9a#Lp4", "longitud": 16, "fuerza": "fuerte"}`

En este caso, la contraseña tiene 16 caracteres e incluye números y símbolos, por lo tanto, su fuerza es fuerte.

Otro ejemplo:

`GET /api/contrasena?longitud=10&numeros=false&simbolos=false`

Debe devolver una respuesta donde el campo `fuerza` tenga el valor `débil`, porque la longitud es menor de 12 caracteres.

## 7. Criterio de éxito
La mejora se considerará terminada cuando se cumplan todas las condiciones siguientes:

- La API devuelve el nuevo campo `fuerza` junto con los campos originales `contrasena` y `longitud`.
- El cálculo de fuerza respeta exactamente las tres condiciones establecidas en el anexo.
- La página principal muestra el indicador con el color correspondiente: rojo, amarillo o verde.
- El indicador se actualiza correctamente al generar una nueva contraseña.
- Existe una nueva prueba en `tests/test_mejora.py` que comprueba los tres niveles de fuerza y sus condiciones.
- El archivo `tests/test_aceptacion.py` permanece sin modificaciones.
- Las funcionalidades originales de la aplicación continúan funcionando.

Para verificar la implementación, ejecuta:

`python -m pytest -v`

También ejecuta:

`ruff check .`

Ambos comandos deben finalizar sin errores.

Tienes un máximo de 3 intentos para corregir los errores encontrados. Si después del tercer intento las pruebas o Ruff siguen fallando, debes detenerte, informar los errores pendientes y explicar qué archivos necesitan atención. No debes continuar modificando el proyecto indefinidamente.
```
**Resultado:** [qué produjo y qué hubo que corregir]

## Comparación
Pruebas aprobadas: todas, requisitos cumplidos: todos y errores de Ruff de cada versión: ninguno, y la
conclusión de la actividad 4: 

La mayor diferencia  fueron los requisitos y restricciones, porque asi el agente dio unos resultados mas precisos y cercanos a lo que se queria lograr, no como el prompt A de una sola linea donde el agente podia tomar sus propias decisiones y usar lo que el quisiera, en con el prompt B hubo una base mas solida y mejores resultados.

El agente tomo desiciones por su cuenta en importacion de dependencias, estructuras de archivos, logica mezclada y tambien los estilos y experiencia de usuario, ya que esto no se le pidio, por esta razon concluyo que en ell resultado del prompt B, creo un formulario sencillo con las tecnologias que se le pidio y no hizo una interfaz mas estilizada como en el prompt A, quiere decir que el agente acata las instrucciones y entiende las restricciones si se le da una buena instruccion, evitando asi que tome decisiones por su cuenta.

Para futuros encargos, dar un contexto estructurado y un conjunto de pruebas predefinidas para evitar código no deseado y retrabajo.