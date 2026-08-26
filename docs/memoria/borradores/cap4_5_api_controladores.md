# Borrador 4.5 — Diseño de la interfaz común de controladores ABR

> BORRADOR para masticar y reescribir (25/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `core/controladores/` del entregable (contrato.py, base.py,
> registro.py, mascara_acciones.py leídos enteros; feedback_reproductor.py).

---

### 4.5. Interfaz común de los controladores ABR

El objetivo central del sistema es comparar algoritmos de adaptación en
igualdad de condiciones. Eso solo es posible si todos los controladores
observan exactamente la misma información y actúan a través del mismo canal.
Este apartado define esa frontera: qué ve un controlador, qué devuelve y qué
garantías impone el cliente alrededor de la decisión.

**El contrato de realimentación.** En cada iteración del bucle de sesión, el
reproductor construye un diccionario de realimentación con un conjunto cerrado
de veinte claves, siempre las mismas y en el mismo orden. Su contenido se
agrupa en cuatro bloques (Tabla 4.5): el estado del buffer, la escalera de
calidades, el resultado de la última descarga y el progreso de la sesión. La
estimación de ancho de banda incluida es deliberadamente simple (tamaño de la
última descarga dividido por su tiempo): las estrategias de estimación más
elaboradas, como las medias armónicas o los modelos de predicción, pertenecen
a cada controlador, no al cliente, de modo que cada algoritmo trabaja con la
señal cruda que asume su diseño original.

Tan importante como lo que el contrato incluye es lo que excluye. El
controlador no recibe ninguna información sobre la identidad de la traza de
red que se está reproduciendo, ni sobre la partición experimental a la que
pertenece, ni sobre la dificultad de la ventana, ni —evidentemente— sobre el
futuro del throughput. Solo observa lo que un reproductor real podría
observar en un despliegue de verdad. Esta restricción, que en el capítulo 6
se convierte en una de las garantías de validez de la comparativa, está
impuesta por construcción: la realimentación se genera en un único punto del
código y el filtrado al conjunto cerrado de claves es automático.

**El ciclo de decisión.** La interfaz de un controlador se reduce a dos
operaciones. Primero, recibir la realimentación. Segundo, calcular la acción
de control, que es una tasa binaria objetivo, un valor continuo en bytes por
segundo. El reproductor convierte después esa tasa en un nivel concreto de la
escalera mediante una cuantización común a todos los controladores: se elige
el escalón más alto cuya tasa nominal no supere el objetivo. Devolver una
tasa, y no directamente un nivel, es una decisión de diseño con dos ventajas:
los algoritmos clásicos de la literatura, que razonan en términos de tasa, se
trasladan al sistema tal como los describen sus artículos; y el redondeo a
nivel quedan centralizado, idéntico para todos, en lugar de repetido en cada
implementación.

El contrato admite una extensión opcional: un controlador puede declarar una
operación de ampliación de la realimentación, que el reproductor invoca si
existe. El controlador propio la utiliza para incorporar a la telemetría sus
entradas de contexto y sus diagnósticos internos. Los controladores clásicos
no la implementan y no se ven afectados: la extensión añade observabilidad
sin modificar la interfaz común.

**El registro de controladores.** Los controladores disponibles se declaran
en un registro central que asocia una clave de configuración con la fábrica
de cada implementación. El cliente instancia el controlador por nombre a
partir del fichero de configuración, con sus parámetros; añadir un algoritmo
nuevo consiste en implementar la interfaz y registrar una entrada, sin tocar
el reproductor. El registro del sistema contiene seis controladores: el
basado en tasa, los dos basados en buffer (BBA y BOLA), los dos de control
predictivo (MPC y su variante robusta) y el controlador propio. Sus diseños
se contextualizan en el capítulo 2 y su implementación se detalla en el
capítulo 5.

**Salvaguardas para controlares con modelo.** La interfaz descrita basta
para los algoritmos deterministas. Un controlador que decide con un modelo
aprendido introduce riesgos nuevos: puede producir una acción sin sentido,
tardar demasiado o fallar al cargar el modelo. El diseño añade para ese caso
una capa de salvaguardas alrededor de la decisión, con tres mecanismos: una
máscara de acciones válidas, que verifica que la acción elegida corresponde a
una representación existente y permitida (y que ofrece la menor acción válida
como alternativa segura); un controlador de respaldo clásico, al que se
delega la decisión si el modelo falla o excede un límite de latencia; y la
verificación de integridad del paquete del modelo en la carga. El resultado
queda registrado en la telemetría decisión a decisión, de forma que la
evaluación puede auditar cuántas decisiones tomó realmente el modelo. El
principio de diseño es que un controlador aprendido nunca puede invalidar
una sesión: en el peor caso, la sesión continúa con el comportamiento del
respaldo, y el hecho queda anotado. Los detalles de esta capa se desarrollan
con el controlador propio en el capítulo 5.

La Figura 4.5 resume la frontera completa: el ciclo de realimentación y
decisión, el contenido del contrato, lo que queda explícitamente fuera y las
salvaguardas.

**[FIGURA 4.5 — Interfaz común de los controladores. Fichero:
`figuras/fig_4_5_interfaz_controladores.svg`]**
*Pie: Figura 4.5: Interfaz común a todos los controladores: un contrato de
realimentación (divido en cuatro bloques), proceso de decisión con cuantización
en un solo punto del código, información descartada por razones de diseño y respaldo para
controladores que usen modelos predictivos.*

**[TABLA 4.5 — Contrato de realimentación de los controladores]**

| Los cuatro bloques | Claves | Aporte en la decisión |
|---|---|---|
| Estado del buffer | ocupación en segundos y bytes | margen existente antes de que ocurra una parada |
| Escalera de calidades | tasas disponibles, tasa y nivel del momento actual,nivel máximo y mínimo, duración en segundos del segmento | El grupo de acciones disponible |
| Última descarga realizada | tamaño, tiempo usado, estimación base del ancho de banda, instantes en los que sucede la petición | La señal de red que se observa |
| Estado de la sesión | índice de cada segmento, numero total de segmentos, bytes acumulados | En que punto está la sesión y cuanto le resta para finalizar |

*Pie: Tabla 4.5: Los cuatro bloques del contrato de realimentación que el reproductor
envía al controlador en cada una de las decisiones.*

*(El apartado 4.6 continúa con la telemetría y el registro de la sesión.)*

---

### Notas para Daniel (no van a la memoria)

- Citas: NINGUNA en este apartado (los papers de cada algoritmo se citan en
  2.4 y 5.5; aquí solo se nombran). Si prefieres, puedes citar aquí también,
  pero recargarías un apartado que es 100% diseño tuyo.
- Verificado en código: `CLAVES_REALIMENTACION` = 20 claves (contrato.py);
  el filtrado automático está en feedback_reproductor.py (la última línea
  construye el dict SOLO con esas claves); interfaz = fijarFeedbackReproductor
  + calcularAccionControl + cuantizarTasa (base.py; cuantizar_tasa_a_nivel =
  escalón más alto ≤ objetivo); registro con 6 fichas y crear_controlador por
  clave (registro.py); máscara (construir/validar/comprobar/menor_accion_valida
  en mascara_acciones.py). El respaldo/latencia/hashes son parámetros reales
  del controlador propio (config: controlador_respaldo=mpc_robusto,
  latencia_max_inferencia_ms=50, verificar_hashes=true) — los números van en
  el cap 5.6, aquí solo el mecanismo.
- La frase "en el mismo orden" importa: las claves ordenadas hacen estable la
  cabecera del CSV de telemetría (enlaza con 4.6).
- El bloque "lo que excluye" es LA garantía anti-fuga del diseño. En la
  defensa, si preguntan "¿cómo sabes que tu modelo no hace trampa?": la
  respuesta empieza aquí (contrato cerrado) y termina en 4.8/6 (auditoría).
- bwe simple = tamaño/tiempo de la ÚLTIMA descarga (feedback_reproductor.py).
  La media armónica la hace basado_en_tasa por dentro; el predictor del propio
  usa su propia historia. Cada uno su señal — tal cual sus papers.
- Longitud: ~900 palabras (apartado denso; es el corazón del capítulo).
