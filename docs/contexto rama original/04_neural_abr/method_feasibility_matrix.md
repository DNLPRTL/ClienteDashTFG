# Phase 4 method feasibility matrix

Phase: Phase 4A1 final
Purpose: feed Phase 4A2 method decision.

| method | evidence support | buildability by student | CPU-first | dependency risk | data risk | leakage risk | reward risk | expected defense quality | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| NeuralABR-Lite candidate scorer + behavior cloning | Very high | 3 | 3 | 2 | 2 | 2 | 1 | 3 | SELECT CANDIDATE |
| NeuralABR-Lite guidance + fallback | High | 3 | 3 | 1 | 2 | 2 | 1 | 3 | SELECT DESIGN PATTERN |
| Fugu-lite predictor + MPC | High | 3 | 3 | 1 | 2 | 2 | 1 | 3 | BACKUP/COMPARATOR |
| BC + tiny PPO fine-tune | Medium/high | 2 | 2 | 3 | 2 | 2 | 3 | 2 | OPTIONAL ONLY |
| Direct PPO/A3C | Medium | 1 | 1 | 3 | 2 | 2 | 3 | 1 | DO NOT SELECT AS BASE |
| Full meta-RL / VAE latent | High frontier | 1 | 1 | 3 | 3 | 2 | 2 | 2 | DO NOT SELECT AS BASE |
| Offline RL full | Medium/high frontier | 1 | 1 | 3 | 3 | 3 | 2 | 2 | DO NOT SELECT AS BASE |
| Multi-model ANT/BETA | High frontier | 1 | 1/2 | 3 | 3 | 3 | 2 | 2 | USE ONLY FOR STRATIFICATION |
| NMoE / preference-aware | Frontier | 1 | 1 | 3 | 3 | 2 | 3 | 1 | FUTURE WORK ONLY |
| AIRL/reward learning | Medium | 1 | 1 | 3 | 2 | 3 | 3 | 1 | DO NOT SELECT |
| No-IA/SODA-like | High | 2 | 3 | 1 | 1 | 1 | 1 | 3 | COMPARATOR/NEGATIVE RESULT CONTEXT |

## Feasibility conclusion

Phase 4A2 should decide between:

```text
Primary:
  NeuralABR-Lite candidate scorer trained by behavior cloning.

Fallback/secondary:
  predictor + policy / Fugu-lite.

Optional extension:
  tiny PPO fine-tune only after BC is stable and only if CPU-first/reproducibility gates pass.
```
