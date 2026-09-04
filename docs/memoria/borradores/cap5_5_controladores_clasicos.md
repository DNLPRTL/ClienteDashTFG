# Borrador 5.5 — Implementación de los controladores clásicos

> BORRADOR para masticar y reescribir (04/09/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: entregable — `core/controladores/base.py`, `contrato.py`,
> `basado_en_tasa.py`, `bba.py`, `bola.py`, `mpc.py`, `robust_mpc.py` (leídos
> enteros el 04/09) + material previo del repo (`01_baselines/<x>/notes_for_memory,
> paper_card, implementation_spec`) + los cinco PDF originales (norma
> PDF-primero; pasajes en las notas) + paquete canónico (parámetros de sesión).

---

### 5.5. Implementación de los controladores clásicos

Los controladores clásicos son los comparadores del capítulo 6. Se
implementan cinco algoritmos de la literatura sobre la interfaz común del
apartado 4.5: el basado en tasa, BBA, BOLA, MPC y su variante robusta. La
comparativa final emplea cuatro de ellos; el MPC básico queda implementado
como paso intermedio hacia la variante robusta, que es la referencia fuerte
de la literatura. Dos principios guían la implementación. El primero es la
fidelidad al artículo original: cada controlador reproduce la regla de
decisión publicada, con sus parámetros, y las simplificaciones adoptadas se
declaran. El segundo es la neutralidad respecto al cliente: cada controlador
lee del contrato de realimentación únicamente las señales que su algoritmo
contempla, de modo que las diferencias de comportamiento provienen del
algoritmo y no de un acceso privilegiado a la información.

Esa segunda regla permite ordenar los cinco por la información que utilizan.
El basado en tasa decide con la medida de la última descarga; BBA solo con la
ocupación del buffer; BOLA con la ocupación y la escalera de calidades; MPC
añade a la ocupación un historial de descargas recientes; y el MPC robusto,
además, la memoria de sus propios errores de predicción. Todos ellos son
reactivos en el sentido del apartado 4.7: observan la variabilidad del
contenido solo a posteriori, a través de la duración de la descarga anterior,
y cuando necesitan un tamaño de segmento emplean el valor nominal de la
escalera, como en sus formulaciones publicadas. La Tabla 5.5 resume la regla,
los parámetros y la información de cada uno.

**Estructura común.** Los cinco controladores comparten una plantilla de
implementación. En cada decisión validan la escalera recibida (valores
numéricos positivos, recortada al nivel máximo permitido), acotan todo índice
de nivel al rango válido y devuelven la tasa objetivo en bytes por segundo,
que el reproductor cuantiza al escalón común (apartado 4.5). Los casos
degenerados tienen una respuesta segura y explícita: sin escalera, tasa cero;
con una única representación, esa; con una señal ausente o inválida, el nivel
de arranque o el mínimo. Los parámetros de configuración inválidos se
sustituyen por los valores por defecto documentados en el propio módulo. Cada
decisión deja un registro diagnóstico local (motivo, señales y valores
intermedios) que sirve para depurar y para las pruebas, pero que no forma
parte de la telemetría. Ningún controlador clásico usa aleatoriedad: ante la
misma realimentación y el mismo estado interno, la decisión es siempre la
misma. En la evaluación del capítulo 6 los cuatro comparados se ejecutaron
con sus parámetros por defecto, sin ajuste alguno.

**Controlador basado en tasa.** Reproduce la adaptación dirigida por el
receptor de Liu et al. \cite{liu2011rateAdaptation}: medir el throughput de
la descarga de cada segmento en la capa de aplicación, suavizarlo y elegir la
representación más alta que quepa bajo una estimación conservadora, sin
recurrir a información de la capa de transporte como el tiempo de ida y
vuelta o las pérdidas. El artículo compara el tiempo de descarga del segmento
con su duración de reproducción; la implementación usa la misma información
en forma de cociente tamaño entre tiempo, que es la estimación cruda que
ofrece el contrato. Sobre ella aplica un suavizado exponencial con α = 0,5 y
un factor de seguridad de 0,85, y elige el escalón más alto cuya tasa no
supera la estimación segura. Las dos asimetrías del artículo —subida
escalonada y bajada agresiva— se implementan así: una subida se limita a un
nivel por decisión; y si la medida instantánea, con su factor de seguridad,
ya no sostiene el nivel actual, la decisión toma la menor entre la medida
suavizada y la instantánea, lo que permite bajar varios niveles de golpe. El
buffer interviene solo como guarda: por debajo de 2 segundos de ocupación se
fuerza al menos un nivel menos que el actual.

**BBA.** Implementa el mapa de tasa de Huang et al. \cite{huang2014bba} en su
forma más simple, la que los autores denominan BBA-0: la ocupación del buffer
se traduce directamente en una representación mediante una función por
tramos. Por debajo de la reserva (5 s) se pide la representación mínima; por
encima de la reserva más el colchón (15 s), la máxima; y en el colchón
intermedio, el nivel crece linealmente con la ocupación, redondeando hacia
abajo al índice de la escalera. Los valores de reserva y colchón son los que
emplea la propia literatura al reproducir BBA como comparador
\cite{yin2015mpc}. El controlador ignora deliberadamente toda medida de
throughput: dos realimentaciones con la misma ocupación y distintas
descargas producen la misma decisión. El artículo señala que una estimación
de capacidad es útil durante el arranque, cuando el buffer está vacío; la
implementación omite ese estimador para aislar el mecanismo de mapa de tasa,
y el transitorio de arranque queda además fuera de la evaluación (apartado
4.6).

**BOLA.** Implementa la versión básica del algoritmo de Spiteri et al.
\cite{spiteri2020bola}, la que los autores derivan directamente de su
problema de optimización: en cada decisión se elige la representación m que
maximiza (V·(υ_m + γp) − Q)/S_m, donde Q es la ocupación del buffer en
segmentos, p la duración del segmento, υ_m la utilidad de la representación
y S_m su tamaño; V y γ son los parámetros de control. La utilidad es la
logarítmica que propone el artículo, υ_m = ln(S_m/S_1), lo que con tamaños
nominales equivale al logaritmo de la tasa relativa a la mínima. Los tamaños
se toman como tasa nominal por duración y se normalizan al menor, lo que no
altera la representación ganadora. Dos decisiones de implementación
requieren mención. Primera: el artículo contempla no descargar cuando ninguna
puntuación es positiva; el contrato del apartado 4.5 no expresa esa opción,
así que en ese caso se elige la representación mínima; en la práctica el tope
del buffer del apartado 4.3 ya detiene las descargas antes. Segunda: los
parámetros se fijan por configuración (V = 5, γ = 0,2) y no se derivan de
objetivos de ocupación como propone el artículo, por lo que BOLA se evalúa
con una parametrización razonable pero no calibrada. Además, con ocupación
menor o igual a un segmento se pide la mínima. La implementación es BOLA en
su forma básica: no incorpora las mejoras que la misma familia de autores
añadió al reproductor de referencia dash.js (segmentos virtuales de
BOLA-E, conmutación dinámica con una regla de throughput a buffer bajo y
sustitución de segmentos) \cite{spiteri2019dashjs}, que responden a
necesidades de producción y desdibujarían la comparación académica.

**MPC.** Implementa el control predictivo de Yin et al. \cite{yin2015mpc}
por enumeración. La predicción de throughput es la media armónica de las
últimas cinco descargas, como en el artículo; el historial se alimenta con la
medida tamaño entre tiempo de cada segmento, una sola vez por segmento. En
cada decisión se enumeran todas las secuencias de niveles sobre un horizonte
de tres segmentos (216 secuencias con seis representaciones; un tope de 4096
reduce el horizonte si la escalera fuera mayor), se simula la evolución del
buffer para cada una (tiempo de descarga igual al tamaño nominal entre la
predicción; rebuffering si ese tiempo excede la ocupación; la ocupación se
reduce en el tiempo de descarga y crece en la duración del segmento) y se
puntúa con el objetivo del artículo: suma de calidades, menos una
penalización por rebuffering, menos otra por variación de calidad entre
segmentos consecutivos. Se aplica la primera acción de la mejor secuencia y
el proceso se repite en el segmento siguiente (horizonte deslizante). Tres
elecciones son propias y se declaran. El horizonte es de tres segmentos, no
de cinco como en el artículo, por tratabilidad de la enumeración en línea; el
artículo resuelve ese coste con tablas precalculadas que aquí no se
implementan. La función de calidad es la misma utilidad logarítmica de BOLA,
una elección admisible dentro de la formulación general del artículo. Y los
pesos de las penalizaciones (4,3 por segundo de rebuffering y 1 por unidad de
variación) coinciden con los de la métrica de evaluación del capítulo 6, pero
aplicados a calidad logarítmica: el objetivo interno de los MPC no es la
métrica lineal con la que se evalúan, un desajuste que se mantiene
deliberadamente y cuya lectura se hace en el capítulo 6.

**MPC robusto.** Es el mismo planificador con una predicción conservadora,
siguiendo la formulación robusta del mismo artículo \cite{yin2015mpc}: la
predicción base (media armónica) se divide por uno más el error máximo
observado en las cinco predicciones anteriores, siendo cada error el valor
absoluto de la diferencia entre lo previsto y lo observado, relativo a lo
observado. El artículo demuestra que este control robusto equivale al MPC
ordinario alimentado con la cota inferior del throughput, y así se
implementa. La contabilidad del error es local al controlador: cada decisión
guarda la predicción que usó y, al llegar la siguiente medida real, calcula
el error y lo añade a una ventana de cinco. Mientras no existe historial de
errores (las primeras decisiones), la predicción base se multiplica por un
factor de arranque de 0,85; la predicción robusta nunca supera a la base.
Este controlador es la referencia de la comparativa del capítulo 6 por ser
el comparador clásico más exigente.

**[TABLA 5.5 — Controladores clásicos implementados]**

| Controlador | Fuente | Regla de decisión | Parámetros en la evaluación | Información que usa |
|---|---|---|---|---|
| Basado en tasa | \cite{liu2011rateAdaptation} | Escalón más alto bajo 0,85 × throughput suavizado; sube un nivel por decisión; baja sin límite | α = 0,5; factor 0,85; buffer crítico 2 s | Última descarga (tamaño/tiempo); buffer solo como guarda |
| BBA (BBA-0) | \cite{huang2014bba} | Mapa por tramos de la ocupación: mínima bajo la reserva, lineal en el colchón, máxima por encima | reserva 5 s; colchón 10 s | Solo la ocupación del buffer |
| BOLA (básico) | \cite{spiteri2020bola} | Máximo de (V(υ_m + γp) − Q)/S_m, con υ_m = ln(S_m/S_1); mínima si ninguna puntuación es positiva | V = 5; γ = 0,2; mínima si buffer ≤ p | Ocupación, duración de segmento y escalera (tamaños nominales) |
| MPC (no comparado) | \cite{yin2015mpc} | Primera acción de la mejor secuencia de 3 segmentos: Σ calidad − 4,3 · rebuffering − 1 · variación; predicción = media armónica de 5 descargas | horizonte 3; ventana 5; pesos 4,3 y 1 | Ocupación, historial de 5 descargas, escalera (tamaños nominales) |
| MPC robusto | \cite{yin2015mpc} | Igual que MPC con predicción base/(1 + err), err = máximo error relativo de las 5 últimas predicciones | + ventana de error 5; factor de arranque 0,85 | Lo de MPC más el historial de sus propios errores |

*Pie: Tabla 5.5: Controladores clásicos implementados: regla de decisión,
parámetros empleados en la evaluación (valores por defecto del código) e
información del contrato que utiliza cada uno.*

*(El apartado 5.6 describe el controlador propio.)*

---

### Notas para Daniel (no van a la memoria)

- **Citas (5), TODAS verificadas contra PDF con pdfminer (04/09):**
  · `liu2011rateAdaptation`: "a smoothed HTTP throughput measured based on
    the segment fetch time (SFT)"; "receiver-driven rate adaptation ...
    step-wise increase/aggressive decrease"; "does not require any transport
    layer information such as round trip time (RTT) and packet loss rates".
  · `huang2014bba`: "create an extra reservoir, noted as r. When the buffer
    is filling up the reservoir ... we request video rate Rmin"; "the buffer
    between the reservoir and the point where f(B) first reaches Rmax the
    cushion"; "We call this algorithm BBA-0 since it is the simplest";
    "capacity estimation is unnecessary in steady state; however ... is
    important during the startup phase". OJO defensa: su teoría asume
    "Videos are encoded at a constant bit-rate (CBR)" (supuesto 3) —
    munición para la familia "reactiva/ciega al contenido".
  · `spiteri2020bola`: solución de (11): "If Q(tk) > V(υm + γp) for all m
    ... the no-download option is chosen ... Else ... m* is the index that
    maximizes the ratio (V υm + V γp − Q(tk))/Sm among all m for which this
    ratio is positive"; "We first implemented a basic version of BOLA, named
    BOLA-BASIC, directly from (11)"; "A natural choice ... logarithmic
    utility function: let υm = ln(Sm/S1)"; "a video provider can use any
    utility function satisfying (1)"; "BOLA does not require prediction of
    available network bandwidth". Su ejemplo usa γ = 5.0/p, V = 0.93 y
    calibra V desde el buffer (§VI-B) — de ahí la frase honesta "no
    calibrada".
  · `yin2015mpc`: "RB: ... throughput prediction using harmonic mean of past
    5 chunks"; "BB: ... f(Bk) with reservoir r = 5s and cushion c = 10s" (=
    NUESTROS defaults de BBA); "FastMPC: look-ahead horizon h = 5";
    "RobustMPC: ... throughput lower bound is Ĉt/(1 + err) ... err is the
    maximum absolute percentage error of the past 5 chunks"; "THEOREM 1. The
    robust MPC controller is equivalent to the regular MPC taking the lower
    bound of throughput as input"; q(·) "non-decreasing function"; en su
    evaluación "q(·) is an identity function ... λ = 1, µ = µs = 3000"
    (kbps). → Por eso el texto atribuye a Yin la ESTRUCTURA del objetivo y
    declara como propias la q logarítmica y los pesos 4,3/1.
  · `spiteri2019dashjs`: BOLA-E = "placeholder algorithm" de segmentos
    virtuales + "insufficient buffer rule"; DYNAMIC = "throughput-based ABR
    when the buffer level is low and then dynamically switch to BOLA";
    FAST SWITCHING = "replaces low-bitrate segments in the client's buffer";
    "all three algorithms ... are now part of the official DASH reference
    player dash.js". Solo contexto (regla del repo).
  · `mao2017pensieve` NO se cita aquí (regla: solo contexto histórico en el
    cap 2; RobustMPC no es Pensieve).
