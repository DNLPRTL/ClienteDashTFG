# Phase 4D test report

Status: PASS for Phase 4D offline pipeline smoke.

## Commands run

```powershell
python -m unittest tests.test_neural_abr_schema tests.test_neural_abr_action_mask tests.test_neural_abr_features tests.test_neural_abr_replay_env tests.test_neural_abr_teacher_policy tests.test_neural_abr_dataset_builder tests.test_neural_abr_normalization tests.test_neural_abr_model tests.test_neural_abr_cli_smoke
```

Result: 20 tests, OK.

```powershell
python -m unittest discover
```

Result: 381 tests, OK.

```powershell
python scripts/check_client_readiness.py --strict
```

Result: PASS, 78 OK, 0 WARN, 0 FAIL.

## Requested synthetic smoke

Commands run with local-only output directories outside the repo:

```powershell
$DatasetDir = "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4D_synthetic_smoke"
$RunDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\smoke"
$ValidationDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\validation"

python scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir $DatasetDir --overwrite
python scripts/validate_neural_abr_dataset.py --dataset-dir $DatasetDir
python scripts/train_neural_abr.py --dataset-dir $DatasetDir --output-dir $RunDir --epochs 1 --batch-size 8 --seed 123 --device cpu --smoke
python scripts/validate_neural_abr_offline.py --dataset-dir $DatasetDir --run-dir $RunDir --output-dir $ValidationDir
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

## Smoke outputs

Dataset sample counts:

```json
{"train": 24, "validation": 12, "ood_diagnostic": 12}
```

Dataset validation: PASS.

Training smoke:

```json
{
  "device": "cpu",
  "loss_last": 1.3737677335739136,
  "validation_valid_action_rate": 1.0,
  "validation_teacher_agreement": 0.75
}
```

Offline validation:

```json
{
  "validation_valid_action_rate": 1.0,
  "validation_teacher_agreement": 0.75,
  "ood_valid_action_rate": 1.0,
  "ood_teacher_agreement": 0.6666666666666666
}
```

These are sanity metrics only. They are not a benchmark, ranking, or real-world validation.

## Artifact paths

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4D_synthetic_smoke
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\smoke
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\validation
```

## Readiness

Client readiness remains PASS. No client/runtime/controller integration was introduced.
