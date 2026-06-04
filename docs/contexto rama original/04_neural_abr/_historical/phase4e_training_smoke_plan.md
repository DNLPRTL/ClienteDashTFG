# Phase 4E — Training smoke + offline validation plan

## Status

This phase starts after Phase 4D has implemented the offline NeuralABR-Lite pipeline.

Phase 4E is not client integration. It trains and validates the model offline only.

## Main goal

Establish whether NeuralABR-Lite is at least a defensible offline candidate, without claiming benchmark superiority or real-world performance.

## Tiered training plan

### Tier 0 — synthetic smoke

Purpose: prove that the implemented pipeline can build a dataset, train a tiny CPU model, and validate actions without leakage or artifacts in the repository.

This tier is necessary but not sufficient for a real model.

Expected status after success:

```text
PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA
```

### Tier 1 — external trace smoke

Purpose: repeat the same pipeline using documented external network traces, never legacy dry-runs.

This requires trace manifests and converted public traces outside the repository.

Expected status after success:

```text
PHASE4E_EXTERNAL_TRACE_SMOKE_PASS
```

### Tier 2 — offline candidate training

Purpose: train on train traces, validate on validation traces, and report OOD diagnostic behavior.

Expected status after success:

```text
PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F
```

## Non-goals

- No neural controller registration.
- No player/runtime/media changes.
- No benchmark.
- No ranking.
- No final comparison claim against BBA/BOLA/MPC/robustMPC.
- No use of legacy dry-run artifacts as training data.
- No SOTA claim.
- No real-world claim.

## Acceptance philosophy

Synthetic smoke proves the machinery. External trace validation proves the model can be studied. Phase 4G decides whether the result is accepted for Phase 5 integration.
