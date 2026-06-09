# Indice del corpus ABR IA

Fecha de auditoria inicial: 2026-06-09.

Ruta externa de PDFs:

```text
C:\Users\danie\Documents\TFG\abr ia pdf\abr ia pdf
```

Extraccion temporal usada para lectura local, fuera de Git:

```text
C:\Users\danie\Documents\TFG\auditorias_trazas\phase4_5_v1_pdf_text_tmp
```

La lectura tecnica detallada esta consolidada en:

```text
docs/contexto rama nueva/fase_4_5_v1/matriz_tecnica_detallada.md
```

## Inventario

| # | PDF | Paper identificado | Tipo | Ficha |
|---:|---|---|---|---|
| 1 | `pensievee.pdf` | Neural Adaptive Video Streaming with Pensieve | RL ABR base | `01_pensieve.md` |
| 2 | `1908.02270v1.pdf` | Comyco: Quality-Aware Adaptive Video Streaming via Imitation Learning | imitation learning | `02_comyco.md` |
| 3 | `2020_yan_puffer_learning_in_situ_nsdi.pdf` | Learning in situ / Puffer / Fugu | deployment + predictor | `03_puffer_fugu.md` |
| 4 | `Oboe.pdf` | Oboe: Auto-tuning Video ABR Algorithms to Network Conditions | auto-tuning | `04_oboe.md` |
| 5 | `CausalSim.pdf` | CausalSim: A Causal Framework for Unbiased Trace-Driven Simulation | evaluacion/simulacion | `05_causalsim.md` |
| 6 | `A2BR.pdf` | A2BR / Learning Tailored ABR Algorithms to Heterogeneous Network Conditions | meta-RL | `06_a2br.md` |
| 7 | `Learning_Tailored_...pdf` | A2BR duplicado del PDF anterior | duplicado | `07_a2br_duplicate.md` |
| 8 | `MERINA.pdf` | Improving Generalization via Meta Reinforcement Learning | meta-RL | `08_merina.md` |
| 9 | `MetaABR_...pdf` | MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection | meta-learning | `09_metaabr.md` |
| 10 | `Bitrate_Adaptation_and_Guidance_With_Meta_Reinforcement_Learning.pdf` | Ahaggar bitrate guidance with meta-RL | server/edge guidance | `10_ahaggar_guidance.md` |
| 11 | `ANT.pdf` | Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming | network-dynamics + multi-model | `11_ant.md` |
| 12 | `BETA.pdf` | Spatial-Temporal Learning for Enhancing Generalization | difficult-trace specialization | `12_beta.md` |
| 13 | `EAStream.pdf` | Environment-Aware ABR for Reliable Video Streaming Services | probabilistic context meta-RL | `13_eastream.md` |
| 14 | `Fortuna.pdf` | Offline Reinforcement Learning and Meta-Learning in Diverse Networks | offline meta-RL | `14_fortuna.md` |
| 15 | `2509.10486v1.pdf` | SABR: BC Pretraining and RL Fine-Tuning | BC + PPO | `15_sabr_bc_ppo.md` |
| 16 | `Gelato.pdf` | Practically High Performant Neural Adaptive Video Streaming / Plume / Gelato | trace balancing + RL | `16_gelato_plume.md` |
| 17 | `SODA.pdf` | SODA: Consistent High-Quality Video Streaming | control/smoothness/safety | `17_soda.md` |
| 18 | `3592473.3592564.pdf` | Incendio: Short Video MARL with Expert Guidance | short-video MARL | `18_short_video_incendio.md` |
| 19 | `PPO-ABR_...pdf` | PPO-ABR | PPO RL | `19_ppo_abr.md` |
| 20 | `1-s2.0-S1084804522001035-main.pdf` | ALVS: Adaptive Live Video Streaming using DRL | live + playback speed | `20_alvs_live.md` |
| 21 | `1-s2.0-S1084804523000231-main.pdf` | RL with Edge Computing Assistance | multi-client edge | `21_edge_assisted_rl.md` |
| 22 | `applsci-13-11697.pdf` | DRL-based DASH with quality distance factor | DRL reward shaping | `22_quality_distance_drl.md` |
| 23 | `075042_1_5.0277381.pdf` | Deep RL enhanced optimization / PLL-ABR | PPO + LSTM/local attention | `23_pll_abr.md` |
| 24 | `Enhancing_Adaptive_...Bandwidth_Prediction...pdf` | BPA: Bandwidth Prediction with DRL | BiLSTM + actor-critic | `24_bpa_bandwidth_prediction.md` |
| 25 | `v1_covered_4254418a-5dc6-4da1-be54-5ccdcf966b39.pdf` | MamBRA: Session-Level Bandwidth Prediction using SSM/Mamba | predictor | `25_mambra.md` |
| 26 | `3524273.3528188.pdf` | GreenABR | energy-aware DRL | `26_greenabr.md` |
| 27 | `3591108.pdf` | Visual Sensitivity Aware ABR via DRL | content-aware DRL | `27_visual_sensitivity.md` |
| 28 | `1-s2.0-S1687850724002206-main.pdf` | Bit rate selection with KPCA/GWO/LSSVM | AI optimization/regression | `28_pca_gwo_bp.md` |
| 29 | `v1_covered.pdf` | Reinforcement Learning-Based Rate Adaptation / DQNReg | DQN variant | `29_dqnreg.md` |
| 30 | `A_Review_of_Learning-Based_Methods_for_Adaptive_Video_Streaming_Over_HTTP.pdf` | Review of learning-based methods, 2025 | survey | `30_learning_based_review_2025.md` |
| 31 | `3736306.pdf` | HTTP Adaptive Streaming review, 2025 | survey | `31_has_review_2025.md` |
| 32 | `kaken.nii.ac.jp_20K14740seika.pdf` | Adaptive bitrate control for high-QoE and fair multi-user networks | research report | `32_kaken_fair_multiuser.md` |

## Primer filtrado critico

Mas transferibles a nuestro objetivo inmediato:

- `SODA`, por buffer safety y penalizacion temprana del riesgo.
- `Gelato/Plume`, por balanceo de trazas raras y tail-end traces.
- `SABR`, por BC pretraining + PPO fine-tuning.
- `Fortuna`, por offline RL/meta-learning sobre datos existentes.
- `BETA`, `ANT` y `EAStream`, por generalizacion y deteccion de entorno.
- `Comyco`, por imitation learning eficiente desde experto.
- `Oboe`, por adaptacion de parametros a condiciones de red.
- `CausalSim`, por cautela metodologica al simular con trazas sesgadas.

Transferibles con mas cambios:

- `Incendio`, porque es short-video y mezcla prefetch/video-id/bitrate.
- `ALVS`, porque anade playback speed y baja latencia live.
- `Ahaggar` y edge-assisted RL, porque asumen servidor/edge coordinador.
- `GreenABR` y visual sensitivity, porque requieren seniales de energia o
  contenido que hoy no forman parte del contrato Phase 6.

Menos prioritarios para Fase 4-5 v1:

- papers que solo cambian el algoritmo DRL base sin resolver safety ni
  generalizacion;
- predictors sin capa ABR segura;
- surveys, que sirven para memoria y matriz de decision, no como controller.
