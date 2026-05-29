# Phase 4E.1 external trace validation report

## Inputs

Dataset:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST
```

Run:

```text
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\external_trace_smoke_TEST
```

Validation output:

```text
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\validation_TEST
```

## Gate table

| gate | result | notes |
|---|---|---|
| external CSV ingestion | PASS | 15 normalized Phase 3 CSV traces loaded. |
| manifest matching | PASS | Matching JSON manifests used for all local smoke traces. |
| missing manifest handling | PASS in unit test | Conservative metadata path tested. |
| split policy | PASS | `phase4e1_trace_level_regime_v1`. |
| trace-level disjointness | PASS | No trace ID appears in multiple splits. |
| leakage-group disjointness | PASS | No leakage group appears in multiple splits. |
| OOD tuning boundary | PASS | OOD marked diagnostic-only and not for tuning. |
| dataset validation | PASS | Dataset validation report status PASS. |
| train-only normalization | PASS | Training fits stats from train samples only. |
| label/action-mask validity | PASS | Labels are valid under action masks. |
| CPU training | PASS | 5 epochs on CPU. |
| offline validation | PASS | Validation and OOD valid action rate = 1.0. |
| no fixed-action collapse | PASS for smoke | Predictions cover all five representations. |
| unit tests | PASS | `python -m unittest discover`: 385 tests OK. |
| readiness | PASS | Strict readiness: 78 OK, 0 WARN, 0 FAIL. |
| generated repo artifacts | PASS | No datasets/checkpoints/logs/JSONL generated inside repo. |

## Offline validation metrics

```json
{
  "validation_metrics": {
    "sample_count": 407,
    "valid_action_rate": 1.0,
    "teacher_agreement": 0.941031941031941,
    "prediction_distribution": {"0": 9, "1": 15, "2": 36, "3": 20, "4": 327}
  },
  "ood_diagnostic_metrics": {
    "sample_count": 427,
    "valid_action_rate": 1.0,
    "teacher_agreement": 0.9133489461358314,
    "prediction_distribution": {"0": 16, "1": 21, "2": 36, "3": 57, "4": 297}
  }
}
```

## Interpretation

The validation supports an external-trace smoke pass. It does not support a benchmark claim or Phase 4F candidate claim.
