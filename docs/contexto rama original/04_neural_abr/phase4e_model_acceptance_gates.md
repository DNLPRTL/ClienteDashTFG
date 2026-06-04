# Phase 4E — Model acceptance gates

## Possible outcomes

```text
PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA
PHASE4E_EXTERNAL_TRACE_SMOKE_PASS
PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F
PHASE4E_DIAGNOSTIC_ONLY_NOT_FOR_EXPORT
PHASE4E_PARTIAL_FIX_REQUIRED
PHASE4E_FAIL
```

## Synthetic smoke gates

Required:

- dataset build command passes;
- dataset validation command passes;
- CPU training command passes;
- offline validation command passes;
- unit tests pass;
- readiness strict passes;
- artifacts remain outside repo;
- reports document that this is not a final model.

## Offline candidate gates

Required before Phase 4F:

- external trace train/validation/OOD split documented;
- train-only normalization confirmed;
- no future leakage confirmed;
- 100% valid actions under action mask;
- no NaN/Inf;
- no collapse to always min, always max or always one fixed representation;
- validation behavior is not pathological;
- OOD diagnostic behavior is reported, not tuned;
- CPU latency is measured;
- model card is written;
- limitations are written.

## What does not gate Phase 4E

Phase 4E does not require formal ranking against BBA/BOLA/MPC/robustMPC. Formal comparison belongs later.
