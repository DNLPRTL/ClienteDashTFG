# Bibliografía definitiva del TFG — lista ganadora, descartes y normativa

> Entregable del hilo de bibliografía (10/08/2026). Convive con
> `00_PLAN_MAESTRO_MEMORIA.md` (estructura de la memoria) y
> `01_INVENTARIO_BIBLIOGRAFIA.md` (identificación fichero a fichero); este
> documento DECIDE qué entra, qué no y por qué, y su gemelo `bibliografia.bib`
> (mismo directorio) contiene las entradas listas para la plantilla LaTeX.

| Campo | Valor |
|---|---|
| Fecha | 2026-08-10 |
| Fichero BibTeX | `docs/memoria/bibliografia.bib` (92 entradas con claves únicas y sintaxis validada; BibTeX solo imprime las citadas) |
| Verificación | Cada entrada verificada contra: source cards del repo (con DOI), los .md convertidos de los PDF reales, y/o Crossref/página del editor (pasada 08/2026). Ninguna entrada de memoria/oídas. |
| Regla heredada | `bibliography_plan.md` (07_memory): "Do not include bibliography entries for papers not cited in the final text" → el .bib es generoso, la memoria cita lo que use. |

---

## 1. Normativa ETSIIT/UGR aplicada (punto 3 del encargo)

Fuentes oficiales leídas (agosto 2026):
- **Directrices TFG de la ETSIIT** (Junta de Centro 18/07/2023).
- **Resolución sobre el TFG de la ETSIIT** (18/07/2023) — incluye la rúbrica.
- **Página TFG del Grado en Ing. de Tecnologías de Telecomunicación** (grados.ugr.es).

Qué dicen que afecte a la bibliografía:

1. **No imponen estilo de citas** (ni IEEE ni APA ni cantidad mínima). El formato
   lo fija en la práctica la **plantilla oficial del grado** — exactamente la que
   tienes en `TFG/Plantilla_TFG_latex` — que usa **BibTeX**:
   `\bibliography{bibliografia/bibliografia}` + `\bibliographystyle{miunsrturl}`
   (estilo por orden de cita, con URLs).
2. **La rúbrica sí evalúa la bibliografía**, en dos criterios:
   - *"Búsqueda y tratamiento de la información"* (10 pts Tipo 1 / 15 pts Tipo 2
     sobre 100): "las fuentes son adecuadas, fiables, hay **variedad**, son
     **suficientes**".
   - *"Comunicación escrita"* (10 pts): "**uso adecuado de bibliografía y
     referencias**" — con asterisco: deficiencia grave aquí puede suponer
     **suspenso global**.
   - *"Conocimientos, habilidades y competencias"*: valora "conocimiento
     **actual o de vanguardia**" → respaldo directo al equilibrio temporal
     (clásicos + 2024-2026) que pide el punto 4 del encargo.
3. Memoria **máx. 100 páginas**, castellano y/o inglés. La política ya fijada en
   el repo (`style_and_format_rules.md`): memoria en español, **títulos de los
   papers sin traducir**.

**RESUELTO (10/08) — `miunsrturl.bst` no existe ni en el ZIP oficial:** Daniel
re-descargó la plantilla oficial del grado y tampoco trae ningún `.bst` (el
`TFG.tex` referencia un estilo que la escuela nunca distribuyó con el ZIP).
**Decisión: usar `\bibliographystyle{unsrt}`** (estándar, viene con cualquier
LaTeX/Prism; misma numeración por orden de cita). El `.bib` está preparado para
ello: los papers se identifican por venue+DOI en `note` cuando hace falta, y
todos los recursos web/software llevan su `\url{}` dentro de `howpublished`,
que `unsrt` SÍ imprime (el `TFG.tex` ya carga `\usepackage{url}`). Cambio
concreto en el proyecto Prism al activar la bibliografía:
`\bibliographystyle{miunsrturl}` → `\bibliographystyle{unsrt}` y copiar
`docs/memoria/bibliografia.bib` como `bibliografia/bibliografia.bib`.

---

## 2. LA LISTA GANADORA (anotada por parte de la memoria)

Criterio de selección: cubrir TODAS las partes del proyecto con el mínimo de
fuentes de máxima calidad; cada bloque de la memoria queda justificado; ni una
fuente sin papel asignado. Claves = las del `.bib` (canónicas del repo donde
existían). "Dónde" = dónde está el PDF/fuente en tu material.

