# Inventario bibliográfico de la memoria

> Identificación real de los 100 ficheros de `literatura/` (80 + 20), con clave de
> cita, título/autor/año/venue, tema, calidad (tier), capítulo(s) destino y notas
> (duplicado / usar / descartar). Es el mapa **fuente → capítulo** que usa el
> `00_PLAN_MAESTRO_MEMORIA.md` y que decide qué subir a cada notebook de NotebookLM.

Identificación obtenida de: 62 papers ya convertidos a Markdown
(`docs/todos los estudios pdf convertidos a md/`) + página 1 de los PDF crípticos +
nombres de los estándares/RFC/docs de herramientas. **Ninguna fuente quedó sin
identificar.**

Leyenda **Tier**: A = venue top (NSDI, SIGCOMM, MM, IEEE/ACM ToN, INFOCOM, COMST,
ACM CSUR, JSAC) · B = IEEE/ACM sólido (TMC, TBC, TSC, Access, MMSys) · C = menor /
tesis / dudoso. **Uso**: NÚCLEO (citar sí o sí) · APOYO · AMPLITUD (cita de barrido) ·
DESCARTAR.

---

## A. Surveys y QoE (Cap 2 estado del arte; Cap 6 métricas)

| Clave | Fichero | Título / autor / año / venue | Tema | Tier | Cap | Uso |
|---|---|---|---|---|---|---|
| `Bentaleb19` | 2019_bentaleb_abr_survey_http_streaming | A Survey on Bitrate Adaptation Schemes for Streaming Media Over HTTP — Bentaleb et al. 2019, IEEE COMST | Survey ABR de referencia | A | 1,2 | NÚCLEO |
| `TimmererReview` | HTTP Adaptive Streaming A Review… | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges — Timmerer et al., ACM CSUR | Survey HAS reciente | A | 1,2 | NÚCLEO |
| `Seufert15` | 01_2015_seufert_qoe_http_adaptive_streaming_survey | A Survey on QoE of HTTP Adaptive Streaming — Seufert et al. 2015, IEEE COMST | Survey QoE clásico | A | 2,6 | NÚCLEO |
| `Alsader25` | 12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey | QoE-Driven Adaptive Video Streaming: Architectures, Techniques, Future — Alsader 2025, IEEE Access | Survey reciente 6G/QoE | B | 1,2 | APOYO |
| `PeroniGorinsky25` | 2025_peroni_gorinsky_video_streaming_best_effort_pipeline_survey | End-to-End Pipeline Perspective on Video Streaming in Best-Effort Networks: Survey & Tutorial — Peroni & Gorinsky 2025 | Survey/tutorial pipeline | A | 1,2 | NÚCLEO |
| `QoEModeling19` | QoE modeling for HTTP adaptive video streaming | QoE Modeling for HTTP Adaptive Video Streaming — A Survey and Open Challenges, IEEE Access 2019 | Survey modelos QoE | B | 2,6 | APOYO |
| `PeroniQoE24` | 06_2024_peroni_qoe_status_quo_pitfalls_guidelines | QoE in Video Streaming: Status Quo, Pitfalls, Guidelines — Peroni 2024, COMSNETS | Buenas prácticas QoE | B | 2,6 | APOYO |
| `DuanmuQoE` | A quality-of-experience database for adaptive video streaming | A Quality-of-Experience Index for Streaming Video — Duanmu et al. 2017, IEEE JSTSP | Índice/DB de QoE | B | 2,6 | APOYO |
| `UnderstandingQoE` | Understanding quality of experience of heuristic-based HTTP adaptive bitrate algorithms | Understanding QoE of Heuristic-based HTTP ABR — IMC | QoE de baselines | B | 2,6 | APOYO |
| `Zuo22` | 11_2022_zuo_ruyi_user_level_qoe_preference | Adaptive Bitrate with User-level QoE Preference (Ruyi) — Zuo et al. 2022 | QoE personalizada | B | 2 | AMPLITUD |
| `ZhouSurvey` | Zhou | A Brief Survey on Adaptive Video Streaming Quality Assessment — Zhou et al. | Survey calidad/QoE | C | 2 | AMPLITUD |
| `LearningReview25` | A review of learning-based methods… | A Review of Learning-Based Methods for Adaptive Video Streaming Over HTTP — IEEE Access 2025 (DOI …3582850) | Survey IA/ABR reciente | B | 2 | NÚCLEO (familia IA) |

## B. Estándares DASH, MPD y herramientas del cliente (Cap 2.2/2.6, Cap 4, Cap 5.1)

