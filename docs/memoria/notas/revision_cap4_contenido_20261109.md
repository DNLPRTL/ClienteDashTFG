# Revisión de CONTENIDO del capítulo 4 (Word de Daniel) contra el sistema final — 09/11/2026

Documento revisado: `G:\Otros ordenadores\Mi portátil\backup memo\Borrador Capitulo 4 Diseño.docx`
(10 492 palabras extraídas, 6 figuras, 7 tablas). Cotejado con el código de
`TFG Material\01_codigo\ClienteDashTFG`, con `docs/blindaje/06_PROTOCOLO_FINAL.md`,
`07_RESULTADO_FINAL.md`, `03_CAMBIOS_CODIGO_BLINDAJE.md` y con el paquete
`04_evidencia_final\20261015_031741_final_blindaje`. Solo contenido; el estilo lo adapta Daniel.

Formato de cada cambio: apartado · frase actual · frase propuesta · por qué (fuente).
Las frases propuestas son borrador: Daniel las reescribe con sus palabras.

## 4.1 Vista global

C1 · «Ya fuera del bucle de sesión restan dos componentes.»
→ «Ya fuera del bucle de sesión restan tres componentes.» Y añadir tras el entrenamiento:
«El tercero es la carpeta de pruebas (`pruebas/`): dieciocho pruebas automáticas (unittest) que fijan
el comportamiento del reproductor, del MPC canónico, de las variantes del controlador propio, de los
contrastes estadísticos y de la carga del modelo. Se ejecutan antes de cada evaluación y no intervienen
en la sesión.»
Por qué: C8 añadió `pruebas/` al código entregado (18 pruebas; la VM las pasa en `comprobar`).

C2 · «calcula la métrica de calidad de experiencia (...) y analiza los resultados obtenidos»
→ añadir «y aplica los contrastes estadísticos fijados antes de ejecutar (apartado 4.8)».
Por qué: C6, módulo nuevo `core/evaluacion/contrastes.py`.

C3 · «su salida es un paquete que el controlador carga a la hora de comenzar su operación»
→ «su salida es un paquete que el controlador carga al crearse, antes de que arranque la sesión».
Por qué: C8 (carga en `__init__`, fuera del tiempo de sesión).

C4 · Texto del flujo: «construye una lista con los segmentos por nivel de calidad disponibles para ese
contenido y toma la primera de las decisiones»
→ «construye la lista de segmentos por nivel y fija el nivel inicial: en la evaluación es el más bajo de
la escalera para todos los controladores (el reproductor puede pedir esa primera decisión al controlador,
pero la opción no se usa). El primer segmento se descarga sin consultar al controlador (calentamiento) y a
partir del segundo se repite el bucle.»
Por qué: `configuracion_cliente.py` (`decision_inicial_controlador = false` por defecto),
`reproductor.py:361-368`; en el paquete final todas las sesiones comprobadas empiezan en nivel 0 y su
primer segmento es `calentamiento` (`config_resuelta.json`, `telemetria_segmentos.csv`).

C5 · Tabla 4.1: fila `core/evaluacion/` → «QoE, contrastes prerregistrados y análisis de los resultados
(fuera de la sesión)»; fila nueva `pruebas/` → «Pruebas automáticas del código entregado (18, unittest;
fuera de la sesión)». Opcional: fila `core/controladores/` → «Registro e implementación de los
controladores: clásicos, MPC robusto canónico, el propio y sus tres variantes de ablación».

Figura 4.1: SE MANTIENE (no incluye `pruebas/`, pero nada de lo que muestra es falso).
Figura 4.2: CAMBIAR UN TEXTO (caja 5). «5. Primera decisión del controlador. nivel de inicio, el primer
segmento no cambia (calentamiento)» → «5. Nivel inicial fijado por configuración (el más bajo en la
evaluación); el primer segmento no cambia (calentamiento)». La caja a («pasos de 0,5 segundos») puede
quedarse: es el valor por defecto; si se toca, «pasos cortos (0,5 s por defecto)».

## 4.2 Analizador del MPD

C6 · «(tanto en el principal contenido como en el del experimento, `PT0H10M0.100S`: diez minutos más una
décima de segundo)»
→ «(en el contenido principal, Paseo de Almuñécar a 30 fps, `PT0H10M0.100S`: diez minutos más una décima;
cada vídeo del experimento lleva la suya, por ejemplo `PT0H10M34.600S` en Blender a 30 fps y
`PT0H10M0.000S` en Tears of Steel)».
Por qué: el experimento final usa cinco vídeos; MPD servidos en `05_contenido_dash`.

