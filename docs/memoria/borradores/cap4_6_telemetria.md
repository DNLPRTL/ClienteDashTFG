# Borrador 4.6 — Diseño de la telemetría y el registro de sesión

> BORRADOR para masticar y reescribir (25/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `core/esquema_telemetria.py` y `core/artefactos_salida.py`
> (leídos enteros) + `reproductor.py` (derivadas, fases, volcado) +
> `core/fases_sesion.py` + `core/contexto_ejecucion.py`.

---

### 4.6. Telemetría y registro de sesión

La telemetría es el único puente entre la ejecución de una sesión y su
evaluación posterior. Por diseño, el análisis del capítulo 6 no accede nunca
al estado interno del cliente: todo lo que se sabe de una sesión está en los
ficheros que esta deja al terminar. Eso convierte el esquema de telemetría en
un contrato tan importante como el de la realimentación: define qué queda
registrado, con qué nombre y con qué garantías.

**Artefactos por sesión.** Cada sesión produce un directorio propio con seis
ficheros: un manifiesto de ejecución con el estado final (creado, en marcha,
completado o fallido), la configuración resuelta con la que se ejecutó, la
información del entorno, el registro de texto de la ejecución y dos ficheros
CSV: la telemetría de segmentos, que es el registro principal, y un resumen
de segmentos para evaluación. Con la configuración resuelta y el manifiesto,
cualquier sesión es auditable y repetible a partir de sus propios artefactos.

**Esquema del registro principal.** La telemetría de segmentos contiene una
fila por segmento del vídeo y su cabecera se compone de cinco bloques en
orden fijo (Tabla 4.6): la identificación de la fila, la realimentación
completa que recibió el controlador en ese paso (cada clave del contrato del
apartado 4.5, con un prefijo que la identifica), los metadatos de la descarga
del segmento, un bloque de columnas derivadas y las medidas de parada. Dos
decisiones sostienen la fiabilidad del esquema. Primero, la cabecera se
valida al construirse (nombres únicos) y cada fila se valida al escribirse
(longitud exacta): una discrepancia detiene la sesión con un error, en lugar
de producir un fichero silenciosamente corrupto. Segundo, la cabecera se
construye dinámicamente a partir de las claves de la realimentación: si un
controlador declara la extensión del apartado 4.5, sus columnas adicionales
aparecen de forma automática. Así es como el controlador propio incorpora al
registro sus diagnósticos internos, que la evaluación audita después decisión
a decisión.

Registrar la realimentación completa tiene una lectura metodológica: el
registro contiene exactamente lo que el controlador vio en cada paso. Ante
cualquier decisión dudosa, puede reconstruirse la situación que la produjo.

**El volcado diferido de filas.** Una fila no se escribe cuando su segmento
se descarga, sino cuando el motor notifica que se ha consumido. El motivo es
la atribución correcta de las paradas: los stalls ocurren durante la
reproducción de un segmento, no durante su descarga, de modo que la fila de
cada segmento debe esperar a conocer las paradas que sucedieron mientras se
reproducía. Mientras la fila está pendiente, se completa también con la
decisión que el controlador tomó tras ese segmento (tasa objetivo, nivel
elegido y latencia de la decisión). El registro documenta así, en una misma
fila, la situación observada, la decisión tomada y las consecuencias sobre la
reproducción. Como salvaguarda de equidad, las paradas del último segmento
común no se contabilizan: el drenaje final del buffer no forma parte de la
dinámica que se compara.

**Dos clasificaciones de fase.** Cada fila incluye dos clasificaciones
complementarias del momento de la sesión, que conviene no confundir:

- **Fase de evaluación** (determinista, por posición): distingue
  inicialización, arranque (los primeros segundos de la sesión, la ventana
  de preroll del apartado 4.3), calentamiento (el primer segmento de vídeo,
  cuya calidad no eligió aún el controlador), régimen estable y vaciado.
  Solo los segmentos de régimen estable se marcan como utilizables para la
  evaluación: la métrica de calidad no premia ni castiga el transitorio
  inicial, que es idéntico en diseño para todos los controladores.
- **Fase de buffer** (descriptiva, por dinámica): un detector con histéresis
  clasifica cada instante como llenando, estable, vaciando o atascado, a
  partir de la evolución de la ocupación (umbral de atasco de 1,2 segundos;
  estabilidad exigida durante un mínimo sostenido). Estas dos columnas no
  filtran nada: describen la dinámica para el análisis posterior.

**El resumen de evaluación.** Junto al registro principal se escribe un
segundo CSV mínimo, con una fila por segmento y siete columnas (índice, si es
inicialización, fase de evaluación, marca de uso, tamaño, tiempo de descarga
y duración). Es la vista que consume el cálculo de la calidad de experiencia:
suficiente para computar la métrica y pequeña, sin arrastrar el esquema
completo.

**[TABLA 4.6 — Bloques del registro de telemetría]**

| Bloque | Contenido | Para qué sirve |
|---|---|---|
| Identificación | índice de segmento, marca de tiempo | Ordenar y cruzar filas |
| Realimentación (20 columnas) | copia exacta de lo que vio el controlador | Reconstruir cada decisión; transparencia |
| Metadatos de descarga | si es init, reintentos, instantes de petición, tiempo de sesión | Trazabilidad de la descarga |
| Derivadas | throughput instantáneo y suavizado, variabilidad reciente, buffer en segmentos, marcas de cambio de nivel, decisión de la política y su latencia, fases, marca de uso en evaluación | Análisis y filtrado posterior |
| Paradas | marca de stall y duración acumulada en el segmento | Componente de rebuffering de la QoE |

*Pie: Tabla 4.6: Bloques de columnas del registro de telemetría de segmentos.*

*(El apartado 4.7 continúa con la emulación de red por trazas y el perfil
real del contenido.)*

---

### Notas para Daniel (no van a la memoria)

- Citas: NINGUNA (diseño 100% propio).
- Verificado en código: cabecera = COLUMNAS_TELEMETRIA_FILA + feedback_* (las
  20 del contrato, prefijo en nombre_columna_realimentacion) +
  COLUMNAS_TELEMETRIA_SEGMENTO + COLUMNAS_TELEMETRIA_DERIVADAS +
  COLUMNAS_TELEMETRIA_STALL; validar_columnas_unicas + validar_longitud_fila
  (RuntimeError → sesión se detiene, no CSV corrupto); volcado diferido en
  _volcar_fila_segmento (dispara segmento_consumido); decisión rellenada a
  posteriori (_rellenar_politica_y_cambios); diagnósticos del propio entran
  como columnas feedback_* extra vía obtener_diagnosticos_red; stall del
  último segmento común forzado a 0 (equidad del drenaje).
- Derivadas concretas (si el tribunal pide detalle): tp_actual = tamaño/tiempo
  de la última descarga; tp_ewma con α=0,6; mín y desviación típica de los
  últimos 5; buffer_sobre_seg = ocupación/duración de segmento; margen =
  tp_actual/bitrate_actual. Detector de fases: atascado <1,2 s; estable si
  buffer >5 s con desviación ≤0,3 s sostenido ≥15 s (readmisión rápida si
  vuelve antes de 10 s).
- "calentamiento" = exactamente 1 segmento (segmentos_calentamiento=1): el
  primer segmento de vídeo se descarga al nivel inicial y el controlador
  decide a partir del segundo. Coherente con lo contado en F4.2 (paso 5).
- La frase sobre "reconstruir la situación que produjo una decisión" es tu
  respuesta a "¿cómo depuras un comportamiento raro del controlador?".
- Longitud: ~850 palabras. Sin figura (F4.2 + la tabla cubren; regla de no
  poner figuras decorativas).
