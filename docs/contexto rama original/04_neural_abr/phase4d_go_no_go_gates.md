# Phase 4D go/no-go gates

## PASS for Phase 4D implementation

Phase 4D implementation can be accepted only if all gates pass:

```text
G1: code only in allowed offline files;
G2: no controller/player/runtime/media integration;
G3: unit tests pass;
G4: client readiness remains PASS;
G5: synthetic dataset build smoke passes;
G6: dataset validation smoke passes;
G7: training CLI smoke runs on CPU without NaN/Inf;
G8: offline validation smoke produces reports outside repo;
G9: action mask prevents invalid representation actions;
G10: train-only normalization is enforced;
G11: leakage audit reports no forbidden feature fields;
G12: implementation docs for memory/defense exist.
```

## Not enough for Phase 5

A Phase 4D PASS does not allow client integration. Client integration requires Phase 4E/F/G and an explicit `ACCEPTED_FOR_PHASE5_INTEGRATION` decision.
