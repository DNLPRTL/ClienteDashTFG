# Phase 3.5 - QoE, reward and final metric semantics

This directory contains the scientific and methodological documentation for Phase 3.5.

## Scope

Phase 3.5 closes the QoE/reward metric semantics needed before any formal evaluation, ranked controller comparison or IA/RL training.

## Current subphase

Phase 3.5A1 - QoE/reward source-card distillation and evidence matrix.

This subphase fills the selected source cards, evidence matrix, term crosswalk and candidate formula notes. It does not close `qoe_selection.md`, `reward_definition.md` or any implementation contract.

## Hard boundaries

- No IA/RL training in Phase 3.5A1.
- No ranked controller comparison in Phase 3.5A1.
- No benchmark claims in Phase 3.5A1.
- No generated CSV/log/run artifacts in Git.
- No raw PDFs, HTML captures or source captures in Git.
- No controller, player, runtime or media-engine changes.
- No QoE/reward code, tests or `core/evaluation` package in this block.
- No Mahimahi or `tc/netem` experiments in this block.

## Evidence flow

1. Search notes and local source batch.
2. Source inventory.
3. Source triage.
4. Source cards distilled in Phase 3.5A1.
5. QoE evidence matrix.
6. QoE terms crosswalk.
7. QoE formula candidates.
8. Final QoE/reward decision documents in a later subphase.
9. Implementation only after documentation is closed.

## Phase 3.5A1 evidence summary

- The repeated common core across the strongest ABR/QoE sources is quality utility, rebuffering/stalling penalty and switching/smoothness penalty.
- Startup delay is a recognized influence factor, but its use should be considered in A2 only if the measurement contract is homogeneous.
- VMAF and perceptual quality are scientifically relevant, but artifact-dependent and likely secondary/deferred unless per-segment reference/distorted video artifacts exist.
- User preference evidence shows that QoE weights are not universal.
- Methodology sources warn against inventing an ad hoc subjective QoE model without validation.

## Documents still deferred to A2

- `qoe_selection.md`
- `reward_definition.md`
- `secondary_metrics.md`
- `metric_formula_catalog.md`
- `benchmark_result_schema.md`
- `evaluation_gate_policy.md`
