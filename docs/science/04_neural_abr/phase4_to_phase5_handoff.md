# Phase 4 to Phase 5 handoff

## Current state

- Latest validated HEAD: `4d2a315 test(neural-abr): fix Phase 4F bundle validation gates`.
- Phase 4F decision: `PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G`.
- Phase 4G decision: `ACCEPTED_FOR_PHASE5_INTEGRATION`.

## What Phase 5 receives

Phase 5 receives:

- an accepted NeuralABR-Lite offline model candidate;
- a Phase 4F local-only inference bundle;
- feature schema and normalization stats;
- ladder/action constraints;
- inference contract;
- fallback policy;
- scientific source cards and evidence matrix;
- method and risk docs;
- tests and validation history.

## What Phase 5 must not do first

Phase 5 must not immediately implement a controller. The next block is a targeted literature delta:

```text
Phase 5A0 — neural controller integration literature delta and implementation triage
```

## Phase 5 core challenge

Phase 5 is not about choosing or training the model. That is done. Phase 5 is about integrating the bundle into DashClientModular4 safely:

- runtime feature availability;
- controller API;
- action mask;
- fallback;
- model loading;
- error handling;
- telemetry;
- avoiding benchmark contamination.

## Handoff warning

Do not use Phase 5 structural smokes as formal benchmarks. Formal comparative validation belongs to Phase 6.
