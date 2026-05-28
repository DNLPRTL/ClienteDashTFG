# Phase 4A2 method acceptance gates

These gates determine whether Phase 4A2 can be considered closed and whether Phase 4B can start.

## Gate A2-G1 — Evidence basis

Pass condition:

```text
Phase 4A1 source cards and evidence matrix exist.
Method decision references those documents.
```

## Gate A2-G2 — CPU-first feasibility

Pass condition:

```text
Selected method is trainable with small CPU-first PyTorch model.
No required CUDA/ROCm/WSL/Ray/RLlib/TensorFlow-legacy gate.
```

## Gate A2-G3 — DASH action compatibility

Pass condition:

```text
Method outputs valid representation_index through candidate scoring or masking.
No free bitrate output.
```

## Gate A2-G4 — Leakage control

Pass condition:

```text
Method explicitly blocks dry-runs legacy as training data.
Method separates expert future information from model inputs.
```

## Gate A2-G5 — Reward discipline

Pass condition:

```text
Method uses Phase 3.5 reward/QoE definitions.
No learned reward or unversioned reward change.
```

## Gate A2-G6 — Scope control

Pass condition:

```text
A2 contains documentation only.
No implementation.
No training.
No benchmark.
No ranking.
No controller/player/runtime/media changes.
```

## Gate A2-G7 — Defense quality

Pass condition:

```text
The method can be defended even if IA loses against BBA/MPC/robustMPC.
Negative results remain academically valid.
```

## A2 gate verdict

Expected verdict:

```text
PASS: start Phase 4B contracts.
```