Carpeta `para justificar el cliente` (20) — la base para justificar el cliente DASH.

| Clave | Fichero | Qué es | Cap | Uso |
|---|---|---|---|---|
| `ISO23009` | 00_ISO_IEC_23009-1_2022_MPEG_DASH_Part1_public | Estándar MPEG-DASH Part 1 (MPD, segmentos) | 2,4,5 | NÚCLEO |
| `ISO14496-12` | 09_ISO_IEC_14496-12_2015 | ISO BMFF (contenedor MP4/fMP4) | 4,5 | APOYO |
| `Stockhammer11` | 02_Stockhammer_2011_DASH_standards_design_principles | DASH: Design Principles and Standards — Stockhammer 2011 | 2,4 | NÚCLEO |
| `Timmerer12` | 03_Timmerer_Griwodz_2012_DASH_content_creation_to_consumption | DASH content creation to consumption — Timmerer & Griwodz 2012 | 2,4 | APOYO |
| `DASH_IF_IOP` | 04_DASH_IF_IOP | DASH-IF Interoperability Points | 2,4 | APOYO |
| `RFC3986` | 05_RFC_3986_URI_Generic_Syntax | URIs (construcción de URL de segmento) | 4,5 | APOYO |
| `RFC9110` | 06_RFC_9110_HTTP_Semantics | Semántica HTTP | 4,5 | APOYO |
| `RFC9111` | 07_RFC_9111_HTTP_Caching | Caching HTTP | 4 | AMPLITUD |
| `RFC9112` | 08_RFC_9112_HTTP_1_1 | HTTP/1.1 (descarga de segmentos) | 4,5 | APOYO |
| `BentalebSurveyCliente` | 01_Bentaleb et al. - 2018 - A Survey… | = `Bentaleb19` (copia en esta carpeta) | 2 | DUP de `Bentaleb19` |
| docs herramientas | 10_GPAC… / 11_dashjs… / 12_Shaka… | Reproductores DASH existentes | 2.6 | APOYO |
| docs Python | 14–16 GStreamer/PyGObject, 17 ElementTree, 18 urllib, 19 Requests, 20 PyYAML | Librerías de implementación | 5.1 | APOYO (cita técnica) |

## C. Baselines clásicos (Cap 5.5 implementación; Cap 2.4 familias)

Ya hay `paper_card.md` + `source_evidence.md` + `notes_for_memory.md` por baseline en
`docs/contexto rama original/01_baselines/`.

| Clave | Fichero | Título / autor / año | Baseline | Tier | Cap | Uso |
|---|---|---|---|---|---|---|
| `Liu11` | 2011_liu_rate_adaptation_adaptive_http_streaming | Rate Adaptation for Adaptive HTTP Streaming — Liu et al. 2011 | `rate_based` | A | 2,5 | NÚCLEO |
| `Huang14` | 2014_huang_bba_buffer_based_rate_adaptation | A Buffer-Based Approach to Rate Adaptation (BBA) — Huang et al. 2014, SIGCOMM | `bba` | A | 2,5 | NÚCLEO |
| `Yin15` | 2015_yin_mpc_control_theoretic_abr_http | A Control-Theoretic Approach for DASH (MPC/RobustMPC) — Yin et al. 2015, SIGCOMM | `mpc`,`robust_mpc` | A | 2,5 | NÚCLEO |
| `Spiteri20` | 2020_spiteri_bola_near_optimal_bitrate_adaptation_ton | BOLA: Near-Optimal Bitrate Adaptation — Spiteri et al. 2020, IEEE/ACM ToN | `bola` | A | 2,5 | NÚCLEO |
| `Spiteri19` | 2019_spiteri_dash_reference_player_bola_dynamic | From Theory to Practice: Improving Bitrate Adaptation in the DASH Reference Player — Spiteri 2019 | `bola` (DYNAMIC) | A | 2,5 | APOYO |
| `Oboe` | Oboe | Oboe: Auto-tuning Video ABR Algorithms to Network Conditions — Akhtar et al., SIGCOMM'18 | auto-tuning | A | 2,5 | APOYO |

## D. IA / Neural ABR — núcleo (Cap 2.4 familia RL; Cap 5.6 contexto del propio)

