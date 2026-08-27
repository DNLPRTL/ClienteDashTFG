# Borrador 4.7 — Diseño de la emulación de red y del perfil real del contenido

> BORRADOR para masticar y reescribir (25/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `core/reproduccion_trazas/` (modelo_red.py y
> descargador_controlado.py leídos enteros) + `perfiles_video/tamanos_segmentos/`
> (JSON reales inspeccionados) + `02_corpus_red\catalogo_trazas.json`.

---

### 4.7. Condiciones experimentales: la red y el contenido

Una sesión de streaming está gobernada por dos fuentes de variabilidad de
naturaleza distinta: la red, que determina cuándo llegan los bits, y el
contenido, que determina cuántos bits hay que traer para cada segmento.
Confundirlas, o fijar solo una de las dos, compromete la validez de cualquier
comparativa. El sistema las trata por separado, con un mecanismo propio para
cada una: la red se emula reproduciendo trazas de ancho de banda reales, y el
contenido se caracteriza midiendo el tamaño real de cada segmento en el
servidor.

**La red: reproducción de trazas.** Las condiciones de red de cada sesión
provienen de un corpus de 6768 trazas de throughput normalizadas a un esquema
común (instante, duración y ancho de banda disponible de cada intervalo). El
corpus procede de doce conjuntos de datos públicos con medidas de despliegues
reales —banda ancha fija del programa de medición de la FCC
\cite{fccMeasuringBroadbandAmerica}, movilidad 3G \cite{riiser2013commutePath},
redes 4G y 5G \cite{raca2018beyondThroughput4g, narayanan2020lumos5g}, entre
otros— completados con un bloque de trazas sintéticas controladas que solo se
usa con fines de diagnóstico. Un catálogo central describe cada traza y le
asigna una partición (entrenamiento, prueba o evaluación) por grupos
semánticos: todas las trazas de un mismo origen y contexto de captura caen en
la misma partición, de modo que ninguna condición de red vista durante el
entrenamiento del controlador propio reaparece en la evaluación. La
composición completa del corpus se detalla en el capítulo 6.

El mecanismo de emulación es el envoltorio del descargador presentado en el
apartado 4.3. Cada sesión recibe una ventana de una traza (300 segundos en la
evaluación) y un modelo de red la consume de forma continua: cuando el
cliente pide un segmento, el modelo integra la traza intervalo a intervalo
—entregando en cada uno tantos bytes como permite su ancho de banda— hasta
completar el tamaño pedido, y devuelve cuánto habría durado esa descarga. La
mecánica del envoltorio tiene un detalle importante: el segmento se descarga
de verdad del servidor, y después se retiene la entrega hasta cumplir la
duración que dicta la traza. Los bytes son siempre los reales del contenido;
lo que la emulación impone es su temporalidad. Además, la posición en la
traza avanza con el tiempo de la sesión: los periodos sin descarga (por
ejemplo, con el buffer lleno) también consumen traza, igual que en una red
real el tiempo no se detiene entre peticiones.

Dos decisiones completan el diseño. Primero, la política de fin es estricta:
si la ventana de traza se agota antes de completar una descarga, la sesión
falla y queda marcada; nunca se inventan condiciones de red. Segundo, cada
descarga emulada queda documentada en la telemetría con sus datos de
reproducción (posición en la traza, muestras usadas, throughput resultante),
de forma que puede auditarse que la sesión siguió su traza.

Esta emulación es aplicativa: actúa dentro del cliente, no en la pila de red
del sistema operativo. Frente a las alternativas de reproducción a nivel de
paquete \cite{netravali2015mahimahi}, ofrece determinismo completo,
portabilidad y ejecución sin privilegios, al precio de no modelar efectos de
nivel inferior como la latencia por paquete o el comportamiento de las colas;
esta limitación se recoge en el capítulo 6. La motivación de fondo es
conocida en la literatura: los resultados obtenidos en simulación heredan los
sesgos del simulador \cite{alomar2023causalsim}, así que el diseño acerca la
emulación todo lo posible a la física real —bytes reales, servidor real,
cliente real— y confina la parte emulada a la temporalidad de la red.

**El contenido: tamaños reales frente al supuesto de tasa constante.** El
razonamiento habitual "tamaño = tasa nominal × duración" es falso en
contenido real. La codificación es de tasa variable (VBR): el tamaño de cada
segmento depende de la complejidad de la escena, con desviaciones que en el
contenido de este trabajo alcanzan el 10% de variación típica en el vídeo
principal (y hasta el 16% en el contenido de animación), aunque la media por
representación sí se aproxima al valor nominal. Para un algoritmo que
planifica descargas, ese error importa exactamente donde más duele: en los
segmentos pesados que llegan cuando la red va justa.

Por ello, el sistema caracteriza el contenido con medidas, no con supuestos.
Una herramienta de extracción recorre por HTTP todos los segmentos de cada
vídeo publicado (906 sondas por perfil: 151 segmentos por 6 representaciones
en el vídeo principal) y escribe un descriptor JSON con el tamaño real de
cada segmento de cada representación, el segmento de inicialización y los
metadatos del perfil. Estos descriptores tienen dos consumidores: el
entrenamiento del controlador propio, cuyo simulador de sesiones descarga
segmentos con sus pesos reales en lugar de pesos nominales, y su
planificador en ejecución, que estima el tiempo de descarga del segmento
concreto que viene a continuación con su tamaño verdadero. Los controladores
clásicos no utilizan esta información, porque sus algoritmos originales no
la contemplan; y conviene subrayar que las sesiones descargan siempre los
bytes reales del servidor, de modo que el descriptor no altera ninguna
sesión: es conocimiento del contenido puesto a disposición de quien sabe
usarlo.

Esta asimetría informativa —el controlador propio conoce los tamaños reales y
los clásicos no los usan— merece justificación explícita, porque podría
parecer una ventaja artificial. No lo es, por tres razones. Primera: el
tamaño de los segmentos es una propiedad estática del contenido, consultable
por cualquier cliente en un despliegue real (los índices de segmentación la
anuncian y una petición de cabecera HTTP la obtiene sin descargar el
segmento); no es información del futuro de la red, que sigue siendo
inobservable para todos los controladores por igual. Segunda: emplearla es
práctica establecida. La formulación original del MPC ya expresa el tiempo de
descarga en función del tamaño de cada segmento según su calidad, advierte de
que en codificación VBR ese tamaño varía entre segmentos y señala como
carencia del estándar que el manifiesto no los anuncie \cite{yin2015mpc}; las
redes neuronales de Pensieve reciben los tamaños de los segmentos entre sus
observaciones \cite{mao2017pensieve}; y el sistema desplegado en Puffer
predice el tiempo de transmisión de cada segmento a partir de su tamaño real,
en lugar de suponerlo proporcional a la tasa nominal \cite{yan2020puffer}.
Tercera: los baselines se mantienen deliberadamente fieles a sus
formulaciones publicadas —el basado en tasa y BBA no contemplan tamaños;
BOLA y los MPC emplean el valor nominal—, porque modificarlos convertiría la
comparativa en una entre variantes propias sin respaldo bibliográfico. El
efecto de la diferencia está además acotado: la media real por
representación coincide con la nominal (desviación del 0,4%), de modo que el
supuesto nominal no está sesgado, solo ignora la varianza entre segmentos; y
el resultado del capítulo 6, donde la variante robusta del MPC empata en
calidad media con el controlador propio, confirma que la comparativa no deja
indefensos a los clásicos.

La Figura 4.6 resume los dos planos y su independencia.

**[FIGURA 4.6 — Los dos ejes de las condiciones experimentales. Fichero:
`figuras/fig_4_6_red_y_medio.svg`]**
*Pie: Figura 4.6: Los dos ejes de las condiciones experimentales: la red se
emula reproduciendo una ventana de una traza real (los bytes se descargan del
servidor; la traza impone su temporalidad) y el contenido se caracteriza con
los tamaños reales de cada segmento, medidos en el servidor.*

*(El apartado 4.8 cierra el capítulo con la separación entre ejecución y
evaluación.)*

---

### Notas para Daniel (no van a la memoria)

- Citas usadas (9): fccMeasuringBroadbandAmerica, riiser2013commutePath,
  raca2018beyondThroughput4g, narayanan2020lumos5g (corpus, representativas),
  netravali2015mahimahi (alternativa a nivel de paquete),
  alomar2023causalsim (sesgo del simulador) + AÑADIDAS 27/08 en el párrafo de
  justificación: yin2015mpc, mao2017pensieve, yan2020puffer. El corpus
  COMPLETO con sus 12 datasets y conteos va en 6.3 (T7).
- PÁRRAFO DE JUSTIFICACIÓN (añadido 27/08 tras tu pregunta "¿no es trampa?"):
  VERIFICADO contra los PDF originales (norma PDF-primero). Citas textuales
  por si el tribunal aprieta:
  · Yin 2015: "Let dk(Rk) be the size of chunk k encoded at bitrate Rk...
    in variable bitrate (VBR) case the dk ~ Rk relationship can differ
    across chunks" + "a key requirement for any control algorithms is to
    know the size (in bytes) of each video chunk, but the standard does not
    mandate the manifest to report chunk sizes, which may be a key
    shortcoming of the current specification". EL PAPER DEL MPC dice que
    conocer tamaños es requisito clave y su ausencia una carencia del
    estándar → tu extractor la resuelve.
  · Pensieve: la red mapea "raw observations (e.g., throughput samples,
    playback buffer occupancy, video chunk sizes)".
  · Puffer/Fugu: el TTP "predicts transmission time given a chunk's file
    size (vs. estimating throughput)... rather than modeling transmission
    time as scaling linearly with chunk size".
  Respuesta-resumen de defensa: "uso información estática del contenido,
  disponible para cualquier cliente y usada por Yin, Pensieve y Fugu; los
  clásicos se quedan como los publicaron sus autores para no comparar contra
  variantes mías; la media real coincide con la nominal (±0,4%) así que el
  nominal no está sesgado; y robust_mpc empata conmigo, prueba de que no
  queda indefenso". Reaparece como limitación honesta en 6.7 (una frase).
