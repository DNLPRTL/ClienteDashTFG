# Phase 4A1 closure report

## Phase status

Phase 4A1 — source cards + evidence matrix — is ready to close after applying Package 3 and validating the repository.

## Completed blocks

- Package 1 source cards: core decision sources.
- Package 2 source cards: generalization, deployment and surveys.
- Package 3 source cards: recent frontier and surveillance.
- Final neural evidence matrix.
- Final method crosswalk.
- Final method feasibility matrix.
- Final risk register.

## Scientific closure

The literature does not support a PPO-first implementation for this TFG. The defensible route is a small CPU-first neural ABR designed around imitation learning, candidate scoring, trace-regime balancing, action masking and classical fallback.

## Selected hypothesis for Phase 4A2

```text
Primary method candidate:
  NeuralABR-Lite candidate-scoring MLP trained by behavior cloning.

Training signal:
  teacher generated from MPC / robustMPC / oracle-limited labels on training traces only.

Action:
  valid MPD representation index selected through candidate scores and hard mask.

Reward:
  qoe_linear_v1 / reward_n from Phase 3.5.

Evaluation in Phase 4:
  sanity validation and OOD diagnostics only; no final benchmark/ranking.
```

## Conditions to close A1

- Package 3 applied.
- Validation script passes.
- `python scripts/check_client_readiness.py --strict` passes.
- Git diff shows only `docs/science/04_neural_abr/**`.
- No forbidden artifacts inside the repo docs directory.

## Next phase

Phase 4A2 — method decision.
