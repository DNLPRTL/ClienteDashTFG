# NeuralABR-Lite module plan

## Allowed new package

```text
core/neural_abr/
  __init__.py
  constants.py
  schemas.py
  trace_source.py
  content_ladder.py
  replay_env.py
  features.py
  action_mask.py
  teacher_policy.py
  dataset_builder.py
  normalization.py
  model.py
  training.py
  validation.py
  artifacts.py
```

## Allowed scripts

```text
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
```

Export/inference scripts belong to Phase 4F unless Codex implements only a non-integrated placeholder documented as future work.

## Allowed tests

```text
tests/test_neural_abr_schema.py
tests/test_neural_abr_action_mask.py
tests/test_neural_abr_features.py
tests/test_neural_abr_replay_env.py
tests/test_neural_abr_teacher_policy.py
tests/test_neural_abr_dataset_builder.py
tests/test_neural_abr_normalization.py
tests/test_neural_abr_model.py
tests/test_neural_abr_cli_smoke.py
```

## Forbidden changes

Do not modify these areas unless a test import path requires a harmless package `__init__` only:

```text
core/controller/
player.py
main.py
core/media_engine/
core/downloader.py
core/run_context.py
core/runtime_feedback.py
scripts/run_trace_dry_run.py
scripts/run_qoe_smoke_scenarios.py
```
