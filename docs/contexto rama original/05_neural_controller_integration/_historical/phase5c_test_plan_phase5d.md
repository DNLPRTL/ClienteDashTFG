# Phase 5C test plan for Phase 5D

These tests are future implementation tests. Phase 5C creates no test files.

## Required Phase 5D tests

| Test | Expected behavior |
|---|---|
| Controller creates with no bundle | Neural disabled and fallback used. |
| Invalid bundle path | Fallback, no crash, reason recorded. |
| Missing manifest | Fallback, no crash, reason recorded. |
| Hash mismatch | Fallback, no crash, reason recorded. |
| Schema mismatch | Fallback, no crash, reason recorded. |
| Unsupported safe torch load | Fallback, no `weights_only=False`. |
| Single representation | Returns the only representation. |
| Variable ladder | Never selects outside current `max_level`. |
| All-false/invalid action mask | Fallback, no crash, reason recorded. |
| NaN/Inf score | Fallback, no crash, reason recorded. |
| Selected masked action | Fallback, invalid-action telemetry recorded. |
| Missing required feature | Fallback, no crash, reason recorded. |
| Deterministic inference | Same input and bundle gives same action. |
| Rate return contract | Controller returns one value from `feedback["rates"]`. |
| Preferred fallback | `robust_mpc` used when neural is disabled and signals are available. |
| Emergency fallback | Lowest valid representation if all fallback controllers fail. |
| Registry | Registry creates controller key `neural_abr_lite`. |
| Config params | Controller params pass through generic config. |
| Optional telemetry hook | Diagnostic fields populate if hook is implemented. |
| Fake engine smoke | Synthetic temp bundle and local MPD only, no external network. |
| Artifact hygiene | No model artifacts committed. |

## Validation boundary

These tests validate structure, safety and error handling. They are diagnostic-only and not benchmark tests.
