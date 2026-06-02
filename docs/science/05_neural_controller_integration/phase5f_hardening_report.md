# Phase 5F hardening report

## Status

Phase 5F implemented fallback/error/telemetry hardening for `neural_abr_lite`.

This report is diagnostic-only. It does not benchmark, rank controllers, retrain, compare against baselines, or claim improvement.

## Files changed

Runtime:

- `core/controller/neural_abr_diagnostics.py`
- `core/controller/neural_abr_lite.py`
- `core/controller/neural_abr_loader.py`
- `core/controller/neural_abr_safety.py`

Tests:

- `tests/test_neural_abr_fault_injection.py`
- `tests/test_neural_abr_hardening.py`
- `tests/test_neural_abr_telemetry_hardening.py`

Docs:

- `docs/science/05_neural_controller_integration/phase5f_scope_and_gate.md`
- `docs/science/05_neural_controller_integration/phase5f_fault_injection_plan.md`
- `docs/science/05_neural_controller_integration/phase5f_error_fallback_matrix.md`
- `docs/science/05_neural_controller_integration/phase5f_telemetry_hardening_matrix.md`
- `docs/science/05_neural_controller_integration/phase5f_hardening_report.md`
- `docs/science/05_neural_controller_integration/phase5f_closure_report.md`
- `docs/science/05_neural_controller_integration/phase5e_closure_report.md`
- `docs/science/05_neural_controller_integration/phase5_remaining_roadmap.md`
- `docs/architecture/telemetry_column_provenance.md`

## Tests added

- `tests.test_neural_abr_fault_injection`
  - Temporary bundle success path.
  - Missing/nonexistent bundle directory.
  - Missing required bundle files.
  - Corrupted manifest.
  - Malformed JSON metadata.
  - Wrong feature schema.
  - Hash mismatch.
  - Architecture mismatch.
  - `torch.load` `TypeError` and `RuntimeError` fail-closed paths.

- `tests.test_neural_abr_hardening`
  - Missing/empty/invalid rates.
  - `max_level` clamp and all-false mask behavior.
  - Missing/out-of-bounds `level`.
  - Missing/non-numeric `queued_time`.
  - Zero download time and missing last-fragment size.
  - Missing fragment duration.
  - Single representation.
  - Forbidden model input fields.
  - Out-of-ladder action.
  - Empty/mismatched scores.
  - Inference exception and timeout.
  - Non-finite safety estimate.
  - Fallback-controller failure.

- `tests.test_neural_abr_telemetry_hardening`
  - Required segment-only diagnostic columns.
  - CSV-safe diagnostic values.
  - Stable fallback reason sanitization.
  - Static runtime source checks for unsafe model-loading patterns.
  - Absence of benchmark/ranking/improvement columns.

## Runtime fixes

- `neural_abr_diagnostics.py`
  - Added stable fallback reason normalization.
  - Unknown reason text maps to `inference_failed`.
  - Diagnostic strings are normalized to avoid embedded newlines.

- `neural_abr_loader.py`
  - Added score-shape validation so empty or action-mask-length-mismatched scorer outputs fail closed.

- `neural_abr_lite.py`
  - Added controller-level score-shape validation for fake/test or alternate runtime engines.
  - Missing feedback `rates` now reports `missing_required_feature`.

- `neural_abr_safety.py`
  - Non-finite estimated download times now request fallback rather than executing an unsafe emergency action.

## Faults covered

- Bundle faults.
- Torch/load faults.
- Runtime feature faults.
- Action mask and selected-action faults.
- Safety guard faults.
- Fallback-controller faults.
- Inference-output faults.
- Diagnostic telemetry faults.

## Remaining limitations

- This is not a QoE benchmark or controller comparison.
- Phase 6 remains the only formal comparative validation phase.
- Runtime inference remains local-only and CPU-first.
- Ubuntu validation is required before full Phase 5F closure.

## Artifact status

- No model artifacts were committed.
- No `.pt`, `.pth`, `.onnx`, `.pkl`, `.joblib`, `.npz`, or `.npy` files were added to Git.
- No run outputs, logs, CSVs, datasets, zips, PDFs, or media files were added to Git.

## Phase 5E optional GStreamer note

Updated. `phase5e_closure_report.md` now records the later user-reported optional Ubuntu/GStreamer structural smoke as passed structural/demo validation only. It is not benchmark evidence.

## Validation summary

```text
git diff --check
PASS

python -m py_compile core/controller/neural_abr_lite.py core/controller/neural_abr_loader.py core/controller/neural_abr_runtime_features.py core/controller/neural_abr_safety.py core/controller/neural_abr_diagnostics.py
PASS

python -m unittest tests.test_neural_abr_registry
PASS - 2 tests

python -m unittest tests.test_neural_abr_model_loading_runtime
PASS - 6 tests

python -m unittest tests.test_neural_abr_runtime_features
PASS - 8 tests

python -m unittest tests.test_neural_abr_safety_fallback
PASS - 6 tests

python -m unittest tests.test_neural_abr_controller
PASS - 8 tests

python -m unittest tests.test_neural_abr_fake_smoke
PASS - 1 test

python -m unittest tests.test_neural_abr_player_telemetry_hook
PASS - 5 tests

python -m unittest tests.test_neural_abr_hardening
PASS - 14 tests

python -m unittest tests.test_neural_abr_fault_injection
PASS - 10 tests

python -m unittest tests.test_neural_abr_telemetry_hardening
PASS - 6 tests

python -m unittest discover
PASS - 471 tests

python scripts\check_client_readiness.py --strict
PASS - 78 OK / 0 WARN / 0 FAIL

Static checks for weights_only=False, torch.hub, URL/request model loading
PASS - no matches in changed runtime files
```
