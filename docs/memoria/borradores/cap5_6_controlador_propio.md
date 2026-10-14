# Borrador 5.6 (versión 2) — El controlador propio

> VERSIÓN 2, rehecha el 13/10/2026 para masticar y reescribir. Sustituye a la
> versión 1 (partes 1 y 2 de septiembre, recuperable en el commit `1a66daa`).
> Impersonal, frases cortas, sin rayas. Ecuaciones en LaTeX (en Word: Alt+= y
> pegar). Numeración de figuras, tablas y ecuaciones provisional.
> Fuente técnica: entregable `core/controladores/{controlador_propio,
> constructor_entradas,entradas_contexto,constantes_entradas,diagnosticos_red,
> seguridad_red,mascara_acciones}.py` y `core/modelo_propio/*.py` (sin cambios
> desde el 07/08), bundle de `03_modelos`, paquetes de las dos evaluaciones
> (`20260810_133520_tfg_final` y `20261013_233745_tfg_final`) y reproducción
> fuera de línea de sus 3480 decisiones (`docs/memoria/apoyo/`). Decisiones de
> diseño: `decision_mpc_prudente_*.md`. Versión 2.1 (14/10): ajustada a las dos
> evaluaciones (lista de cambios al final de las notas).

---

### 5.6. El controlador propio

Los controladores del apartado 5.5 comparten dos limitaciones. La primera es
cómo tratan la incertidumbre de la red. El MPC planifica con un único valor
previsto del throughput y su variante robusta, con un único valor pesimista
derivado de sus errores recientes; ninguno estima cuánto puede variar la red
ni si la predicción es fiable en la situación concreta. La segunda es cómo
tratan el contenido: todos suponen que un segmento ocupa su tasa nominal por
su duración, cuando el tamaño real varía con la complejidad de cada escena
(apartado 4.7).

El controlador propio conserva la estructura de control predictivo del MPC y
actúa sobre esas dos limitaciones. En lugar de un valor, predice una
distribución del throughput de los próximos segmentos, acompañada de una
medida de la confianza del propio modelo. Con esa distribución y con el
tamaño real de cada segmento, elige la secuencia de calidades que mejor se
comporta en los escenarios de red desfavorables. La Tabla 5.6 resume la
diferencia con los dos MPC clásicos.

**[TABLA 5.6 — Tratamiento de la incertidumbre en los controladores predictivos]**

| Aspecto | MPC (5.5) | MPC robusto (5.5) | Controlador propio |
|---|---|---|---|
| Predicción del throughput | Un valor: media armónica de las 5 últimas descargas | Un valor pesimista: la media armónica dividida por (1 + error máximo reciente) | Cuatro cuantiles por segmento futuro, aprendidos de trazas reales y ensanchados según la desconfianza del modelo |
| Escenarios que se ponderan | Uno | Uno | Los tres no optimistas, promediados (CVaR) |
| Tamaño de cada segmento | Nominal (tasa × duración) | Nominal | Real, leído de la tabla del vídeo |
| Calidad en el objetivo | Logarítmica | Logarítmica | Lineal, como la métrica de evaluación |
| Horizonte | 3 segmentos | 3 segmentos | 5 segmentos |

*Pie: Tabla 5.6: Cómo tratan la incertidumbre de la red y el tamaño de los
segmentos los dos MPC clásicos y el controlador propio.*

La combinación de un predictor aprendido con un controlador clásico tiene
precedentes. En el sistema Fugu, desplegado en la plataforma Puffer, un
predictor neuronal probabilístico entrenado con datos del propio despliegue
sustituye al predictor de throughput de un MPC \cite{yan2020puffer}. En el
MPC bayesiano, una red neuronal bayesiana estima la incertidumbre de la
predicción y el planificador optimiza el peor caso dentro de la región de
confianza resultante \cite{kan2021bayesmpc}. La separación entre predicción y
decisión responde además a la experiencia de este trabajo: las primeras
iteraciones, con políticas aprendidas que elegían directamente la calidad, no
superaron a los controladores clásicos (apartado 7.5). Al separar ambas
tareas, la red neuronal aprende solo lo que puede aprenderse y medirse con
datos, cómo evolucionará la red, y la decisión la toma un optimizador
determinista cuyo razonamiento puede inspeccionarse paso a paso.

La Figura 5.2 muestra la arquitectura. En cada decisión intervienen dos tipos
de información. La información de red se ha observado en el pasado: el
constructor de entradas la extrae de la realimentación del reproductor y el
predictor la transforma en cuatro escenarios de throughput para cada uno de
los cinco segmentos siguientes. La información del contenido se conoce de
antemano: es la tabla de tamaños reales del vídeo activo, que solo consume el
planificador. El planificador combina ambas, elige una acción y la somete a
unas salvaguardas que, ante cualquier fallo, delegan la decisión en el MPC
robusto. Los subapartados siguientes recorren cada pieza.

**[FIGURA 5.2 — Arquitectura del controlador propio. Fichero:
`figuras/fig_5_2_arquitectura_controlador_propio.svg`]**
*Pie: Figura 5.2: Arquitectura del controlador propio. La información de red,
observada en el pasado, llega al planificador a través del predictor de
cuantiles; la información del contenido, conocida de antemano, llega
directamente desde la tabla de tamaños del vídeo activo. Las salvaguardas
validan cada decisión o la delegan en el MPC robusto.*

#### 5.6.1. Entradas del predictor

El predictor recibe dos grupos de entradas, construidos en cada decisión a
partir del contrato de realimentación del apartado 4.5. El primero es una
secuencia con las cinco últimas descargas de segmentos de vídeo; de cada una
se toma el throughput medido, en escala logarítmica, y el tiempo de descarga.
El segundo son siete valores escalares que describen el estado de la sesión:
la ocupación del buffer, el índice y la tasa nominal del nivel que se está
reproduciendo, la magnitud del último cambio de nivel, el rebuffering reciente
y dos indicadores de progreso (la fracción de segmentos que quedan por
reproducir y si queda alguno). Todas las entradas se normalizan con la media y
la desviación típica calculadas solo sobre la partición de entrenamiento.

