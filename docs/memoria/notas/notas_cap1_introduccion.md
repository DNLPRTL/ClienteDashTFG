# Notas del capítulo 1 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap1_introduccion.docx` (≈3400 palabras de cuerpo, 8 páginas: apertura,
1.1 Motivación y contexto (4 párrafos), 1.2 Problema (4), 1.3 Enfoque del trabajo (6 + Figura 1.1), 1.4 Objetivos
(objetivo general + Objetivos 1–5 en lista + correspondencia con capítulos), 1.5 Alcance (3), 1.6 Estructura de la
memoria (lista, una frase por capítulo y anexos + convenciones); 17 citas, sin tablas). Generado por
`docs/memoria/apoyo/generar_cap1.py`. Comprobador sin avisos. Sin cierre propio: el capítulo acaba en la estructura,
como en los TFG del tutor.

## Qué comprueba el script (regla cero)

- Escalera (6 calidades, 300–4300 kbit/s) y segmento de 4 s leídos del MPD entregado.
- Del protocolo del experimento final: 4 clásicos (`basado_en_tasa, bba, bola, mpc_robusto`), `controlador_propio`
  y 3 variantes (`propio_mediana`, `propio_cuantiles_recientes`, `propio_cuantiles_fijos`), 5 hipótesis con
  referencia el propio, motor simulado.
- Ninguna fuente `.py` del código entregado menciona «audio» (por eso el 1.5 dice «una sola pista de vídeo, sin
  audio ni subtítulos»).
- Del descriptor de tamaños entregado (`perfiles_video/tamanos_segmentos/paseo_almunecar_10min_30fps_4s.json`), calidad
  4300 kbit/s: 151 segmentos, mín 168 367 B, máx 2 465 881 B, cociente 14,65 (> 14, «más de 14 veces»); nominal CBR
  2 150 000 B → máx/nominal 1,15 (> 10 %), mín/nominal 0,08 (< décima parte). Todo con aserciones.
- Del catálogo de trazas entregado: 12 `id_dataset` distintos = 12 carpetas de `datasets_normalizados`.
- Existencia de los siete bloques de `TFG Material` que enumera el 1.5 (00–06).
- Ninguna cifra decimal ni «1208» ni «41,3» en el texto: el capítulo no adelanta resultados (biblia §4).

## Citas (todas verificadas ya en los capítulos 2 y 5; página del PDF en `biblioteca_final/`)

| Clave | Afirmación en el cap 1 | Dónde |
|---|---|---|
| `seufert2015hasQoeSurvey` | vídeo > mitad del tráfico de consumo (57 % en 2012); paradas = factor que más degrada; cambios frecuentes/bruscos penalizan | p. 1; §IV p. 3–9 y 11 |
| `timmerer2025hasReview` | «more than half of global Internet traffic»; revisión de la cadena completa | p. 2 |
| `iso23009_1_2022` | DASH normaliza MPD y segmentos | p. 21 (§5.3.1) |
| `stockhammer2011dash` | HTTP sin estado, NAT/cortafuegos, cachés y CDN, control en el cliente | p. 1–2 |
| `bentaleb2019survey` | recorrido de heurísticos a MDP/aprendizaje | p. 3 y 7 |
| `amer2025learningReview` | revisión de métodos con aprendizaje | p. 1 |
| `peroni2025pipelineSurvey` | cadena de distribución codificador → cliente | p. 1 |
| `alsader2025qoeDriven6g` | redes móviles de próxima generación | p. 1 |
| `ameigeiras2012youtubeTraffic` | ráfaga + throttling; interrupciones al caer el ancho de banda | p. 1–2, Tabla p. 5 |
| `ramosMunoz2014mobileYoutube` | umbrales de buffer fijos en terminales móviles | p. 1 |
| `yin2015mpc` | objetivos en conflicto; MPC robusto como respuesta al error de predicción | p. 1, 3; p. 5–7 |
| `kan2021bayesmpc` | modelar la incertidumbre y decidir con ella | p. 1–3 |
| `yan2020puffer` | buenos en simulador ≠ buenos en red real | p. 1–3 |
| `hoffman2025intoTheWildABR` | distancia simulación–realidad medida | p. 1 |
| `alomar2023causalsim` | las trazas llevan impresa la política; sesgo | p. 1 |
| `peroni2024qoePitfalls` | el orden cambia con el modelo de QoE | p. 7–8 (Tabla II) |
| `mao2017pensieve` | RL de extremo a extremo (contraste con el enfoque acotado) | p. 2, 5–6 |

