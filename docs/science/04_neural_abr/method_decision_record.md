# Method decision record — NeuralABR-Lite Candidate Scorer

Decision ID: `PHASE4A2-MDR-001`  
Status: **Accepted for specification**  
Scope: Phase 4 IA/RL ABR method family  
Implementation status: **not implemented**

## Context

DashClientModular4 already has a stable DASH client, classical ABR controllers, a trace-driven Python pipeline and Phase 3.5 QoE/reward methodology.
Phase 4 must add an IA/ML/RL ABR path that is academically defensible, reproducible, CPU-first and feasible for a TFG.

Hardware constraints:

```text
Windows 11
Intel i5-14600KF
32 GB RAM
AMD RX 7800 XT 16 GB
Python 3.12.8
PyTorch 2.6.0+cpu
CUDA unavailable
torch_directml not installed
WSL not installed
```

Project constraints:

```text
No IA implementation before method/specs.
No dry-runs legacy as training dataset.
No benchmark/ranking in Phase 4.
No claims SOTA/real-world.
No code changes to controllers/player/runtime/media in A2.
```

## Decision drivers

| Driver | Requirement |
|---|---|
| Scientific defensibility | Must be justified by Phase 4A0/A1 evidence. |
| CPU-first feasibility | Must train and infer with small CPU-friendly models. |
| Student ownership | Must be implementable and explainable by the student. |
| DASH compatibility | Must output valid representation choices from MPD ladders. |
| Reproducibility | Must support deterministic seeds, fixed splits and artifact discipline. |
| Leakage resistance | Must separate teacher labels from model inputs and block biased traces. |
| Robust defense | Must be able to explain when IA loses against BBA/MPC. |

## Decision

Select:

```text
NeuralABR-Lite Candidate Scorer
```

The model scores each valid representation candidate using a small shared neural scorer. It does not output arbitrary bitrates.
The final action is the valid `representation_index` with the best safe score after masking/fallback logic.

Training family:

```text
behavior cloning / imitation learning
```

Teacher family, to be specified later:

```text
MPC / robust_mpc / oracle-limited expert trajectories
```

## Rationale

The evidence matrix favors imitation learning and candidate scoring over direct RL.
Comyco/SABR support imitation/pretraining for sample efficiency.
ABRL/Facebook supports scoring available representations instead of fixed bitrate outputs.
Oboe, Plume/Gelato, ANT and BETA support trace-regime awareness and OOD diagnostics.
Puffer/Fugu, CausalSim and Into the Wild impose humility: no simulator-only overclaims, no biased legacy dry-run training, and no real-world claims.
SODA proves that non-IA baselines can be strong, so the method must be evaluated honestly against classical controllers later.

## Consequences

Positive consequences:

- small model feasible on CPU;
- clear `state -> score(candidate) -> action` story;
- output compatible with MPD representation ladders;
- easier defense than PPO-first;
- safer integration path through fallback;
- good material for memory, figures, tables and defense.

Negative consequences:

- may not outperform its teacher;
- may inherit teacher biases;
- may lose against BBA/MPC/robustMPC;
- requires careful split and trace balancing;
- requires strict prevention of future-information leakage.

## Non-decisions

A2 does not decide final feature normalization, exact model size, teacher implementation, trace datasets, loss function details, seeds, or training commands.
Those belong to Phase 4B and 4C.

## Implementation gate

Codex implementation remains blocked until the Phase 4B contract documents exist and are validated.
