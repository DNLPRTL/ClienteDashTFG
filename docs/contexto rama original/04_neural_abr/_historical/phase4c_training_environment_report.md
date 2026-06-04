# Phase 4C — Training environment / simulator contract report

Status: draft package generated after Phase 4B validation.

## Scope

Phase 4C defines the offline training environment and simulator contract for NeuralABR-Lite. It does not implement the model, does not train, does not create datasets, and does not integrate a neural controller into DashClientModular4.

The purpose is to turn the Phase 4B contracts into a precise environment boundary:

```text
external network traces
  -> trace conversion
  -> trace manifest
  -> deterministic replay
  -> teacher policy replay
  -> supervised sample generation
  -> train/validation/OOD manifests
  -> offline sanity validation
```

## Current inherited decision

From Phase 4A2 and Phase 4B:

```text
Selected method:
  NeuralABR-Lite Candidate Scorer

Training family:
  behavior cloning / imitation learning

Teacher:
  robust_mpc primary
  mpc secondary/comparator
  bounded oracle diagnostic only

Action:
  representation_index in the MPD ladder

Reward:
  qoe_linear_v1 / reward_n

Safety:
  action mask + fallback classic controller

Hard blocks:
  no dry-runs legacy as training data
  no benchmark/ranking in Phase 4
  no future leakage
  no PPO-first
  no full meta-RL/offline RL/MoE as base
```

## What Phase 4C closes

Phase 4C closes:

- simulator vs client boundary;
- trace format and conversion contract;
- manifest requirements;
- deterministic replay rules;
- teacher replay contract;
- supervised sample generation contract;
- offline validation protocol;
- artifact layout outside the repository;
- acceptance gates before implementation.

## What Phase 4C does not close

Phase 4C does not choose final trace files, train a model, produce checkpoints, or change the client. Those belong to later phases.

## Next phase

After Phase 4C validation, the next allowed block is Phase 4D:

```text
Phase 4D — offline training pipeline implementation and controlled smoke runs
```

Phase 4D is the first phase where Codex implementation prompts may be generated, but only for the offline neural ABR pipeline, not for client/player/controller integration.