| Clave | Fichero | Título / año / venue | Tier | Cap | Uso |
|---|---|---|---|---|---|
| `Pensieve17` | Pensieve | Neural Adaptive Video Streaming with Pensieve — Mao et al. 2017, SIGCOMM | A | 2,5 | NÚCLEO |
| `Puffer20` | 2020_yan_puffer_learning_in_situ_nsdi | Learning in situ (Puffer) — Yan et al. 2020, NSDI | A | 1,2,5,6 | NÚCLEO |
| `Real-worldRL` | Real-world Video Adaptation with Reinforcement Learning | Real-world Video Adaptation with RL — Mao et al. (Facebook) | A | 2,5 | APOYO |
| `Comyco` | Comyco | Comyco: Quality-aware Neural ABR with Lifelong Imitation Learning — Huang et al., MM'19 | A | 2 | APOYO |
| `Gelato` | Gelato | Practically High Performant Neural Adaptive Video Streaming — Patel et al. | B | 2 | AMPLITUD |
| `Plume` | Plume | Plume: High Performance Deep RL Network Controllers via Prioritized Trace Sampling — Patel et al. | B | 2 | AMPLITUD |

## E. IA / Neural ABR — generalización, meta, offline (Cap 2.4 amplitud)

| Clave | Fichero | Título / venue | Tier | Cap | Uso |
|---|---|---|---|---|---|
| `MERINA` | MERINA | Improving Generalization via Meta RL — Kan et al. | B | 2 | AMPLITUD |
| `Fortuna` | Fortuna | Offline RL + Meta-Learning in Diverse Networks — IEEE TMM 2025 | B | 2 | AMPLITUD |
| `MetaABR` | MetaABR | MetaABR: Meta-Learning for Bitrate Selection — IEEE TMC 2024 | B | 2 | AMPLITUD |
| `A2BR` | A2BR | Learning Tailored ABR to Heterogeneous Networks (A²BR, Domain Priors + Meta-RL) — JSAC 2022 | A | 2 | AMPLITUD |
| `BentalebMetaRL` | Bitrate Adaptation and Guidance With Meta Reinforcement Learning | Bentaleb et al., IEEE TMC 2024 | B | 2 | AMPLITUD |
| `ANT` | ANT | Learning Accurate Network Dynamics for Enhanced ABR — IEEE TBC 2024 | B | 2 | AMPLITUD |
| `BETA` | BETA | Spatial-Temporal Learning for Generalization in ABR — IEEE TMC 2025 | B | 2 | AMPLITUD |
| `NMoEABR` | NMoEABR | Mixture of Experts for ABR in Heterogeneous Wireless — IEEE TMC 2026 | B | 2 | AMPLITUD |
| `BufferAware` | Buffer awareness neural adaptive video streaming… | Buffer-Awareness Neural ABR — Huang et al. | B | 2 | AMPLITUD |
| `EAStream` | EAStream | Environment-Aware Adaptive Bitrate — IEEE TSC 2026 | B | 2 | AMPLITUD |
| `HybridABR` | Hybrid Adaptive Bitrate for Video Streaming | Tesis MS (Corea), híbrido | C | 2 | AMPLITUD/opcional |
| `AIRL` | AIRL | RL ABR — Chinese Journal of Electronics 2025 | C | 2 | opcional |

## F. Riesgo / incertidumbre / consistencia — alineados con TU tesis (Cap 2.7, 5.6)

**Las más importantes para justificar el controlador propio.**

| Clave | Fichero | Título / venue | Tier | Cap | Uso |
|---|---|---|---|---|---|
| `BayesMPC` | Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control | Uncertainty-Aware Robust ABR with Bayesian NN + MPC | A | 2,5 | **NÚCLEO** |
| `SafeSABR` | SafeSABR | SafeSABR: Risk-Calibrated Adaptive Bitrate over Starlink — Xie et al. | B | 2,5 | **NÚCLEO** |
| `SODA` | SODA | SODA: Adaptive Bitrate Controller for Consistent High-Quality Streaming — Chen et al. (UMass/Caltech) | A | 2,5 | **NÚCLEO** |
| `SABR` | SABR | SABR: Stable ABR via Behavior Cloning + RL Fine-Tuning — Luo et al. | B | 2,5 | APOYO |

## G. Trazas, datasets, emulación, sim-to-real (Cap 4.7, 6.3, 2.7)