### 2.1 NÚCLEO — citar sí o sí (28)

**Contexto y surveys (Cap 1, 2.1, 2.4, 2.7):**
| Clave | Fuente | Justifica |
|---|---|---|
| `bentaleb2019survey` | Bentaleb 2019, IEEE COMST | Taxonomía ABR de referencia; vertebra el cap 2. |
| `timmerer2025hasReview` | Timmerer 2025, ACM TOMM | Estado del arte HAS reciente (equilibrio temporal). |
| `peroni2025pipelineSurvey` | Peroni & Gorinsky 2025, ACM CSUR | Visión pipeline extremo a extremo; motivación cap 1. |
| `seufert2015hasQoeSurvey` | Seufert 2015, IEEE COMST | Survey QoE clásico; base del cap 2.5. |
| `amer2025learningReview` | Amer 2025, IEEE Access | Review de métodos con aprendizaje; enmarca la familia IA. |

**Trabajos locales UGR (Cap 1 motivación + Cap 2 "Antecedentes locales") — el
acuerdo del tutor, recuperado de `07_memory/originality_and_citation_policy.md`
y `0_field_map/local_streaming_source_evidence.md`:**
| Clave | Fuente | Justifica |
|---|---|---|
| `ameigeiras2012youtubeTraffic` | Ameigeiras, Ramos-Muñoz, Navarro-Ortiz, López-Soler 2012 | Caracterización de tráfico de vídeo del grupo del profesor; motivación local. **Hay hasta un párrafo en español ya redactado** en `local_streaming_source_evidence.md` (líneas 103-105) para el cap 2. |
| `ramosMunoz2014mobileYoutube` | Ramos-Muñoz et al. 2014, IEEE Wireless Comm. | Ídem, versión móvil. **El primer autor ES el tutor del TFG (Juan José Ramos Muñoz, confirmado 10/08)** → cita doblemente obligada. |

**DASH y estándar (Cap 2.2, 4.2):**
| Clave | Fuente | Justifica |
|---|---|---|
| `iso23009_1_2022` | ISO/IEC 23009-1:2022 | EL estándar: MPD, segmentos, terminología. Política del repo: no citar pasajes largos. |
| `stockhammer2011dash` | Stockhammer 2011, MMSys | Principios de diseño DASH; el paper fundacional. |

**Baselines clásicos (Cap 2.4, 5.5) — atribución exacta verificada código↔paper
en el HANDOFF (líneas 64-68):**
| Clave | Fuente | Justifica |
|---|---|---|
| `liu2011rateAdaptation` | Liu 2011, MMSys | `basado_en_tasa` (rate-based). |
| `huang2014bba` | Huang 2014, SIGCOMM | `bba` (BBA-0 reservoir/cushion). |
| `yin2015mpc` | Yin 2015, SIGCOMM | `mpc` (FastMPC) + `mpc_robusto` (fórmula exacta) + **la QoE compuesta del proyecto**. |
| `spiteri2020bola` | Spiteri 2020, IEEE/ACM ToN | `bola` (BOLA-BASIC). |

**IA-ABR de referencia (Cap 2.4, 5.6):**
| Clave | Fuente | Justifica |
|---|---|---|
| `mao2017pensieve` | Mao 2017, SIGCOMM (Pensieve) | La referencia RL; el repo obliga: citar "solo como contexto histórico, NO como implementación propia" (`robust_mpc/notes_for_memory.md`). |
| `yan2020puffer` | Yan 2020, NSDI (Puffer/Fugu) | El paradigma predictor+control del controlador propio; despliegue real; además fuente del dataset Puffer. |

**Riesgo, incertidumbre y sim-to-real — la tesis del controlador propio (Cap 2.7, 5.6):**
| Clave | Fuente | Justifica |
|---|---|---|
| `kan2021bayesmpc` | Kan 2021, NOSSDAV (BayesMPC) | LA referencia del CVaR/riesgo del planner; citada textualmente en las decisiones del giro de riesgo. |
| `chen2024soda` | Chen 2024, SIGCOMM (SODA) | Consistencia/estabilidad no neuronal; contrapunto moderno. |
| `hoffman2025intoTheWildABR` | Hoffman 2025, ACM PACMI | Sim-to-real: por qué validar contra servidor real. |
| `alomar2023causalsim` | Alomar 2023, NSDI (CausalSim) | Sesgo de la simulación con trazas; justifica la metodología de fidelidad al medio. |

