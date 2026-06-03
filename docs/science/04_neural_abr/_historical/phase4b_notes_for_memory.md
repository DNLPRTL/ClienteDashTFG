# Phase 4B notes for memory

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Thesis chapter support

### State of the art

Phase 4B supports the thesis explanation that neural ABR is not adopted blindly. It is constrained by evidence from RL, imitation learning, real-world deployment, causal simulation and OOD generalization.

### Design chapter

Use these figures/tables:

```text
Figure: NeuralABR-Lite candidate scorer data flow
Figure: online features vs teacher-only future information
Table: allowed and forbidden features
Table: trace split and leakage gates
Table: selected method vs rejected alternatives
```

### Implementation chapter

Phase 4B will later justify why the implementation contains:

```text
feature builder
candidate scorer
teacher label generator
split manifest
normalization manifest
action mask
fallback policy
```

### Evaluation chapter

Phase 4B prepares the evaluation language:

```text
sanity validation, not benchmark
OOD diagnostic, not tuning target
no ranking final in Phase 4
no real-world deployment claim
```

### Defense points

Useful defense statements:

```text
The IA controller is intentionally small because the project targets reproducibility and CPU-first training.
The model cannot output invalid bitrates; it scores valid MPD representations.
The training data contract blocks legacy dry-runs and leakage.
The project accepts that ML may lose to BBA/MPC under some conditions.
```