| Clave | Fichero | Título / venue | Tema | Tier | Cap | Uso |
|---|---|---|---|---|---|---|
| `Puffer20` | (ver D) | Learning in situ | despliegue real | A | 6,2 | NÚCLEO |
| `Hoffman25` | 2025_hoffman_into_the_wild_ml_based_abr | Into the Wild: Real-World Testing for ML-Based ABR — ETH 2025 | sim-to-real | A | 2,5 | **NÚCLEO** |
| `CausalSim23` | CausalSim | CausalSim: Unbiased Trace-Driven Simulation — Alomar et al. 2023, NSDI | sesgo simulación | A | 2,4 | **NÚCLEO** |
| `Veritas23` | 2023_bothra_veritas_causal_queries_video_streaming_traces | Veritas: Causal Queries from Video Streaming Traces — Bothra et al. 2023 | trazas causales | A | 2,4 | APOYO |
| `Mahimahi15` | 2015_netravali_mahimahi_record_replay_http | Mahimahi: Accurate Record-and-Replay for HTTP — Netravali et al. 2015 | emulación | A | 4 | APOYO |
| `CellReplay` | CellReplay | CellReplay: record-and-replay for cellular networks | emulación celular | B | 4 | AMPLITUD |
| `Wei19` | 2019_wei_trace_based_emulation_throughput_prediction_abr | Evaluation of Throughput Prediction for ABR (trace-based emulation) — 2019, IEEE Access | predicción throughput | B | 4,5 | APOYO |
| `Riiser13` | 2013_riiser_commute_path_bandwidth_traces_3g_networks | Commute Path Bandwidth Traces from 3G (Norway/HSDPA) — Riiser et al. 2013 | dataset trazas | A | 4,6 | NÚCLEO (corpus) |
| `Raca18` | 2018_raca_4g_lte_dataset_channel_context_metrics | Beyond Throughput: 4G LTE Dataset — Raca et al. 2018, MMSys | dataset 4G | A | 4,6 | NÚCLEO (corpus) |
| `Raca20` | 2020_raca_5g_dataset_channel_context_metrics_mmsys | Beyond Throughput, Next Gen: 5G Dataset — Raca et al. 2020, MMSys | dataset 5G | A | 4,6 | APOYO |
| `Lumos5G20` | 2020_narayanan_lumos5g_imc | Lumos5G: Predicting mmWave 5G Throughput — Narayanan et al. 2020, IMC | dataset 5G | A | 4,6 | APOYO (corpus) |
| `VanderHooft16` | 2016_van_der_hooft_http2_hevc_video_over_4g_lte | HTTP/2 Adaptive Streaming of HEVC over 4G/LTE — van der Hooft 2016 | dataset/HTTP2 | B | 2,4 | AMPLITUD |

## H. Tooling ML y seguridad (Cap 5.1, Anexos)

| Clave | Fichero | Qué es | Cap | Uso |
|---|---|---|---|---|
| `PyTorchDoc` | PyTorch 2.12 documentation | torch.load / framework IA | 5.1 | APOYO |
| `ONNXDoc` | ONNX Runtime Python API | inferencia runtime | 5.1 | APOYO (si se usa ONNX) |
| `MLModelSecurity` | On the (In)Security of Loading Machine Learning Models | riesgo de cargar modelos serializados | 5.1, Anexo | APOYO (decisión de diseño) |

## I. Tráfico de vídeo / contexto (Cap 1 motivación; autores UGR-cercanos)

| Clave | Fichero | Título / autores | Cap | Uso |
|---|---|---|---|---|
| `Ameigeiras12` | 2012_ameigeiras_youtube_traffic_analysis_modelling | YouTube Traffic Analysis and Modelling — Ameigeiras et al. (Granada) | 1,2 | APOYO (cercanía UGR) |
| `RamosMunoz14` | 2014_ramos_munoz_mobile_youtube_traffic_characteristics | Characteristics of Mobile YouTube Traffic — Ramos-Muñoz et al. (Granada) | 1,2 | APOYO (cercanía UGR) |

## J. IA / ABR — amplitud secundaria (citar solo si aportan; si no, fuera)

