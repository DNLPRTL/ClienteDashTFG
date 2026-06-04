# Source card: eastream2026_environment_aware

## Bibliographic data

- Title: EAStream: An Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services
- Authors: Zeming Huang, Wenjing Xiao, Miaojiang Chen, Zhiquan Liu, Min Chen, Athanasios V. Vasilakos, Ahmed Farouk, Houbing Herbert Song
- Year: 2026
- Venue: IEEE Transactions on Services Computing, Vol. 19, No. 2, March/April 2026
- DOI / stable URL: `10.1109/TSC.2026.3671090`
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\EAStream.pdf`

## Method family

- Family: environment-aware meta-reinforcement learning.
- Learning type: VAE latent belief inference + DRL policy.
- Main contribution: infer hidden network dynamics from history and adapt decisions without online fine-tuning.

## State / action / reward

### State

- Physical ABR state plus a latent belief variable.
- The latent belief is inferred from historical interaction data using a VAE-like belief module.
- The decoder predicts state transitions and rewards from the latent belief, forcing the latent space to capture predictive network dynamics.

For DashClientModular4:

- the useful lesson is not full VAE meta-RL, but the need for a compact environment context / regime feature.

### Action

- Discrete bitrate decision through a policy conditioned on current state and latent belief.

For DashClientModular4:

- action must remain `representation_index`.

### Reward / QoE

- RL expected return with a task-inference objective.
- The combined objective trades off expected reward and latent reconstruction through a hyperparameter.

For this TFG:

- reward learning/objective coupling is not adopted;
- Phase 3.5 reward remains the source of truth.

## Model and training

- Belief inference module:
  - recurrent belief encoder;
  - predictive decoder;
  - variational latent variable.
- DRL policy module:
  - policy uses current state plus sampled latent variable.
- Training:
  - combined policy reward + ELBO objective.
- Online behavior:
  - no additional online gradient update required.
- Overhead:
  - belief module overhead reported as 0.0224 MFLOPs;
  - total inference latency reported as 0.2258 ms on Intel i9-13900K, single-threaded;
  - faster than RobustMPC in the reported comparison.

## Data and evaluation

- Diverse real-world network traces.
- In-distribution hybrid test set includes 3G, FCC and 4GSyd.
- OOD test sets include Oboe and 4GNy.
- Evaluation includes QoElin/QoElog CDFs, bitrate behavior under bandwidth drop, ablations and overhead analysis.

## Relevance to DashClientModular4

### What this source justifies

- Neural inference latency can be tiny when the model is small.
- Environment context matters.
- OOD tests must be separated from in-distribution validation.
- A future regime feature or small context encoder is reasonable.

### What this source does NOT justify

- It does not justify implementing VAE/meta-RL in the base TFG method.
- It does not justify online fine-tuning or large training.
- It does not justify replacing the Phase 3.5 reward.

### Risks for this TFG

- Offline meta-training complexity.
- Dependence on diverse training traces.
- Latent belief can be inaccurate on extreme outliers.
- Harder to explain than a supervised candidate scorer.

## Decision impact

- Supports: environment/regime-aware design and OOD validation.
- Blocks: meta-RL/VAE as base implementation.
- Implementation consequence:
  - if the selected method needs a context feature, start with explicit trace-regime features before learned latent variables.

## Memory / thesis usage

- State of the art: 2026 environment-aware ABR.
- Defense: validates CPU inference feasibility but not CPU training feasibility.
- Threats: trace diversity limits generalization.