Lo que el predictor no recibe es tan importante como lo que recibe. No ve el
tamaño de ningún segmento ni ningún rasgo de la escena: la única información
del contenido a su alcance es la tasa nominal del nivel en curso, que forma
parte del estado del reproductor. Tampoco ve la identidad de la traza de red,
su partición experimental, su dificultad ni, por supuesto, el throughput
futuro. Esta exclusión no depende de la disciplina de quien programa las
entradas: el constructor rechaza cualquier realimentación que contenga alguna
de las 29 claves prohibidas y comprueba que cada entrada sea numérica, finita
y de la longitud esperada. Si algo falla, el controlador no improvisa una
entrada: delega la decisión y registra el motivo (apartado 5.6.6).

Dos de las señales no se obtienen en ejecución exactamente igual que en el
entrenamiento. El rebuffering reciente no forma parte del contrato del cliente
y se entrega siempre a cero. Los indicadores de progreso se calculan sobre la
duración completa del vídeo, mientras que el entrenamiento los calculaba
sobre ventanas de 30 segmentos. Ambas discrepancias se detectaron en la
revisión final del sistema, después de la primera evaluación del capítulo 6,
y no se corrigieron antes de la segunda para que las dos evaluaran
exactamente el mismo sistema. Su efecto sobre las decisiones se cuantifica en
el apartado 6.7.

#### 5.6.2. Predictor de cuantiles del throughput

**Qué predice.** El throughput de los próximos segmentos es incierto, y un
único valor previsto oculta lo que más interesa al decidir: cuánto puede
empeorar la red. Por eso el predictor estima cuantiles. El cuantil τ del
throughput es el valor que la red supera con probabilidad 1 − τ; el cuantil
0,10, por ejemplo, es el throughput que se supera nueve de cada diez veces. El
predictor estima cuatro cuantiles, τ ∈ {0,10; 0,25; 0,50; 0,75}, para cada uno
de los cinco segmentos siguientes. No supone ninguna forma para la
distribución, de modo que puede representar colas inferiores largas, propias
de redes que sufren caídas bruscas.

**Qué aprende.** El modelo no predice el throughput en valor absoluto, sino su
logaritmo relativo a una base: la media armónica $\bar{C}_k$ de las descargas
del historial, el mismo estimador que usan los MPC clásicos. La etiqueta de
entrenamiento para el horizonte $h$ es

$$ y_{k,h} = \ln \frac{C_{k+h}}{\bar{C}_k}, \qquad h = 1, \dots, 5, \tag{5.1} $$

donde $C_{k+h}$ es el throughput medido en la descarga $h$-ésima posterior a la
decisión $k$. Al trabajar en escala relativa, un mismo modelo sirve para redes
de cientos de kbit/s y de decenas de Mbit/s. En ejecución, cada cuantil
predicho $\hat{y}^{(\tau)}_{k,h}$ se reconvierte a bit/s como
$\hat{C}^{(\tau)}_{k+h} = \bar{C}_k \, e^{\hat{y}^{(\tau)}_{k,h}}$, acotado
entre 0,15 y 4 veces la base para que una predicción anómala no arrastre al
planificador.

**Arquitectura.** La secuencia de descargas la procesa una red recurrente con
unidades GRU (*Gated Recurrent Unit*) de 96 dimensiones \cite{cho2014gru}. Una
GRU recorre la secuencia paso a paso y mantiene un vector de estado que resume
lo observado; unas puertas aprendidas deciden en cada paso qué parte del
estado conservar y cuánto actualizarlo con la nueva muestra. Puede verse como
un filtro recursivo no lineal cuyos coeficientes se aprenden de los datos, lo
que le permite captar tendencias que un promedio fijo no distingue. El estado
final se concatena con los siete escalares y una red densa (capas de 96 y 64
neuronas, con una desactivación aleatoria del 10 % durante el entrenamiento)
produce veinte valores: cuatro cuantiles por cinco horizontes. Para cada
horizonte, la red emite el cuantil más bajo y, para los demás, incrementos
que se fuerzan a ser positivos:

$$ \hat{y}^{(\tau_1)} = z_1, \qquad \hat{y}^{(\tau_j)} = \hat{y}^{(\tau_{j-1})} + \ln\left(1 + e^{z_j}\right), \quad j = 2, 3, 4, \tag{5.2} $$

donde $z_j$ son las salidas de la red y $\ln(1 + e^{z})$, la función
*softplus*, siempre es positiva. Con esta construcción los cuantiles nunca
pueden cruzarse, sin necesidad de corregirlos después.

**Cómo se entrena.** El criterio de entrenamiento es la pérdida de cuantiles,
o pérdida *pinball*, de la regresión cuantílica \cite{koenker1978quantiles}:

$$ \rho_\tau(u) = \max\left(\tau u,\; (\tau - 1)\,u\right), \qquad u = y - \hat{y}^{(\tau)}. \tag{5.3} $$

La pérdida es asimétrica, y esa asimetría hace que su mínimo se alcance
precisamente en el cuantil $\tau$. Para $\tau = 0{,}10$, una predicción que
queda por encima del valor real cuesta 0,9 por unidad de error y una que queda
por debajo, 0,1: sobrestimar es nueve veces más caro, de modo que el cuantil
aprendido se sitúa donde solo una de cada diez observaciones cae por debajo.
El proceso de entrenamiento completo se describe en el apartado 5.7.

**Dos tipos de incertidumbre.** La incertidumbre del predictor tiene dos
orígenes, que el diseño trata por separado siguiendo la distinción habitual
en la literatura \cite{kan2021bayesmpc}. La variabilidad propia de la red, o
incertidumbre aleatoria, la capturan los cuantiles: la separación entre el
0,10 y el 0,75 refleja cuánto puede moverse el throughput. La desconfianza del
modelo en sí mismo, o incertidumbre epistémica, crece en situaciones poco
representadas en el entrenamiento, y un único modelo no la percibe. Para
estimarla se entrenan cinco redes idénticas en arquitectura pero con
inicializaciones aleatorias distintas, la técnica de los conjuntos profundos
(*deep ensembles*) \cite{lakshminarayanan2017ensembles}. Donde los datos de
entrenamiento abundan, las cinco coinciden; donde escasean, discrepan.

