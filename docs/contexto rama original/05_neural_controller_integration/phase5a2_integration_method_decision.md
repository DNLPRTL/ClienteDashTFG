# Phase 5A2 integration method decision

## Decision

```text
ACCEPTED: guarded neural scorer controller
```

## Rationale

This method matches the Phase 4 NeuralABR-Lite Candidate Scorer:

- it scores each candidate representation;
- it handles variable ladders;
- it supports mandatory action masks;
- it keeps the final action on an existing MPD representation;
- it supports fallback and safety guard intervention;
- it keeps inference CPU-first and local-only;
- it minimizes runtime contamination by keeping telemetry diagnostic-only and not benchmark output.

## Selected runtime pattern

```text
feedback before decision
-> runtime feature builder
-> bundle and feature schema checks
-> train-only normalization
-> action mask from current valid MPD representations
-> CPU scorer inference
-> masked argmax raw_action
-> safety guard
-> safe_action or fallback
-> diagnostic-only telemetry
```

## Alternatives rejected or deferred

- full neural controller;
- neural predictor plus new MPC;
- server-side guidance;
- ONNX migration now;
- online learning;
- multi-model switching;
- retraining.

## Benchmark boundary

This is not a benchmark decision. Phase 5 can only validate structure, fallback behavior and telemetry plumbing. Formal comparison belongs to Phase 6.
