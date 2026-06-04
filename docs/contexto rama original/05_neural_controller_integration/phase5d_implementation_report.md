﻿# Phase 5D implementation report

## Scope

Phase 5D implements the guarded NeuralABR-Lite scorer controller for structural integration only. It does not benchmark, rank controllers, retrain, compare against baselines, or claim improvement.

## Files created

- `core/controller/neural_abr_diagnostics.py`
- `core/controller/neural_abr_loader.py`
- `core/controller/neural_abr_runtime_features.py`
- `core/controller/neural_abr_safety.py`
- `core/controller/neural_abr_lite.py`
- `tests/test_neural_abr_registry.py`
- `tests/test_neural_abr_model_loading_runtime.py`
- `tests/test_neural_abr_runtime_features.py`
- `tests/test_neural_abr_safety_fallback.py`
- `tests/test_neural_abr_controller.py`
- `tests/test_neural_abr_player_telemetry_hook.py`
- `tests/test_neural_abr_fake_smoke.py`

## Files modified

- `core/controller/registry.py`
- `player.py`
- `config/client.example.yaml`
- `docs/architecture/telemetry_column_provenance.md`
- `docs/science/05_neural_controller_integration/_historical/phase5_remaining_roadmap.md`

## Controller registration

`neural_abr_lite` is registered in `core/controller/registry.py` as `NeuralABR-Lite guarded scorer controller`. Creating the controller with no params succeeds and falls back when no bundle is configured.

## Safe loader behavior

`core/controller/neural_abr_loader.py` validates a local bundle directory, required files, manifest metadata, hashes, feature schema, normalization stats, ladder schema, inference contract, fallback policy, and model config.

PyTorch and `NeuralAbrLiteCandidateScorer` are imported lazily only when a configured bundle is loaded. Runtime loading instantiates the local architecture and calls `torch.load(model_state_path, map_location="cpu", weights_only=True)`. If `weights_only` is unavailable, runtime fails closed. There is no unsafe retry.

## Runtime features and action mask

`core/controller/neural_abr_runtime_features.py` builds context and candidate features only from current controller feedback and previous completed downloads. Ladder rates remain bytes per second in the controller API and are converted to bits per second only for model features. Estimated candidate chunk size is marked unavailable unless an explicit pre-decision size is present.

The action mask length matches the current ladder, respects `max_level`, rejects invalid rates, and requires at least one valid action.

## Safety and fallback

`core/controller/neural_abr_safety.py` preserves safe raw actions, downshifts unsafe actions to the highest lower feasible representation, and uses an emergency lowest representation if no feasible action remains. Missing or invalid safety signals request fallback instead of guessing.

Fallback is local and registry-independent. The supported order is `robust_mpc`, `mpc`, `rate_based`, `bba`, `min_rate`, then lowest valid representation.

## Telemetry

Neural diagnostics are diagnostic-only. `NeuralAbrLiteController.augment_feedback()` adds stable feedback keys before CSV header creation. `player.py` adds a generic optional post-decision hook that copies values from `get_last_decision_telemetry()` only into columns that already exist.

`evaluation_segments.csv` is unchanged and receives no neural diagnostic fields.

## Tests added

The new tests cover registry import safety, safe runtime loading, safe-load failure, missing/tampered bundles, runtime feature mapping, action mask rules, safety guard behavior, fallback behavior, controller fail-closed paths, player telemetry plumbing, and fake-engine structural smoke with a temporary local bundle.

## Non-goals

- No benchmark.
- No controller ranking.
- No baseline comparison mode.
- No Phase 6 validation script.
- No retraining.
- No training pipeline changes.
- No model artifacts committed.
- No run outputs, logs, CSVs, datasets, checkpoints, zips, PDFs, `.pt`, `.pth`, `.onnx`, `.pkl`, `.joblib`, `.npz`, or `.npy` files added to Git.
