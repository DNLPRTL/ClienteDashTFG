# Phase 5F telemetry hardening matrix

## Boundary

All `feedback_neural_*` fields are diagnostic-only structural telemetry. They may appear in `segment_telemetry.csv` when `neural_abr_lite` is selected. They must not appear in `evaluation_segments.csv`.

These fields are not QoE metrics, not ranking inputs, not improvement evidence, not retraining labels, and not Phase 6 comparative validation outputs.

## Required fields

| Field | Source | May appear in `segment_telemetry.csv`? | May appear in `evaluation_segments.csv`? | Diagnostic-only? |
| --- | --- | --- | --- | --- |
| `feedback_neural_enabled` | `augment_feedback()` base state and `get_last_decision_telemetry()` | Yes | No | Yes |
| `feedback_neural_bundle_configured` | `augment_feedback()` base state and bundle config flag | Yes | No | Yes |
| `feedback_neural_bundle_loaded` | Runtime loader state | Yes | No | Yes |
| `feedback_neural_bundle_schema_ok` | Runtime bundle validation result | Yes | No | Yes |
| `feedback_neural_bundle_hash_ok` | Runtime hash validation result | Yes | No | Yes |
| `feedback_neural_feature_schema_ok` | Runtime feature schema validation result | Yes | No | Yes |
| `feedback_neural_feature_vector_ok` | Runtime feature construction result | Yes | No | Yes |
| `feedback_neural_missing_features` | Runtime feature error metadata | Yes | No | Yes |
| `feedback_neural_action_mask_valid_count` | Runtime action mask | Yes | No | Yes |
| `feedback_neural_raw_action` | Raw scorer action before safety guard | Yes | No | Yes |
| `feedback_neural_raw_rate_Bps` | Raw scorer action mapped to ladder rate | Yes | No | Yes |
| `feedback_neural_safe_action` | Executed action after safety/fallback | Yes | No | Yes |
| `feedback_neural_safe_rate_Bps` | Executed ladder rate after safety/fallback | Yes | No | Yes |
| `feedback_neural_safety_intervened` | Safety guard decision | Yes | No | Yes |
| `feedback_neural_fallback_used` | Controller fallback path flag | Yes | No | Yes |
| `feedback_neural_fallback_reason` | Stable fallback reason label | Yes | No | Yes |
| `feedback_neural_inference_ms` | Local CPU inference timing | Yes | No | Yes |
| `feedback_neural_nan_inf_detected` | Non-finite score detection | Yes | No | Yes |
| `feedback_neural_invalid_action_detected` | Masked/out-of-ladder action detection | Yes | No | Yes |
| `feedback_neural_diagnostic_only` | Explicit diagnostic-only marker | Yes | No | Yes |

## Hardening expectations

- The player copies post-decision telemetry only into columns that already exist in the row header.
- Hook exceptions are swallowed defensively and do not crash non-neural or neural runs.
- `neural_fallback_reason` is stable and enum-like; unknown text is normalized to `inference_failed`.
- Diagnostic strings are newline-safe before CSV writing.
- Existing non-neural controllers do not gain `feedback_neural_*` columns unless they explicitly augment feedback with those keys.
- `evaluation_segments.csv` remains free of neural diagnostic fields.
- No benchmark/ranking/improvement columns are added.
