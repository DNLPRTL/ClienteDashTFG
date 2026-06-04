# Phase 4E offline validation report template

## Input

- dataset dir:
- run dir:
- validation output dir:

## Gates

| gate | result | notes |
|---|---|---|
| valid actions | TBD | |
| no NaN/Inf | TBD | |
| train-only normalization | TBD | |
| leakage audit | TBD | |
| collapse check | TBD | |
| OOD diagnostic present | TBD | |
| artifacts outside repo | TBD | |

## Decision

One of:

```text
PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA
PHASE4E_EXTERNAL_TRACE_SMOKE_PASS
PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F
PHASE4E_DIAGNOSTIC_ONLY_NOT_FOR_EXPORT
PHASE4E_PARTIAL_FIX_REQUIRED
PHASE4E_FAIL
```
