# Phase 5C file change plan for Phase 5D

## Recommended new files in Phase 5D

```text
core/controller/neural_abr_lite.py
core/controller/neural_abr_loader.py
core/controller/neural_abr_runtime_features.py
core/controller/neural_abr_safety.py
core/controller/neural_abr_diagnostics.py
```

## Recommended modified files in Phase 5D

| File | Phase 5D purpose | Phase 5C status |
|---|---|---|
| `core/controller/registry.py` | Register `neural_abr_lite`. | Not modified in Phase 5C. |
| `config/client.example.yaml` | Add disabled/example-only params if approved. | Not modified in Phase 5C. |
| `player.py` | Add generic optional post-decision diagnostic hook if approved. | Not modified in Phase 5C. |
| `core/dataset_schema.py` | Add static diagnostic columns only if dynamic feedback-key telemetry is insufficient. | Not modified in Phase 5C; prefer no change. |
| `docs/architecture/telemetry_column_provenance.md` | Document any new CSV columns if player/schema telemetry changes. | Not modified in Phase 5C. |

## Recommended tests in Phase 5D

```text
tests/test_neural_abr_controller.py
tests/test_neural_abr_runtime_features.py
tests/test_neural_abr_safety_fallback.py
tests/test_neural_abr_model_loading_runtime.py
tests/test_neural_abr_registry.py
tests/test_neural_abr_fake_smoke.py
```

`tests/test_neural_abr_fake_smoke.py` should exist only if the fake smoke can use a synthetic temporary bundle and local MPD without external network and without committed model artifacts.

## Phase 5C rule

Phase 5C creates none of these implementation or test files.
