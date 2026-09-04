# Borrador 5.6 — El controlador propio (PARTE 1 de 2: visión general, entradas, predictor y generalización)

> BORRADOR para masticar y reescribir (05/09/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: entregable — `core/controladores/controlador_propio.py`,
> `constructor_entradas.py`, `entradas_contexto.py`, `constantes_entradas.py`,
> `diagnosticos_red.py`, `seguridad_red.py`, `mascara_acciones.py`,
> `core/modelo_propio/{modelo,bundle,planificador,perfil_video,escalera_contenido,
> estado_sesion,integridad}.py` (leídos enteros el 05/09) + bundle canónico de
> `03_modelos` (configuración del modelo y del planificador, manifiesto,
> normalización; pesos cargados para contar parámetros) + `esquema_targets.json`
> del dataset + PDFs de Puffer y BayesMPC (norma PDF-primero; pasajes en notas).
> La PARTE 2 (planificador CVaR, salvaguardas, paquete del modelo, T5.6 y
> F5.3) está incluida al final de este mismo fichero (entregada 05/09).

---

### 5.6. El controlador propio

Los apartados anteriores describen controladores que deciden con reglas
fijas. El controlador propio sustituye la parte que peor resuelven los
clásicos —anticipar la red— por un modelo aprendido, y conserva para la
decisión un planificador de control predictivo, la estructura que mejor
resultado da entre los clásicos. Es, por tanto, un controlador de
predicción más control: un predictor de cuantiles de throughput, entrenado
de forma supervisada sobre trazas reales, alimenta a un planificador MPC que
optimiza una medida de riesgo en lugar de un valor esperado. El paradigma
tiene precedentes en la literatura: el sistema desplegado en Puffer combina
un predictor neuronal probabilístico entrenado con datos reales con un
controlador MPC clásico \cite{yan2020puffer}, y el trabajo sobre MPC
bayesiano deriva de la incertidumbre de la predicción una cota inferior del
throughput con la que planificar el peor caso \cite{kan2021bayesmpc}. El
controlador propio se sitúa en esa línea y aporta tres decisiones de diseño
que se desarrollan en este apartado y en el 5.7: un predictor que estima
cuantiles con incertidumbre epistémica explícita, un planificador que
consume el tamaño real de cada segmento, y un entorno de entrenamiento con
la misma física que el cliente.

**Visión general.** La Figura 5.2 muestra la arquitectura completa. En cada
decisión, el constructor de entradas transforma la realimentación del
apartado 4.5 en las entradas del modelo. El predictor —un conjunto de cinco
redes recurrentes idénticas en arquitectura pero entrenadas de forma
independiente— produce, para cada uno de los cinco segmentos siguientes,
cuatro cuantiles del throughput. El planificador enumera secuencias de
acciones, simula el buffer bajo cada escenario de throughput con el tamaño
real de cada segmento, puntúa cada escenario y elige la primera acción de
la secuencia con mejor valor en riesgo condicional. Una capa de
salvaguardas comprueba la acción y, si algo falla, delega en el MPC robusto.
Dos fuentes de datos externas completan el esquema: el paquete del modelo,
que contiene los pesos y las configuraciones, y la tabla de tamaños del
vídeo activo, que solo consume el planificador.

**[FIGURA 5.2 — Arquitectura del controlador propio. Fichero:
`figuras/fig_5_2_arquitectura_controlador_propio.svg`]**
*Pie: Figura 5.2: Arquitectura del controlador propio: constructor de
entradas, predictor de cuantiles (ensemble de cinco redes recurrentes),
planificador MPC con valor en riesgo condicional y salvaguardas. El paquete
del modelo alimenta al predictor; la tabla de tamaños del vídeo activo, solo
al planificador.*

**Entradas del modelo.** El constructor de entradas mantiene un historial
con las cinco últimas descargas de segmentos de vídeo (throughput medido y
tiempo de descarga de cada una, deduplicadas por índice de segmento) y
calcula siete escalares que describen el estado de la sesión: la ocupación
del buffer, el índice y la tasa de la última representación, la magnitud
del último cambio de nivel, el rebuffering reciente, y dos medidas del
progreso de la sesión (fracción de segmentos restantes y si queda alguno).
De estas señales, el rebuffering reciente no forma parte del contrato del
cliente y se entrega a cero en ejecución; el entrenamiento sí la aporta,
como se indica en el apartado 5.7. Todas las entradas provienen del contrato
del apartado 4.5; ninguna describe el contenido. El constructor impone
además la garantía anti-fuga en tiempo de ejecución: rechaza cualquier
realimentación que contenga alguna de las veintisiete claves prohibidas
(identidad de la traza, partición experimental, dificultad, throughput
futuro, resultados de evaluación) y audita que cada entrada sea numérica,
finita y de la longitud esperada. Si algo falla, el controlador no adivina:
delega la decisión en el respaldo y deja constancia del motivo.

**El predictor de cuantiles.** El modelo es una red recurrente con unidades
GRU \cite{cho2014gru} de 96 unidades que resume la secuencia de descargas,
seguida de una red densa que combina ese resumen con los siete escalares
(capas de 96 y 64 unidades, con desactivación aleatoria del 10 % durante el
entrenamiento) y produce veinte valores: cuatro cuantiles (0,10, 0,25, 0,50
y 0,75) para cada uno de los cinco segmentos futuros. Tres decisiones dan
forma a esa salida.

Primera, la salida es relativa: el modelo no predice el throughput en
valor absoluto, sino su logaritmo respecto a una base, la media armónica
del historial de descargas. Así el mismo modelo sirve a redes de decenas de
kilobits y de decenas de megabits por segundo, y la predicción se reconvierte
a bits por segundo multiplicando la base por la exponencial del cociente,
acotado entre 0,15 y 4 veces la base para descartar extrapolaciones
absurdas. Segunda, los cuantiles son monótonos por construcción: la red
emite el cuantil más bajo y, para los siguientes, incrementos forzados a ser
positivos que se acumulan, de modo que ningún cuantil puede cruzarse con
otro. Tercera, el modelo se entrena por regresión de cuantiles con la
pérdida de cuantiles (*pinball*) \cite{koenker1978quantiles}, que es
asimétrica: para el cuantil 0,10 penaliza diez veces más quedarse por
encima del valor observado que por debajo. El entrenamiento se describe en
el apartado 5.7.

La incertidumbre del predictor tiene dos fuentes, y el diseño las trata por
separado siguiendo la distinción habitual en la literatura
\cite{kan2021bayesmpc}. La variabilidad intrínseca de la red (incertidumbre
aleatoria) la capturan los propios cuantiles: la distancia entre el 0,10 y
el 0,75 refleja cuánto puede moverse el throughput. La incertidumbre del
modelo sobre sí mismo (epistémica), que crece en situaciones poco
representadas en el entrenamiento, se estima con un conjunto de cinco redes
entrenadas de forma independiente con semillas distintas, el método de los
ensembles profundos \cite{lakshminarayanan2017ensembles}: cuando los cinco
miembros discrepan, el modelo está fuera de su terreno. La combinación de
los miembros es deliberadamente asimétrica. Para cada horizonte y cuantil
se toma la media de los cinco; después, la desviación típica de las cinco
medianas —el desacuerdo— se resta de los cuantiles inferiores, con más peso
cuanto más bajo es el cuantil (el 0,10 baja el 80 % del desacuerdo; el 0,25,
la mitad), y los cuantiles se reordenan para conservar la monotonía. El
efecto es que la incertidumbre epistémica ensancha solo la cola inferior de
la predicción, que es la que gobierna el riesgo de parada; los cuantiles
altos no se inflan. El planificador, en la segunda parte de este apartado,
explota exactamente esa cola.

El modelo es pequeño a propósito: unos 46 000 parámetros por miembro,
231 000 en el conjunto, y menos de un megabyte de pesos. En la máquina de
validación, sin aceleración, los cinco miembros se evalúan en unos 1,3 ms de
media por decisión (capítulo 6), muy por debajo del límite de latencia que
impone la salvaguarda. Las entradas se normalizan con la media y la
desviación típica calculadas únicamente sobre la partición de entrenamiento,
guardadas en el paquete del modelo junto a los pesos.

**Arquitectura de generalización: el vídeo como dato.** La separación entre
predictor y planificador no es solo una división de responsabilidades; es
lo que permite que el controlador funcione con vídeos distintos sin
reentrenar. El predictor es agnóstico al contenido: sus entradas describen la
red y el estado del reproductor, nunca el vídeo, de modo que lo aprendido es
la dinámica del throughput y no la de un contenido concreto. El conocimiento
del contenido entra por otro camino: el planificador recibe la tabla de
tamaños reales del vídeo activo (el descriptor del apartado 4.7) como un
dato de configuración, inyectado por sesión por el lanzador (apartado 5.4).
Al arrancar, el controlador carga el descriptor del vídeo indicado y
comprueba que su escalera coincide con la que el reproductor extrajo del
manifiesto: mismo número de representaciones y mismas tasas nominales. Si no
coinciden, no planifica con una tabla equivocada: delega en el respaldo y lo
anota. La consecuencia práctica se comprobó en la evaluación del capítulo 6:
un único paquete de modelo, entrenado una vez, sirvió a los cuatro vídeos
del experimento, y lo único que cambió de una sesión a otra fue la tabla
inyectada. Un vídeo nuevo requiere una tabla nueva —un subproducto del
empaquetado, que cualquier servidor puede generar al publicar el
contenido— y ningún reentrenamiento. El apartado 5.7 explica por qué el
entrenamiento rota varios vídeos para que el predictor no se acople a
ninguno.

*(Continúa en la PARTE 2: el planificador con valor en riesgo condicional,
las salvaguardas, el paquete del modelo, la Tabla 5.6 y la Figura 5.3.)*

---

### Notas para Daniel (no van a la memoria) — parte 1

- **Citas usadas en esta parte (5):** `yan2020puffer` y `kan2021bayesmpc`
  (CON PDF, verificadas 05/09 con pdfminer), `cho2014gru`,
  `koenker1978quantiles`, `lakshminarayanan2017ensembles` (sin PDF local:
  fundamentos verificados por Crossref en el hilo de bibliografía; se citan
  por lo que son, sin atribuirles frases). Citas textuales:
  · Puffer: "it predicts transmission time given a chunk's file size (vs.
    estimating throughput), it outputs a probability distribution (vs. a
    point estimate)"; "Fugu is based on MPC ... but replaces its throughput
    predictor with a deep neural network trained using supervised learning
    on data recorded in situ"; "The use of uncertainty in model predictive
    control has a long history, but to our knowledge Fugu is the first to
    use stochastic MPC in this context"; "daily training".
  · BayesMPC: "the BNN predictor learns uncertainty and provides confidence
    regions on throughput predictions"; "the lower bound of which then
    leads to an uncertainty-aware robust MPC strategy to maximize the
    worst-case user quality-of-experience"; distingue "epistemic and
    aleatoric uncertainty" (por eso el texto usa esa distinción con su
    cita); su predictor usa l = 10 muestras y T = 3 futuros.
  · Diferencias honestas con ambos (por si preguntan): Puffer predice
    TIEMPO DE TRANSMISIÓN dado el tamaño y usa estadísticas TCP; el propio
    predice THROUGHPUT relativo y aplica el tamaño real en el planificador;
    BayesMPC usa una BNN con muestreo Monte Carlo y la cota inferior;
    el propio usa cuantiles + ensemble y CVaR (parte 2).
