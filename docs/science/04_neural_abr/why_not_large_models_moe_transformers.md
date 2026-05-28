# Why not large models, MoE or transformer-like ABR as base

Status: **large neural ABR rejected as Phase 4 base**

## Decision

Do not select NMoE/MoE/large preference-aware/transformer/LLM-style ABR as the base TFG method.

## Reasons

Large models and mixture-of-experts systems are useful frontier references, but they are misaligned with the project constraints:

- too many moving parts;
- preference data may be unavailable;
- training cost is high;
- implementation is harder to own and defend;
- dependency risk increases;
- failures are harder to diagnose;
- the TFG does not need SOTA claims.

## What is retained

From these sources we keep:

```text
heterogeneity matters;
network/user preferences can matter;
OOD/generalization matters;
future work can extend beyond one small model.
```

## Implementation consequence

NeuralABR-Lite stays intentionally small.
If it loses against classical controllers, that result is acceptable and scientifically meaningful.
