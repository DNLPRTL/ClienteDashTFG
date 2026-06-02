# Phase 5D Codex implementation prompt

```text
Repo: DashClientModular4
Branch: main

Expected starting state:
- HEAD must be the Phase 5C closure commit for "docs(neural-abr): finalize Phase 5C implementation specs", or later only if commits are documentation-only and already validated.
- Phase 5A0/A1/A2/B/C documentation is complete.
- Working tree must be clean before starting.

Phase:
Phase 5 - NeuralABR-Lite controller integration.

Block:
Phase 5D - guarded NeuralABR-Lite controller implementation.

Block type:
Runtime implementation with tests.
No benchmark.
No ranking.
No retraining.
No model artifacts in Git.

Mission:
Implement NeuralABR-Lite as a guarded neural scorer controller in DashClientModular4.

Required design:
- Controller key: neural_abr_lite.
- Class: NeuralAbrLiteController.
- Compatible with BaseController.
- Uses setPlayerFeedback, calcControlAction, quantizeRate, getControlAction.
- Returns a rate in bytes per second from feedback["rates"].
- Never returns arbitrary bitrate outside the current ladder.
- Uses dict-based feedback.
- Does not require GStreamer.
- Passes fake-engine smoke before real playback.
- Remains diagnostic-only in Phase 5.

Allowed implementation files:
- core/controller/neural_abr_lite.py
- core/controller/neural_abr_loader.py
- core/controller/neural_abr_runtime_features.py
- core/controller/neural_abr_safety.py
- core/controller/neural_abr_diagnostics.py
- core/controller/registry.py
- player.py only for a generic optional post-decision diagnostic hook if needed
- config/client.example.yaml only for disabled/documented example params if approved
- core/dataset_schema.py only if static diagnostic columns are strictly required; prefer dynamic feedback-key header through augment_feedback
- docs/architecture/telemetry_column_provenance.md only if CSV columns are added

Allowed tests:
- tests/test_neural_abr_controller.py
- tests/test_neural_abr_runtime_features.py
- tests/test_neural_abr_safety_fallback.py
- tests/test_neural_abr_model_loading_runtime.py
- tests/test_neural_abr_registry.py
- tests/test_neural_abr_fake_smoke.py if it uses a temp synthetic bundle and local MPD only
- Updates to existing registry/feedback/telemetry tests only if required by the implementation

Forbidden:
- Do not modify main.py.
- Do not modify core/media_engine/.
- Do not modify core/client_config.py unless a later reviewed spec explicitly allows it.
- Do not modify core/neural_abr/inference.py to make runtime loading work.
- Do not reuse core/neural_abr/inference.py as the runtime loader.
- Do not create or modify training/replay/export code except through tests that build temporary fixtures.
- Do not add PDFs.
- Do not add .pt, .pth, .onnx, .pkl, .joblib, .npz, .npy.
- Do not add logs, CSVs, datasets, run outputs, zips or checkpoints.
- Do not benchmark.
- Do not rank controllers.
- Do not claim improvement.
- Do not retrain.
- Do not add online learning.
- Do not use future throughput, future download time, future rebuffer, teacher labels, trace ids, split labels, benchmark data or controller identity as runtime model inputs.

Critical security:
- Runtime must not use weights_only=False.
- Runtime must not use plain torch.load(path, map_location="cpu") fallback.
- Runtime must not use torch.hub, URL loading or automatic downloads.
- Runtime must call torch.load(model_state_path, map_location="cpu", weights_only=True).
- If weights_only is unsupported or loading fails, fail closed and fallback.

Required runtime flow:
1. Receive feedback through setPlayerFeedback.
2. Build online-only runtime context and candidate features.
3. Validate bundle manifest, hashes and schemas before model load.
4. Load local state_dict on CPU with weights_only=True.
5. Apply train-only normalization.
6. Build action mask from feedback["rates"] and max_level.
7. Score valid candidate representations on CPU under model.eval() and torch.no_grad().
8. Select raw_action with action mask.
9. Validate raw_action and finite scores.
10. Run safety guard.
11. Preserve safe raw_action or downshift to highest lower feasible action.
12. Fallback if unsafe, invalid or failed.
13. Return feedback["rates"][safe_action].
14. Emit diagnostic-only telemetry.

Fallback chain:
1. robust_mpc
2. mpc
3. rate_based
4. bba
5. min_rate
6. lowest valid representation

Required diagnostic fields:
- neural_enabled
- neural_bundle_configured
- neural_bundle_loaded
- neural_bundle_schema_ok
- neural_bundle_hash_ok
- neural_feature_schema_ok
- neural_feature_vector_ok
- neural_missing_features
- neural_action_mask_valid_count
- neural_raw_action
- neural_raw_rate_Bps
- neural_safe_action
- neural_safe_rate_Bps
- neural_safety_intervened
- neural_fallback_used
- neural_fallback_reason
- neural_inference_ms
- neural_nan_inf_detected
- neural_invalid_action_detected
- neural_diagnostic_only

Tests to implement:
- no bundle -> neural disabled and fallback
- invalid bundle path -> fallback
- missing manifest -> fallback
- hash mismatch -> fallback
- schema mismatch -> fallback
- unsupported safe torch load -> fallback and no weights_only=False
- single representation -> only representation returned
- variable ladder -> never selects outside current max_level
- all-false/invalid action mask -> fallback
- NaN/Inf score -> fallback
- selected masked action -> fallback
- missing required feature -> fallback
- deterministic inference for same input and bundle
- returned rate is from feedback["rates"]
- robust_mpc fallback when neural disabled and signals available
- emergency lowest representation if fallbacks fail
- registry creates key neural_abr_lite
- config params pass through
- telemetry hook populates diagnostic fields if implemented
- fake engine smoke with synthetic temp bundle and local MPD only
- no model artifacts committed

Validation commands:
- git status --short --branch
- git diff --check
- python -m unittest discover
- python scripts/check_client_readiness.py --strict

Expected validation:
- Tests pass.
- Readiness strict passes.
- No model artifacts in Git.
- No benchmark output.
- No ranking or improvement claims.

Staging:
Do not use git add .
Stage only intended implementation, tests and required docs:
git add core/controller/neural_abr_lite.py core/controller/neural_abr_loader.py core/controller/neural_abr_runtime_features.py core/controller/neural_abr_safety.py core/controller/neural_abr_diagnostics.py core/controller/registry.py tests/test_neural_abr_controller.py tests/test_neural_abr_runtime_features.py tests/test_neural_abr_safety_fallback.py tests/test_neural_abr_model_loading_runtime.py tests/test_neural_abr_registry.py
Only add player.py, config/client.example.yaml, core/dataset_schema.py, docs/architecture/telemetry_column_provenance.md, or tests/test_neural_abr_fake_smoke.py if they were actually changed and approved by the Phase 5C specs.

Commit message:
feat(neural-abr): integrate guarded NeuralABR-Lite controller

Final report:
- files changed
- implementation summary
- security confirmation: no weights_only=False runtime
- fallback behavior
- telemetry hook status
- validation results
- git status
- commit hash if committed
```
