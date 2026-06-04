# Phase 5B fallback policy contract

## Purpose

NeuralABR-Lite must not be a single point of failure. Any unsafe, invalid or failed neural path must fallback to a classical controller or conservative representation.

## Preferred fallback order

```text
1. robust_mpc
2. mpc
3. rate_based
4. bba
5. min_rate
6. lowest valid representation
```

The future implementation may adapt names to the controllers actually available in `core/controller/`, but the order must remain conservative.

## Requirements

- Fallback must be visible in diagnostic telemetry.
- Fallback must never crash the run.
- Fallback cannot be used to claim neural success.
- `fallback_reason` enum is required.
- Missing bundle and runtime errors must fail closed.

## Initial fallback reason enum

```text
BUNDLE_MISSING
MANIFEST_INVALID
HASH_MISMATCH
SCHEMA_MISMATCH
MODEL_LOAD_FAILED
PYTORCH_UNAVAILABLE
SAFE_LOAD_UNSUPPORTED
FEATURE_BUILD_FAILED
REQUIRED_FEATURE_MISSING
ACTION_MASK_INVALID
ALL_ACTIONS_INVALID
NON_FINITE_SCORE
SELECTED_ACTION_MASKED
SAFETY_REJECTED
INFERENCE_TIMEOUT
RUNTIME_EXCEPTION
FALLBACK_CONTROLLER_UNAVAILABLE
```

## Diagnostic boundary

Fallback records are diagnostic-only. They are not benchmark results and must not be converted into rankings.
