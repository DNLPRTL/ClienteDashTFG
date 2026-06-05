# Phase 5 - Cierre

Status: closed_on_ubuntu.

## Implementado

- Dos controllers registrados:
  - `neural_abr_lite_robust_mpc`
  - `neural_abr_lite_teacher_hibrido`
- Runtime comun con guarded neural scorer.
- Loader seguro de bundles Phase 4 con `weights_only=True`.
- Validacion de hashes, schema, feature schema y teacher esperado.
- Feature builder online sin metadata de traza ni futuro throughput.
- Action mask, safety guard y fallback clasico.
- Telemetria `feedback_neural_*` solo en `segment_telemetry.csv`.
- Tests unitarios y smoke fake con bundle temporal.

## Validacion Ubuntu cliente

Ubuntu cliente ejecuto:

```text
git pull --ff-only origin rebuild/phase3-from-phase2
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

Resultado:

```text
333 tests OK
87 OK / 0 WARN / 0 FAIL
```

Tambien ejecuto smokes estructurales con los dos bundles reales:

```text
/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite
/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite
```

Runs aceptados:

```text
/home/daniel/TFG/runs_trazas/phase5/smoke_neural_robust_mpc/run_20260605_143034
/home/daniel/TFG/runs_trazas/phase5/smoke_neural_teacher_hibrido/run_20260605_143136
```

Resultado observado en ambos:

```text
status=completed
segment_telemetry.csv existe
evaluation_segments.csv existe
dataset.csv ausente
dataset_training.csv ausente
feedback_neural_* presente solo en segment_telemetry.csv
feedback_neural_bundle_loaded incluye 1
feedback_neural_fallback_used=0
feedback_neural_fallback_reason incluye success_neural
feedback_neural_diagnostic_only=1
```

La red usada fue la red rapida de adaptador puente. Esto no contamina Phase 5,
porque el objetivo era validar integracion tecnica con bundles reales. No debe
usarse para comparacion de QoE, ranking ni conclusiones de rendimiento.

## No realizado

- benchmark;
- ranking;
- ganador;
- comparacion QoE formal;
- claim de mejora;
- entrenamiento nuevo.

## Decision

```text
PHASE5_ACCEPTED_AS_TWO_GUARDED_NEURAL_CONTROLLERS_INTEGRATED
```
