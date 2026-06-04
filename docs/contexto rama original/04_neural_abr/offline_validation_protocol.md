# Offline validation protocol

## Scope

Phase 4 validation is sanity validation, not formal benchmark and not final ranking.

## Validation objects

The offline validation environment may validate:

```text
dataset integrity
teacher label distribution
trained model action validity
trained model non-collapse
latency of inference
reward sanity on validation traces
OOD diagnostic behavior
```

## Required future sanity checks

A future trained candidate must pass:

```text
100% valid actions under action mask
0 NaN/Inf scores
0 labels outside ladder
no validation/OOD leakage
normalization train-only
no constant min_rate collapse
no constant max_rate collapse
no fixed-rate trivial collapse unless explicitly diagnosed
CPU inference latency within budget
validation sanity reward above random/pathological sanity baseline
OOD diagnostic reported, not hidden
```

## What does not have to happen in Phase 4

The model does not have to beat every classical controller in Phase 4. If it loses to BBA/MPC/robustMPC, that may still be academically valid if the pipeline, evidence, and limitations are rigorous. Formal controller ranking is reserved for a later benchmark phase.

## Acceptance terms

```text
DIAGNOSTIC_ONLY:
  useful for analysis, not for client integration.

OFFLINE_CANDIDATE:
  passes dataset/model sanity, but export/inference not closed.

ACCEPTED_FOR_PHASE5_INTEGRATION:
  passes Phase 4E validation and Phase 4F export/inference gates, then closed in Phase 4G.
```
