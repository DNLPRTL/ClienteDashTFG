# Phase 4E.1 Acceptance Gates

## Phase 4E.1 PASS means

Phase 4E.1 passes if the project can:

- stage Phase 3 normalized traces safely into the Phase 4 external trace workspace;
- verify no dry-run artifacts are used as training data;
- build a NeuralABR-Lite dataset from external normalized traces;
- validate trace-level split and train-only normalization;
- run a CPU training smoke;
- run offline validation;
- produce a model card/report that clearly says diagnostic-only;
- keep all generated datasets, models, logs and runs outside Git;
- keep `python -m unittest discover` and readiness PASS.

## Phase 4E.1 PASS does not mean

It does not mean:

- final model accepted;
- Phase 4F opened automatically;
- controller integration allowed;
- benchmark or ranking allowed;
- superiority over BBA/MPC claimed;
- real-world claim.

## Hard fail gates

Any of these blocks progress:

- dry-run or benchmark artifact used as training data;
- row-level leakage across splits;
- OOD used for tuning;
- normalization fit outside train;
- actions outside ladder;
- labels outside ladder;
- invalid artifact inside repo;
- controller/player/runtime/media touched;
- failed unit tests/readiness;
- undocumented change to reward formula.

## Candidate signal for later Phase 4F

A model can be considered for Phase 4F only if a later Phase 4E report says:

```text
PHASE4E_EXTERNAL_TRACE_CANDIDATE_READY_FOR_PHASE4F=true
```

The current synthetic Tier 0 result does not satisfy this.
