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
> F5.3) llega en el turno siguiente.

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
