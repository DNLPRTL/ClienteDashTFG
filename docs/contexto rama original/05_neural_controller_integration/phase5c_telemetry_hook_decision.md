# Phase 5C telemetry hook decision

## Current player telemetry constraints

Current code behavior:

- `player.py` calls `controller.augment_feedback(fb0, context={"phase": "header"})` before CSV header creation.
- `core/dataset_schema.py` builds the segment telemetry header from the initial feedback keys.
- Feedback-derived CSV columns are prefixed as `feedback_<key>`.
- Row feedback is built before `calcControlAction()`.
- Neural `raw_action`, `safe_action` and fallback reasons are known only after `calcControlAction()`.
- `_update_pending_policy_and_switch()` updates the pending row after the decision.
- `evaluation_segments.csv` has a static compact header and must not receive neural diagnostic fields.

## Decision

Recommended Phase 5D decision:

```text
Allow a minimal optional post-decision telemetry hook in player.py, with strict tests.
```

The hook should be generic, optional, backward-compatible and ignored for existing controllers.

## Proposed hook

If the controller has `get_last_decision_telemetry()`, `player._update_pending_policy_and_switch()` may copy matching telemetry fields into the pending segment row.

To make columns exist, `NeuralAbrLiteController.augment_feedback(..., context={"phase": "header"})` should add the diagnostic keys with safe default values. In the current CSV design these will appear as `feedback_neural_*` columns unless Phase 5D explicitly approves static schema columns.

## Strict limits

The hook must:

- be optional;
- be no-op for existing controllers;
- not change `evaluation_segments.csv`;
- not introduce benchmark fields;
- not change controller selection semantics;
- not crash if telemetry is missing or malformed;
- update only columns already present in the pending row/header.

## If the player hook is rejected

If `player.py` change is rejected in Phase 5D, diagnostics remain in `controller.last_metrics` / `get_last_decision_telemetry()` and tests only. CSV telemetry would then be limited to pre-decision default fields from `augment_feedback`.

## Diagnostic fields

The canonical diagnostic keys are:

```text
neural_enabled
neural_bundle_configured
neural_bundle_loaded
neural_bundle_schema_ok
neural_bundle_hash_ok
neural_feature_schema_ok
neural_feature_vector_ok
neural_missing_features
neural_action_mask_valid_count
neural_raw_action
neural_raw_rate_Bps
neural_safe_action
neural_safe_rate_Bps
neural_safety_intervened
neural_fallback_used
neural_fallback_reason
neural_inference_ms
neural_nan_inf_detected
neural_invalid_action_detected
neural_diagnostic_only
```

These fields are diagnostic-only and not benchmark results.
