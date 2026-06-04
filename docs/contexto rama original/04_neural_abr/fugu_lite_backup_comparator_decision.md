# Backup/comparator decision: Fugu-lite predictor + policy

Status: **retained as backup/comparator, not selected as primary**

## Concept

Fugu-lite would train a small supervised predictor for transmission/download time or future throughput and then feed that prediction into MPC/robust_mpc.

```text
observable state -> predictor -> MPC/robust_mpc -> representation_index
```

## Why it remains useful

This path is scientifically strong because it separates prediction from control.
A prediction error can be inspected directly, and the decision layer remains interpretable.
It is also CPU-first and easier to debug than direct RL.

## Why it is not the primary method

The goal of Phase 4 is to develop a neural ABR controller path.
Candidate-scoring behavior cloning gives a clearer neural policy component while still staying feasible.
Fugu-lite remains a fallback if candidate scoring becomes weak, hard to validate, or overfits.

## Role in future phases

Fugu-lite may be used as:

- a backup if behavior cloning fails;
- an additional non-RL ML comparator;
- a memory/defense argument showing that ML can help prediction without replacing ABR control;
- future work if Phase 4 scope is constrained.

## Constraints

Fugu-lite must not become a hidden benchmark in Phase 4.
It can only be implemented after specs and Codex gates if selected later.
