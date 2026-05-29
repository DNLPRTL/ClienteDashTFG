# Phase 4E.1 to Phase 4F Gate

Phase 4F remains blocked until Phase 4E produces a valid external-trace offline candidate.

## Gate required for Phase 4F

The following must be true:

```text
PHASE4E_EXTERNAL_TRACE_CANDIDATE_READY_FOR_PHASE4F=true
```

and:

- external-trace dataset built from normalized traces;
- trace-level split manifest present;
- dataset validation PASS;
- CPU training PASS;
- offline validation PASS;
- 100% valid actions;
- no labels outside ladder;
- no NaN/Inf;
- no row-level split leakage;
- train-only normalization;
- no collapse to a single action unless explicitly accepted as a limitation and marked not candidate;
- artifacts outside repo;
- unit tests PASS;
- readiness PASS;
- no forbidden claims.

## If collapse persists

If the model collapses to one representation on external traces, record:

```text
PHASE4E1_EXTERNAL_TRACE_SMOKE_PASS_NOT_CANDIDATE
```

and do not open Phase 4F.