C7 · «(en las variantes del contenido a 60 frames por segundo de 60000 con mismo resultado)»
→ «(Paseo a 60 fps usa `timescale` 60000 y `duration` 240000, con el mismo resultado de 4,000 s; Blender a
60 fps conserva 15360 y 61440)».
Por qué: MPD servidos; solo Paseo 60 fps usa 60000.

Figura 4.3: SE MANTIENE (valores de Paseo 30 fps, vídeo del experimento; 151 segmentos es correcto para él).
Tabla 4.2: se mantiene.

## 4.3 Descarga y buffer

C8 · «espera dando pasos de 0,5 segundos hasta que el umbral baje»
→ «espera en pasos cortos hasta que la ocupación baja del tope (0,5 s por defecto; 0,01 s en la evaluación,
para que la espera no retrase la siguiente descarga más de lo imprescindible)».
Por qué: `scripts/3_evaluacion/ejecutar_evaluacion.py` fija `espera_vaciado_buffer_s = 0.01`; confirmado en
`config_resuelta.json` de las sesiones del paquete final.

C9 · «ordena una degradación al nivel de calidad más bajo en la petición y lo vuelve a intentar; solo en el
caso de que el fallo continue aun con el nivel más bajo, el segmento es abandonado»
→ «baja un nivel de calidad y repite el ciclo de seis intentos; solo cuando el fallo persiste ya en el
nivel más bajo, el segmento se abandona y se pasa al siguiente».
Por qué: `reproductor.py:626-637` baja un nivel (`nivel_actual -= 1`), no al mínimo directamente.

C10 · «espera hasta 10 segundos con un retroceso exponencial de 0,5 segundos que se duplican hasta alcanzar
ese límite» y fila de la tabla «Espera entre intentos | 0,5 s hasta 10 s»
→ «espera que se duplica en cada intento, de 1 s a un tope de 10 s (1, 2, 4, 8 y 10 s)» y en la tabla
«1 s, doblando hasta 10 s».
Por qué: `reproductor.py:638`, `espera = min(0,5·2^n, 10)` con n desde 1. Precisión menor.

C11 · «la tabla 4.3 (...) recopila sus valores por defecto, que son exactamente los que se usan en la
evaluación del capítulo 6»
→ «recopila sus valores por defecto y, cuando difieren, los fijados en la evaluación del capítulo 6».
Tabla 4.3: cabecera «Valor por defecto (en la evaluación, si difiere)»; fila «Paso de espera | 0,5 s
(0,01 s en la evaluación)»; fila nueva «Cola mínima del motor para arrancar o reanudar | 1 s (0,1 s en la
evaluación) | Umbral de histéresis del motor (apartado 4.4)».
Por qué: tres parámetros difieren en la evaluación (paso de espera 0,01 s, preroll 0 s, cola mínima
0,1 s), `ejecutar_evaluacion.py` (construir_config_cliente).

Figura 4.4: SE MANTIENE (valor por defecto; opcional «pasos cortos (0,5 s por defecto)»).

## 4.4 Motores de reproducción

C12 · «Solo da lugar el comienzo de la reproducción cuando se llega en la cola a un mínimo configurable
(este valor es de 1 segundo por defecto)»
→ «(1 s por defecto; 0,1 s en la evaluación, para que el arranque y la salida de cada parada dependan de
la red y no del umbral)».
Por qué: `ejecutar_evaluacion.py` fija `tiempo_min_cola = 0.1` para el motor simulado.

Resto del 4.4 y Tabla 4.4: se mantienen (eventos, hilo propio, reloj del sistema, pipeline GStreamer con
`appsrc`, `qtdemux`, `h264parse`, decodificación opcional, comprobados en el código).

## 4.5 Interfaz común de los controladores