- **Verificado en código y bundle (05/09):** secuencia = 5 descargas
  (`LONGITUD_HISTORIAL_CONTEXTO`), 2 rasgos (throughput log1p, tiempo);
  7 escalares = `NOMBRES_FEATURES_ESCALARES`; z-score con
  `normalizacion.json` (train-only); GRU 96 × 1 capa; MLP (96, 64) ReLU
  + dropout 0,1; salida 5×4 con base + cumsum(softplus) (monotonía);
  cuantiles (0,10, 0,25, 0,50, 0,75); ensemble 5 (`member_state_dicts`);
  combinación = media + resta de (0,5−q)/0,5 × std de las medianas con
  `ensanchado_cola = 1,0` → q10 baja 0,8·std, q25 baja 0,5·std, q50/q75
  intactos; sort final; conversión base × exp(ratio) con ratio acotado
  [ln 0,15, ln 4] y valor en [0,15·base, 4·base]; base = media armónica
  (300 kbps si no hay historial); latencia medida con `perf_counter`
  alrededor de la inferencia. **Parámetros contados cargando el bundle
  real: 46 292 por miembro, 231 460 en total** (GRU 28 800 + MLP 17 492);
  `pesos_modelo.pt` = 941 582 bytes. Inferencia media del paquete canónico:
  1,255 ms (memoria: "1.26 ms") → en el texto "unos 1,3 ms".
  Campos prohibidos: 27 claves en `CAMPOS_PROHIBIDOS_MODELO` (contadas).
  Coherencia escalera↔descriptor: `_asegurar_escalera` exige mismo número
  de representaciones y tasas iguales (tolerancia 8 bit/s) → si no,
  `ErrorBundle` → respaldo con motivo `fallo_carga_bundle` (el motivo
  `perfil_video_no_disponible` salta si el descriptor no existe).
  Ids cortos del lanzador → descriptor: `MAPA_ID_CORTO_A_DESCRIPTOR`.
