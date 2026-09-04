# Borrador 5.4 — Lanzador de experimentos y configuración

> BORRADOR para masticar y reescribir (04/09/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`
> (este apartado no introduce ninguna; ver notas).
> Fuente técnica: entregable — `scripts/3_evaluacion/ejecutar_evaluacion.py`,
> `gui_evaluacion.py`, `analizar_resultados.py`, `verificar_paquete.py`,
> `core/evaluacion/configuracion.py`, `catalogo.py`, `seleccion.py`,
> `core/configuracion_cliente.py`, `core/contexto_ejecucion.py`,
> `config/evaluacion.local.json` (leídos enteros el 04/09) + paquete canónico
> `04_evidencia_final\20260810_133520_tfg_final` (protocolo, 300 configs de
> sesión y ejecuciones inspeccionados).

---

### 5.4. Lanzador de experimentos y configuración

El apartado 4.8 definió el plan de experimento y la separación entre ejecutar
sesiones y evaluarlas. Este apartado describe el software que lo lleva a la
práctica: la capa de configuración, con sus dos niveles; el lanzador, que
convierte un experimento declarado en un paquete de evidencia; y la interfaz
gráfica desde la que se lanzó la evaluación final.

**Dos niveles de configuración.** El sistema distingue la configuración de
una sesión de la configuración de un experimento. La primera es la que
consume el cliente (`main.py`): un fichero JSON o YAML con ocho secciones
—dirección del manifiesto, motor de reproducción, controlador y sus
parámetros, reproducción, descargador, reproducción de trazas, salida y
registro— que se convierte en un objeto inmutable de clases de datos. La
conversión valida cada campo y cada regla cruzada con un mensaje que nombra
la clave afectada (por ejemplo, la ruta de la traza es obligatoria si la
emulación está activada, y la política de fin solo admite dos valores), de
modo que un error de configuración se detecta antes de tocar la red. Los
valores por defecto son los de la Tabla 4.3. La configuración resuelta —la
que resulta tras aplicar valores por defecto y conversiones— se archiva en el
directorio de cada sesión (apartado 4.6): lo que queda documentado es lo que
se ejecutó, no lo que se escribió.

La segunda es la configuración de la evaluación, que consume el lanzador. Sus
valores por defecto viven en el código y un fichero local los sobrescribe
mediante una mezcla profunda, clave a clave. Sus secciones fijan las rutas
(catálogo de trazas, raíz de salida, repositorio e intérprete, y una lista de
reescrituras de rutas para mover el corpus entre máquinas), el experimento
(preset, semilla, motor, controladores, perfiles de vídeo, inclusión de
ventanas sintéticas y repeticiones), los parámetros de reproducción y de
emulación que recibirán todas las sesiones, las opciones de ejecución (tiempo
límite por sesión, reanudación, si se ejecutan sesiones y análisis) y los
parámetros específicos de cada controlador. El fichero real de la evaluación
final ocupa cuarenta líneas: declara los cinco controladores, el preset, las
rutas y los parámetros del controlador propio; todo lo demás son valores por
defecto documentados en el código.

**Presets: el tamaño del experimento en una palabra.** Un preset es una
especificación cerrada del tamaño y las condiciones de un experimento
(Tabla 5.4): cuántas ventanas de red reales y sintéticas se seleccionan, qué
vídeos participan, cuántos segmentos dura cada sesión, cuánto dura la ventana
de traza, cuál es el tiempo límite de una sesión y si el experimento queda
habilitado para comparar y ordenar controladores. Los presets forman una
escalera: los tres primeros son pruebas de humo y diagnóstico y no habilitan
comparación alguna; los tres últimos sí, y solo con el motor simulado. El
preset sobrescribe los parámetros de reproducción y emulación que le
corresponden, y su especificación efectiva queda escrita en el protocolo del
paquete. La evaluación del capítulo 6 empleó el preset final de la tabla,
cuyo producto (15 ventanas, cuatro vídeos y cinco controladores) da las 300
sesiones del paquete canónico.

**[TABLA 5.4 — Presets de evaluación]**

| Preset | Ventanas reales | Ventanas sintéticas | Vídeos | Segmentos por sesión | Ventana de traza | Habilita comparación |
|---|---|---|---|---|---|---|
| `diagnostico` | 2 | 1 | 1 | 6 | 90 s | No |
| `rapido` | 8 | 2 | 1 | 30 | 300 s | No |
| `comparativa` | 12 | 3 | 1 | 30 | 300 s | Sí |
| `equilibrado` | 24 | 4 | 2 | 30 | 300 s | Sí |
| `tfg_final` (evaluación final) | 12 | 3 | 4 | 30 | 300 s | Sí |
| `extendido` | 48 | 8 | 4 | 30 | 300 s | Sí |

*Pie: Tabla 5.4: Presets de evaluación definidos en el sistema. El tiempo
límite por sesión es de 240 s en el preset de diagnóstico y de 900 s en los
demás. "Habilita comparación" indica si el paquete puede autorizar
comparaciones y ordenaciones entre controladores (siempre con el motor
simulado).*

**El lanzador: del plan al paquete.** El lanzador se ejecuta desde la línea
de órdenes y acepta el preset, el fichero de configuración y modos de
operación auxiliares (generar solo el plan, ensayo sin sesiones, ejecución
sin análisis, reanudación y un límite técnico de sesiones para pruebas). Su
trabajo tiene cinco pasos.

Primero, crea la raíz del paquete de evidencia, nombrada con el sello de
tiempo y el preset, con los cinco bloques del apartado 4.8 (protocolo,
ejecución, resultados, gráficas e informe). Segundo, construye el protocolo y
el plan de sesiones: el protocolo recoge la versión del esquema, la versión
de la fórmula de calidad, el preset efectivo, los perfiles de vídeo, los
controladores y las ventanas de red seleccionadas; el plan es el producto de
repeticiones por ventanas, vídeos y controladores, en ese orden de
anidamiento, con lo que todas las sesiones de una misma ventana y vídeo
quedan contiguas. Ambos se escriben en JSON y en CSV antes de ejecutar nada:
el experimento es inspeccionable antes de empezar. Cada sesión recibe un
identificador legible que concatena su índice, el controlador, el vídeo, la
ventana de red y la repetición.

Tercero, ejecuta las sesiones una a una. Para cada una escribe su
configuración de cliente completa —el manifiesto del vídeo, la traza y su
ventana, el motor simulado con un mínimo de cola de 0,1 segundos, el
arranque en el nivel más bajo sin decisión inicial del controlador, treinta
segmentos de vídeo, un paso de espera de buffer de 0,01 segundos y sin
ventana de arranque— y lanza el cliente como un proceso independiente, con un
tiempo límite de quince minutos, capturando toda su salida en un registro de
comando que anota el instante de inicio, la orden exacta y el código de
retorno. Ejecutar cada sesión en su propio proceso es una decisión
deliberada: un fallo o un bloqueo no contamina al resto, la memoria se libera
entre sesiones, el estado del cliente nace limpio, y cualquier sesión puede
repetirse aisladamente con su fichero de configuración y la misma orden.
Antes de lanzar una sesión, el lanzador comprueba si ya existe para ella una
ejecución cuyo manifiesto esté en estado completado; en ese caso la omite. Un
experimento interrumpido se reanuda, por tanto, sin repetir trabajo hecho.
Tras cada sesión emite una línea de progreso con contadores de ejecutadas,
fallidas y omitidas, el tiempo transcurrido y una estimación del restante.

Cuarto, al terminar las sesiones, invoca el análisis del paquete y su
verificación (apartado 4.8), y quinto, devuelve un código de salida que solo
es cero si ninguna sesión falló y la verificación se superó. El análisis y la
verificación existen también como herramientas independientes, para volver a
analizar o verificar un paquete existente sin ejecutar nada.

**Selección de ventanas de red.** La selección determinista descrita en el
apartado 4.8 se implementa en tres pasos. Se filtran las trazas candidatas:
partición de evaluación, marcadas como utilizables y con duración suficiente
para la ventana; las reales deben superar además un suelo mínimo de
throughput medio y máximo, para que la sesión tenga sentido frente a la
escalera de calidades. Se agrupan por procedencia y carácter (conjunto de
datos, semántica, condición de red y un tramo de dificultad derivado del
throughput medio y de su variabilidad), y dentro de cada grupo se ordenan
por un resumen criptográfico de la semilla y del identificador de la traza:
un orden pseudoaleatorio pero fijo. Las ventanas se toman por turnos entre
los grupos hasta alcanzar el número que fija el preset, lo que balancea la
procedencia. El instante inicial de cada ventana dentro de su traza también
se deriva de la semilla, en múltiplos del intervalo de decisión, de modo que
dos ejecuciones con la misma semilla y el mismo catálogo producen exactamente
las mismas ventanas. Las sintéticas se seleccionan aparte, con una semilla
derivada, y quedan etiquetadas como diagnóstico.

**Inyección del vídeo por sesión.** El catálogo de perfiles de vídeo asocia
a cada identificador la URL de su manifiesto, la duración de segmento y su
clase. La configuración de cada sesión recibe el manifiesto del vídeo que le
corresponde y, si el controlador es el propio, el identificador del perfil de
tamaños de ese mismo vídeo entre sus parámetros. Así, el mismo paquete de
modelo sirve a los cuatro vídeos del experimento: cambia el dato que
describe el contenido, no el modelo (apartado 5.6).

**La interfaz gráfica.** El lanzador tiene una interfaz gráfica mínima,
construida con `tkinter`, con la que se lanzó la evaluación final. Ofrece el
preset, una casilla por controlador registrado, los botones de ejecutar y
detener y una barra de progreso. Muestra en todo momento la orden exacta que
va a ejecutar: la interfaz no hace nada que no pueda hacerse desde la línea
de órdenes. Al ejecutar, escribe una configuración temporal con los
controladores elegidos, arranca el lanzador como subproceso y un hilo lee su
salida; las líneas de progreso, con un formato fijo de pares clave-valor,
actualizan la barra y la estimación de tiempo restante.

*(El apartado 5.5 desciende a la implementación de los controladores
clásicos.)*

---

### Notas para Daniel (no van a la memoria)

- **Citas: NINGUNA** (implementación propia; `tkinter`/Python ya citados en
  5.1). Sin figura nueva: el paquete de cinco bloques ya se enunció en 4.8 y
  el texto + T5.4 cubren la mecánica; una figura del flujo del lanzador
  sería decorativa. Los números de T5.4 salen literalmente de
  `ESPECIFICACIONES_PRESET` (catalogo.py).
- **CORRECCIÓN QUE AFECTA AL CAP 4 (error mío del 4.3, no tuyo):** la T4.3
  dice "Paso de espera 0,5 s" como "valor por defecto usado en el capítulo
  6". Es FALSO para la evaluación: el lanzador fija
  `espera_vaciado_buffer_s = 0.01` en TODAS las sesiones (verificado en las
  300 configs de `00_protocolo/configs_cliente` del paquete canónico y en
  `construir_config_cliente`). 0,5 s es solo el valor por defecto del cliente
  suelto. Propuesta para la fila de T4.3: "Paso de espera | 0,5 s (0,01 s en
  la evaluación) | Tiempo de espera cuando el buffer se llena". Y en el texto
  del 4.3 ("espera en pasos de 0,5 segundos") añadir "(0,01 s en la
  evaluación)" o dejar "en pasos cortos". Mismo tratamiento que ya tiene el
  preroll (10 s → 0). Análogo opcional en 4.4: el mínimo de cola del motor
  es "1 segundo por defecto" (correcto), pero la evaluación fija 0,1 s
  (`tiempo_min_cola: 0.1`) — el 5.4 ya lo dice; si quieres coherencia total,
  añade "(0,1 s en la evaluación)" en 4.4/T4.4.
- **Verificado contra el paquete canónico (04/09):** 300 configs en
  `00_protocolo/configs_cliente`; id real
  `s00001_basado_en_tasa_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1`
  (índice/alias/perfil/ventana+hash corto/repetición); protocolo con
  `preset_efectivo` = {30 segmentos, ventana 300 s, límite 900 s, 125 s
  estimados/sesión → 37500 s totales}, 15 ventanas, 4 perfiles, 5
  controladores, `apto_benchmark`/`apto_ranking` = True; ejecución de sesión
  = `ejecucion_<sello>/` con los 6 artefactos del 4.6; la traza FCC de la
  primera ventana arranca en `inicio_ventana_s = 1352.0` = 338 × 4 s
  (desplazamiento determinista en múltiplos del intervalo de decisión, como
  dice el texto).
- **Verificado en código:** `construir_config_cliente` (tiempo_min_cola 0.1
  si simulado; calidad_inicial 0; decision_inicial_controlador False;
  max_segmentos 30; espera 0.01; preroll 0; max_reintentos 3; política
  fail; tiempos compactos; con esperas); subprocess con `timeout=900`
  (`tiempo_limite_s` del preset) y log `inicio=/comando=/codigo_retorno=`
  (o `timeout_s=` si expira); reanudación por manifiesto `estado ==
  "completado"` del último `ejecucion_*`; código de salida `0` solo si
  `num_fallidas == 0` y verificación superada; GUI: config temporal en el
  directorio temporal del sistema, `Popen` + hilo lector, parseo de
  `PROGRESO_EVALUACION k=v`; selección: filtros (eval + usable + duración ≥
  ventana; suelos por defecto media ≥ 450 kbps y máx ≥ 300 kbps), agrupación
  (dataset, semántica, condición, tramo), orden por SHA-256(semilla:id),
  round-robin, inicio = hash mod posiciones × 4 s; sintéticas con semilla+17;
  tramos de dificultad: media < 1500 baja, < 5000 media, < 20000 alta, resto
  muy alta; "variable" si (máx−mín)/media ≥ 1,5. Los umbrales concretos NO
  van en 5.4 (van con las ventanas en 6.3 si hace falta).
- **Sobre el nombre `tfg_final` en T5.4:** 04_CORRESPONDENCIAS prohíbe usarlo
  como NOMBRE de la evaluación en la prosa; en la tabla aparece como clave
  literal de configuración (dato), y la prosa dice "el preset final de la
  tabla". Si prefieres, la fila puede rotularse solo "final (evaluación)".
  No renombrar la clave en el código: el protocolo del paquete canónico ya
  la lleva.
- **AVISOS de restos en el entregable (no tocados):**
  1. `configuracion_cliente.py` referencia `config/client.example.yaml` y
     `config/client.local.yaml` como defaults del cliente: no existen (la
     carga los salta) y son nombres viejos en inglés.
  2. `configuracion.py` escribe el ejemplo en `config/evaluacion.example.json`
     (`--escribir-config-ejemplo`), pero el fichero real se llama
     `evaluacion.local.example.json`.
  3. Defaults con nombre inglés: `dir_raiz="logs"`,
     `analisis.raiz_salida="analysis_output"`, claves `decision_interval_s`,
     `min_media_throughput_kbps_for_formal`, `min_max_throughput_kbps_for_formal`
     (claves de la config de evaluación; cambiarlas no afecta al paquete
     canónico, pero es un cambio de código que hay que validar).
  4. Las configs por sesión se escriben con extensión `.yaml` y contenido
     JSON (el cargador lo detecta por la llave inicial). Funciona, pero
     despista; NO cambiar ahora: el paquete canónico ya está así.
- **Fronteras:** qué ventanas y vídeos concretos se eligieron y sus números
  (→6.1/6.3); análisis estadístico, compuertas y verificación (→4.8 diseño,
  6.1 protocolo); parámetros del controlador propio (`alfa_riesgo`,
  respaldo, latencia máxima, hashes — →5.6).
- Longitud: ~1250 palabras. Recortables al masticar: el párrafo de la
  interfaz gráfica (a tres frases) y los modos auxiliares del lanzador.