El comprobador solo detecta 14 de las 17 porque tres van dentro de corchetes múltiples `[a, b]` (Daniel las convierte
a «[n], [m]» al maquetar, biblia §5); el script las valida todas contra el .bib.

## Decisiones de redacción

- **Estructura frente al plan inicial.** El plan proponía 1.3 «Por qué un cliente DASH propio»; se amplió a «Enfoque
  del trabajo» con las cuatro decisiones de partida (entorno propio, fidelidad al medio, aprendizaje acotado,
  evaluación prerregistrada) porque la biblia pide «alcance» como apartado propio y porque el «cliente propio» ya
  tiene su justificación larga en el 2.6. Se añadió el 1.5 Alcance.
- **Objetivos 1–5** con entradilla «Objetivo n» (lista con infinitivo, numerable): el 7.1 debe responderlos por
  número. Reparto declarado en el último párrafo del 1.4: O1, O2, O3 → caps 4 y 5; O4 → 4, 5 y 6; O5 → 6.
- **Figura 1.1** (SVG propio, paleta sobria: grises, azul `#1971c2` para el propio y el lema del entrenamiento,
  amarillo `#fff9db` para protocolo y paquete, rojo `#c92a2a` para «una sola vez»; red emulada con borde
  discontinuo). Solapes comprobados con getBBox (40 textos, 0 problemas); la flecha del entrenamiento se reencaminó
  por debajo de las subcajas porque cruzaba el texto de los clásicos.
- Los nombres internos no aparecen (04_CORRESPONDENCIAS §5): «controlador propio», «predictor de cuantiles»,
  «planificador de control predictivo con medida de riesgo», «variantes».
- Las variantes se describen funcionalmente: dos sustituyen el predictor por cuantiles recientes o fijos; la tercera
  decide con la mediana sin la medida de riesgo (coincide con P3, P4 y P5 del protocolo).
- Antecedentes locales dentro del 1.1 (biblia §9: citar lo pertinente del grupo del tutor), enlazando con el 2.1.
- «Ensayo prerregistrado» se usa como analogía; el 6.1 y el 6.3 cuentan el mecanismo real (protocolo congelado con
  huellas).
- **Ampliación 09/11 (Daniel: «alargar el cap 1»)**, de 7 a 8 páginas con cinco párrafos sin relleno: (1.1) el buffer
  como variable que media entre red y usuario, con la preferencia por el retardo inicial frente a la parada (Seufert
  p. 3); (1.2) la variabilidad real de los tamaños en el contenido principal, con cifras leídas del descriptor; (1.3)
  las cuatro aportaciones (instrumento, controlador, método de evaluación, resultados negativos); (1.5) el material
  entregado, bloque a bloque; (1.6) convenciones (préstamos del inglés, siglas, numeración, cifras del cap 6
  regenerables). Se descartó un párrafo sobre el coste de las paradas para el proveedor porque exigiría una referencia
  nueva, y otro sobre las cuatro máquinas porque ya está en 6.1 (T6.3).

## Preguntas probables del tribunal

1. **¿Por qué no usar dash.js y añadir un plugin?** Navegador no controlable ni reproducible, sin telemetría de
   decisiones, controlador en Python: 1.3 primera decisión y 2.6.
2. **¿Qué aporta el trabajo frente a Pensieve o Fugu?** Aprendizaje acotado a la predicción con cuantiles, decisión
   con medida de riesgo, tamaños reales del medio, y una evaluación prerregistrada con variantes que aíslan cada pieza.
3. **¿Los objetivos se cumplieron?** Respuesta en el 7.1, objetivo a objetivo; el 1.4 los numera para eso.
4. **¿Por qué «una sola vez»?** Para que las hipótesis fijadas antes no se ajusten a los datos (1.3 cuarta decisión).

## Qué se puede recortar

El tercer párrafo del 1.1 (revisiones y antecedentes locales) a tres frases; el último párrafo del 1.5 (clásicos sin
ajuste) ya se repite en 6.1. Mantener 1.2, las cuatro decisiones del 1.3 con la figura y los Objetivos 1–5.