- **Honestidad incluida en el texto:** `rebuffering_reciente_s` va a 0.0 en
  ejecución (el constructor la fija; el contrato no trae stalls) mientras
  que el simulador de entrenamiento sí la calcula → pequeño desajuste
  entrenamiento/ejecución declarado en una frase. Chuleta: "el modelo
  aprendió con esa señal y en el cliente la ve siempre a cero; equivale a
  operar en el régimen 'sin parada reciente', que es el más frecuente; el
  planificador compensa porque él sí ve el buffer".
- **AVISO (resto, no tocado):** el constructor calcula y audita por
  decisión siete "entradas candidatas" por representación
  (`_entradas_candidatas`, con tamaño NOMINAL tasa×duración) que el
  predictor NO consume — herencia de las líneas descartadas (puntuación
  con horizonte). Coste despreciable, pero es código muerto funcional; si
  quieres lo dejamos para la pasada final o lo quito (implica tocar la
  auditoría de entradas: validar con humo).
- **Fronteras:** planificador, CVaR, α, salvaguardas, respaldo, hashes,
  paquete → parte 2; dataset, simulador, rotación de vídeos, pinball con
  suavidad temporal, épocas → 5.7; números de resultados → 6.6 (salvo la
  latencia media, que es una propiedad del artefacto y ya está en el plan
  del cap 6 como dato canónico).