- Verificado en código/datos: ModeloRedPorTraza integra la traza muestra a
  muestra (kbps→bytes/s × duración útil) y devuelve duración exacta +
  throughput medido; politica_fin=fail (lanza error si la traza se agota);
  el envoltorio descarga PRIMERO los bytes reales, calcula la duración según
  la traza y duerme la diferencia (con_esperas); la posición en la traza =
  tiempo de sesión (inicio_replay = ahora − inicio_reloj_replay) → los
  huecos consumen traza; columnas replay_* en la info → telemetría.
- Números VBR REALES (del JSON del perfil): paseo 30fps vbr_cv_max=0.0977
  (~10%), 151 segmentos, 906 sondas, rep 300 kbps: nominal 150000 B, reales
  130643–167995 B, ratio media real/nominal = 1.0036. El "hasta 16%" es de
  los perfiles Blender (vbr_cv_max≈0.16, doc de componentes). Si quieres el
  cv exacto de Blender para el texto, lo saco del JSON en un momento.
- El párrafo "bytes reales, servidor real, cliente real; lo emulado es la
  temporalidad" es la BALA de la defensa contra "tu entorno es un simulador".
  Interiorízalo: es la respuesta entera en una frase.
- Frontera: el corpus detallado y las tablas de vídeos van en 6.3; la
  garantía anti-fuga completa (splits) reaparece en 4.8/6.1; el uso del
  descriptor por el planificador se desarrolla en 5.6/5.7.
- Longitud: ~950 palabras (apartado denso; es la aportación metodológica).