**Fundamentos matemáticos del controlador propio (Cap 5.6) — sin PDF en tu
material, verificados vía Crossref/editor (los pediste explícitamente):**
| Clave | Fuente | Justifica |
|---|---|---|
| `koenker1978quantiles` | Koenker & Bassett 1978, Econometrica | Regresión de cuantiles = la pinball loss del predictor. |
| `rockafellar2000cvar` | Rockafellar & Uryasev 2000, J. of Risk | Definición canónica del CVaR del planner. |
| `cho2014gru` | Cho 2014, EMNLP | La GRU del predictor temporal. |
| `lakshminarayanan2017ensembles` | Lakshminarayanan 2017, NIPS | Deep ensembles = el ensemble de 5 GRUs con incertidumbre. |

**Datasets de mayor peso del corpus (Cap 6.3):**
| Clave | Fuente | Justifica |
|---|---|---|
| `fccMeasuringBroadbandAmerica` | FCC MBA (web oficial) | 4174/6768 trazas (62% del corpus). |
| `riiser2013commutePath` | Riiser 2013, MMSys | Norway/HSDPA, el dataset clásico de ABR. |
| `raca2018beyondThroughput4g` | Raca 2018, MMSys | UCC 4G LTE. |

**Metodología QoE (Cap 2.5, 6.5):**
| Clave | Fuente | Justifica |
|---|---|---|
| `peroni2024qoePitfalls` | Peroni 2024, COMSNETS | "Reportar distribuciones y por régimen, no solo medias" — ya guio el diseño de la evaluación (catálogo de métricas). |

### 2.2 APOYO — citar donde el capítulo lo pide (27)

| Clave | Fuente | Dónde encaja |
|---|---|---|
| `timmerer2012dashCreationConsumption` | Timmerer & Griwodz 2012, ACM MM | Cap 2.2 (cadena creación→consumo). |
| `dashIfIop` | DASH-IF IOP (guía) | Cap 2.2/4 (interoperabilidad; anota la versión del PDF que tienes). |
| `iso14496_12_2015` | ISO/IEC 14496-12:2015 | Cap 4/5 (fMP4/init segments). |
| `rfc3986`, `rfc9110`, `rfc9112` | RFCs IETF | Cap 4/5 (URLs de segmento, HTTP del cliente). |
| `spiteri2019dashjs` | Spiteri 2019, ACM TOMM | Cap 5.5: BOLA práctico en dash.js ("solo como contexto de reproductor real", regla del repo). |
| `akhtar2018oboe` | Akhtar 2018, SIGCOMM (Oboe) | Cap 2.4 (auto-tuning) + fuente de las trazas Oboe del corpus (427). |
| `huang2020comyco` | Huang 2020, IEEE JSAC (Comyco ext.) | Cap 2.4 (imitación). El PDF que tienes ES la versión JSAC, no la MM'19 — por eso se cita esta. |
| `xie2026safesabr` | SafeSABR, arXiv 2026 | Cap 2.7 (riesgo calibrado; preprint — citar como arXiv). |
| `luo2025sabr` | SABR, arXiv 2025 | Cap 2.4 (BC+RL; preprint). |
| `bothra2023veritas` | Bothra 2023, SIGCOMM (Veritas) | Cap 2.7/4.7 (causalidad en trazas). OJO: tu `Veritas.pdf` es el preprint 2022; el bueno es `2023_bothra_veritas...pdf`. |
| `netravali2015mahimahi` | Mahimahi, ATC'15 | Cap 4.7 (record-and-replay como alternativa de emulación). |
| `wei2019traceBasedEmulation` | Wei 2019, IEEE Access | Cap 4.7/5.6 (predicción de throughput evaluada con emulación de trazas). |
| `barman2019qoeModeling` | Barman & Martini 2019, IEEE Access | Cap 2.5 (modelos QoE). |
| `taraghi2021understandingQoe` | Taraghi 2021, NOSSDAV | Cap 2.5/6 (QoE de heurísticos = tus baselines). |
| `duanmu2017qoeIndex` | Duanmu 2017, IEEE JSTSP | Cap 2.5 (índice QoE continuo). OJO nombre de fichero engañoso: el PDF es el paper del *índice*, no la "database". |
| `alsader2025qoeDriven6g` | Alsader 2025, IEEE Access | Cap 1/2 (contexto reciente 6G). |
| `raca2020beyondThroughput5g` | Raca 2020, MMSys | Corpus: UCC 5G (83 trazas). |
| `narayanan2020lumos5g` | Narayanan 2020, IMC | Corpus: Lumos5G (118). |
| `vanDerHooft2016ghent4g` | van der Hooft 2016, IEEE Comm. Letters | Corpus: Ghent 4G/LTE (40) — paper + URL del dataset. |
| `kousias2024romaDataset` | Kousias 2024, IEEE Comm. Magazine | Corpus: Roma 4G/NB-IoT/5G-NSA (438) — identificado desde la carpeta de datos brutos y verificado. |
| `mei2019nyumetsPam` + `nyuMetsDataset` | Mei 2019, PAM + repo GitHub | Corpus: NYU-METS (28). |
| `hassanein2025gavist5g` | GAViST5G, IEEE DataPort | Corpus: GaVist5G (122). |
| `pufferDataArchive` | Puffer data archive | Corpus: Puffer (93; datos abril 2025). |
| `digregorio2026mlLoading` | Digregorio 2026, IEEE S&P | Cap 5.1: justifica `weights_only` al cargar bundles (¡resultó estar publicado en S&P 2026, mejor de lo que creíamos!). |
| Software (14 entradas `@misc`) | ffmpeg, GPAC/MP4Box, Apache, GStreamer, PyGObject, PyTorch, ROCm, requests, PyYAML, ElementTree, urllib.parse, Python, dash.js, Shaka | Cap 2.6, 5.1 y 6.2 — todas con la VERSIÓN REAL del experimento (de `docs/defensa/componentes_experimento.md`). |