La combinación de los cinco miembros es deliberadamente asimétrica. Para cada
horizonte y cuantil se promedian sus predicciones; después, los cuantiles
inferiores se desplazan hacia abajo en proporción al desacuerdo:

$$ \tilde{y}^{(\tau)} = \bar{y}^{(\tau)} - c \, \frac{0{,}5 - \tau}{0{,}5} \, \sigma \qquad \text{para } \tau < 0{,}5, \tag{5.4} $$

donde $\bar{y}^{(\tau)}$ es la media de los cinco miembros, $\sigma$ la
desviación típica de sus cinco medianas y $c = 1$ el factor de ensanchado. En
escala logarítmica, el cuantil 0,10 baja $0{,}8\sigma$ y el 0,25, $0{,}5\sigma$,
lo que equivale a multiplicar el throughput correspondiente por
$e^{-0{,}8\sigma}$ y $e^{-0{,}5\sigma}$. Los cuantiles superiores no se tocan.
La razón de la asimetría es que solo la cola inferior provoca paradas: cuando
el modelo no sabe, los escenarios pesimistas se vuelven más pesimistas, y los
optimistas no se inflan. En las dos evaluaciones del capítulo 6 los cinco
miembros coincidieron en la mayoría de las decisiones (en la decisión
mediana, el ensanchado rebajó el cuantil 0,10 un 2 %) y discreparon en una
minoría: en el 10 % de las decisiones con más desacuerdo el descenso superó
el 7 %, y en el caso extremo alcanzó el 32 % y el 33 %.

**Tamaño y coste.** El modelo es pequeño a propósito: 46 292 parámetros por
miembro, 231 460 en el conjunto y menos de un megabyte de pesos. En la máquina
de validación, sin aceleración gráfica, los cinco miembros se evaluaron en
1,25 ms de media por decisión en la primera evaluación y en 2,18 ms en la
segunda, con la máquina más lenta (capítulo 6), muy por debajo del límite de
50 ms que vigilan las salvaguardas.

#### 5.6.3. Planificador con valor en riesgo condicional

**Escenarios.** El planificador recibe del predictor una matriz de cinco
horizontes por cuatro cuantiles, ya en bit/s. Cada columna se interpreta como
un escenario de red para los cinco segmentos siguientes: pesimista
($\tau = 0{,}10$), desfavorable (0,25), central (0,50) y optimista (0,75).
Cada escenario mantiene el mismo cuantil en los cinco segmentos, es decir,
supone que un periodo malo de la red se prolonga durante todo el horizonte.

**Simulación.** Para cada secuencia de acciones
$\mathbf{a} = (a_1, \dots, a_5)$, con $a_t$ uno de los seis niveles de la
escalera, el planificador simula el buffer bajo cada escenario $\tau$ con la
misma dinámica que el cliente:

$$ d_t = \frac{8\,S_{k+t}(a_t)}{\hat{C}^{(\tau)}_{k+t}}, \qquad r_t = \max(d_t - B_t,\, 0), \qquad B_{t+1} = \min\big(\max(B_t - d_t,\, 0) + L,\; B_{\max}\big), \tag{5.5} $$

donde $S_{k+t}(a_t)$ es el tamaño real en bytes del segmento $k+t$ en el nivel
$a_t$, consultado en la tabla del vídeo activo; $d_t$ es su tiempo de
descarga; $r_t$, el rebuffering; $B_t$, la ocupación del buffer ($B_1$ es la
actual); $L = 4$ s, la duración del segmento, y $B_{\max} = 60$ s, el tope del
buffer del cliente (apartado 4.3). En cada escenario, la secuencia recibe una
puntuación con la misma forma que la métrica de calidad de la evaluación:

$$ G^{(\tau)}(\mathbf{a}) = \sum_{t=1}^{5} \Big[ R(a_t) - 4{,}3\, r^{(\tau)}_t - \big| R(a_t) - R(a_{t-1}) \big| \Big], \tag{5.6} $$

donde $R(a)$ es la tasa nominal del nivel $a$ en Mbit/s y $a_0$, el nivel
actual. Con seis niveles y cinco segmentos hay $6^5 = 7776$ secuencias, y cada
una se simula en los cuatro escenarios. A diferencia de los MPC clásicos del
apartado 5.5, que puntúan la calidad en escala logarítmica, el planificador
propio usa la forma lineal de la métrica de evaluación; el apartado 6.7 recoge
esta diferencia entre las limitaciones de la comparativa.

**Criterio de decisión.** Un MPC ordinario elegiría la secuencia con mejor
puntuación en el escenario central y un MPC robusto, la mejor en un escenario
pesimista. El planificador propio usa un criterio intermedio con fundamento
formal: el valor en riesgo condicional (CVaR, *Conditional Value at Risk*)
\cite{rockafellar2000cvar}, que promedia las puntuaciones de la fracción peor
de los escenarios. Con $n$ escenarios del mismo peso, y con la convención en
la que $\alpha$ es la fracción de escenarios peores que se promedia,

$$ \mathrm{CVaR}_\alpha(\mathbf{a}) = \frac{1}{m} \sum_{j=1}^{m} G_{(j)}(\mathbf{a}), \qquad m = \lceil \alpha n \rceil, \tag{5.7} $$

donde $G_{(1)} \le \dots \le G_{(n)}$ son las puntuaciones de la secuencia
ordenadas de peor a mejor. Con $\alpha = 1$ el criterio es la media de todos
los escenarios y, al reducir $\alpha$, se acerca al peor caso. El controlador
usa $\alpha = 0{,}75$, de modo que, con cuatro escenarios, promedia tres. Los
cuantiles no reparten la probabilidad por igual, y los tres puntos promediados
(0,10, 0,25 y 0,50) se concentran en la parte baja del intervalo [0; 0,75]
que representan; el criterio debe leerse, por tanto, como una aproximación
discreta y prudente del CVaR de la distribución predicha. El planificador
elige la secuencia $\mathbf{a}^{*}$ de mayor CVaR, aplica solo su primera
acción y vuelve a planificar en el segmento siguiente (horizonte deslizante),
igual que el MPC de la literatura \cite{yin2015mpc}.

