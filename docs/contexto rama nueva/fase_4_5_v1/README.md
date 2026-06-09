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