- **F5.2:** verificada renderizada (ver captura). Estilo del cap 4:
  grises + azul (decisión/planificador) + amarillo (datos: bundle y tabla
  del vídeo) + rojo (salvaguardas y anti-fuga). La flecha amarilla de la
  tabla al planificador bordea por la derecha para no cruzar cajas.
- Longitud parte 1: ~1300 palabras. La parte 2 añadirá ~1100 + T5.6 + F5.3.

---
---

# PARTE 2 de 2 — planificador, salvaguardas y paquete del modelo

*(Continúa el apartado 5.6 tras "Arquitectura de generalización".)*

**El planificador: control predictivo sobre escenarios.** El planificador
recibe del predictor una matriz de cinco horizontes por cuatro cuantiles,
ya en bits por segundo. Cada columna es un escenario de red para los cinco
segmentos siguientes: pesimista (cuantil 0,10), desfavorable (0,25),
central (0,50) y optimista (0,75). Sobre esos escenarios el planificador
enumera todas las secuencias de cinco acciones entre las representaciones
que admite la máscara —7776 secuencias con las seis del experimento; el
horizonte se acorta cuando quedan menos segmentos— y simula cada secuencia
bajo cada escenario. La simulación reproduce la dinámica del cliente: el
tiempo de descarga de cada segmento es su tamaño real en bits dividido por
el throughput del escenario, con el tamaño consultado en la tabla del vídeo
activo para el segmento concreto que tocaría descargar; hay rebuffering si
ese tiempo supera la ocupación; y la ocupación se actualiza restando el
tiempo de descarga y sumando la duración del segmento, sin superar el tope
de 60 segundos del cliente. Cada paso suma a la puntuación del escenario una
recompensa con la misma forma que la métrica de calidad del capítulo 6: la
tasa en megabits por segundo, menos 4,3 por cada segundo de rebuffering,
menos la magnitud del cambio de tasa respecto al segmento anterior. Así,
cada secuencia recibe cuatro puntuaciones, una por escenario (Figura 5.3).

