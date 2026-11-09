# Notas del 6.2 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap6_2_metricas_hipotesis.docx` (≈1810 palabras de cuerpo, 5 páginas,
3 subapartados, Tablas 6.4 y 6.5, ecuaciones 6.1 a 6.3, 6 citas, sin figura). Generado por
`docs/memoria/apoyo/generar_cap6_2.py`. Comprobador sin avisos; render con Word revisado.

## Cambio de numeración respecto al esquema del plan

El esquema preveía una sola tabla en el 6.2 (hipótesis = T6.4). Se añade la tabla de métricas (biblia §4: «tabla de
definición de métricas»), así que **T6.4 = métricas y T6.5 = hipótesis**, y las tablas siguientes del capítulo corren
un número: integridad T6.6, P1–P5 T6.7, agregados T6.8, descomposición T6.9, estratos T6.10. Actualizado en el mapa
de tablas del plan maestro.

## Qué hace el script (todo por programa; falla si algo no cuadra)

- Importa `core/evaluacion/qoe.py` y `contrastes.py` del entregable y comprueba las constantes: μ = 4,3, peso log
  2,66, suavidad 1,0, margen 0,15, 10 000 remuestreos, semilla 2026, referencia `controlador_propio`, cinco
  hipótesis con tipos equivalencia/menor/menor/mayor/menor; y que el protocolo del paquete lleva la misma versión
  `hipotesis_blindaje_v1`, α 0,05 y las mismas secundarias.
- Comprueba las funciones del entregable sobre valores conocidos: `_cola_binomial(13, 1) = 14/2^13`,
  `_normal(1,6449) = 0,95`, y Holm sobre {0,01; 0,03; 0,04} → ajustados 0,03 / 0,06 / 0,06 (solo la primera se
  rechaza).
- Del paquete: 1208 sesiones, 1184 reales, 148 escenarios reales, 74 ventanas, 29 segmentos evaluables en TODAS las
  sesiones; una parada = fila evaluable con rebuffering > 0 (447 filas = Σ num_stalls = 447).
- Ejemplo (misma regla que el 6.1: primera sesión del plan del propio = sesión 8): recalcula la QoE lineal con
  `calcular_qoe_lineal` desde los 29 segmentos de `segmentos.csv` y, además, con la ecuación (6.1) escrita a mano;
  las dos coinciden con `sesiones.csv` (3,974137…). También la QoE log (2,4648) y la suavidad (4,0).

## Fuente de cada número

| Dato | Fuente |
|---|---|
| 29 evaluables, 148 escenarios, 74 ventanas | `sesiones.csv` |
| μ = 4,3; 2,66; ln(R/Rmín) | `qoe.py` del entregable; Pensieve p. 8, Tabla 1 (QoE_lin, μ = 4,3; QoE_log, log(R/Rmin), 2,66) |
| 0,074 puntos por media parada de 0,5 s | 4,3 · 0,5 / 29 |
| margen 0,15 ≈ 4,3/29 = 0,148 | `contrastes.py` (comentario en el código) |
| 10 000 remuestreos, semilla 2026, percentiles 2,5/97,5 y 5/95 | `contrastes.bootstrap_por_ventanas` y `contraste` |
| TOST: p = máx de los dos unilaterales con aproximación normal sobre las medias por ventana; `equivalente_ic90` | `contrastes.contraste`, rama «equivalencia» |
| Holm: ajustado = máx acumulado de mín(1, (m−i)·p) | `contrastes.holm` |
| ejemplo: 300 → 2850 → 4300; 4,112 Mbit/s; suavidad 2,55 + 1,45 = 4,0; QoE 3,974; log 2,465; ln(4300/300) = 2,663 | `segmentos.csv` + `sesiones.csv` + recálculo |
| estratos y la interacción | `contrastes.contrastes_prerregistrados` y `_interaccion_contenido` |

## Citas (verificadas en el PDF)

- `mao2017pensieve` p. 8: ecuación (6) «QoE = Σ q(Rn) − μ Σ Tn − Σ |q(Rn+1) − q(Rn)|» y Tabla 1 (QoE_lin: q(R) = R,
  μ = 4,3; QoE_log: log(R/Rmin), 2,66). Nuestra (6.1) es la media por segmento de esa suma, con el término de
  suavidad desplazado al segmento n (vale 0 en el primero).
