# Phase 4A2 — Method decision report

Status: **closed as method decision, pending Phase 4B contracts**  
Project: DashClientModular4 — ABR con IA para streaming DASH  
Flow position:

```text
search
  -> PDFs
  -> source_cards
  -> evidence_matrix
  -> method_decision      <-- THIS DOCUMENT SET
  -> specs                <-- NEXT: Phase 4B
  -> Codex                <-- STILL BLOCKED
```

## Decision summary

Phase 4A2 selects the following method family for the future IA/RL ABR work:

```text
NeuralABR-Lite Candidate Scorer
  = small CPU-first neural ABR policy component
  + candidate-scoring over valid MPD representations
  + behavior cloning / imitation learning from expert trajectories
  + trace-regime balancing
  + action mask
  + classical fallback / safety layer
```

The selected method is **not** a final implemented controller yet. It is the method selected for the next specification block.
Implementation, training and integration remain blocked until Phase 4B/4C/4D are closed.

## Sources of the decision

The decision is based on the completed Phase 4A0/A1 evidence set:

- source cards for all three PDF waves;
- final `../neural_evidence_matrix.md`;
- final `../neural_methods_crosswalk.md`;
- final `../method_feasibility_matrix.md`;
- final `../risk_register.md`;
- hardware constraints for the local machine;
- Phase 3.5 reward/QoE closure.

## Why this method

The selected method is the strongest compromise between scientific evidence and TFG feasibility:

1. **It is own-work friendly.** A small scoring model can be implemented, trained, tested and explained by the student.
2. **It is CPU-first.** It does not require CUDA, ROCm, WSL, Ray/RLlib, TensorFlow 1.x or a large GPU training stack.
3. **It is compatible with DASH.** It scores valid representations instead of inventing arbitrary bitrates.
4. **It is compatible with the existing project.** It can eventually sit behind the controller interface without touching player/runtime/media in this phase.
5. **It is backed by literature.** It combines Pensieve-style state/action/reward, Comyco/SABR-style imitation, ABRL-style candidate scoring, Plume/Oboe/ANT/BETA-style regime awareness, and Puffer/CausalSim/Into-the-Wild humility.
6. **It avoids overclaiming.** It does not assume SOTA, real-world superiority, or guaranteed wins against BBA/MPC/robustMPC.

## Selected method

```text
Name:
  NeuralABR-Lite Candidate Scorer

Learning family:
  Imitation learning / behavior cloning

Policy form:
  Candidate-scoring model with shared weights over valid representations

Teacher family:
  MPC / robustMPC / oracle-limited expert, to be specified in Phase 4B

Reward basis:
  qoe_linear_v1 / reward_n from Phase 3.5

Runtime action:
  representation_index within MPD ladder

Safety:
  action mask + fallback classical controller

Training hardware target:
  CPU-first PyTorch
```

## Alternative retained

The secondary method retained as backup/comparator is:

```text
Fugu-lite predictor + policy
  = supervised predictor for download time / throughput
  + MPC or robust_mpc decision layer
```

It remains useful if behavior cloning proves weak, unstable or hard to justify with available traces.

## Optional extension retained but not selected

```text
BC + very small PPO/A2C fine-tune
```

This is allowed only as a later optional experiment if all gates pass:

- behavior cloning baseline is stable;
- CPU-first training is still feasible;
- reward hacking checks pass;
- validation split is not contaminated;
- extra dependency risk is acceptable;
- the experiment is not required for Phase 4 closure.

## Methods explicitly rejected as Phase 4 base

```text
PPO-first / A3C-first / Pensieve clone
Full meta-RL / MAML / VAE-meta adaptation
Full offline RL
AIRL / learned reward
NMoE / mixture-of-experts / large preference-aware systems
Transformer / LLM-style ABR
Real-world/SOTA claim path
```

These methods remain usable as literature context, future work, or defensive comparison, but not as the base implementation path.

## Gates carried into Phase 4B

Phase 4B must close the following before any implementation prompt exists:

- state representation;
- action space;
- reward usage contract;
- teacher policy contract;
- training data contract;
- trace split and OOD contract;
- leakage prevention rules;
- safety/fallback contract;
- artifact policy for models/datasets/logs.

## What is not happening in A2

- No implementation.
- No training.
- No dataset generation.
- No controller IA integration.
- No Codex implementation prompt.
- No benchmark.
- No ranking.
- No dry-runs legacy as training data.