**El valor en riesgo condicional.** Un MPC ordinario elegiría la secuencia
con mejor puntuación bajo la predicción central; un MPC robusto, la mejor
bajo el peor escenario. El planificador propio adopta un criterio
intermedio y formal: puntúa cada secuencia con su valor en riesgo
condicional (CVaR, *Conditional Value at Risk*) al nivel α = 0,75, esto es,
la media de las puntuaciones en la fracción peor de los escenarios
\cite{rockafellar2000cvar}. Con cuatro escenarios, la fracción 0,75 peor
son tres: los cuantiles 0,10, 0,25 y 0,50; el optimista no cuenta. La
interpretación es directa: se elige la secuencia que mejor se comporta, en
promedio, cuando la red va como se espera o peor, y ninguna secuencia se
premia por lo bien que iría si la red fuera generosa. Es la lógica del peor
caso de los enfoques robustos —el MPC robusto de Yin et al. y el MPC
bayesiano que planifica sobre la cota inferior de la predicción
\cite{kan2021bayesmpc}—, pero graduada: planificar solo contra el escenario
pesimista produciría un controlador sistemáticamente conservador, mientras
que la media de los escenarios desfavorables conserva la prudencia sin
renunciar a la calidad cuando la cola inferior de la predicción es
estrecha. Y aquí se cierra el diseño del predictor: como la incertidumbre
epistémica solo ensancha esa cola inferior, las situaciones en las que el
modelo no sabe se traducen automáticamente en decisiones más prudentes. La
estructura del planificador —horizonte finito, simulación del buffer,
primera acción de la mejor secuencia y nueva planificación en el segmento
siguiente— es la del MPC clásico \cite{yin2015mpc}; lo que cambia es la
señal (cuantiles en lugar de un valor puntual) y el criterio (CVaR en lugar
de valor esperado o peor caso). El nivel α es fijo en toda la evaluación,
como parámetro del paquete del modelo; el código contiene una variante que
gradúa α con la ocupación del buffer, que no se activó para no introducir
un ajuste adicional en la comparativa.

Conviene subrayar una asimetría con los MPC clásicos del apartado 5.5:
aquellos puntúan con una calidad logarítmica, mientras que el planificador
propio puntúa con la misma forma lineal de la métrica de evaluación. Es una
diferencia de diseño conocida, y el capítulo 6 la recoge entre las
limitaciones de la comparativa.

El coste del planificador es el grueso de la latencia de decisión: 7776
secuencias por cuatro escenarios y cinco pasos son unos 155 000 pasos
simulados por decisión, en Python, que en la máquina de validación
supusieron unos 174 ms de media (capítulo 6); la inferencia neuronal aporta
alrededor del 1 % de ese tiempo. Ese tiempo transcurre dentro de la sesión
y consume buffer, como ocurriría en un despliegue real, y queda registrado
en la telemetría decisión a decisión.

