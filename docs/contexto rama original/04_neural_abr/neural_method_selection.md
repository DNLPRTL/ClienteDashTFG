# Neural method selection

Status: **selected method family for Phase 4B specs**

## Selected path

```text
Primary method:
  NeuralABR-Lite Candidate Scorer

Training family:
  behavior cloning / imitation learning

Safety pattern:
  neural guidance + classical fallback
```

## Candidate methods compared

| Method | Evidence support | CPU-first | Data feasibility | Leakage risk | Defense quality | Decision |
|---|---:|---:|---:|---:|---:|---|
| Candidate-scoring imitation learning | 3 | 3 | 2 | 2 | 3 | **SELECT** |
| Guidance + fallback | 3 | 3 | 2 | 1 | 3 | **SELECT AS DESIGN PATTERN** |
| Fugu-lite predictor + policy | 3 | 3 | 2 | 2 | 3 | **BACKUP / COMPARATOR** |
| BC + tiny PPO fine-tune | 2 | 2 | 2 | 3 | 2 | OPTIONAL ONLY |
| Direct PPO/A3C/A2C | 2 | 1 | 2 | 3 | 1 | REJECT AS BASE |
| Full meta-RL | 3 | 1 | 3 | 2 | 2 | REJECT AS BASE |
| Full offline RL | 2 | 1 | 3 | 3 | 2 | REJECT AS BASE |
| Multi-model DRL / ANT-like | 2 | 1/2 | 3 | 2 | 2 | INSPIRATION ONLY |
| MoE / preference-aware / large neural | 2 | 1 | 3 | 2 | 1 | FUTURE WORK |
| AIRL / learned reward | 2 | 1 | 2 | 3 | 1 | REJECT AS BASE |
| SODA-like no-IA | 3 | 3 | 2 | 1 | 3 | COMPARATOR / DEFENSE |

Scoring: `3 = strong`, `2 = medium`, `1 = weak/high risk`.

## Why candidate scoring wins

A fixed-output classifier assumes that the representation ladder is fixed and ordered exactly as during training.
A candidate scorer is more compatible with DASH because it can score the actual representations available for the current MPD.
This is the best fit for a reusable ABR controller.

The intended future interface is conceptually:

```text
context_features = f(client_state)
for each valid representation r:
    candidate_features = g(r, context)
    score[r] = model(context_features, candidate_features)
choose argmax(score) after masks and fallback checks
```

This remains a design intent, not implementation code.

## Why behavior cloning wins

Behavior cloning gives a supervised learning problem that can be trained on CPU with modest data.
It is easier to explain, test and reproduce than direct online RL.
It allows the project to reuse the existing MPC/robustMPC scientific baseline as a teacher, while still producing a neural policy component.

## Why the selected path is still honest

The method may lose against BBA/MPC/robustMPC.
The thesis must state this possibility explicitly.
Success in Phase 4 means a reproducible, safe, non-trivial neural candidate that obeys contracts, not a guaranteed QoE win.