C13 · «El registro cuenta con seis controladores: uno basado en la tasa de bits, dos basados en el buffer
(BOLA y BBA), dos basados en control con carácter predictivo (MPC y su versión robusta) y el controlador
propio propuesto en este trabajo.»
→ «El registro cuenta con nueve entradas: uno basado en la tasa de bits, dos basados en el buffer (BBA y
BOLA), el MPC y su versión robusta en la forma canónica de Yin et al. y del código de referencia de
Pensieve (horizonte de cinco segmentos, QoE lineal, tamaños reales de los segmentos y error medido frente a
la media armónica), el controlador propio y tres variantes de ablación del propio, que comparten su
planificador y cambian solo la predicción: solo la mediana de la red, cuantiles fijos sin red y cuantiles
de las últimas descargas sin red. En la evaluación del capítulo 6 corren ocho de ellos: todos salvo el MPC
no robusto.»
Por qué: C3 y C4; `core/controladores/registro.py` (9 claves) y `config/evaluacion.local.json` (8).

C14 · «un controlador clásico a modo de respaldo, el cual recibe el peso de la decisión si el modelo falla
o supera un límite de tiempo en su ejecución»
→ «el MPC robusto canónico como respaldo, creado junto al controlador propio para el mismo vídeo y
alimentado con toda la realimentación de la sesión, de modo que su historial está completo si tiene que
decidir; entra si el modelo falla, si la acción no es válida o si la inferencia supera el límite de 50 ms».
Por qué: C4 y C8; `controlador_propio.py` (`RESPALDO_POR_DEFECTO = "mpc_robusto"`, `fijarFeedbackReproductor`
reenvía al respaldo, `LATENCIA_MAX_INFERENCIA_MS = 50`).

C15 · «y la comprobación del estado de integridad en la carga del paquete del modelo predictivo»
→ «y la carga del paquete del modelo con comprobación de integridad (huellas) al crear el controlador, antes
de que empiece la sesión; si la carga falla, se reintenta en cada decisión y mientras tanto decide el
respaldo».
Por qué: C8.

C16 · «(ofreciendo la acción menor válida como alternativa de seguridad)»
→ «(si la acción no pasa la máscara, decide el respaldo; la acción válida más baja queda como último
recurso si el respaldo también falla)».
Por qué: `controlador_propio._decidir_por_respaldo` y `seguridad_red.py`. Precisión menor.

Tabla 4.5: se mantiene (20 claves comprobadas en `contrato.py`).
Figura 4.5: CAMBIAR DOS TEXTOS. Caja «Registro de controladores»: añadir «propio_mediana ·
propio_cuantiles_fijos · propio_cuantiles_recientes» (y, si cabe, «8 en la evaluación»). Caja «Respaldo a
controlador clásico» → «Respaldo al MPC robusto». El resto se mantiene.

## 4.6 Telemetría

C17 · «A modo de respaldo para que la medida entre todos los controladores sea equitativa, las paradas
producidas por el último segmento no valen en la evaluación, lo cual es razonable dado que el consumo
último del buffer no es motivo de comparación.»
→ «Cada parada se apunta al segmento que el cliente está esperando descargar en ese momento, que es el que
falta en el buffer. Las paradas que empiezan cuando ya no queda nada por descargar corresponden al vaciado
final del buffer y se ignoran: la sesión las distingue por su estado, no por la posición del segmento, y la
fila del último segmento se conserva como las demás.»
Por qué: C2 (`reproductor.py:216-231` y `_descargas_terminadas`). La contabilidad antigua (cabeza de la
cola, fila anulada) perdía a veces la parada previa al último segmento y contaba a veces la previa al
segundo.

C18 (opcional) · Lista de fases: «la etapa donde se produce un régimen estable y finalmente el vaciado del
contenido»
→ «la etapa de régimen estable. El vaciado final del buffer no genera filas: se trata como estado de la
sesión (ver arriba).»
Por qué: `reproductor.py:876-885` nunca etiqueta una fila como vaciado.

Tabla 4.6: se mantiene en contenido. Errata: el pie dice «cuatro bloques» y el texto y la tabla dan cinco.

## 4.7 Condiciones del experimento

C19 · «tres particiones existentes (fase de entrenamiento, test y evaluación)»
→ «tres particiones (entrenamiento, validación y evaluación)».
Por qué: convención de la memoria; la partición `test` del catálogo es la de validación, donde se tomaron las
decisiones de diseño; la de evaluación no se toca hasta el experimento final.