**[FIGURA 5.3 — Una decisión del controlador propio, paso a paso. Fichero:
`figuras/fig_5_3_bucle_decision_propio.svg`]**
*Pie: Figura 5.3: Una decisión del controlador propio: de la matriz de
escenarios a la tasa objetivo. Cada secuencia de acciones se simula bajo los
cuatro escenarios con los tamaños reales de los segmentos; el CVaR al nivel
0,75 promedia los tres escenarios peores; las salvaguardas validan la acción
o delegan en el respaldo; toda decisión deja su diagnóstico en la
telemetría. Los valores numéricos son ilustrativos.*

**Salvaguardas.** El apartado 4.5 fijó el principio: un controlador con
modelo nunca puede invalidar una sesión. La implementación lo cumple con
rutas de respaldo exhaustivas alrededor de tres puntos de fallo. Antes de la
inferencia, si la realimentación no permite construir las entradas (una
clave obligatoria ausente o no numérica, una máscara sin acciones válidas,
un campo prohibido), el controlador delega con un motivo que nombra la
causa. En la carga, si el paquete del modelo no supera la verificación —un
fichero ausente, un esquema desconocido, un tamaño o un resumen SHA-256 que
no coincide con el manifiesto— o si el descriptor del vídeo no existe o su
escalera no coincide con la del manifiesto, delega igualmente. Tras la
inferencia, comprueba que la latencia de la inferencia neuronal no superó
los 50 ms, que la acción elegida está dentro de la máscara y que la tasa
resultante es finita y positiva; cualquier excepción inesperada se trata
como fallo de inferencia. El respaldo es una instancia del MPC robusto que
recibe exactamente la misma realimentación; su tasa se cuantiza y se
comprueba también contra la máscara, y si el propio respaldo fallara se
devolvería la menor tasa válida. El reproductor recibe siempre una tasa.

Cada decisión deja además veinticinco campos de diagnóstico —paquete
cargado y verificado, entradas válidas, número de acciones válidas, acción
bruta del planificador y acción segura, latencia de inferencia, si se usó el
respaldo y por qué motivo— que entran en la telemetría a través de la
extensión del contrato (apartados 4.5 y 4.6). Con ellos la evaluación audita
el controlador decisión a decisión: en el experimento del capítulo 6, las
1740 decisiones del controlador propio (29 por sesión en 60 sesiones)
quedaron auditadas y ninguna recurrió al respaldo. Los motivos de respaldo
forman un vocabulario cerrado, de modo que la telemetría es agregable y
cualquier fallo futuro queda clasificado.

**El paquete del modelo.** Todo lo que el controlador necesita del
entrenamiento viaja en un directorio de cinco ficheros: los pesos de los
cinco miembros del conjunto (un único fichero de tensores y metadatos, sin
código), la configuración del modelo (arquitectura, horizonte, cuantiles y
nombres de las entradas), la normalización (medias y desviaciones de la
partición de entrenamiento), la configuración del planificador (α, pesos,
horizonte, ensanchado de la cola, origen de los tamaños de segmento y vídeo
por defecto) y un manifiesto con el resumen SHA-256 y el tamaño de cada
fichero. La carga comprueba la presencia de los cinco, el identificador de
esquema, los tamaños y los resúmenes, y solo entonces lee los pesos con la
carga restringida del apartado 5.1 y reconstruye cada miembro desde la
definición de la red que vive en el código. El paquete es, así, la frontera
entre la fabricación del modelo (apartado 5.7) y su ejecución: lo que
decidió en el capítulo 6 es exactamente el paquete cuyos resúmenes
acompañan la evidencia, y cualquier alteración posterior lo haría
inservible en lugar de silenciosamente distinto. La Tabla 5.6 reúne los
parámetros del controlador propio con los valores empleados en la
evaluación.

**[TABLA 5.6 — Parámetros del controlador propio en la evaluación]**

