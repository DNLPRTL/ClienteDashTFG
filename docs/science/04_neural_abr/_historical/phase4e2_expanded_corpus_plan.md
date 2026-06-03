# Phase 4E.2 — Expanded external corpus plan

## Status before this block

Phase 4E.1 is closed as `PHASE4E1_EXTERNAL_TRACE_SMOKE_PASS_NOT_CANDIDATE`.

The external trace smoke proved that normalized external trace ingestion works, but it used only 15 traces and remains diagnostic-only. Therefore Phase 4F export is blocked until a candidate-readiness gate is defined and executed over a broader, balanced external corpus.

## Goal

Phase 4E.2 expands from smoke validation to candidate-readiness assessment:

```text
Phase 4E.1: can the external trace path run?
Phase 4E.2: can a small CPU-first model become a Phase 4F candidate?
```

## Method kept from previous phases

NeuralABR-Lite Candidate Scorer:

```text
behavior cloning / imitation learning
teacher = robust_mpc primary
action = representation_index
output = score per valid representation
reward basis = qoe_linear_v1 / reward_n
action mask mandatory
CPU-first
```

## Required outcome

Exactly one of:

```text
PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F
PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE
PHASE4E2_BLOCKED_NEEDS_FIX
```
