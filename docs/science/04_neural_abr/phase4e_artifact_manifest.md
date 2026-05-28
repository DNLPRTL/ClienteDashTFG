# Phase 4E artifact manifest

## Run Identity

- Phase: 4E Tier 0 synthetic smoke
- Stamp: `20260528_155800`
- Decision: `PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA`
- Artifact policy: external-only, no generated datasets/checkpoints/logs in repository.

## Dataset Directory

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E_synthetic_smoke_20260528_155800
```

| file | size bytes | purpose |
|---|---:|---|
| `dataset_manifest.json` | 1603 | Dataset schema, split and ladder manifest. |
| `dataset_validation_report.json` | 894 | Dataset validation summary. |
| `feature_schema.json` | 3624 | Context/candidate feature schema. |
| `label_schema.json` | 760 | Teacher label schema. |
| `leakage_audit.json` | 767 | Leakage gate audit. |
| `train.jsonl` | 56879 | Synthetic train samples. |
| `validation.jsonl` | 28639 | Synthetic validation samples. |
| `ood_diagnostic.jsonl` | 28938 | Synthetic OOD diagnostic samples. |

## Training Run Directory

```text
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_20260528_155800
```

| file | size bytes | purpose |
|---|---:|---|
| `checkpoint.pt` | 8486 | CPU PyTorch smoke checkpoint. |
| `model_config.json` | 261 | Small shared MLP config. |
| `normalization_stats.json` | 2069 | Train-only normalization stats. |
| `training_report.json` | 1087 | Training smoke report. |

## Offline Validation Directory

```text
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\validation_20260528_155800
```

| file | size bytes | purpose |
|---|---:|---|
| `offline_validation_report.json` | 619 | Offline sanity validation report. |

## Repository Artifact Check

The forbidden artifact check passed:

```powershell
$Forbidden = git status --porcelain | Where-Object { $_ -match "\.pdf$|\.zip$|\.csv$|\.log$|\.mp4$|\.m4s$|\.ts$|__pycache__|\.pyc|\.venv|\.idea|\.htm$|\.html$|\.pt$|\.pth$|\.onnx$|\.ckpt$|events\.out|\.npy$|\.npz$|\.pkl$|\.joblib$" }
```

Result: PASS, no forbidden generated artifacts in repository status.
