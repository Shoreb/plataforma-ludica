# Especificacion

## Contexto

El cliente organiza clubes de lectura en colegios publicos y privados y quiere una plataforma web ludica para que los niños practiquen la comprension lectora entre una sesion del club y la siguiente. El MVP corresponde al curso de Lectura y utiliza la mecanica Racha diaria.

Los roles del MVP son docente y niño. El niño entra a una clase con su codigo, su alias y un avatar, sin correo electronico.

## Historias de usuario

### H1. Gestionar las actividades del curso

Como docente, quiero gestionar las actividades del curso, para ofrecer a mi grupo actividades con preguntas.

**Criterios de aceptacion**

- Dado que el docente crea una actividad del curso, cuando registra sus preguntas, entonces cada actividad contiene un minimo de 5 preguntas y cada pregunta tiene de 3 a 4 opciones y una sola respuesta correcta.
- Dado que el docente gestiona una actividad existente, cuando modifica su enunciado, sus opciones o su respuesta correcta, entonces la actividad conserva como minimo 5 preguntas y una sola respuesta correcta por pregunta.

### H2. Iniciar con contenido del curso

Como plataforma, quiero iniciar con contenido del curso, para que el MVP tenga datos utilizables desde el primer acceso.

**Criterios de aceptacion**

- Dado que la base de datos esta vacia, cuando se inicia la aplicacion, entonces carga una clase de ejemplo, 3 actividades de 5 preguntas del curso Lectura y 3 niños ficticios.
- Dado que la base de datos ya contiene datos, cuando se inicia la aplicacion, entonces no carga nuevamente la clase de ejemplo, las 3 actividades ni los 3 niños ficticios.

### H3. Entrar con codigo de clase, alias y avatar

Como niño, quiero entrar con el codigo de la clase, mi alias y un avatar, para comenzar a jugar sin correo.

**Criterios de aceptacion**

- Dado que el niño conoce el codigo de su clase, cuando escribe ese codigo y elige su alias de la lista de niños de la clase, entonces queda asociado a esa clase.
- Dado que el niño va a entrar a la plataforma, cuando elige uno de los avatares, entonces puede guardar el avatar identificado por colibri, tortuga, delfin, jaguar, buho o rana.

### H4. Resolver una actividad y conocer el resultado

Como niño, quiero resolver una actividad y saber de inmediato si acerté, para reconocer mis aciertos y errores.

**Criterios de aceptacion**

- Dado que el niño abre una actividad, cuando responde una pregunta con 3 o 4 opciones, entonces la plataforma indica de inmediato si su respuesta coincide con la unica respuesta correcta.
- Dado que el niño termina una actividad completa, cuando se registra el intento, entonces se guardan los aciertos, el total de preguntas, la duracion en segundos y la fecha.

### H5. Aplicar la regla de la mecanica

Como niño, quiero acumular una racha diaria al terminar actividades, para ganar puntos por practicar de manera sostenida.

**Criterios de aceptacion**

- Dado que el niño termina su primera actividad del dia, cuando completa esa actividad segun la fecha de Colombia, entonces gana 10 puntos y su racha actual pasa a 1 dia.
- Dado que el niño jugo ayer y mantiene su racha actual en 1 dia, cuando termina su primera actividad del dia de hoy segun la fecha de Colombia, entonces su racha actual pasa a 2 dias y gana 15 puntos.
- Dado que el niño mantiene una racha de 2 dias, cuando termina su primera actividad del tercer dia segun la fecha de Colombia, entonces su racha actual pasa a 3 dias y gana 20 puntos.
- Dado que el niño mantiene una racha de al menos 5 dias, cuando termina una actividad el siguiente dia segun la fecha de Colombia, entonces gana 35 puntos.
- Dado que el niño ya termino una actividad hoy, cuando completa una segunda actividad el mismo dia segun la fecha de Colombia, entonces su racha actual no aumenta y no gana puntos adicionales.
- Dado que el niño deja pasar un dia sin terminar ninguna actividad, cuando vuelve a jugar segun la fecha de Colombia, entonces su racha actual vuelve a 1 y conserva los puntos historicos ya reunidos.
- Dado que el niño juega varias veces o reinicia su racha, cuando se actualiza su progreso, entonces se conserva su racha actual y su racha mas larga.

### H6. Consultar el progreso de cada niño

Como docente, quiero consultar el progreso de cada niño, para identificar dificultades y revisar su participacion.

**Criterios de aceptacion**

- Dado que existen intentos registrados para un niño, cuando el docente consulta su progreso, entonces puede ver los aciertos, el porcentaje de aciertos calculado como aciertos dividido por el total de preguntas multiplicado por 100 y las actividades completadas sin repetir.
- Dado que existen intentos registrados para un niño, cuando el docente consulta su progreso, entonces puede ver la suma de la duracion en segundos de todos sus intentos, la racha actual, la racha mas larga y los puntos reunidos.

## Requisitos funcionales

