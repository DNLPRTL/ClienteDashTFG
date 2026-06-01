# Phase 5B error handling contract

## Rule

Every failure must lead to fallback or neural disabled. `calcControlAction` must not allow an uncaught neural exception to crash the client.

## Failure table

| Failure | Behavior | Fallback reason |
|---|---|---|
| Bundle path not configured | Disable neural and fallback | `BUNDLE_MISSING` |
| Bundle directory missing | Disable neural and fallback | `BUNDLE_MISSING` |
| Manifest invalid | Disable neural and fallback | `MANIFEST_INVALID` |
| Hash mismatch | Disable neural and fallback | `HASH_MISMATCH` |
| Schema mismatch | Disable neural and fallback | `SCHEMA_MISMATCH` |
| `model_state.pt` load failure | Disable neural and fallback | `MODEL_LOAD_FAILED` |
| PyTorch unavailable | Disable neural and fallback | `PYTORCH_UNAVAILABLE` |
| Safe `torch.load` unsupported | Disable neural and fallback | `SAFE_LOAD_UNSUPPORTED` |
| Feature build exception | Fallback for decision | `FEATURE_BUILD_FAILED` |
| Required feature missing | Fallback for decision | `REQUIRED_FEATURE_MISSING` |
| Invalid action mask | Fallback for decision | `ACTION_MASK_INVALID` |
| All-false action mask | Fallback for decision | `ALL_ACTIONS_INVALID` |
| NaN/Inf score | Fallback for decision | `NON_FINITE_SCORE` |
| Selected action masked out | Fallback for decision | `SELECTED_ACTION_MASKED` |
| Safety guard rejects raw action and no safe lower action exists | Fallback/min representation | `SAFETY_REJECTED` |
| Inference timeout | Fallback for decision | `INFERENCE_TIMEOUT` |
| Any runtime exception | Catch, record and fallback | `RUNTIME_EXCEPTION` |

## Requirements

- No crash on missing bundle.
- No uncaught exception in `calcControlAction`.
- Fail closed by default.
- Record `fallback_reason`.
- Keep records diagnostic-only and not benchmark output.