- **Verificado contra el paquete canónico:** las configs de sesión de bba,
  bola y mpc_robusto llevan `"parametros": {}` → parámetros por defecto
  del código (los de T5.5). Con 6 niveles y horizonte 3, cada decisión MPC
  enumera 6³ = 216 secuencias (tope 4096 no interviene).
- **Verificado en código:** basado_en_tasa (`bwe` primero, si no
  tamaño/tiempo; EWMA α 0,5; bajada agresiva = min(suavizada, instantánea)
  cuando medida×0,85 < tasa actual; guarda buffer ≤ 2 s → nivel actual−1;
  subida +1); bba (floor(x·(n−1)); buffer inválido → 0); bola (utilidad
  ln(R/Rmin); tamaños R·p normalizados al mínimo; Q = buffer/p; score;
  ≤0 → mínimo; respaldo si buffer ≤ p); mpc (media armónica; dedup de
  muestra por (índice, valor, tamaño, tiempo); itertools.product; primera
  acción; buffer inválido → 0); robusto (error = |prev−real|/max(real, ε);
  ventana 5; base×0,85 sin historial; robusta acotada en [ε, base]; la
  predicción pendiente solo se guarda si la decisión fue por secuencia).
  Todos: `fijarDuracionInactividad(0.0)`, `ultimas_metricas` local,
  determinismo (sin `random`).
