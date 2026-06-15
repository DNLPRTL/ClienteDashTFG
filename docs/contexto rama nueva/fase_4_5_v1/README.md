# Fase 4-5 v1 - Iteracion nueva IA ABR

## Estado

Fase 4-5 v1 queda abierta como una iteracion nueva para disenar, entrenar e
integrar controllers IA ABR propios mas defendibles.

Esta fase no sustituye a las Phase 4 y Phase 5 cerradas. Los controllers
anteriores (`neural_abr_lite_robust_mpc` y
`neural_abr_lite_teacher_hibrido`) siguen existiendo como historia, runtime y
comparadores, pero no son el punto de partida obligatorio del nuevo diseno.

El rastro documental antiguo de esta carpeta se considera descartado. No se
debe restaurar ni continuar un plan previo. Antes de elegir modelo, arquitectura
o dataset derivado hay que leer el corpus nuevo de papers en Markdown.

## Fuente canonica de papers

El corpus operativo nuevo esta en:

```text
docs/contexto rama nueva/fase_4_5_v1/abr ia md/
```

Estos `.md` son la fuente de trabajo para Codex. Los PDF originales siguen
siendo fuente de verdad para formulas, tablas y figuras cuando la extraccion
textual pierda layout, pero no se debe implementar directamente desde PDFs
brutos si ya existe un `.md` operativo.

## Corpus disponible

La carpeta contiene 32 `.md` operativos:

```text
01_comyco_2019_imitation_learning.md
02_puffer_fugu_2020_learning_in_situ.md
03_sabr_2025_bc_rl_finetuning.md
04_pll_abr_2025_ppo_lstm_attention.md
05_greenabr_2022_energy_aware_drl.md
06_alvs_2022_live_video_drl.md
07_edge_rl_adaptive_streaming_2023.md
08_pca_gwo_bp_mpeg_dash_ai_bitrate_selection.md
09_a2br_2022_meta_rl_domain_priors.md
10_ant_2024_network_dynamics_dedicated_models.md
11_souane_2023_drl_dash.md
12_beta_2025_spatial_temporal_generalization.md
13_visual_sensitivity_aware_drl_abr.md
14_incendio_sabr_marl_expert_guidance.md
15_http_adaptive_streaming_review_2025.md
16_learning_based_methods_has_review_2025.md
17_bpa_bandwidth_prediction_drl_abr.md
18_fortuna_2025_offline_meta_rl_diverse_networks.md
19_gelato_plume_2024_trace_skew_neural_abr.md
20_kaken_20k14740_fair_high_qoe_multiuser_abr_report.md
21_a2br_learning_tailored_abr_domain_priors_meta_rl.md
22_ahaggar_bitrate_guidance_meta_rl_cmcd_cmsd.md
23_causalsim_2023_unbiased_trace_driven_simulation.md
24_eastream_2026_environment_aware_abr_meta_rl_vae.md
25_ppo_abr_2023_proximal_policy_optimization_drl.md
26_soda_2024_consistent_high_quality_non_neural_abr.md
27_dqnreg_2022_reinforcement_learning_rate_adaptation.md
28_mambra_2026_session_bandwidth_prediction_ssm_mamba.md
29_merina_2022_meta_rl_generalization_neural_abr.md
30_metaabr_2024_meta_learning_adaptive_bitrate_selection.md
31_oboe_2018_auto_tuning_abr_network_conditions.md
32_pensieve_2017_neural_adaptive_video_streaming.md
```

## Reglas de decision

- No hay decision de modelo tomada al iniciar esta fase.
- No reutilizar por inercia el diseno `NeuralABR-Lite`.
- No entrenar todavia sin una spec escrita de dataset, simulador, state, action,
  reward/loss, arquitectura, bundle, telemetria y acceptance tests.
- No mezclar resultados sinteticos con conclusiones principales sobre trazas
  reales.
- No llamar benchmark a entrenamiento offline, smokes, dry-runs ni auditorias.
- No declarar ganador, mejora QoE ni generalizacion antes de Phase 6 autorizada.

## Entorno de entrenamiento disponible

Hay WSL2 Ubuntu con ROCm/PyTorch y GPU AMD disponible para entrenamientos largos.
La nota operativa esta en:

```text
docs/contexto rama nueva/fase_4_5_v1/wsl_rocm_gpu_context.md
```

Resumen de responsabilidades:

- Windows fisico: desarrollo, tests rapidos, commits y push.
- WSL2 Ubuntu/ROCm: entrenamiento IA pesado y artefactos externos bajo `~/TFG`.
- Ubuntu cliente: validacion real y Phase 6.
- Ubuntu servidor: MPD, segmentos e inicializaciones DASH.

## Siguiente paso real

El siguiente bloque no es implementar. Es leer el corpus nuevo y producir una
decision tecnica de Fase 4-5 v1 que convierta los papers en uno o varios planes
implementables para DashClientModular4.

Cada plan candidato debe explicar:

- tipo de IA;
- entrenamiento previsto;
- dataset derivado necesario;
- compatibilidad con el cliente y Phase 6;
- coste computacional;
- riesgos de leakage;
- telemetria de inferencia;
- acceptance tests;
- por que es defendible academicamente.

## Decision tecnica inicial

La lectura del corpus y la primera decision de modelos quedan documentadas en:

```text
docs/contexto rama nueva/fase_4_5_v1/decision_tecnica_modelos_v1.md
```

Decision de arranque:

- construir primero `spc_abr_v1`, predictor neural + planner ABR seguro;
- construir tambien `spbc_abr_v1`, policy por behavioral cloning desde oracle
  offline;
- dejar `spbc_ppo_abr_v1` como fine-tuning condicionado a gates;
- no empezar por meta-RL, Mamba, MARL, edge, energia ni VMAF.

## Bloque 1-3 implementado: dataset derivado

El primer bloque operativo de Fase 4-5 v1 queda documentado en:

```text
docs/contexto rama nueva/fase_4_5_v1/runbook_phase45_v1_dataset_wsl.md
```

Este bloque implementa solo:

1. generador offline de dataset `phase45_v1`;
2. sincronizacion manual de datasets/manifests a WSL2;
3. generacion validada del dataset derivado.

No entrena modelos, no exporta bundles, no integra controllers y no ejecuta
Phase 6.

Script principal:

```text
scripts/build_phase45_v1_dataset.py
```

Salidas externas previstas:

```text
~/TFG/datasets_normalizados/phase45_v1/phase45v1B_spc_spbc_dataset_v1/
```

El dataset contiene targets para:

- `spc_abr_v1`: prediccion de capacidad futura y riesgo de rebuffer;
- `spbc_abr_v1`: behavioral cloning desde `oracle_qoe_beam_v1`.

Los controllers clasicos reales se consultan como auditoria, no como profesor
principal.

## Bloque 4 implementado: entrenamiento `spc_abr_v1`

El runbook operativo de entrenamiento queda en:

```text
docs/contexto rama nueva/fase_4_5_v1/runbook_phase45_v1_spc_training_wsl.md
```

Este bloque entrena solo el predictor `spc_abr_v1` sobre el dataset derivado
`phase45_v1`.

No exporta bundle, no registra controller, no ejecuta Phase 6 y no declara
mejora.

Script principal:

```text
scripts/train_phase45_v1_spc_abr.py
```

Salidas externas previstas:

```text
~/TFG/modelos/phase45_v1/spc_abr_v1/<profile>/
```

## Decision Phase45 v3: Neural Throughput-Calibrated MPC

Tras el bloqueo del `phase45_v3_qh_scorer` como controller directo, la nueva
linea principal queda documentada en:

```text
docs/contexto rama nueva/fase_4_5_v1/decision_phase45_v3_neural_throughput_calibrated_mpc_v1_20260612.md
```

Decision:

- parar `Q_H scorer` como driver principal;
- conservarlo como diagnostico/ablacion;
- abrir `phase45_v3_neural_throughput_calibrated_mpc_v1`;
- entrenar un predictor de cuantiles de throughput futuro;
- decidir acciones con un planner MPC explicito sobre `qoe_linear_v1`;
- evaluar primero en closed-loop offline diagnostico, sin benchmark ni ranking.

El siguiente diagnostico ampliado queda documentado en:

```text
docs/contexto rama nueva/fase_4_5_v1/decision_phase45_v3_neural_mpc_expanded_diagnostic_20260615.md
```

Este runbook aumenta cobertura diagnostica con varias seeds y mas ventanas. No
convierte el resultado en benchmark, ranking, ganador ni claim de mejora QoE.

Tras superar el diagnostico ampliado, la preparacion de candidato IA
experimental queda documentada en:

```text
docs/contexto rama nueva/fase_4_5_v1/decision_phase45_v3_neural_mpc_experimental_candidate_20260615.md
```

Este bloque solo prepara readiness reproducible del candidato. No crea bundle,
no integra runtime y no autoriza comparacion formal.
