# Phase 4E training smoke report

## Run status

- Status: PASS for Tier 0 synthetic smoke.
- Decision: `PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA`
- Date/time: 2026-05-28 15:58:00 Europe/Madrid.
- Repository branch: `main`
- Repository commit at run start: `109ced8` with uncommitted Phase 4E docs.
- Python version: 3.12.8
- PyTorch version: 2.6.0+cpu
- Device: CPU
- Seed: 123
- Code fixes during Phase 4E: none required.

## Commands Executed

```powershell
$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$DatasetDir = "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E_synthetic_smoke_$Stamp"
$RunDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_$Stamp"
$ValidationDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\validation_$Stamp"

New-Item -ItemType Directory -Path $DatasetDir -Force | Out-Null
New-Item -ItemType Directory -Path $RunDir -Force | Out-Null
New-Item -ItemType Directory -Path $ValidationDir -Force | Out-Null

python scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir $DatasetDir --overwrite
python scripts/validate_neural_abr_dataset.py --dataset-dir $DatasetDir
python scripts/train_neural_abr.py --dataset-dir $DatasetDir --output-dir $RunDir --epochs 3 --batch-size 8 --seed 123 --device cpu --smoke
python scripts/validate_neural_abr_offline.py --dataset-dir $DatasetDir --run-dir $RunDir --output-dir $ValidationDir
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

The executed shell also printed the resolved timestamped paths after the required commands:

```text
PHASE4E_STAMP=20260528_155800
PHASE4E_DATASET_DIR=C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E_synthetic_smoke_20260528_155800
PHASE4E_RUN_DIR=C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_20260528_155800
PHASE4E_VALIDATION_DIR=C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\validation_20260528_155800
```

## Artifact Paths

- Dataset dir: `C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E_synthetic_smoke_20260528_155800`
- Run dir: `C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_20260528_155800`
- Validation dir: `C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\validation_20260528_155800`

All generated dataset, JSONL, checkpoint and validation artifacts are outside the repository.

## Dataset Summary

| split | traces | samples | teacher label distribution |
|---|---:|---:|---|
| train | 2 | 24 | `{"0": 2, "1": 2, "2": 2, "3": 18}` |
| validation | 1 | 12 | `{"0": 1, "1": 1, "2": 2, "3": 8}` |
| ood_diagnostic | 1 | 12 | `{"0": 2, "1": 1, "3": 9}` |

Dataset validation status: PASS.

Leakage audit status: PASS, `blocked=false`.

## Training Summary

| field | value |
|---|---|
| model | NeuralABR-Lite Candidate Scorer |
| training family | behavior cloning / imitation learning |
| loss | masked cross entropy over valid candidate scores |
| optimizer | Adam |
| epochs | 3 |
| batch size | 8 |
| seed | 123 |
| device | CPU |
| final loss | 1.3416582345962524 |
| mean loss | 1.3560392591688368 |
| checkpoint | `C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_20260528_155800\checkpoint.pt` |

Training smoke status: PASS.

## Validation Summary

| split | valid action rate | teacher agreement | prediction distribution |
|---|---:|---:|---|
| train | 1.0 | 0.75 | `{"3": 24}` |
| validation | 1.0 | 0.6666666666666666 | `{"3": 12}` |
| ood_diagnostic | 1.0 | 0.75 | `{"3": 12}` |

The action-validity gate passed. The prediction distribution collapsed to representation `3` in this tiny synthetic Tier 0 run. This does not fail Tier 0, but it blocks any stronger offline-candidate interpretation.

## Interpretation

This is a synthetic pipeline smoke only. It proves that dataset build, validation, CPU training, offline validation, unit tests and readiness can run end to end without repository artifacts or client integration. It does not prove model quality, benchmark performance, real-world behavior, or readiness for Phase 4F.
