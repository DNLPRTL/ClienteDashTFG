# Implementation go/no-go policy

## Two different implementations

There are two implementation boundaries:

```text
Phase 4D implementation:
  offline training pipeline implementation.

Phase 5 implementation:
  client/controller integration inside DashClientModular4.
```

Phase 4D may happen after Phase 4C validation. Phase 5 may only happen after Phase 4G acceptance.

## Go for Phase 4D

Allowed after Phase 4C:

```text
Codex prompt for offline pipeline;
core/neural_abr/ offline modules;
dataset builder script;
training script;
offline validation script;
unit tests and smoke tests.
```

Still forbidden:

```text
controller registry changes;
player/runtime/media changes;
formal benchmark;
ranking;
claiming final QoE superiority.
```

## Go for Phase 5

Allowed only if Phase 4G states `ACCEPTED_FOR_PHASE5_INTEGRATION`:

```text
experimental neural controller wrapper;
model bundle loader;
feature extraction adapter;
action mask enforcement;
fallback to classical controller;
inference failure handling;
integration tests.
```

## No-go conditions

Hard no-go for Phase 5:

```text
leakage audit failure;
invalid action possible;
no fallback;
model collapse;
unbounded latency;
non-reproducible training;
missing model card;
missing inference contract;
artifacts inside repo;
claims not supported by evidence.
```

## Final benchmark boundary

Formal benchmark/ranking is still not Phase 4. It belongs to a later evaluation phase after integration and after benchmark methodology is explicitly opened.