| Parámetro | Valor | Dónde se fija |
|---|---|---|
| Historial de entrada | 5 descargas (throughput y tiempo) | código |
| Escalares de sesión | 7 | código |
| Miembros del conjunto | 5 redes GRU de 96 unidades | paquete del modelo |
| Horizonte de planificación | 5 segmentos | paquete del modelo |
| Cuantiles predichos | 0,10 · 0,25 · 0,50 · 0,75 | paquete del modelo |
| Ensanchado epistémico de la cola inferior | 1,0 (factor sobre el desacuerdo) | paquete del modelo |
| Nivel de riesgo α del CVaR | 0,75 (media de los 3 escenarios peores de 4) | paquete y configuración |
| Pesos del objetivo (rebuffering; cambios) | 4,3 por segundo; 1,0 por Mbit/s | paquete del modelo |
| Tamaños de segmento en la simulación | reales del servidor (tabla del vídeo activo) | inyectado por sesión |
| Tope del buffer simulado | 60 s | configuración |
| Latencia máxima de inferencia | 50 ms | configuración |
| Controlador de respaldo | MPC robusto | configuración |
| Verificación de resúmenes del paquete | activada | configuración |

*Pie: Tabla 5.6: Parámetros del controlador propio y valores empleados en
la evaluación del capítulo 6.*

*(El apartado 5.7 describe el entorno con el que se fabrica el paquete del
modelo: el simulador de sesiones, el dataset de cuantiles y el
entrenamiento del conjunto.)*

---

### Notas para Daniel (no van a la memoria) — parte 2

- **Citas de la parte 2 (3):** `rockafellar2000cvar` (sin PDF local; se cita
  como definición del CVaR = media de la cola peor de una distribución de
  pérdidas/ganancias; es exactamente lo que implementa `_cvar`),
  `kan2021bayesmpc` (PDF verificado: "lower bound ... robust MPC ...
  worst-case QoE" — el texto lo usa para "planificar sobre la cota
  inferior") y `yin2015mpc` (PDF verificado en 5.5: estructura MPC y
  RobustMPC = MPC con la cota inferior). Sin citas nuevas sin verificar.
