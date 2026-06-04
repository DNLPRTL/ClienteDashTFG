# Phase 4D — offline training pipeline implementation specs report

## Status

This document opens Phase 4D after the validated closure of Phase 4C.

Phase 4D is the first block where code implementation is allowed, but the implementation boundary is still **offline only**:

```text
Allowed:
  - core/neural_abr/ offline modules;
  - scripts for dataset build/validation/training smoke/offline validation;
  - tests for those modules;
  - documentation updates explaining the implementation.

Forbidden:
  - controller registration;
  - player/runtime/media changes;
  - benchmark or ranking;
  - real training claims;
  - client integration;
  - dry-runs legacy as training dataset.
```

## Inherited decision

Phase 4A2 selected:

```text
NeuralABR-Lite Candidate Scorer
  small CPU-first neural ABR
  behavior cloning / imitation learning
  score per valid representation candidate
  action = representation_index inside the MPD ladder
  reward = qoe_linear_v1 / reward_n
  teacher = robust_mpc primary, mpc secondary, bounded oracle diagnostic-only
  safety = action mask + fallback policy
```

## Goal of Phase 4D

Phase 4D must implement the offline machinery needed to build, validate, train-smoke and sanity-check a NeuralABR-Lite candidate scorer without touching the client runtime.

The goal is **not** to prove final QoE superiority. The goal is to prove that the implementation pipeline is correct, reproducible, artifact-safe, leakage-aware and ready for Phase 4E training smoke.

## Deliverable standard

At the end of implementation, the repository must contain enough code and documentation for the thesis to explain:

- what was implemented;
- why it follows the paper-driven decision;
- how traces become training samples;
- how teacher labels are produced;
- how future-information leakage is blocked;
- how actions are masked to MPD-valid representations;
- how CPU-first reproducibility is enforced;
- how artifacts stay outside the repository;
- why this is not yet a benchmark or final ranking.