C20 · «En cada ejecución una ventana de una traza es recibida (en el caso de la evaluación, 300 segundos)»
→ «(en la evaluación, 160 s, con una vuelta de seguridad: si la sesión consume la ventana entera, la traza
vuelve a su inicio una sola vez; una sesión de 30 segmentos consume como mucho unos 145 s de traza)».
Por qué: C6; preset `final_blindaje` (`duracion_ventana_red_s = 160`, `politica_fin = loop`,
`max_bucles = 1`), `config_resuelta.json` del paquete.

C21 · «las condiciones de red nunca son inventadas, si se agotase la ventana en medio de una descarga, la
sesión falla y se marca»
→ «las condiciones de red nunca se inventan: si la ventana se agota, la traza se repite desde su inicio una
sola vez (política de bucle con un máximo de una vuelta) y, si aun así se agota, la sesión falla y queda
marcada».
Por qué: `core/reproduccion_trazas/modelo_red.py` y preset final.

C22 · «aparecen unas desviaciones en el tamaño del contenido entre segmentos de la misma representación de
hasta el 16 por ciento, por otro lado, la media total por representación si se aproxima razonablemente al
valor nominal»
→ «en los vídeos vistos por el modelo, el coeficiente de variación del tamaño dentro de una representación
está entre 0,05 y 0,19 en los 30 segmentos que dura una sesión (hasta 0,16 sobre el vídeo completo), y en el
contenido nuevo del experimento, Tears of Steel, sube a 0,28–0,31. La media por representación queda cerca
del nominal en los vídeos vistos (de un 6 % por debajo a un 3 % por encima) y entre un 8 y un 12 % por
debajo en Tears of Steel, cuyos dos primeros segmentos son casi negros.»
Por qué: calculado por programa sobre `perfiles_video/tamanos_segmentos/*.json` (los 5 vídeos del
experimento, 30 primeros segmentos). Cifras exactas:
Paseo 30 fps cv30 0,052–0,060, media/nominal 1,001–1,016; Paseo 60 fps 0,049–0,057, 1,007–1,027;
Blender 30 fps 0,156–0,188, 0,939–0,990; Blender 60 fps 0,129–0,178, 0,946–1,009;
Tears of Steel 0,276–0,307, 0,878–0,917.

C23 · «Este contenido es consumido por dos entidades: primero por el entrenamiento del controlador
propuesto (...) y segundo el planificador de la ejecución»
→ «por tres consumidores: el entrenamiento del controlador propio (su simulador usa los tamaños reales),
el planificador del controlador propio y el MPC robusto canónico, que decide con el mismo planificador y
los mismos tamaños reales con un único escenario de throughput».
Por qué: C3.

C24 · «Hablando de los algoritmos clásicos, ellos no emplean este dato, dado que su literatura oficial no lo
toma en cuenta; cabe destacar que el JSON que describe los tamaños reales no tiene efecto en la sesión:
solo sirve para aquel que sepa usarlo.»
→ «El basado en tasa, BBA y BOLA no usan este dato: los dos primeros no razonan con tamaños y BOLA usa el
nominal, como su artículo. El MPC robusto sí lo usa, porque su forma de referencia (el código de Pensieve)
planifica con los tamaños reales de cada segmento. El descriptor no altera la sesión: solo lo lee quien lo
necesita.»
Por qué: C3.

C25 · «Por último, se decide que los baselines continúen fieles a sus publicaciones originales, por ejemplo,
el que se basa en la tasa y BBA no contemplan tamaños en su horizonte; tanto BOLA como MPC usan el dato
nominal. Modificarlos podría dejar a la comparativa sin un respaldo bibliográfico (...). Para los clásicos,
el resultado de esta diferencia esta mas que contenido, dado que la media de tamaño del contenido real
coincide con la media nominal, con una desviación muy pequeña (0,4 por ciento), por consiguiente, no existe
un sesgo, tan solo se ignora la variabilidad entre el tamaño de los segmentos.»
→ «Por último, los algoritmos clásicos se mantienen fieles a sus referencias: el basado en tasa y BBA no
contemplan tamaños; BOLA usa el nominal; el MPC robusto, la referencia fuerte de la comparativa, usa los
tamaños reales como el código de Pensieve, de modo que frente al controlador propio solo cambia la
predicción. Modificar los demás los convertiría en versiones propias sin respaldo bibliográfico. Para BOLA
el efecto está acotado: en los vídeos vistos la media real por representación se desvía del nominal entre
un −6 % y un +3 %, así que solo ignora la variabilidad entre segmentos; en Tears of Steel el nominal
sobreestima el tamaño medio entre un 8 y un 12 %, un sesgo hacia la prudencia.»
Por qué: C3 y cifras de C22. El «0,4 por ciento» no se sostiene con los cinco vídeos del experimento.