| Clave | Fichero | Título / venue | Tier | Uso |
|---|---|---|---|---|
| `GreenABR` | 3524273.3528188 | GreenABR: Energy-Aware ABR with Deep RL — MMSys'22 | A | AMPLITUD (eje energía) |
| `VisualSensitivity` | 3591108 | Visual Sensitivity Aware ABR for DASH via Deep RL — ACM TOMM | B | AMPLITUD |
| `ShortVideoMARL` | 3592473.3592564 | ABR for Short Video via Multi-Agent RL with Expert Guidance — 2023 | B | AMPLITUD |
| `ALVS` | 1-s2.0-S1084804522001035-main | ALVS: Adaptive Live Video Streaming with Deep RL — JNCA 2022 | B | AMPLITUD (live) |
| `EdgeRL` | 1-s2.0-S1084804523000231-main | HAS based on RL with Edge Computing Assistance — JNCA 2023 | B | AMPLITUD |
| `PPO-ABR` | PPO-ABR_Proximal_Policy_Optimization… | PPO-ABR: PPO Deep RL for ABR | C | AMPLITUD |
| `EnhancingBWpred` | Enhancing_Adaptive_Video_Streaming_through_Bandwidth_Prediction… | BW Prediction + Deep RL for ABR | C | AMPLITUD |
| `RLSharjah` | v1_covered | RL-Based Rate Adaptation in Dynamic Video Streaming — Amer. Univ. Sharjah | C | AMPLITUD |
| `MamBRA` | v1_covered_4254418a-… | MamBRA: Session-Level Bandwidth Prediction with Selective State Space Models (Mamba) | B | AMPLITUD (predicción, afín a tu predictor) |
| `MDPIdrl` | applsci-13-11697 | Deep RL Approach for DASH — MDPI Applied Sciences 2023 | C | opcional |
| `AIPdrl` | 075042_1_5.0277381 | Deep RL Enhanced Optimization for ABR — AIP Advances 2025 | C | opcional |

## K. DESCARTAR (duplicados y baja calidad / no usados)

**Duplicados a borrar del disco (mismo paper, distinto nombre — conserva el de la
izquierda):**

| Conservar | Borrar (duplicado) | Ahorro |
|---|---|---|
| `A2BR.pdf` | `Learning_Tailored_Adaptive_Bitrate_Algorithms_..._Approach.pdf` | 2.6 MB |
| `Comyco.pdf` | `1908.02270v1.pdf` | 1.6 MB |
| `SABR.pdf` | `2509.10486v1.pdf` | **18.9 MB** |
| `A review of learning-based methods… .pdf` | `A_Review_of_Learning-Based_Methods… .pdf` **y** `Surveys de 2025.pdf` | 3.5 MB |
| `2023_bothra_veritas… .pdf` | `Veritas.pdf` | 1.5 MB |
| `2015_netravali_mahimahi… .pdf` | `Mahimahi.pdf` | 0.8 MB |
| `2018_raca_4g_lte… .pdf` | `Beyond Throughput a 4G LTE Dataset… .pdf` | 1.2 MB |
| `2020_raca_5g… .pdf` | `Beyond Throughput The Next Generation… 5G… .pdf` | 1.1 MB |

**Cross-folder (mismo paper en las dos carpetas):** `Bentaleb19`, `Stockhammer11`,
`ISO23009` están en ambas. Para NotebookLM, sube **una sola** copia (la de
`para justificar el cliente` para el notebook de cliente; la de `todo lo demás` para
el de estado del arte; no subas las dos al mismo notebook).

**Baja calidad / probablemente no usados (no citar salvo necesidad real):**

| Fichero | Motivo |
|---|---|
| `1-s2.0-S1687850724002206-main.pdf` | "Bit rate selection… in MPEG-DASH" en *Journal of Radiation Research and Applied Sciences* → venue **inadecuado/dudoso**. DESCARTAR. |
| `kaken.nii.ac.jp_20K14740seika.pdf` | Informe de subvención KAKEN (japonés), sin texto extraíble. DESCARTAR. |
| `075042_1_5.0277381.pdf` (AIP Advances), `applsci-13-11697.pdf` (MDPI), `AIRL.pdf` | venues menores; usar solo como cita de barrido si hace falta. |

---

## Resumen para NotebookLM

- **NB_estado_del_arte:** A (surveys/QoE) + `Bentaleb19`/`TimmererReview`/`Seufert15`/
  `PeroniGorinsky25`/`LearningReview25` + familias núcleo (`Pensieve17`, `Yin15`,
  `Huang14`, `Spiteri20`, `Liu11`, `Oboe`) + riesgo (`BayesMPC`,`SafeSABR`,`SODA`).
- **NB_cliente_dash:** `ISO23009`, `Stockhammer11`, `Timmerer12`, `DASH_IF_IOP`,
  RFCs HTTP, docs herramientas (ElementTree/Requests/PyYAML/GPAC/dash.js/Shaka).
- **NB_ia_riesgo:** `Pensieve17`, `Puffer20`, `BayesMPC`, `CausalSim23`, `Hoffman25`,
  `SafeSABR`, `SODA`, `Oboe`, `MamBRA`, `Wei19` (predicción throughput).

**Total identificado:** ~70 papers distintos + estándares/RFC + 3 docs de tooling.
**Para la bibliografía final solo entran los citados de verdad** (núcleo + apoyo). La
columna AMPLITUD es munición para el cap 2; no estás obligado a citarlos todos.
