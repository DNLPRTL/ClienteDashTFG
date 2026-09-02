# Borrador 5.2 — El cliente: sesión, movimiento de datos y reproducción de trazas

> BORRADOR para masticar y reescribir (02/09/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`
> (este apartado no introduce ninguna nueva; ver notas).
> Fuente técnica: entregable — `main.py`, `reproductor.py`, `core/descargador.py`,
> `core/motores/simulado.py`, `core/feedback_reproductor.py`, `core/fases_sesion.py`
> y `core/reproduccion_trazas/` (los cinco módulos), leídos enteros el 02/09.

---

### 5.2. El cliente: sesión, movimiento de datos y reproducción de trazas

El capítulo 4 estableció qué hace cada módulo del cliente y por qué. Este
apartado describe cómo están construidos: el montaje de una sesión, la
mecánica del bucle de reproducción y su concurrencia, el descargador, y la
implementación de la emulación de red cuyo diseño se presentó en el
apartado 4.7.

**Montaje de una sesión.** El punto de arranque (`main.py`) convierte la
configuración en una sesión en marcha. Primero carga y valida el fichero de
configuración y crea el contexto de ejecución: el directorio de la sesión,
donde deja la configuración resuelta, la información del entorno (versión del
intérprete, plataforma, estado del repositorio y disponibilidad del motor
real) y un manifiesto de ejecución cuyo estado avanza por cuatro valores
(creado, en marcha, completado, fallido). Cualquier excepción durante la
sesión marca el manifiesto como fallido antes de propagarse: ninguna sesión
termina en un estado ambiguo. A continuación instancia las piezas: el
controlador, por su clave en el registro del apartado 4.5; el motor de
reproducción que indique la configuración; y el descargador. Si la
configuración activa la emulación de red, el descargador se envuelve en ese
momento con el descargador controlado por traza, al que se pasan la ruta del
fichero de la traza, la ventana (instante inicial y duración) y la política
de fin. El reproductor recibe todas las piezas ya construidas como
parámetros: no crea ninguna por sí mismo, de modo que cualquier componente
puede sustituirse (motor simulado o real, descarga directa o emulada) sin
tocar su código, y la emulación resulta invisible para él porque el
envoltorio ofrece exactamente la misma operación de descarga.

**El bucle de sesión y su concurrencia.** Una sesión son dos hilos. El hilo
principal ejecuta el bucle de segmentos; el motor de reproducción consume el
buffer en un hilo propio (apartado 4.4). La comunicación entre ambos tiene
dos sentidos: el bucle consulta la ocupación de la cola cuando la necesita, y
el motor notifica sus eventos (consumo, parada, recuperación) mediante una
función de aviso que el reproductor le registra al arrancar. Todas las
medidas de tiempo de la sesión (descargas, paradas, latencia de decisión) se
toman con el reloj monotónico del sistema, inmune a ajustes de la hora.

Antes de entrar en el bucle, el reproductor construye la lista de
reproducción a partir del contrato del analizador (apartado 4.2): ordena las
representaciones por tasa creciente para formar la escalera de niveles y
genera, por nivel, la secuencia de descargas. El segmento de inicialización
ocupa siempre el índice cero; si una representación no lo declara, se inserta
una entrada virtual de duración nula. Esta normalización mantiene los índices
alineados entre niveles y con las filas de la telemetría. El número de
segmentos de la sesión es el mínimo común entre niveles y puede recortarse
por configuración a un máximo de segmentos de vídeo; la evaluación del
capítulo 6 usa ese recorte para fijar sesiones de duración uniforme.

El cuerpo del bucle materializa el ciclo descrito en la Figura 4.2. Si la
ocupación supera el tope del buffer, el bucle espera en pasos fijos, con
salida anticipada en cuanto baja del umbral. Después descarga el segmento del
nivel vigente aplicando la política de robustez del apartado 4.3, con un
reparto estricto entre capas: el descargador agota sus reintentos de
transporte y, si fracasa, devuelve el fallo como resultado, no como
excepción; la espera exponencial, la degradación de nivel y el abandono del
segmento son decisiones del bucle. El segmento descargado se entrega al
motor y se construye la realimentación del contrato del apartado 4.5 en un
único punto del código; en la primera iteración, sin descargas previas, la
estimación de ancho de banda toma como valor neutro la tasa del nivel
vigente. Con la realimentación entregada, el controlador decide el nivel del
siguiente segmento (salvo en el primer segmento de vídeo, el calentamiento
del apartado 4.6), y el tiempo que tarda en decidir se mide y se anota en la
fila correspondiente.

La atribución de paradas a segmentos, cuyo criterio se definió en el
apartado 4.6, se implementa con una cola de índices: cada segmento entregado
al motor apunta su índice; el evento de consumo retira el más antiguo y
desencadena el volcado de su fila; y una parada abierta se atribuye al índice
en cabeza, que es el segmento que se estaba reproduciendo al agotarse el
buffer. Al terminar los segmentos, el bucle drena el buffer esperando a que
la cola quede vacía, con un límite de seguridad proporcional a lo encolado, y
cierra en orden: vuelca las filas aún pendientes, cierra los ficheros de
telemetría y detiene el motor.

**El descargador.** El descargador mantiene una única sesión HTTP persistente
durante toda la reproducción y descarga cada segmento completo en memoria; en
el contenido del experimento, los segmentos ocupan entre decenas de kilobytes
y algo más de dos megabytes, tamaños que no justifican una descarga por
fragmentos y que permiten medir el par tamaño-tiempo sin ambigüedad. Cada
petición sale con las cabeceras deliberadas del apartado 4.3 y admite rango
de bytes. El resultado de toda descarga es un par de datos e informe, con el
tamaño, el código de estado, los tiempos y el número de intento; ese informe
alimenta la realimentación del controlador y la telemetría. El descargador
ofrece además una consulta del tamaño de un fichero remoto, resuelta con una
petición de cabeceras y, si el servidor no la responde, con una petición de
rango de un solo byte; la necesita el esquema de direccionamiento por
fichero único del apartado 4.2.

**La reproducción de trazas.** La emulación de red se implementa en un
paquete propio con tres piezas: el cargador con su validación, el modelo de
red y el descargador controlado que los envuelve.

El cargador lee el fichero CSV de la traza y lo convierte en una estructura
inmutable de muestras (instante, duración, throughput). Ninguna traza entra
en una sesión sin superar la validación de la Tabla 5.2: el objetivo es que
un fichero corrupto produzca un error inmediato y explicable, nunca una
sesión con condiciones de red silenciosamente falsas. La validación calcula
además las estadísticas de la traza (mínimo, media, máximo y duración total)
y una huella criptográfica de su contenido, que la identifica con
independencia del nombre del fichero.

**[TABLA 5.2 — Validación de una traza de red]**

| Comprobación | Qué evita |
|---|---|
| Columnas obligatorias presentes (instante, duración, throughput) | Aceptar un CSV ajeno al esquema del corpus |
| Valores numéricos y finitos | Que un valor corrupto envenene la emulación |
| Instantes no negativos y no decrecientes | Una línea temporal incoherente |
| Duración de cada muestra positiva | Intervalos degenerados |
| Throughput no negativo | Caudales imposibles |
| Traza no vacía y con algún caudal positivo | Sesiones sin condiciones de red reales |

*Pie: Tabla 5.2: Comprobaciones que debe superar una traza antes de usarse en
una sesión. Un fallo detiene la sesión con un error explícito.*

Sobre la traza cargada se aplican dos transformaciones. La primera compacta
la línea temporal: los instantes se reescriben para que las muestras formen
una secuencia contigua desde cero. La segunda recorta la ventana de la
sesión, definida por su instante inicial y su duración; la muestra que cruza
un borde se recorta proporcionalmente. Ambas operaciones devuelven una traza
nueva que pasa otra vez por la validación completa y cuyo identificador
hereda el original con sufijos que documentan la transformación aplicada.

El modelo de red responde a una única pregunta: cuánto habría durado
descargar un número de bytes empezando en un instante dado de la ventana. La
Figura 5.1 ilustra el cálculo. El modelo recorre las muestras desde la
posición de partida; cada una puede entregar como máximo su caudal por su
duración útil; una muestra con caudal nulo consume su duración sin entregar
nada (un corte de red); y la muestra en la que se completa el tamaño pedido
se usa en fracción, dividiendo los bytes restantes entre su caudal, de modo
que la duración resultante es exacta y no depende de ninguna discretización.
El resultado incluye, junto a la duración y el throughput efectivo, la
posición inicial y final dentro de la traza y el número de muestras
consumidas. Si la ventana se agota antes de completar la entrega, el modelo
lanza un error de reproducción y la sesión queda marcada como fallida: es la
política de fin estricta del apartado 4.7.

**[FIGURA 5.1 — Emulación de una descarga sobre la ventana de traza.
Fichero: `figuras/fig_5_1_emulacion_descarga.svg`]**
*Pie: Figura 5.1: Emulación de una descarga (esquema). La posición en la
traza sigue al reloj de la sesión; la descarga entrega los bytes reales del
segmento y su duración se obtiene integrando la ventana de traza muestra a
muestra, con la última usada en fracción.*

El descargador controlado une el modelo con la descarga real. Al
construirse, al inicio de la sesión, ancla un reloj de reproducción; en cada
petición, la posición de partida en la traza es el tiempo de sesión
transcurrido desde ese anclaje, y de ahí que los periodos sin descarga
(esperas por buffer lleno, pausas del bucle) también consuman traza. La
petición se resuelve entonces en tres pasos: se descargan del servidor los
bytes reales del segmento; se pregunta al modelo cuánto debería haber durado
esa descarga; y se espera la diferencia, puesto que en la red local del
experimento la descarga real es muy inferior a la emulada. En el informe de
la descarga, los tiempos medidos se sustituyen por los emulados —que son los
que ven el controlador y la telemetría— y se añaden los campos de auditoría
del apartado 4.7: la ventana configurada, las posiciones inicial y final en
la traza, las muestras consumidas y el throughput resultante. Si la descarga
real fracasa, el envoltorio no consulta el modelo y propaga el fallo tal
cual: un error real nunca se disfraza de condición emulada.

*(El apartado 5.3 desciende a la implementación del analizador del MPD.)*

---

### Notas para Daniel (no van a la memoria)

- **Citas: NINGUNA.** Decisión deliberada: el apartado es implementación
  100% propia; los papers de emulación (mahimahi, causalsim) ya se citaron
  en 4.7 con el diseño, y el plan maestro no asigna bibliografía al 5.2.
- **Verificado en código (02/09), por si el tribunal aprieta:**
  · Estados del manifiesto: creado/en_marcha/completado/fallido
    (`main.ejecutar_cliente`; el except escribe "fallido" y relanza).
  · Entorno registrado: python, plataforma, git (commit y si hay cambios),
    disponibilidad de GStreamer y rutas de herramientas
    (`contexto_ejecucion.py`).
  · Init virtual: si la representación no trae init, se inserta entrada con
    duración 0 (`reproductor.run`); índice 0 = init SIEMPRE.
  · Recorte de sesión: `max_segmentos_video` cuenta solo segmentos de vídeo
    (los init no computan); el valor de la evaluación (30) va en el cap 6.
  · Espera de buffer: pasos de `PASO_VACIADO_S` con salida anticipada
    (`break` si la ocupación baja del tope).
  · Robustez: descargador devuelve `(None, info_error)` tras agotar sus 3
    reintentos (NUNCA lanza); el bucle aplica espera `min(0,5·2^n, 10)` s,
    baja de nivel tras 6 intentos y, en el nivel 0, abandona el segmento.
  · Cola de índices: `_cola_reproduccion` (deque); consumo → `popleft` +
    volcado; stall abierto → se atribuye a `[0]` (el que se reproduce).
  · Drenaje: espera hasta cola < 0,01 s con límite `max(5, cola+5)` s.
  · Realimentación: `construir_realimentacion_controlador` filtra al final
    a `CLAVES_REALIMENTACION`; sin descarga previa, `bwe` = tasa del nivel
    vigente (arranque conservador).
  · Validación de trazas: columnas exactas `tiempo_s,duracion_s,
    throughput_kbps`; finito; `tiempo_s>=0` y no decreciente; `duracion_s>0`;
    `throughput_kbps>=0`; no vacía; el MODELO exige además alguna muestra >0.
    Estadísticas + huella SHA-256 (formato canónico `%.9f,%.9f,%.9f\n`).
  · Transformaciones: `compactar_tiempos_traza` y `recortar_ventana_traza`
    RE-validan (pasan por `cargar_filas_traza_normalizada`) y anotan sufijos
    en el id (`:compact_timeline`, `:window_<ini>_<dur>s`).
  · Modelo: integración por muestras con hueco→avanza reloj, caudal 0→
    consume duración, última muestra en fracción (`restantes/Bps`);
    kbps→bytes/s = ×1000/8; `politica_fin=fail` lanza `ErrorReplayTraza`
    (existe `loop` con `max_bucles`, no usada en la evaluación).
  · Envoltorio: ancla `perf_counter()` al construirse; posición = ahora −
    anclaje; descarga real primero; `sleep(duracion_modelo −
    transcurrido_real)` si `con_esperas`; sobrescribe
    `transcurrido_total/carga` y añade `replay_*`; fallo real → propaga sin
    emular. `obtener_tamano_fichero` delega SIN consumir traza (metadatos;
    solo lo usa el esquema de fichero único, que no es el del experimento).
  · Tamaños reales de segmento (perfil paseo 30 fps): 11,7 KB–174 KB en la
    representación de 300 kbps y 168 KB–2,47 MB en la de 4300 kbps (el
    mínimo pequeño es el segmento residual de 0,1 s) — respaldan la frase
    "decenas de kilobytes a algo más de dos megabytes".
- **Detalle que el texto NO cuenta** (por si lees el código): el contrato de
  controladores incluye `obtenerDuracionInactividad` (pausa entre
  iteraciones, 1 s por defecto en la base) y el bucle la respeta, pero LOS
  SEIS controladores la fijan a 0. Sin efecto en el experimento; contarlo
  solo abriría preguntas. Si sale: "mecanismo del contrato para ritmos de
  sondeo pausados; ningún controlador de la comparativa lo usa".
- **Argumentos de defensa del apartado:**
  · "Los fallos viajan como valores, no como excepciones: el transporte no
    decide política" (frontera descargador/bucle).
  · "La posición en la traza es el reloj de la sesión": una sola frase
    explica por qué el buffer lleno consume traza (fidelidad temporal).
  · "Un error real nunca se disfraza de condición emulada" (el envoltorio
    propaga los fallos reales sin tocar el modelo).
  · "La duración emulada es exacta: la última muestra se usa en fracción,
    sin redondeos de discretización".
- **Fronteras respetadas:** el parseo del `sidx` y el direccionamiento por
  fichero único (→5.3); el runner, el preset y la generación de configs por
  sesión (→5.4); qué trazas y ventanas se eligen (catálogo/selección →6.1 y
  6.3); los valores 60 s / 0,5 s / reintentos ya dados en T4.3 (no se
  repiten números aquí).
- **Figura 5.1:** verificada renderizada (sin solapes). Valores de la
  escalera ESQUEMÁTICOS (el pie lo dice: "esquema"); la mecánica dibujada es
  exactamente la del código (anclaje, integración, fracción final, corte a
  cero, fallo por ventana agotada, nota bytes reales/temporalidad).
- Longitud: ~1250 palabras. Si al masticar quieres recortar: el párrafo del
  descargador es el más comprimible (sus cabeceras ya se contaron en 4.3);
  no recortes la parte de reproducción de trazas, que es lo prometido en 4.7.