### 2.3 AMPLITUD / RESERVA — en el `.bib`, se imprimen solo si el cap 2 las nombra (~20)

La tabla de familias del cap 2.4 puede citar 1-2 ejemplos por familia; están
todas verificadas con DOI: `kan2022merina` (MM'22), `huang2022a2br` (JSAC'22),
`li2024metaabr` (TMC'24), `bentaleb2024ahaggar` (TMC'24), `yin2024ant` (TBC'24),
`zhang2025beta` (TMC'25), `yi2025fortuna` (TMM'25), `huang2026eastream`
(TSC'26), `wang2026nmoeabr` (TMC'26), `huang2023deepbuffer` (INFOCOM'23),
`mao2020abrl` (arXiv Facebook), `patel2024gelato` (PACM Netw'24),
`patel2023plume` (arXiv), `zhou2022adaptiveStreamingQualityAssessment` (JVCIR),
`zuo2022ruyiPreferenceQoe` (INFOCOM'22), `yi2025airl` (CJE), `hussein2026mambra`
(preprint Research Square — **existe y es verificable**, pero NO revisado por
pares: citar solo como preprint), `kingma2015adam`, `rfc9111`, `netflixVmaf`,
`virtualboxDoc`/`wslDoc`/`dockerDoc`.

Recomendación concreta para la tabla del cap 2.4 (una cita por familia, sin
inflar): meta/generalización → `kan2022merina` + `huang2022a2br`; dinámica de
red → `yin2024ant`; mixture-of-experts → `wang2026nmoeabr`; RL en producción →
`mao2020abrl` o `patel2024gelato`. El resto se queda en reserva.

---

## 3. DESCARTES (con motivo, punto 1 del encargo)

**Duros (no citar; no aportan o desentonan):**
| Fichero | Identidad real | Motivo |
|---|---|---|
| `1-s2.0-S1687850724002206-main.pdf` | "Bit rate selection... based on AI in MPEG-DASH" (J. Radiation Research and Applied Sciences 2024) | Venue fuera de ámbito (ciencias de radiación); calidad dudosa. |
| `kaken.nii.ac.jp_20K14740seika.pdf` | Informe de subvención KAKEN (Japón) | No es una publicación citable; sin texto extraíble. |
| `Hybrid Adaptive Bitrate for Video Streaming.pdf` | Tesis de máster de Seoul National Univ. (autor en coreano, 2023) | Tesis en coreano, nada que no den los papers publicados. |
| `075042_1_5.0277381.pdf` | "Deep RL enhanced optimization for ABR" (Zhang, AIP Advances 2025) | Venue menor y fuera del área; cubierto por los TMC/TBC de amplitud. |
| `v1_covered.pdf` | "DQNReg" RL rate adaptation 2022 (preprint "covered") | Preprint sin identidad de venue verificable. |
| `applsci-13-11697.pdf` | Souane 2023, MDPI Applied Sciences | Venue menor; redundante con la familia RL ya cubierta. |
| `PPO-ABR...pdf` | PPO-ABR, IWCMC 2023 | Redundante (PPO ya se descarta con argumento propio en `why_not_ppo_first.md`; si el cap 7.5 lo menciona, se puede recuperar — DOI verificado: 10.1109/IWCMC58020.2023.10182379). |
| `Enhancing_...Bandwidth_Prediction...pdf` | "BPA" (IEEE TNSM, DOI 10.1109/TNSM.2026.3696658) | Predicción BW con RL; tu predictor es supervisado — no aporta al hilo argumental. |
| `3524273.3528188.pdf` (GreenABR) | GreenABR, MMSys'22 | Eje energía: la memoria no lo toca. |
| `3591108.pdf` | Visual Sensitivity ABR, ACM TOMM | Eje percepción visual: fuera de guion. |
| `3592473.3592564.pdf` (Incendio) | MARL para short video, 2023 | Short video/MARL: fuera de guion. |
| `1-s2.0-S1084804522001035-main.pdf` (ALVS) | Live streaming DRL, JNCA 2022 | Live: fuera de guion (tu sistema es VoD). |
| `1-s2.0-S1084804523000231-main.pdf` | Edge-assisted RL HAS, JNCA 2023 | Edge: infraestructura que no existe en el proyecto (ya diferido en `decision_tecnica_modelos_v1.md`). |

**Material del repo que NO pasa a bibliografía (regla del propio
`bibliography_plan.md`: solo se cita lo realmente usado):**
| Elemento | Motivo |
|---|---|
| Lancaster ABR-Throughput-Traces (trace card) | El dataset NO está en el corpus final (verificado contra `catalogo_trazas.json`). |
| `tc-netem` (method card) | El replay del cliente es aplicativo, no usa netem. Solo si el cap 4.7 lo menciona como alternativa. |
| ONNX Runtime (doc) | El runtime final carga PyTorch (`weights_only`), no ONNX. |
| FESTIVE / PANDA / WISH / Lumos / RBC (candidate cards) | Candidatos no implementados. FESTIVE y PANDA tienen DOI verificado en las cards por si la tabla del cap 2.4 los quiere como ejemplos históricos — pedidlos y los añado al `.bib`. |
| CS2P (mención en decisión de frontera) | No está en tu material; solo si el cap 7.4 (trabajo futuro del predictor) lo quiere — se conseguiría el PDF y se añadiría. |

---

## 4. Duplicados físicos (limpieza de disco, cuando quieras)

- **Carpeta entera `TFG/abr ia pdf/`**: sus 32 PDFs están TODOS en
  `literatura/todo lo demas...` (mismo tamaño byte a byte, a veces otro nombre:
  `pensievee.pdf`=`Pensieve.pdf`, `3736306.pdf`=`HTTP Adaptive Streaming A
  Review...pdf`, `MetaABR_...pdf`≈`MetaABR.pdf`). → puede irse entera a
  `legacy/` (regla de la casa: mover, no borrar).
- Dentro de `literatura/todo lo demas...`: los 8 pares ya cazados en
  `01_INVENTARIO_BIBLIOGRAFIA.md` §K (conservar izquierda): A2BR↔Learning_Tailored,
  Comyco↔1908.02270v1, SABR↔2509.10486v1, Review↔A_Review↔**Surveys de 2025**
  (verificado: es el MISMO survey de Amer et al., versión de autor),
  Veritas(2023)↔Veritas.pdf(preprint 2022), Mahimahi, Raca 4G, Raca 5G.
- Cross-carpeta: `01_Bentaleb...pdf` (en "para justificar el cliente") =
  `2019_bentaleb...pdf`; ISO 23009 y Stockhammer también están duplicados entre
  las dos subcarpetas de literatura.

---

## 5. Dudas marcadas (regla de oro: se preguntan, no se inventan)

1. ~~¿Quién firma como tutor?~~ **RESUELTO (10/08): el tutor es Juan José
   Ramos Muñoz** — primer autor de `ramosMunoz2014mobileYoutube` y coautor de
   `ameigeiras2012youtubeTraffic`. Va a la portada (`\myProf` de la plantilla)
   y da todo el sentido a la subsección de antecedentes locales del cap 2.
2. ~~`miunsrturl.bst`~~ **RESUELTO (10/08)**: el ZIP oficial tampoco lo trae →
   `\bibliographystyle{unsrt}` (ver sección 1).
3. ~~DASH-IF IOP sin versión~~ **RESUELTO (10/08)**: portada del PDF local =
   **Version 4.1, 7 de septiembre de 2017** — fijado en el `.bib`.
4. **Estadística del cap 6** (bootstrap CI95, sign test): no hay fuente en tu
   material. Si quieres cita metodológica (recomendable pero opcional), la
   clásica es Efron & Tibshirani, *An Introduction to the Bootstrap* — dila y la
   verifico/añado.
5. **MamBRA**: existe como preprint Research Square (DOI verificado) de autores
   Hussein/Mohammed/Abdullah 2026. Al ser no-revisado y no esencial, lo dejé en
   RESERVA. Tú decides si el cap 5 lo menciona.
6. Dos PDFs sueltos quedaron sin uso asignado por ilegibles/no convertidos:
   ninguno afecta a la lista (los dos identificados están descartados: DQNReg y
   AIP). No hay más ficheros sin identificar.

---

## 6. Números finales (variedad y equilibrio temporal — rúbrica y punto 4)

Lista ganadora (núcleo+apoyo, sin reservas): **55 entradas** →
- Por época: 1978-2015: 14 · 2016-2020: 14 · 2021-2023: 8 · **2024-2026: 19**.
  Mitad clásicos consolidados, mitad recientes: exactamente el "conocimiento
  actual o de vanguardia" que puntúa la rúbrica.
- Por tipo: 33 papers (24 de venue A: SIGCOMM×5, NSDI×2, ATC, IMC, MMSys×4,
  COMST×2, ToN, JSAC, CSUR, TOMM×2, S&P...), 2 estándares ISO, 3 RFCs + 1 guía
  DASH-IF, 5 datasets citados como recurso, 14 software con versión real, 2
  trabajos locales UGR. Variedad = casilla de la rúbrica cubierta.
- Cobertura por capítulo del plan maestro: Cap 1 ✔ (5 fuentes), Cap 2 ✔ (todas
  las familias con ejemplo), Cap 4 ✔ (estándar+RFCs+emulación+datasets), Cap 5 ✔
  (baselines con paper primario, controlador propio con sus 4 fundamentos + 4
  referencias de riesgo, software con versión), Cap 6 ✔ (QoE+datasets+
  metodología), Cap 7 ✔ (los why_not_* del repo dan los resultados negativos
  sin fuentes nuevas).

## 7. Cómo se montó (trazabilidad de este trabajo)

1. Inventario de las dos carpetas de PDFs y cruce por tamaño (duplicados).
2. Peinado COMPLETO de `docs/` (786 md): field map con claves BibTeX
   (`0_field_map`, `01_baselines`, `02_traces_replay`, `03_qoe_reward`,
   `04_neural_abr`, `05_...`, `07_memory` con su `bibliography_plan.md`
   histórico), las 32 fichas de `abr ia md`, decisiones `decision_*` y el
   catálogo de métricas.
3. Identificación real de los 63 md convertidos (título/autores/venue/DOI de la
   primera página, incluidos DOIs en texto espejado del sello IEEE).
4. Corpus verificado contra `catalogo_trazas.json` (12 datasets, conteos) y
   origen de cada dataset por su carpeta de datos brutos.
5. Normativa ETSIIT leída de los PDF oficiales; plantilla LaTeX inspeccionada.
6. Pasada Crossref/editor para los 16 metadatos que faltaban o dudaban.