- **Verificado en código (05/09):** `planificar_accion`: `itertools.product`
  sobre acciones válidas con `horizonte_efectivo = min(5, len(pred),
  restantes)`; `_puntuar_secuencia_cvar` simula POR CUANTIL con
  `bits = 8·escalera.bytes_segmento(accion, indice_segmento + h)` (tabla
  real), `throughput = max(pred[h][k], 1)`, `rebuffer = max(t − B, 0)`,
  `B ← min(max(B − t, 0) + p, buffer_maximo_s = 60)`, recompensa =
  `bitrate/1e6 − 4,3·rebuffer − |Δbitrate|/1e6`; `_cvar` ordena y promedia
  los `ceil(α·n)` peores → con n = 4 y α = 0,75, `ceil(3,0) = 3` → q10, q25,
  q50. **α fijo:** `controlador_propio` pasa `alfa_riesgo` (config 0,75) o
  `bundle.alfa_riesgo` (0,75) → la función `alfa_riesgo_por_buffer`
  (0,25/0,50/0,75/1,0 con umbrales 4/12/20 s) existe pero NUNCA se ejecuta
  en la evaluación. Es lo que dice el texto ("variante no activada"); si el
  tribunal pregunta por qué existe: "se probó en la iteración de junio;
  fijar α evita que la comparativa dependa de un ajuste más".
  Alineación de índices: el reproductor decide en el índice k (segmento ya
  descargado; 0 = init) para el k+1; el descriptor indexa desde 0 el primer
  segmento de vídeo → `bytes_segmento(a, k)` = tamaño del SIGUIENTE
  segmento. Coherente con 4.7 ("el segmento concreto que viene a
  continuación").
  Salvaguardas: motivos `falta_entrada_obligatoria`,
  `fallo_construccion_entradas`, `mascara_acciones_invalida`,
  `todas_las_acciones_invalidas`, `fallo_carga_bundle`,
  `perfil_video_no_disponible`, `latencia_excedida`, `accion_enmascarada`,
  `tasa_invalida`, `fallo_inferencia`; `motivo_estable` canoniza a un
  vocabulario cerrado de 20 valores. El límite de 50 ms se compara con
  `bundle.ultima_latencia_ms` = SOLO la inferencia neuronal (no el
  planificador) — el texto lo dice así, a propósito. Respaldo =
  `ControladorMpcRobusto()` con `fijarFeedbackReproductor(mismo feedback)`;
  su tasa se cuantiza y se valida contra la máscara; si falla, `_menor_tasa_
  valida`. Diagnóstico: `CLAVES_DIAGNOSTICO_RED` = 25 claves (contadas).
  Bundle: `FICHEROS_BUNDLE_REQUERIDOS` = 5; hashes para 4 (el manifiesto no
  se hashea a sí mismo); `verificar_ficheros_del_manifiesto` compara
  tamaño SIEMPRE y sha256 si `verificar_hashes`; `torch.load(weights_only)`;
  `clave_modelo` comprobada; miembros reconstruidos con `PredictorCuantiles`
  del código.
- **Aritmética del coste:** 6⁵ = 7776; × 4 escenarios × 5 pasos = 155 520
  pasos simulados por decisión. Latencia de decisión media del paquete
  canónico 174 ms; inferencia 1,255 ms → ≈ 0,7 % ("alrededor del 1 %").
  1740 decisiones = 60 sesiones del propio (15 ventanas × 4 vídeos) × 29
  decisiones (30 segmentos, el primero es calentamiento sin decisión).
- **Chuletas de defensa:**
  · "¿Por qué CVaR y no el peor caso?" → "El peor caso (q10) sería un
    RobustMPC con predictor neuronal: prudente pero conservador siempre.
    CVaR 0,75 promedia q10, q25 y q50: prudente cuando la cola inferior es
    ancha, ambicioso cuando es estrecha. Y la cola inferior es justo donde
    el ensemble mete la incertidumbre epistémica: no saber ⇒ prudencia."
  · "¿Por qué α = 0,75?" → "Con cuatro cuantiles, 0,75 es la fracción que
    excluye exactamente al optimista. Se fijó antes de la evaluación y no
    se tocó; la variante adaptativa por buffer existe pero no se usó".
  · "¿Tu planificador optimiza tu propia métrica?" → "Sí, la misma forma
    lineal (bitrate − 4,3·rebuffer − |Δ|), declarado en 5.6 y en 6.7; los
    MPC clásicos usan calidad log. La comparativa lo reconoce como
    limitación. Lo que NO hago es cambiar la métrica después de ver
    resultados".
  · "¿Y si el modelo tarda?" → "Solo vigilo la inferencia (50 ms; mide
    1,3 ms). El planificador es determinista y su coste está acotado por la
    enumeración; los 174 ms se pagan dentro de la sesión, consumen buffer y
    quedan en la telemetría — no hay trampa de tiempo".
  · "¿Cómo sé que corrió tu modelo y no el respaldo?" → "1740/1740
    decisiones con `exito_red` y 0 respaldos, auditadas por compuerta".
- **F5.3:** verificada renderizada (ver captura). Ejemplo numérico
  ILUSTRATIVO (el pie lo dice); el resto (fórmulas, parámetros, coste) es
  literal del código y del paquete canónico.
- **Fronteras:** cómo se fabrica el paquete (simulador, dataset, pinball con
  suavidad temporal, rotación de vídeos, épocas, WSL/ROCm) → 5.7; números de
  QoE → 6.6; la asimetría log/lineal como limitación → 6.7; la iteración con
  α adaptativo y la variante MLP → 7.5 (cualitativo).
- Longitud parte 2: ~1250 palabras + T5.6. Apartado 5.6 completo ≈ 2550
  palabras: es el más largo del capítulo, como corresponde a la aportación.
