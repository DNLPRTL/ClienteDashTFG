# Phase 4A2 notes for memory and defense

## Memory chapter use

### State of the art

Phase 4A2 supports a section explaining why the project does not simply implement PPO/Pensieve.
The literature shows multiple families: direct RL, imitation learning, predictor+policy, meta-RL, offline RL, real-world learning and non-IA deployable controllers.

### Design chapter

The selected design can be represented with a figure:

```text
observable client state + candidate representation features
  -> shared neural scorer
  -> score per valid representation
  -> mask/fallback
  -> representation_index
```

### Evaluation chapter

The thesis should state that Phase 4 does not perform formal benchmark/ranking.
It prepares method, contracts and later offline validation.
Real-world claims are explicitly out of scope.

### Defense points

- IA is not assumed to win.
- BBA/MPC/robustMPC may remain stronger in some scenarios.
- The chosen method is small because reproducibility and explainability matter more than SOTA claims.
- PPO is not selected by inertia because direct RL is expensive and reward-sensitive.
- Meta-RL/offline RL/MoE are discussed as frontier/future work, not copied.
- CausalSim-style bias and future-information leakage are explicitly blocked.

## Table candidates

- Method selection table.
- Rejected-method rationale table.
- Acceptance gates table.
- Phase 4 flow table.
- Risk mitigation table.

## Figure candidates

- NeuralABR-Lite candidate scorer diagram.
- Phase 4 flow diagram.
- Teacher-label generation vs model-input boundary.
- Trace split / OOD regime diagram.