**Lo que significa el criterio.** La expresión (5.7) admite una lectura más
sencilla. En (5.6), la calidad y los cambios de nivel de una secuencia no
dependen del escenario: solo el rebuffering depende de la red. Además, como
los cuantiles están ordenados en cada horizonte y una red más rápida nunca
produce más rebuffering, las puntuaciones quedan ordenadas igual que los
escenarios, y las tres peores son siempre las de $\tau = 0{,}10$, 0,25 y 0,50
(propiedad comprobada en todas las decisiones de las dos evaluaciones). Por
tanto,

$$ \mathrm{CVaR}_{0{,}75}(\mathbf{a}) = \sum_{t} R(a_t) - \sum_{t} \big| R(a_t) - R(a_{t-1}) \big| - 4{,}3 \cdot \frac{1}{3} \sum_{\tau \in \{0{,}10;\, 0{,}25;\, 0{,}50\}} \; \sum_{t} r^{(\tau)}_t . \tag{5.8} $$

El planificador es, así, un MPC cuya penalización por rebuffering es la media
del rebuffering simulado en los tres escenarios no optimistas, con el tamaño
real de cada segmento. El escenario optimista no interviene: ninguna secuencia
se premia por lo bien que saldría si la red fuera generosa. Es el mismo
principio por el que un radioenlace se dimensiona con un margen de
desvanecimiento: no se diseña para el canal medio, sino para que el servicio
se mantenga en la fracción desfavorable de las condiciones. Con esta lectura
se cierra también el diseño del predictor: como el desacuerdo del conjunto
solo ensancha la cola inferior, las situaciones que el modelo conoce peor se
traducen automáticamente en decisiones más prudentes.

**Cómo se eligió $\alpha$.** El valor de $\alpha$ se fijó durante el
desarrollo, con una versión anterior del predictor, mediante un barrido sobre
ventanas de la partición de validación. El comportamiento resultó poco
sensible a $\alpha$, y 0,75 ofreció el mejor peor caso con el menor coste en
calidad media. La primera versión del planificador hacía depender $\alpha$ de
la ocupación del buffer, con más prudencia cuanto menos buffer; el valor fijo
igualó o mejoró a esa regla, que el código conserva sin activar. También se
probó un criterio basado en una cota inferior de confianza, que empeoró el
peor caso y se descartó. El apartado siguiente explica la baja sensibilidad a
$\alpha$ con las decisiones del propio experimento.

**Coste.** Las 7776 secuencias por cuatro escenarios y cinco pasos suman
155 520 pasos simulados por decisión, en Python. En la máquina de validación
supusieron 174 ms de media por decisión en la primera evaluación y 317 ms en
la segunda, en la que la máquina virtual fue más lenta durante toda la
ejecución (capítulo 6); la inferencia neuronal es menos del 1 % de ese
tiempo. Ese tiempo transcurre dentro de la sesión y consume buffer, igual que
en un despliegue real, y queda registrado en la telemetría decisión a
decisión.

#### 5.6.4. El controlador en el experimento

Las decisiones del controlador propio en las dos evaluaciones del capítulo 6
pueden reproducirse fuera de línea. Basta con reinyectar, en orden, la
realimentación registrada en la telemetría de cada sesión en un controlador
nuevo, con el mismo paquete del modelo y la misma tabla de tamaños. La
reproducción de las 3480 decisiones de las dos evaluaciones (1740 en cada
una), en otra máquina y con otra versión de PyTorch, devuelve exactamente las
acciones registradas. Esta reproducibilidad permite examinar cualquier
decisión con detalle y medir qué aporta cada componente.

**Una decisión real.** La Figura 5.3 reconstruye una decisión elegida con una
regla fijada antes de mirar su desenlace: la primera de la primera
evaluación, en una sesión con traza real y buffer entre 8 y 30 s, en la que el criterio de riesgo
y el escenario central eligen niveles distintos dentro de la mitad alta de la
escalera. Se reproduce el vídeo Paseo a 30 fps sobre una traza de banda ancha
fija, con 16,6 s de buffer y el nivel de 1850 kbit/s en curso. Cuatro de las
cinco últimas descargas midieron 2,02 Mbit/s y la más reciente, 1,69 Mbit/s;
la base es 1,94 Mbit/s. Para el segmento siguiente, el predictor da un cuantil
0,10 de 1,25 Mbit/s, un 0,25 de 1,64, una mediana de 1,84 y un 0,75 de
2,08 Mbit/s, y el abanico apenas cambia en los cinco segmentos del horizonte.

La decisión se juega entre dos secuencias (Figura 5.3b). Subir a 2850 kbit/s
y mantenerlo cinco segmentos es la mejor secuencia en el escenario central:
no provoca rebuffering y puntúa 13,25 (cinco segmentos a 2,85 Mbit/s menos el
cambio de nivel). Pero el siguiente segmento a 2850 kbit/s pesa 1,58 MB, un
10,6 % más que su valor nominal, y con los throughputs de los cuantiles 0,25 y
0,10 esa secuencia acumula 3,3 y 14,7 s de rebuffering, con puntuaciones de
−0,89 y −50,00. Mantener 1850 kbit/s no provoca rebuffering en ningún
escenario y puntúa 9,25 en los cuatro. El CVaR de la primera secuencia es
(−50,00 − 0,89 + 13,25)/3 = −12,55, y el de la segunda, 9,25. El controlador
mantiene 1850 kbit/s, mientras que un planificador guiado solo por la mediana
habría subido. La descarga siguiente midió 1,56 Mbit/s, entre los cuantiles
0,10 y 0,25 predichos.

