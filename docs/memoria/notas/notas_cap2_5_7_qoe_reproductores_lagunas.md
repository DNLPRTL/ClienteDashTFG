# Notas de 2.5, 2.6, 2.7 y cierre del capítulo 2 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap2_5_7_qoe_reproductores_lagunas.docx` (≈1790 palabras de cuerpo, 4
páginas: 2.5 QoE (3 párrafos), 2.6 reproductores (2), 2.7 lagunas (3) y cierre sin epígrafe (2); 22 citas, sin figuras
ni tablas). Generado por `docs/memoria/apoyo/generar_cap2_5_7.py` (lee los pesos 4,3 y 2,66 de `qoe.py` del
entregable). Comprobador sin avisos. **CAPÍTULO 2 COMPLETO** (2.1–2.7 + cierre; Tabla 2.1; sin figuras).

## Citas verificadas (página del PDF en `biblioteca_final/`)

| Clave | Afirmación | Dónde |
|---|---|---|
| `seufert2015hasQoeSurvey` | tres grupos de factores (retardo inicial, paradas, adaptación: nivel, frecuencia, amplitud) | §IV (p. 3–9); amplitud p. 11 |
| ídem | retardo inicial preferido a parada por ~90 %; retardos hasta 16 s tolerados | p. 3 |
| `barman2019qoeModeling` | survey de modelos QoE para HAS y problemas abiertos (dependencia del contenido, validación) | p. 1 (título y resumen) |
| `duanmu2017qoeIndex` | índice continuo; «same bitrate … drastically different presentation quality»; interacción calidad–paradas | p. 1 (resumen) |
| `zuo2022ruyiPreferenceQoe` | estudio con 90 sujetos; ABR diseñado para un «usuario medio» | p. 1 (resumen) |
| `taraghi2021understandingQoe` | heurísticos de reproductores reales (BOLA, BBA0, Quetra, Shaka, FastMPC) con estudio objetivo y subjetivo | p. 1 (public review y resumen) |
| `yin2015mpc` / `mao2017pensieve` | métrica suma por segmento; QoE_lin 4,3, QoE_log 2,66, QoE_hd | Yin p. 3; Pensieve p. 8 (ec. 6 y Tabla 1) |
| `peroni2024qoePitfalls` | proliferación de modelos sin consenso; el orden cambia con el modelo (Tabla II); guías | p. 1, 7–8 |
| `dashjsRefClient`, `shakaPlayer`, `gpacMp4boxWiki` | documentación oficial (HTML guardado en `08_herramientas_seguridad/`) | — |
| `spiteri2019dashjs` | BOLA-E y DYNAMIC en el reproductor de referencia dash.js; simulador Sabre | p. 1–2 |
| `yan2020puffer` | algoritmos buenos en simuladores/emuladores no lo son en la red real; dificultad de simular la dinámica | p. 1–3 |
| `hoffman2025intoTheWildABR` | «gap between simulation and reality»; pruebas reales en una región generalizan mal; sesgo de supervivencia | p. 1 (resumen) |
| `alomar2023causalsim` | sesgo de la simulación con trazas; marco causal | p. 1 (título «Unbiased Trace-Driven Simulation») y resumen |
| `bothra2023veritas` | preguntas «what-if» sin ensayos aleatorizados a partir de trazas de un solo ABR | p. 1 (resumen) |
| `amer2025learningReview` | review de métodos con aprendizaje; retos de despliegue y problemas abiertos | p. 1 |
| `timmerer2025hasReview`, `alsader2025qoeDriven6g`, `peroni2025pipelineSurvey` | revisiones recientes (contexto) | p. 1 cada una |
| `kan2021bayesmpc`, `xie2026safesabr` | decidir con la incertidumbre / riesgo | p. 1–3 (ya verificadas) |

## Decisiones de redacción

- 2.5 justifica la QoE lineal con tres razones (escala conocida, componentes interpretables, calculable desde la
  telemetría) y declara el coste (bitrate como sustituto). Pesos leídos del código.
- 2.6: tres reproductores y por qué no sirven de banco controlado (navegador, algoritmos entrelazados, telemetría);
  reconoce que GPAC es la herramienta que genera el propio contenido.
- 2.7: tres lagunas (simulador-realidad; generalización/fiabilidad; riesgo) y las tres respuestas del trabajo
  (fidelidad al medio; aprendizaje acotado a la predicción; decisión y evaluación con la incertidumbre), con la
  limitación de la emulación declarada (TCP, tráfico competidor, huella de la política en las trazas → 6.7).
- Cierre: dos párrafos que recapitulan 2.1–2.7 y enlazan con el capítulo 3 (planificación y costes), que es el que
  sigue en la estructura del plan maestro.
- Citas múltiples con una sola pareja de corchetes y comas (`[a, b, c]`): Daniel las convierte a «[n], [m]» al
  maquetar (biblia §5). El comprobador no detecta las claves dentro de corchetes múltiples: el script del
  apartado sí las valida contra el .bib (22).

## Preguntas probables del tribunal

1. **¿Por qué una QoE tan simple y no VMAF?** Escala de la literatura, interpretabilidad, sin decodificar; VMAF es la
   limitación declarada y trabajo futuro.
2. **¿Tu emulación no tiene el sesgo de CausalSim?** Sí, parcialmente: las trazas llevan la política con que se
   recogieron; se declara. La fidelidad al medio corrige otra cosa: los bytes reales y el servidor real.
3. **¿Por qué no dash.js con un plugin?** Navegador no controlable ni reproducible; sin telemetría de decisiones;
   controlador en Python. El cliente propio renuncia a generalidad por control.

## Qué se puede recortar

El segundo párrafo del 2.5 (modelos) a tres frases; las revisiones generales del 2.7 a una cita. Mantener la
justificación de la QoE lineal, el 2.6 y las tres lagunas con sus tres respuestas.
