# Teacher policy contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This document defines the teacher policies allowed to generate labels for imitation learning.

## Teacher tiers

### T0 — primary teacher

```text
robust_mpc_policy_replay
```

Role:

```text
primary teacher for initial NeuralABR-Lite behavior cloning
```

Rationale:

- already aligned with ABR control;
- safer than a full oracle;
- compatible with online-observable state;
- defensible if the student model is framed as policy distillation / lightweight approximation.

### T1 — secondary teacher/comparator

```text
mpc_policy_replay
```

Role:

```text
secondary teacher, ablation or fallback comparator
```

### T2 — diagnostic upper-bound teacher

```text
bounded_oracle_teacher
```

Role:

```text
diagnostic upper bound only unless a later contract explicitly promotes it
```

Rules:

- May use limited future information only to estimate an upper bound.
- Must not leak future information into model input features.
- Must be clearly labeled as oracle/diagnostic.

## Forbidden teachers

Forbidden as default training labels:

```text
legacy dry-run actions
smoke scenario actions
human-picked best-looking actions
actions selected after looking at validation/OOD results
actions from a controller whose objective is undocumented
actions from benchmark/test artifacts
```

## Label format

A teacher-labeled sample must include:

```text
teacher_id
teacher_version
teacher_action_representation_index
teacher_action_validity
teacher_reward_n
teacher_policy_inputs_summary
trace_id
segment_index
split
```

## Student target

The base target is:

```text
cross-entropy / classification target over valid representation candidates
```

Ranking loss can be considered later if the candidate scorer design benefits from ordered teacher alternatives, but it is not required in Phase 4B.

## Teacher disagreement

If T0 and T1 disagree, the dataset may record both actions, but the primary label remains T0 unless a later decision defines consensus labeling.

## Phase 4B decision

The primary training teacher is robust MPC replay. Oracle-like teachers are diagnostic-only by default.