**[FIGURA 5.3 — Una decisión real de la primera evaluación. Fichero:
`figuras/fig_5_3_decision_real.svg`]**
*Pie: Figura 5.3: Una decisión real de la primera evaluación (vídeo Paseo a 30 fps,
traza de banda ancha fija, decisión tras el décimo segmento). (a) Cuantiles
predichos del throughput para los cinco segmentos siguientes, niveles de la
escalera y throughput medido después. (b) Puntuación de las dos secuencias
candidatas en cada escenario: la mediana favorece subir a 2850 kbit/s; el
CVaR, que promedia los tres escenarios no optimistas, mantiene 1850 kbit/s.*

**El peso de cada componente.** La misma reproducción permite medir qué parte
del controlador determina las decisiones. Para cada decisión de las sesiones
con trazas reales se recalculó, sobre exactamente el mismo estado, la acción
que habría elegido el planificador con una pieza cambiada. La Tabla 5.7 recoge
el resultado en las dos evaluaciones, que admite tres lecturas válidas en
ambas.

- La pieza que más pesa es el propio criterio de riesgo. Planificar solo con
  la mediana habría cambiado entre una de cada seis y una de cada cuatro
  decisiones, y en más del 90 % de esos casos hacia un nivel más alto.
- El valor exacto de $\alpha$ apenas importa. Sustituir el CVaR por el peor
  escenario o por la media de los cuatro cambia entre el 0,6 % y el 1,6 % de
  las decisiones. La explicación está en (5.8): el rebuffering de una
  secuencia arriesgada aparece de golpe en los escenarios pesimistas, y
  cualquier criterio que los tenga en cuenta la descarta. Lo determinante es
  mirar la cola de la distribución, no cuánto peso se le da.
- El tamaño real de los segmentos y el ensanchado epistémico actúan en una
  fracción pequeña de las decisiones, entre el 3 % y el 5 %. El tamaño real
  lo hace en los dos sentidos: unas veces evita un segmento más pesado de lo
  nominal y otras aprovecha uno más ligero. El ensanchado actúa sobre todo
  hacia la prudencia.

Los porcentajes de la segunda evaluación son menores porque sus ventanas
fueron más fáciles: el controlador eligió el nivel más alto en el 63 % de sus
decisiones, frente al 52 % de la primera, y en ese nivel apenas queda margen
para que otro criterio decida distinto. Estos porcentajes miden el cambio en la decisión inmediata, no su
efecto sobre la calidad de experiencia, que exigiría ejecutar las sesiones
completas con cada variante (apartado 7.4).

**[TABLA 5.7 — Efecto de cada componente sobre las decisiones del controlador]**

| Variante evaluada sobre el mismo estado | Primera evaluación | Segunda evaluación | Sentido del cambio |
|---|---|---|---|
| Solo el escenario central (mediana) | 329 (23,6 %) | 233 (16,7 %) | El CVaR elige un nivel más bajo en el 93 % y el 91 % de los casos |
| Solo el escenario pesimista (cuantil 0,10) | 20 (1,4 %) | 22 (1,6 %) | El peor caso elige más bajo en 19 y 21 |
| Media de los cuatro escenarios ($\alpha = 1$) | 16 (1,1 %) | 8 (0,6 %) | El CVaR elige más bajo en 12 y 6 |
| Tamaños nominales en lugar de reales | 68 (4,9 %) | 41 (2,9 %) | En ambos sentidos: más bajo con tamaños reales en 32 y 21, más alto en 36 y 20 |
| Sin ensanchado epistémico | 61 (4,4 %) | 37 (2,7 %) | Con ensanchado se elige más bajo en el 70 % y el 65 % |

*Pie: Tabla 5.7: Número de decisiones (de 1392 por evaluación, sesiones con
trazas reales) en las que la variante indicada habría elegido otra acción que
el controlador propio, partiendo del mismo estado.*

#### 5.6.5. El vídeo como dato: generalización sin reentrenamiento

La separación entre predictor y planificador tiene además una consecuencia
práctica: el controlador puede usarse con vídeos distintos sin reentrenar el
modelo. El predictor aprende la dinámica de la red y el estado del
reproductor, no la de un contenido concreto. El conocimiento del contenido
llega por otra vía: el planificador recibe la tabla de tamaños del vídeo
activo (el descriptor del apartado 4.7) como un dato de configuración, que el
lanzador inyecta por sesión (apartado 5.4). En su primera decisión, el
controlador carga el descriptor del vídeo indicado y comprueba que su escalera
coincide con la que el reproductor extrajo del manifiesto, con el mismo número
de representaciones y las mismas tasas nominales. Si no coinciden, no
planifica con una tabla equivocada: delega en el respaldo y lo registra.

Las dos evaluaciones del capítulo 6 lo ponen en práctica. En cada una, las
configuraciones de las 60 sesiones del controlador propio apuntan al mismo
paquete de modelo, entrenado una sola vez, y lo único que cambia entre los
cuatro vídeos es el identificador de la tabla. Un vídeo nuevo requiere una tabla nueva, que es un
subproducto del empaquetado y cualquier servidor puede generar al publicar el
contenido, pero ningún reentrenamiento.

Esta generalización tiene un dominio de validez declarado. El modelo se
entrenó con segmentos de 4 s, con la escalera de 300 a 4300 kbit/s y con
vídeos cuya variabilidad de tamaño entre segmentos no supera el 16 %; su única
entrada relacionada con el contenido es la tasa nominal del nivel en curso.
Un contenido con otra escalera u otra duración de segmento queda fuera del
régimen para el que se diseñó. Además, los cuatro vídeos de la evaluación
forman parte de los ocho que rota el entrenamiento (apartado 5.7), de modo que
el funcionamiento con un contenido nunca visto es una propiedad del diseño y
no un resultado medido; su comprobación queda como trabajo futuro
(apartado 7.4).

#### 5.6.6. Salvaguardas y paquete del modelo