| Codigo | Requisito | Historia |
| --- | --- | --- |
| RF1 | Permitir al docente crear, consultar y modificar actividades del curso con un minimo de 5 preguntas. | H1 |
| RF2 | Validar que cada pregunta tenga de 3 a 4 opciones y una sola respuesta correcta. | H1 |
| RF3 | Cargar una clase de ejemplo, 3 actividades de 5 preguntas y 3 niños ficticios solo cuando la base de datos esta vacia. | H2 |
| RF4 | Permitir al niño ingresar mediante el codigo de la clase, elegir su alias de esa clase y seleccionar uno de los 6 avatares. | H3 |
| RF5 | Mostrar la respuesta correcta o incorrecta inmediatamente despues de cada respuesta del niño. | H4 |
| RF6 | Registrar por intento los aciertos, el total de preguntas, la duracion en segundos y la fecha al terminar una actividad completa. | H4 |
| RF7 | Calcular la fecha de juego segun la zona horaria de Colombia y aplicar la racha diaria una vez por dia. | H5 |
| RF8 | Otorgar 10 puntos base, sumar 5 puntos extra por cada dia de racha a partir del segundo, con un maximo de 25 puntos extra, y conservar el total historico. | H5 |
| RF9 | Guardar la racha actual y la racha mas larga de cada niño. | H5 |
| RF10 | Calcular el tiempo de juego como la suma de las duraciones de los intentos y contar las actividades completadas sin repetir. | H6 |
| RF11 | Mostrar el porcentaje de aciertos como aciertos dividido por el total de preguntas multiplicado por 100. | H6 |
| RF12 | Mostrar al docente la racha actual, la racha mas larga y los puntos reunidos de cada niño. | H6 |

## Requisitos no funcionales

| Codigo | Requisito | Como se verifica |
| --- | --- | --- |
| RNF1 | Las preguntas deben tener exactamente una respuesta correcta. | Validar el modelo de datos y los intentos de respuesta antes de guardar la actividad. |
| RNF2 | Los intentos incompletos no deben registrarse como actividad terminada. | Completar una actividad y verificar que solo se cree el intento al finalizar todas sus preguntas. |
| RNF3 | Las fechas de juego deben evaluarse con la fecha de Colombia, no con la fecha del dispositivo o del servidor. | Ejecutar pruebas con una fecha de Colombia y verificar racha y puntos. |

## Casos limite

- Cada actividad debe tener como minimo 5 preguntas.
- Una pregunta puede tener 3 o 4 opciones.
- Un niño puede completar varias actividades el mismo dia, pero solo cuenta una vez para la racha y los puntos diarios.
- La racha vuelve a 1 cuando el niño deja pasar un dia sin jugar.
- Los puntos historicos se conservan cuando la racha se reinicia.
- El dia 1 otorga 10 puntos, el dia 2 otorga 15 puntos, el dia 3 otorga 20 puntos y el bono extra tiene un limite de 25 puntos. Por tanto, a partir del dia 6 el total diario es 35 puntos.
- Los avatares permitidos son colibri, tortuga, delfin, jaguar, buho y rana.
- Un intento registra aciertos, total de preguntas, duracion en segundos y fecha solo cuando el niño termina la actividad completa.

## Fuera de alcance

- Actividades que no sean preguntas con 3 o 4 opciones y una sola respuesta correcta.
- Ordenar tres imagenes segun lo ocurrido en el cuento.
- Actividades de opinion sin una sola respuesta correcta.
- Actividades o contenidos que no pertenezcan al curso de Lectura.
- Gestionar multiples tipos de mecanica dentro del MVP.

## Criterios de terminado

- Las seis historias de usuario tienen al menos dos criterios Dado/Cuando/Entonces.
- Cada actividad tiene como minimo 5 preguntas, de 3 a 4 opciones y una sola respuesta correcta.
- El contenido inicial se carga una sola vez, exclusivamente sobre una base de datos vacia.
- El niño puede entrar con codigo de clase, alias y uno de los 6 avatares.
- Cada respuesta registrada indica correctamente si fue acertada.
- Los intentos completos guardan aciertos, total de preguntas, duracion en segundos y fecha.
- La racha, los puntos y las rachas actual y mas larga cumplen la regla de Racha diaria.
- El docente puede consultar las metricas de progreso por niño.
- Las pruebas de aceptacion cubren los criterios de las seis historias.

## Dudas abiertas

| Duda | Supuesto |
| --- | --- |
| ¿En que consiste la ayuda que la plataforma debe ofrecer a los niños que leen despacio? | Se ofrece la opcion de audiolibro o de resaltado guiado de palabras. |
| ¿El docente elige los cuentos para todo el grupo o puede asignarlos de manera distinta a cada niño? | Se asignan al grupo en general, con opcion de personalizacion individual. |
| ¿Que se considera dificultad y como se determina en que tipo de pregunta se presenta? | La dificultad se define como un porcentaje de aciertos menor al 50% en una categoria de pregunta. |
| ¿Que ocurre con los puntos ya reunidos cuando la racha se reinicia? | Los puntos historicos totales se conservan; solo el contador de dias seguidos vuelve a cero. |
| ¿La racha actual y la mas larga se calculan por niño en general o por curso o grupo? | Se calculan por el perfil global del niño en la plataforma. |
| ¿El codigo de clase identifica a un grupo, a un docente o a una clase especifica, y que ocurre si un niño tiene mas de una clase? | Identifica a un grupo especifico y el niño puede asociar varios codigos a su perfil. |
ss