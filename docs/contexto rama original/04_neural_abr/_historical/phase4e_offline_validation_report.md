# Phase 4E offline validation report

## Input

- Dataset dir: `C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E_synthetic_smoke_20260528_155800`
- Run dir: `C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_20260528_155800`
- Validation output dir: `C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\validation_20260528_155800`

## Gates

| gate | result | notes |
|---|---|---|
| dataset build | PASS | Synthetic diagnostic dataset created outside repository. |
| dataset validation | PASS | `dataset_validation_report.json` status PASS. |
| CPU training smoke | PASS | 3 epochs, batch size 8, seed 123, device CPU. |
| offline validation | PASS | `offline_validation_report.json` status PASS. |
| valid actions | PASS | Validation and OOD valid action rate = 1.0. |
| train-only normalization | PASS | Training produced train-fitted `normalization_stats.json`; validation/OOD used those stats. |
| leakage audit | PASS | `blocked=false`; no future throughput/download time or teacher labels in model inputs. |
| OOD diagnostic present | PASS | OOD diagnostic split reported separately. |
| artifacts outside repo | PASS | Dataset, checkpoint and reports live under `C:\Users\danie\Documents\TFG\_datasets` and `C:\Users\danie\Documents\TFG\_runs`. |
| forbidden repo artifact check | PASS | `git status --porcelain` check found no `.csv`, `.jsonl`, `.pt`, logs, media, cache, or similar generated artifacts in repo status. |
| unit tests | PASS | `python -m unittest discover`: 381 tests OK. |
| readiness strict | PASS | `python scripts/check_client_readiness.py --strict`: 78 OK, 0 WARN, 0 FAIL. |
| collapse diagnostic | WARNING | Predictions were all representation `3`; acceptable for Tier 0 smoke only, not for Phase 4F readiness. |

## Offline Validation Metrics

```json
{
  "validation_metrics": {
    "sample_count": 12,
    "valid_action_rate": 1.0,
    "teacher_agreement": 0.6666666666666666,
    "prediction_distribution": {"3": 12}
  },
  "ood_diagnostic_metrics": {
    "sample_count": 12,
    "valid_action_rate": 1.0,
    "teacher_agreement": 0.75,
    "prediction_distribution": {"3": 12}
  }
}
```

## Decision

```text
PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA
```

This decision is intentionally weaker than `PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F` because no external traces were used and the Tier 0 model showed a fixed-representation prediction pattern.