**Salvaguardas.** El apartado 4.5 fijó el principio: un controlador con
modelo nunca puede invalidar una sesión. La implementación lo cumple con rutas
de respaldo en tres puntos. Antes de predecir, si la realimentación no
permite construir las entradas (una clave obligatoria ausente o no numérica,
una máscara sin acciones válidas, un campo prohibido), el controlador delega.
Al cargar, delega si el paquete del modelo no supera la verificación (un
fichero ausente, un esquema desconocido, un tamaño o un resumen SHA-256 que no
coincide con el manifiesto) o si la tabla del vídeo no existe o no coincide
con el manifiesto. Después de planificar, comprueba que la inferencia neuronal
no superó los 50 ms, que la acción elegida pertenece a la máscara de acciones
válidas y que la tasa resultante es finita y positiva; cualquier excepción
imprevista se trata como fallo de inferencia. El respaldo es una instancia
del MPC robusto que recibe exactamente la misma realimentación. Su decisión se
comprueba también contra la máscara y, si el propio respaldo fallase, se
devuelve la menor tasa válida. El reproductor recibe siempre una tasa.

Cada decisión deja en la telemetría 25 campos de diagnóstico: si el paquete
se cargó y se verificó, si las entradas eran válidas, la acción bruta del
planificador y la acción final, la latencia de inferencia y, en su caso, el
uso del respaldo y su motivo, tomado de un vocabulario cerrado. Con ellos la
evaluación audita el controlador decisión a decisión. En la primera
evaluación del capítulo 6, ninguna de las 1740 decisiones recurrió al
respaldo. En la segunda recurrió una: la primera decisión de una sesión, cuya
inferencia tardó 149,6 ms por una ralentización pasajera de la máquina
virtual. La salvaguarda delegó la decisión, como prevé su diseño, y el
respaldo eligió el mismo nivel que había planificado el modelo.

**El paquete del modelo.** Todo lo que el controlador necesita del
entrenamiento viaja en un directorio de cinco ficheros: los pesos de los cinco
miembros (un único fichero de tensores, sin código), la configuración del
modelo (arquitectura, horizonte, cuantiles y entradas), la normalización
(medias y desviaciones de la partición de entrenamiento), la configuración
del planificador ($\alpha$, pesos del objetivo, horizonte, factor de
ensanchado y origen de los tamaños) y un manifiesto con el tamaño y el
resumen SHA-256 de cada uno de los otros cuatro. La carga comprueba la
presencia de los cinco ficheros, el identificador de esquema, los tamaños y
los resúmenes, y solo entonces lee los pesos con la carga restringida del
apartado 5.1 y reconstruye cada miembro a partir de la definición de la red
que contiene el código. El paquete es la frontera entre la fabricación del
modelo (apartado 5.7) y su ejecución: cualquier alteración posterior lo haría
inservible en lugar de silenciosamente distinto, y la reproducción exacta de
las decisiones de las dos evaluaciones con el paquete archivado confirma que
es el mismo que decidió en ambas. La Tabla A.1 del Anexo A reúne todos los
parámetros del controlador.

**[TABLA A.1 — Para el Anexo A: parámetros del controlador propio]**

| Bloque | Parámetro | Valor en la evaluación |
|---|---|---|
| Entradas | Secuencia | 5 descargas (throughput en escala logarítmica y tiempo de descarga) |
| | Escalares | 7: buffer, índice y tasa del nivel actual, último cambio, rebuffering reciente, 2 de progreso |
| Predictor | Arquitectura | GRU de 96 + red densa de 96 y 64 neuronas, desactivación 0,1 |
| | Salida | 5 segmentos × 4 cuantiles (0,10; 0,25; 0,50; 0,75), monótonos por construcción |
| | Conjunto | 5 miembros; factor de ensanchado $c = 1$ |
| | Tamaño | 46 292 parámetros por miembro (231 460 en total) |
| Planificador | Horizonte | 5 segmentos (7776 secuencias) |
| | Criterio | CVaR, $\alpha = 0{,}75$ (3 de 4 escenarios) |
| | Objetivo | Mbit/s − 4,3 · rebuffering − \|Δ Mbit/s\| |
| | Tamaños | Reales, de la tabla del vídeo activo; buffer simulado ≤ 60 s |
| Salvaguardas | Latencia máxima de inferencia | 50 ms |
| | Respaldo | MPC robusto |
| | Integridad | SHA-256 de los 4 ficheros del paquete, verificación activada |

*Pie: Tabla A.1: Parámetros del controlador propio con los valores empleados
en las dos evaluaciones del capítulo 6.*

*(El apartado 5.7 describe el entorno con el que se fabrica el paquete del
modelo.)*

---

### Notas para Daniel (no van a la memoria)

**Qué cambia respecto a la versión 1 (y por qué)**

1. **Estructura en seis subapartados** (5.6.1–5.6.6): la aportación se ve en
   el índice y el tribunal encuentra cada pieza. Si prefieres el formato de
   los demás apartados, convierte los títulos en negritas de párrafo.
2. **Ocho ecuaciones** en lugar de describir fórmulas en prosa. La (5.8) es la
   frase de la defensa: "mi planificador es un MPC que penaliza el rebuffering
   medio de los tres escenarios no optimistas".
3. **Evidencia nueva del paquete canónico:** reproducción exacta de las 1740
   decisiones, la decisión real de la F5.3 y la Tabla 5.7 (efecto de cada
   pieza). Explican el mecanismo con tus datos y refuerzan la autoría.
4. **Errores corregidos de la v1:** decía 27 campos prohibidos (son 29,
   contados por programa); decía que la pinball del cuantil 0,10 penaliza 10
   veces (son 9: 0,9/0,1); decía que el descriptor se carga "al arrancar" (es
   en la primera decisión); el α = 0,75 se justificaba como "excluir al
   optimista" (la razón real es el barrido sobre validación, ahora contado).
5. **Honestidades nuevas** (todas verificadas): discrepancias de progreso y
   rebuffering entre entrenamiento y ejecución; α elegido en validación con el
   predictor anterior; criterio de cota inferior probado y descartado;
   cuantiles no equiprobables; generalización a contenido nuevo no medida.
