# Phase 4D tests and acceptance

## Unit tests

Codex must add tests for:

```text
schema validation
action mask validation
feature construction and forbidden-feature rejection
replay state update
theater action validity
sample generation
train-only normalization
candidate scorer output shape/masking
CLI synthetic smoke
artifact hygiene
```

## Required commands after implementation

```text
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

## Optional local smoke commands

```text
python scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4D_synthetic_smoke --overwrite
python scripts/validate_neural_abr_dataset.py --dataset-dir C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4D_synthetic_smoke
python scripts/train_neural_abr.py --dataset-dir C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4D_synthetic_smoke --output-dir C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\smoke --epochs 1 --batch-size 8 --seed 123 --device cpu --smoke
python scripts/validate_neural_abr_offline.py --dataset-dir C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4D_synthetic_smoke --run-dir C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\smoke --output-dir C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\validation
```

These smokes do not constitute a benchmark.