- `yin2015mpc` p. 3: los cuatro objetivos (rebuffering, bitrate, startup delay, suavidad); Pensieve atribuye la
  QoE lineal a «MPC [51]».
- `schuirmann1987tost` p. 657 (resumen: TOST frente al power approach) y p. 661: «operationally identical to the
  procedure of declaring equivalence only if the ordinary 1−2α (not 1−α) confidence interval … is completely contained
  in the equivalence interval».
- `holm1979bonferroni`: SIN PDF; se cita como el método de la corrección (secuencial, controla el FWER, más potente
  que Bonferroni). No se le atribuyen frases.
- `efron1993bootstrap`: libro, sin PDF; se cita como referencia general del bootstrap percentil.
- `peroni2024qoePitfalls` p. 8, Tabla II: el algoritmo con mayor QoE media cambia con el modelo de QoE («TR provides
  the highest average QoE according to five of the 10 QoE models … BBA … four»). Sostiene la frase «el orden entre
  algoritmos puede cambiar con el modelo de calidad de experiencia».

## Avisos y matices (no van a la memoria)

- **Retardo de arranque.** El protocolo (06 §4) lo lista como «solo informativa», pero `analisis.py` NO lo calcula
  ni hay columna en `sesiones.csv`. El texto dice, con verdad, que no interviene porque es idéntico por construcción
  (preroll 0, nivel inicial 0, cola mínima 0,1 s). Si el tribunal pregunta: no se midió; es constante por diseño.
- **QoE log con R_mín de la propia sesión.** `resumir_sesion` pasa `min_bitrate_kbps = min(bitrates de la sesión)`,
  no el mínimo de la escalera (300). Una sesión que nunca bajó de 750 tiene su log relativo a 750. Por eso el texto
  la describe así y la deja como «contraste de la lineal». En el 6.5 no se saca ninguna conclusión de la QoE log.
- **Suavidad del primer segmento evaluable.** El salto entre el calentamiento (300) y el primer segmento evaluable
  NO se penaliza (la lista de deltas empieza en 0). Dicho en el texto («vale cero en el primer segmento evaluable»).
- **Paradas.** `num_stalls` cuenta segmentos con rebuffering > 0; una espera larga en un solo segmento es una parada.
  Coherente con la asignación de paradas del reproductor (C2).
- **Prueba del signo unilateral para «menor».** El p es P(X ≤ n_positivas) con X ~ Bin(n+ + n−, 1/2): «pocas ventanas
  con más paradas en el propio». Correcto.
- **TOST normal.** Con 74 bloques la aproximación es razonable; el `equivalente_ic90` bootstrap es la comprobación
  sin supuesto. Se dice.

## Preguntas probables del tribunal

1. **¿Por qué equivalencia y no superioridad en QoE?** Porque el diseño no pretende más QoE: pretende la misma con
   menos paradas. Pedir superioridad habría sido una hipótesis que el controlador no está diseñado para cumplir.
2. **¿Por qué 0,15?** Un segundo de rebuffering en 29 segmentos (4,3/29). Es un margen pequeño: la escalera entera
   son 4 Mbit/s de QoE. Fijado antes.
3. **¿Por qué la ventana es el bloque?** Dos escenarios de una ventana comparten la red; tratarlos como independientes
   duplica artificialmente la muestra.
4. **¿Por qué el signo y no la t?** Sin supuesto de distribución y robusto a colas (BOLA llega a −17 de QoE en una
   sesión). Menos potente: va contra nosotros.
5. **¿Holm o Bonferroni?** Holm controla el mismo error familiar y es uniformemente más potente.
6. **¿La QoE lineal es «la» calidad?** No: es un proxy con bitrate; por eso se informan componentes, distribuciones
   y la QoE log, y la limitación VMAF va en 6.7.

## Qué se puede recortar

El párrafo final (descriptivos y límites) a la mitad; la frase sobre Wilcoxon. Mantener (6.1), (6.2), la Tabla 6.5 y
el ejemplo de cálculo.
