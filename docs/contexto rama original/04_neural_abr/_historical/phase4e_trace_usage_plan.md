# Phase 4E — Trace usage plan

## Allowed trace sources

Allowed:

- documented external network traces;
- converted public traces from previous trace conversion infrastructure;
- synthetic traces for smoke only.

Forbidden:

- DashClientModular4 legacy dry-runs;
- QoE smoke outputs;
- benchmark outputs;
- player/runtime logs without a new data contract;
- test/OOD traces used for training.

## Split unit

The split unit is the trace, not the segment.

Samples from the same trace must not be split randomly between train and validation.

## Required splits

```text
train
validation
ood_diagnostic
```

## What Phase 4E can close

Synthetic-only Phase 4E can close only:

```text
PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA
```

A defensible offline candidate needs external traces and must close:

```text
PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F
```

## Why this matters

The papers behind Phase 4 warn that trace replay and learned ABR can be misleading when the data distribution is biased. Therefore, the trace manifest, train-only normalization and leakage audit are part of the scientific result, not bookkeeping.