En 4.7 no hay ninguna frase de empate ni de resultados: nada que quitar.

Figura 4.6: CAMBIAR CINCO TEXTOS (el dibujo vale).
«Ventana 300 s de una traza por sesión (carácter determinista)» → «Ventana 160 s de una traza por sesión,
con una vuelta de seguridad (inicio determinista)».
«entrenamiento / prueba / evaluación» → «entrenamiento / validación / evaluación».
«en caso de que se falle algo la sesión se detiene, las condiciones de red no se inventan» → «la traza se
repite como mucho una vez; si aun así se agota, la sesión se detiene: las condiciones de red no se
inventan».
«8 vídeos en el servidor» → «9 vídeos en el servidor (5 en el experimento, uno de ellos nuevo)».
«la variación típica del tamaño es aproximadamente del 10 % llegando hasta el 16 % en fragmentos de
animación» → «coeficiente de variación de 0,05 a 0,19 en los vídeos vistos y de 0,28 a 0,31 en el contenido
nuevo (Tears of Steel)».
Opcional: «Planificador» → «Planificador (propio y MPC robusto)».

## 4.8 Ejecución frente a evaluación

C26 · «Las ventanas de red marcadas para su uso en el experimento (aquellas de la partición de evaluación)
son las únicas que se utilizan, se escogen de manera balanceada respecto a su origen y tienen asociada una
seed o semilla fija que da lugar a repetirlo si fuera necesario.»
→ «Se usan todas las ventanas de 160 s de la partición de evaluación que superan un filtro de relevancia
tomado de Pensieve (throughput medio menor de 6 Mbit/s y mínimo mayor de 0,2 Mbit/s, medidos sobre la propia
ventana), excluidos los 42 grupos de captura empleados durante el desarrollo, de modo que ninguna ventana
del experimento se había ejecutado antes. El inicio de cada ventana se sortea con una semilla fija que
permite repetir la selección.»
Por qué: C6; `core/evaluacion/seleccion.py`, preset `final_blindaje`, `config/evaluacion.local.json`
(42 grupos: 39 reales y 3 sintéticos), `06_PROTOCOLO_FINAL.md`.

C27 · «la metodología se basa en emparejar, eso quiere decir que todos los controladores se ejecutan para
cada combinación entre vídeo y ventana de red»
→ «cada ventana real se empareja con dos vídeos, uno visto en el entrenamiento (en rotación entre los
cuatro) y el contenido nuevo (Tears of Steel), y cada escenario (ventana y vídeo) se ejecuta con los ocho
controladores en un orden sorteado con semilla, para que la posición en la serie no favorezca a ninguno. Las
comparaciones posteriores se hacen entre sesiones del mismo escenario.»
Por qué: `ejecutar_evaluacion.py` (`videos_de_la_ventana`, sorteo `"606|ventana|vídeo|repetición"`).

C28 · Añadir tras «Cada experimento genera consigo el archivo de configuración que se usó, haciendo posible
su auditoría.»: «y copia en el protocolo, antes de ejecutar la primera sesión, las hipótesis que se
contrastarán (referencia, rivales, métricas, margen de equivalencia y método), de modo que el análisis no
se elige a la vista de los resultados».
Por qué: `core/evaluacion/contrastes.py` (`definicion_hipotesis`) y `protocolo_validacion.json` del paquete.

C29 (recomendado por la regla «solo el experimento final») · «En el momento de realizar los experimentos,
esta medida de seguridad fue de gran ayuda dado que algunas ejecuciones que parecían completas fueron
descartadas al fallar en una de las pruebas, permitiendo así detectar el problema y repetir el experimento
habiéndolo solucionado.»
→ «Esta separación entre validez y comparación evita que una ejecución incompleta o contaminada entre en la
comparativa.»
Por qué: la frase actual alude a ejecuciones de desarrollo; no lo obliga el código.

