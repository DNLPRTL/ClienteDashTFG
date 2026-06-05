# Phase 4G - Cierre de NeuralABR-Lite offline

Status: closed_on_ubuntu.

## Decision

Phase 4 queda cerrada con dos modelos offline exportados como bundles de
inferencia CPU:

1. `NeuralABR-Lite robust_mpc`
2. `NeuralABR-Lite teacher_hibrido`

Ambos modelos son `NeuralABR-Lite Candidate Scorer`, entrenados por behavior
cloning, con `qoe_linear_v1`, action space `representation_index`, segmento
primario de `4s` y ladder:

```text
300000, 750000, 1200000, 1850000, 2850000, 4300000 bps
```

No hay controller integrado, benchmark, ranking, ganador, claim de mejora QoE,
claim SOTA ni claim de generalizacion real-world.

## Modelo 1 - robust_mpc

El primer modelo imita al controller real:

```text
core.controller.robust_mpc.RobustMpcController
```

No se usa una replica `robust_mpc-style` separada. Los labels se generan
ejecutando el controller real de Phase 2 dentro del replay offline mediante:

```text
core.neural_abr.hybrid_teacher.ClassicControllerTeacher
```

Rutas Ubuntu:

```text
/home/daniel/TFG/datasets_normalizados/phase4/phase4B_datos_para_entrenamiento
/home/daniel/TFG/modelos/phase4/phase4E_modelo_candidato_neural_abr_lite
/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite
/home/daniel/TFG/runs_trazas/phase4/phase4F_validacion_bundle_inferencia
```

Rutas Windows equivalentes:

```text
C:\Users\danie\Documents\TFG\datasets_normalizados\phase4\phase4B_datos_para_entrenamiento
C:\Users\danie\Documents\TFG\modelos\phase4\phase4E_modelo_candidato_neural_abr_lite
C:\Users\danie\Documents\TFG\modelos\phase4\phase4F_bundle_para_inferencia_neural_abr_lite
C:\Users\danie\Documents\TFG\runs_trazas\phase4\phase4F_validacion_bundle_inferencia
```

Validacion Ubuntu:

```text
training_samples=100050
validation_samples=23700
training_teacher_agreement=0.9158420789605197
validation_teacher_agreement=0.9249367088607595
valid_action_rate=1.0
checkpoint_sha256=f2d8196f9d35d98984dc8ade6b839d01052efb313c4078133a98449601b416ea
bundle_decision=PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G
bundle_p95_latency_ms=0.12679817155003548
bundle_teacher_agreement_report_only=0.9140625
deterministic_rate=1.0
```

## Modelo 2 - teacher_hibrido

El segundo modelo imita una politica experta compuesta. Para cada ventana se
simulan los controllers reales:

```text
rate_based
bba
bola
mpc
robust_mpc
```

La trayectoria ganadora se selecciona por `qoe_linear_v1_mean`; esa seleccion
solo genera labels offline. El modelo no recibe como feature el controller
ganador, QoE futuro, throughput futuro, `trace_id`, `dataset_id`, `split` ni
`leakage_group`.

Rutas Ubuntu:

```text
/home/daniel/TFG/datasets_normalizados/phase4/phase4H_datos_teacher_hibrido_sin_vmaf
/home/daniel/TFG/modelos/phase4/phase4H_modelo_teacher_hibrido_neural_abr_lite
/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite
/home/daniel/TFG/runs_trazas/phase4/phase4H_validacion_bundle_teacher_hibrido
```

Rutas Windows equivalentes:

```text
C:\Users\danie\Documents\TFG\datasets_normalizados\phase4\phase4H_datos_teacher_hibrido_sin_vmaf
C:\Users\danie\Documents\TFG\modelos\phase4\phase4H_modelo_teacher_hibrido_neural_abr_lite
C:\Users\danie\Documents\TFG\modelos\phase4\phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite
C:\Users\danie\Documents\TFG\runs_trazas\phase4\phase4H_validacion_bundle_teacher_hibrido
```

Validacion Ubuntu:

```text
training_samples=100050
validation_samples=23700
winner_counts:
  robust_mpc=2822
  mpc=744
  bba=267
  bola=167
  rate_based=125
training_teacher_agreement=0.9240679660169915
validation_teacher_agreement=0.9326582278481013
valid_action_rate=1.0
checkpoint_sha256=e9fa8f1b463b51f68df703ddfdf8190080df9b0cfdf70753ab139ae85336e744
bundle_decision=PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G
bundle_p95_latency_ms=0.1200730912387371
bundle_teacher_agreement_report_only=0.916015625
deterministic_rate=1.0
```

## Corpus y datos

Phase 4A genero un plan balanceado desde:

```text
/home/daniel/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
```

Salida del plan:

```text
/home/daniel/TFG/manifests_trazas/phase4/phase4A_plan_de_trazas_para_entrenamiento
```

Conteos principales:

```text
candidate_window_count=63301
training_windows=3338
validation_windows=792
unfilled_requested_training_window_count=758
unfilled_requested_validation_window_count=232
```

Las cinco ventanas saltadas en Phase 4B/4H corresponden a trazas sin entregas
positivas o agotadas antes de entregar segmentos pequenos. Se auditan y no se
tratan como fallo del corpus.

## Limitaciones cerradas

- VMAF queda diferido.
- Segmentos `2s` quedan diagnostic-only.
- Los resultados sobre sinteticas deben reportarse separados en futuras fases.
- No se usan dry-runs legacy como training data.
- No se integran controllers IA en Phase 4.
- No se declara que ningun modelo gana a los baselines.
- No se declara mejora QoE hasta una evaluacion formal autorizada.

## Go / No-Go

Decision:

```text
PHASE4G_ACCEPTED_FOR_PHASE5_INTEGRATION
```

Phase 5 puede empezar integrando los dos bundles como controllers IA separados,
con action mask, carga segura, fallback clasico y telemetria diagnostica. La
integracion no debe convertirse todavia en benchmark.
