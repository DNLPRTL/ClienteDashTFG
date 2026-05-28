# Why not full meta-RL as base

Status: **full meta-RL rejected as Phase 4 base**

## Decision

Do not implement A2BR/MERINA/MetaABR/EAStream/NMoE-style full meta-RL as the base method.

## Reasons

Meta-RL addresses a real problem: ABR policies under-generalize across network regimes, users, regions and traces.
However, full meta-RL introduces complexity that is not suitable as the core of this TFG:

- multiple task distributions;
- offline and online adaptation phases;
- MAML or equivalent meta-gradient logic;
- possible latent encoders/VAE;
- larger experiment design;
- heavier dependencies;
- harder reproducibility;
- harder defense if the method fails.

## What is retained

The ideas retained from meta-RL literature are:

```text
trace-regime split
OOD diagnostic validation
environment/context awareness
short temporal history
explicit under-generalization discussion
```

## Implementation consequence

NeuralABR-Lite may include simple regime-aware design later:

```text
balanced sampling by trace regime
regime labels for analysis only
OOD clusters held out
```

But it will not implement full meta-RL in the base path.