C30 · Tabla 4.7, dos filas:
«Sin uso del respaldo en sesiones evaluables | El controlador con modelo fue siempre quien tomó las
decisiones» → «El controlador propio y sus tres variantes decidieron siempre por sí mismos, sin recurrir al
respaldo».
«Inferencia ha sido verificada | Cada decisión quedo registrada para ser auditada» → «Cada decisión del
propio y de sus variantes lleva su auditoría (acción, máscara, motivo); el tiempo de inferencia de la red se
exige solo a las dos variantes que la usan».
Por qué: C5 (`analisis.evaluar_gates`). Las ocho pruebas de la tabla coinciden con las ocho compuertas del
código.

C31 (opcional) · «se comprueba por medio de una verificación automática que todo el paquete de evidencia sea
integro»
→ «una verificación automática de quince comprobaciones (estructura, ficheros de resultados, coincidencia
del plan con las sesiones ejecutadas, ausencia de sesiones fallidas, sintéticas aparte y gráficas
generadas)».
Por qué: `verificar_paquete.py`; en el paquete final, 15/15.

C32 · Párrafo del análisis estadístico entero («En relación con el análisis estadístico (...) presentados
en el capítulo 6.»)
→ «El análisis estadístico se fijó antes de ejecutar. Las comparaciones son pareadas: cada controlador se
compara con el propio en los mismos escenarios (ventana y vídeo). Como los dos escenarios de una ventana
comparten red, la unidad de inferencia es la ventana: la prueba del signo se aplica a la diferencia media
por ventana y los intervalos de confianza se obtienen por bootstrap de ventanas. La hipótesis principal
frente al MPC robusto es de equivalencia en QoE (procedimiento TOST con margen fijado de antemano),
acompañada de hipótesis de superioridad en paradas frente al MPC robusto y frente a las variantes de
ablación; el conjunto se corrige por multiplicidad con el método de Holm. No se asume normalidad y los
resultados se presentan con intervalos y distribuciones, no solo con medias, siguiendo las recomendaciones
de la literatura sobre evaluación de QoE [peroni2024qoePitfalls]. El detalle y los resultados van en el
capítulo 6.»
Por qué: C6 y `06_PROTOCOLO_FINAL.md` §5.

## Erratas de forma (una línea cada una, no se tocan)

- Títulos de nivel 2 salen «Capítulo 4.2. …» por la numeración automática; la biblia pide «4.2. Título».
- 4.1, punto del motor: la frase termina en «(apartado» sin cerrar.
- Pie de la Tabla 4.6: «cuatro bloques»; son cinco.
- «se haya» por «se halla» (varias veces), «Adaptative» por «Adaptive», «Dash» por «DASH».

## Avisos que no van a la memoria

1. **Indicador «benchmark autorizado» del paquete final: falso.** `evaluar_gates` solo marca
   `benchmark_autorizado`/`ranking_autorizado` para los presets antiguos (`comparativa`, `tfg_final`,
   `equilibrado`, `extendido`); `final_blindaje` no está en esa lista. Las ocho compuertas se superan
   (`gates_superados = true`) y `verificar_paquete` da 15/15, pero `resumen_resultados.md` imprime
   «Benchmark autorizado: no». En la memoria se habla de compuertas superadas y de los contrastes
   prerregistrados, nunca de ese indicador ni del «ranking». Respuesta preparada si el tribunal lo ve:
   indicador heredado de los presets de desarrollo, sin efecto sobre la inferencia, que es la
   prerregistrada en `contrastes.py`. El código está congelado: no se toca.
2. `.idea\` sigue dentro de `TFG Material\01_codigo\ClienteDashTFG` (5 ficheros), aunque C8 lo daba por
   movido a `legacy`. El kit cuenta 103 ficheros de código sin él. Limpieza pendiente, no afecta al código.
3. Los SVG de las seis figuras van embebidos en el `.docx` (`word/media/image2.svg` … `image12.svg`) además
   del PNG; los fuentes están en `docs/memoria/figuras/fig_4_*.svg`. Los cambios de F4.2, F4.5 y F4.6 son
   solo de texto.
4. Comprobado por programa: 20 claves de realimentación, 6 artefactos por sesión, 7 columnas del fichero
   de evaluación, 8 compuertas, 15 comprobaciones, 9 entradas del registro, 42 grupos excluidos, 103
   ficheros de código, nivel inicial 0 y primer segmento de calentamiento en las sesiones del paquete.