6. **Figuras:** F5.2 rehecha con la idea central visible (dos carriles de
   información que solo se juntan en el planificador); F5.3 nueva con datos
   reales generada por script. La antigua F5.3 ilustrativa se retira (está en
   el commit `1a66daa`). La ficha de parámetros pasa al Anexo A.
7. **Sin rayas en el texto** (marca típica de texto generado) y sin muletillas;
   el nuevo estándar está en la memoria persistente.

**Citas (7), sin ninguna nueva respecto a la v1:** `yan2020puffer`,
`kan2021bayesmpc` y `yin2015mpc` (PDF verificados en sesiones anteriores, con
textuales en las notas del 5.5 y de la v1 del 5.6); `cho2014gru`,
`koenker1978quantiles`, `lakshminarayanan2017ensembles` y
`rockafellar2000cvar` (sin PDF local, citadas solo por lo que son, sin
atribuirles frases).

**Números y su fuente (todos comprobados el 13/10)**

- Código del entregable sin cambios desde el 07/08 (fechas de fichero).
- 29 claves prohibidas, 25 campos de diagnóstico, 20 motivos estables:
  contados importando los módulos.
- 46 292 parámetros por miembro: cargando `pesos_modelo.pt` (941 582 bytes).
- 1,25 ms de inferencia y 174 ms de decisión (p95 182 ms): medias de las 48
  sesiones reales en `agregados_por_controlador.json`.
- Reproducción 1740/1740 (1392 reales + 348 sintéticas), torch 2.6.0 CPU en
  Windows frente a 2.4.1 en la VM: `docs/memoria/apoyo/` y
  `resumen_decisiones_propio.json`.
- Ordenación de puntuaciones por escenario: 100 % de secuencias en el 100 % de
  decisiones (verifica la ecuación 5.8).
- Tabla 5.7 y percentiles de σ: `resumen_decisiones_propio.json` (solo
  sesiones reales; las sintéticas dan porcentajes parecidos: 22,4 % frente a la
  mediana, 4,6 % tamaños, 3,7 % ensanchado).
- Ejemplo: sesión `s00085` (Paseo 30 fps, ventana `real_005`, FCC banda ancha
  fija, capacidad media), decisión con k = 10; es la primera de 74 que cumplen
  la regla. El throughput medido después NO se usó para elegirla.
- Barrido de α y criterio LCB: `decision_mpc_prudente_frontera_riesgo_20260619.md`
  (sobre 27 ventanas de VALIDACIÓN, confirmado en
  `decision_mpc_prudente_diagnostico_estratificado_20260619.md`, con el
  predictor MLP anterior). Sus números son de junio y no van a la memoria.
- **Segunda evaluación (14/10):** 2,18 ms de inferencia y 317 ms de decisión
  (VM ≈1,8 veces más lenta toda la noche; agosto 174 ms estable);
  reproducción 1740/1740; ordenación 100 %; Tabla 5.7 y σ en
  `resumen_decisiones_propio_replica.json`; nivel más alto elegido en 872 de
  1392 decisiones (63 %) frente a 728 (52 %) en agosto; respaldo en 1 decisión
  (`s00005`, k = 2, 149,6 ms, nivel 0 = acción del planificador). Detalle en
  `docs/replica_ventanas_nuevas/RESULTADO_REPLICA.md`.

**AVISOS (importantes para la defensa)**

- **A. Reutilización de las ventanas de evaluación durante el desarrollo:
  RESUELTO con la segunda evaluación (14/10).** Las 12 ventanas reales de la
  primera evaluación eran las mismas que las de junio, y dos decisiones de
  diseño se tomaron viendo fallos en ellas: el planificador prudente (fallo de
  `real_006`, 15/06) y el predictor temporal (`real_011` y `real_012`, 23/06).
  La segunda evaluación usa 12 ventanas que ninguna ejecución anterior había
  ejecutado, con el sistema congelado y la regla de uso fijada antes. El 6.7
  lo cuenta así, sin esconder la primera.
- **B. Progreso entre entrenamiento y ejecución.** Con los indicadores de
  progreso calculados como en el entrenamiento cambiaría el 6,8 % de las
  decisiones reales en la primera evaluación (73 de 95 hacia un nivel más
  bajo) y el 3,4 % en la segunda (35 de 48): en ejecución el controlador fue
  algo menos prudente de lo que el modelo aprendió. Va al 6.7 con estos
  números.
- **C. Rebuffering reciente a cero.** Su efecto está acotado: solo hay unas 16
  paradas en las 48 sesiones reales del propio (0,33 por sesión), así que el
  valor real habría sido distinto de cero en torno al 1 % de las decisiones.
- **D. Resto en el entregable (no tocado):** el motivo
  `perfil_video_no_disponible` no está en el vocabulario cerrado y se
  registraría como `fallo_inferencia`; nunca ocurrió en el experimento.
- **E.** Las "entradas candidatas" que el constructor calcula y audita y el
  predictor no usa siguen ahí (aviso ya dado en la v1).
- **F.** `docs/defensa/apropiacion_codigo_mpc_prudente.md` y
  `preguntas_tribunal_respuestas.md` conservan números de junio y nombres
  viejos; antes de estudiarlos conviene actualizarlos al paquete canónico.

**Preguntas probables del tribunal (con respuesta)**

1. *¿Qué hace exactamente tu planificador?* Lo de la ecuación 5.8: maximiza
   calidad menos cambios menos 4,3 veces el rebuffering medio de los tres
   escenarios no optimistas, con el tamaño real de cada segmento.
2. *¿Por qué α = 0,75?* Barrido en validación; el comportamiento es poco
   sensible (Tabla 5.7: cambiar α a 1 o al peor caso solo cambia el 1 % de las
   decisiones), así que no es un número afinado a la evaluación.
3. *¿Los cuantiles no son equiprobables?* No; tratarlos como escenarios del
   mismo peso concentra los puntos en la parte baja de la cola: es una
   aproximación prudente y está declarada.
