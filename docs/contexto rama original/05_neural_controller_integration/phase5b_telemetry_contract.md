# Phase 5B telemetry contract

## Purpose

Future telemetry must make the neural path observable without creating benchmark claims or training labels.

## Required diagnostic fields

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

## Interpretation

These fields are diagnostic-only. They show whether integration behaved structurally as expected. They must not be interpreted as benchmark results.

## Forbidden Phase 5 claims

Telemetry must not emit or imply:

- benchmark rank;
- winner;
- improvement percentage;
- final QoE comparison;
- statistical significance;
- real-world validation.