- **Desviaciones declaradas en el texto (para la defensa, no ocultarlas):**
  rate: cociente tamaño/tiempo en vez de SFT/MSD literal (misma
  información); BBA: sin estimador de arranque; BOLA: sin no-descarga, V/γ
  fijos, sin BOLA-E/DYNAMIC/FAST SWITCHING; MPC: horizonte 3 vs 5, sin tabla
  FastMPC, q logarítmica, pesos de la métrica de eval; todos: tamaños
  nominales (4.7).
- **Chuletas de defensa:**
  · "¿Por qué el objetivo interno de los MPC no es tu métrica?" → "Es la
    estructura de Yin con la utilidad log de BOLA; los pesos son los de la
    métrica pero sobre calidad log. Lo mantuve así porque cambiarlo tras
    ver resultados sería ajustar el comparador a mi favor; el desajuste
    juega EN CONTRA del propio y está declarado (6.7)".
  · "¿Por qué horizonte 3?" → "Enumeración en línea: 216 secuencias por
    decisión en Python; el artículo usa 5 con tablas precalculadas
    (FastMPC) que no implemento. Es tratabilidad, y está declarado".
  · "¿BBA sin arranque?" → "Aíslo el mapa de tasa; el arranque no puntúa
    (4.6); Yin usa el mismo BB sin estimador como comparador".
  · "¿Cómo sé que son fieles?" → "Cada uno tiene ficha del artículo,
    especificación y mapeo fórmula→código escritos ANTES de programar; y
    los parámetros de BBA son literalmente los de Yin".
- **Apunte para 6.7 (no aquí):** con V = 5 y γp = 0,8, el buffer objetivo
  implícito de BOLA, V(υ_M + γp) ≈ 5·(2,66 + 0,8) ≈ 17 segmentos ≈ 69 s,
  supera el tope de 60 s del cliente: BOLA tiende a llenar y a elegir alto.
  Es una explicación plausible de su QoE baja en el paquete (1,24) — para
  la interpretación del cap 6, como hipótesis, no como hecho probado.
- **Sin figura:** el plan no la prevé; las notas antiguas sugerían
  mini-diagramas por algoritmo, que serían decorativos. T5.5 concentra el
  mapeo. Las familias se ilustrarán en la T1 del cap 2.4 (columna
  "información que usa", pedida el 27/08).
- **Fronteras:** familias y contexto histórico (→2.4); salvaguardas y
  contrato (→4.5); controlador propio (→5.6); resultados e interpretación
  del desajuste log/lineal (→6.6/6.7).
- Longitud: ~1450 palabras (cinco algoritmos). Si recortas, el candidato
  es el párrafo de estructura común (fúndelo con la intro); no recortes las
  desviaciones declaradas.