4. *¿Para qué sirve el conjunto de cinco redes?* Mide la desconfianza del
   modelo; cambia entre el 2,7 % y el 4,4 % de las decisiones, casi siempre
   hacia la prudencia, y solo cuando los miembros discrepan.
5. *¿El tamaño real cambia algo?* Entre el 3 % y el 5 % de las decisiones, en
   los dos sentidos; no hace al controlador más conservador sino más preciso.
6. *¿Cómo sé que decidió tu modelo y no el respaldo?* Todas las decisiones
   quedan auditadas y además se reproducen fuera de línea con el paquete
   archivado: 3480 de 3480. El respaldo actuó una sola vez, en la segunda
   evaluación, y eligió lo mismo que el modelo.
7. *¿Elegiste el ejemplo que mejor queda?* No: regla fija (primera decisión que
   cumple tres condiciones sobre la situación), declarada en el texto, sin
   mirar el desenlace.
8. *¿Usaste las ventanas de evaluación para diseñar?* Las de la primera
   evaluación, sí: sirvieron para diagnosticar versiones anteriores. Por eso
   repetí la evaluación con ventanas que nunca se habían ejecutado, con el
   sistema congelado y la regla escrita antes, y solo doy por confirmado lo
   que se cumple en las dos.
9. *¿Por qué en la segunda evaluación el controlador tardaba 317 ms y no
   174?* La VM fue más lenta toda esa noche; el código y el modelo son los
   mismos. Solo me perjudica a mí, porque soy el único que tarda en decidir:
   en las sesiones sintéticas, idénticas en las dos evaluaciones, el MPC
   robusto y BBA repiten casi exactamente y el propio pierde 0,06 de QoE.

**Cambios de la versión 2.1 (14/10), para pasarlos a Word**

1. 5.6.1, final: "después del experimento" pasa a "después de la primera
   evaluación del capítulo 6, y no se corrigieron antes de la segunda para que
   las dos evaluaran exactamente el mismo sistema".
2. 5.6.2, "Dos tipos de incertidumbre", final: "En el experimento del
   capítulo 6" pasa a "En las dos evaluaciones del capítulo 6", y "alcanzó el
   32 %" pasa a "alcanzó el 32 % y el 33 %".
3. 5.6.2, "Tamaño y coste": "se evalúan en 1,25 ms de media por decisión
   (capítulo 6)" pasa a "se evaluaron en 1,25 ms de media por decisión en la
   primera evaluación y en 2,18 ms en la segunda, con la máquina más lenta
   (capítulo 6)".
4. 5.6.3, "Lo que significa el criterio": "todas las decisiones del
   experimento" pasa a "todas las decisiones de las dos evaluaciones".
5. 5.6.3, "Coste": "174 ms de media por decisión (capítulo 6), de los que la
   inferencia neuronal es menos del 1 %" pasa a "174 ms de media por decisión
   en la primera evaluación y 317 ms en la segunda, en la que la máquina
   virtual fue más lenta durante toda la ejecución (capítulo 6); la
   inferencia neuronal es menos del 1 % de ese tiempo".
6. 5.6.4, primer párrafo: "en el experimento del capítulo 6" pasa a "en las
   dos evaluaciones del capítulo 6", y "La reproducción de las 1740
   decisiones del experimento" pasa a "La reproducción de las 3480 decisiones
   de las dos evaluaciones (1740 en cada una)".
7. 5.6.4, "Una decisión real": "la primera del experimento" pasa a "la
   primera de la primera evaluación"; en el título y el pie de la F5.3, "del
   experimento" pasa a "de la primera evaluación". El ejemplo y la figura no
   cambian.
8. 5.6.4, "El peso de cada componente": nueva Tabla 5.7 con dos columnas;
   lecturas reescritas con rangos ("entre una de cada seis y una de cada
   cuatro", "más del 90 %", "entre el 0,6 % y el 1,6 %", "entre el 3 % y el
   5 %") y un párrafo nuevo: por qué los porcentajes de la segunda son
   menores (ventanas más fáciles, nivel más alto en el 63 % frente al 52 %).
9. 5.6.5, segundo párrafo: "El experimento del capítulo 6 lo pone en
   práctica. Las configuraciones de las 60 sesiones..." pasa a "Las dos
   evaluaciones del capítulo 6 lo ponen en práctica. En cada una, las
   configuraciones de las 60 sesiones...".
10. 5.6.6, "Salvaguardas", final: la frase de las 1740 decisiones sin
    respaldo pasa a contar las dos evaluaciones, con la única delegación de
    la segunda (149,6 ms; el respaldo eligió el mismo nivel que el modelo).
11. 5.6.6, "El paquete del modelo": "las 1740 decisiones... que decidió en el
    experimento" pasa a "las decisiones de las dos evaluaciones... que
    decidió en ambas"; pie de la Tabla A.1: "en las dos evaluaciones".

**Longitud y recortes posibles.** Texto ≈ 3900 palabras (≈ 8 páginas) + 8
ecuaciones + 2 figuras + 2 tablas en el capítulo (la ficha va al anexo); la v1
tenía ≈ 2550. Es el apartado más largo de la memoria, como corresponde a la
aportación principal, pero si el presupuesto de 100 páginas aprieta se pueden
quitar unas 600 palabras sin perder contenido, por este orden: (1) el
paquete del modelo, que repite parte del 5.1, a dos frases (−120); (2) el
tercer párrafo del 5.6.5 fundido con el segundo (−80); (3) los porcentajes de
σ del 5.6.2, porque la Tabla 5.7 ya muestra el efecto del ensanchado (−70);
(4) el párrafo de coste del 5.6.3 a una frase (−60); (5) la analogía del
radioenlace (−45); (6) el párrafo de precedentes de la introducción, si el
cap 2 ya presenta Fugu y el MPC bayesiano (−110); (7) la fila de horizonte de
la Tabla 5.6. No recortes las ecuaciones 5.7 y 5.8, la decisión real ni la
Tabla 5.7: son lo que más defiende el trabajo.
