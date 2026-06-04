# Phase 5A1 telemetry contamination matrix

## Diagnostic telemetry allowed in Phase 5

| Field | Meaning | Benchmark status |
|---|---|---|
| `neural_enabled` | Controller path is configured to attempt neural scoring | Diagnostic-only |
| `model_loaded` | Bundle model state loaded successfully | Diagnostic-only |
| `bundle_schema_ok` | Bundle schema checks passed | Diagnostic-only |
| `feature_schema_ok` | Runtime feature schema matches bundle | Diagnostic-only |
| `action_mask_valid_count` | Number of valid current candidates | Diagnostic-only |
| `raw_action` | Neural best valid candidate before safety guard | Diagnostic-only |
| `safe_action` | Executed candidate after safety guard/fallback | Diagnostic-only |
| `safety_intervened` | Guard changed the raw action | Diagnostic-only |
| `fallback_used` | Fallback path executed | Diagnostic-only |
| `fallback_reason` | Enumerated fail-closed reason | Diagnostic-only |
| `inference_ms` | Per-decision CPU inference time | Diagnostic-only |
| `nan_inf_detected` | Non-finite score detected | Diagnostic-only |
| `invalid_action_detected` | Mask or selected action violation detected | Diagnostic-only |
| `diagnostic_only` | Explicit marker that this is not benchmark output | Diagnostic-only |

## Forbidden Phase 5 telemetry

The future controller must not emit:

- `benchmark_rank`;
- `improvement_percent`;
- `controller_winner`;
- `final_qoe_comparison`;
- `p_value`;
- statistical significance claim.

## Contamination warning

CausalSim warns that trace-driven replay can be biased because actions affect observed traces. Puffer/Fugu and Into the Wild show that real-world ABR uncertainty is large and that one environment may not generalize. Therefore Phase 5 telemetry is for integration diagnosis only. It is not training data, not dry-run labels, not a benchmark and not evidence of controller superiority.
