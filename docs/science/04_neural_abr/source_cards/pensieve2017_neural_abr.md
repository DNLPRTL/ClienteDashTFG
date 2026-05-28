# Source card: pensieve2017_neural_abr

## Bibliographic data

- Title: Neural Adaptive Video Streaming with Pensieve
- Authors: Hongzi Mao, Ravi Netravali, Mohammad Alizadeh
- Year: 2017
- Venue: ACM SIGCOMM 2017
- DOI / stable URL: http://dx.doi.org/10.1145/3098822.3098843
- Local PDF: C:\Users\danie\Documents\TFG\_literature\phase4_AI\01_wave1_core_decision\pdfs\Pensieve.pdf
- Code URL: historical public implementations exist, but this TFG must not clone a legacy TensorFlow stack.
- Dataset URL: not adopted directly in Phase 4A1; traces must be decided later under the training data contract.

## Method family

- Family: reinforcement learning / actor-critic / A3C neural ABR.
- Client-side / server-side / hybrid: ABR decisions are for the client/player; the paper also describes serving neural decisions from an ABR server to reduce client compute.
- Learning type: online-style RL training in a simulator; learned policy used for bitrate decisions.
- Relation to ABR: foundational neural ABR reference that maps client observations to a discrete bitrate action.

## State / action / reward

### State

Pensieve uses an explicit ABR state after each downloaded chunk:

- past network throughput measurements for the last `k` chunks;
- download time for the last `k` chunks;
- available sizes for the next video chunk;
- current playback buffer level;
- number of chunks remaining;
- bitrate selected for the previous chunk.

The implementation uses `k = 8` past bandwidth measurements and feeds throughput history and next chunk sizes through 1D convolutional layers.

### Action

Discrete bitrate/representation selection for the next chunk. The multi-video extension uses a mask so that the softmax only assigns probability to bitrate levels actually supported by the current video.

### Reward / QoE

Pensieve optimizes a QoE objective of the form:

```text
QoE = sum(q(R_n)) - mu * sum(rebuffer_time_n) - sum(abs(q(R_{n+1}) - q(R_n)))
```

The paper evaluates variants such as linear bitrate utility, logarithmic utility, and an HD-favoring mapping. This aligns conceptually with DashClientModular4 Phase 3.5 `qoe_linear_v1`, but does not override it.

## Model and training

- Architecture: actor-critic network; 1D-CNN for throughput history and chunk sizes, hidden layer with 128 neurons, softmax actor output, scalar critic output.
- Training method: A3C with entropy regularization; multiple parallel agents; chunk-level simulator.
- Expert / teacher: none; learns by RL reward feedback.
- Online interaction: simulation/training interaction; deployment can query trained policy.
- Offline data: network traces for simulator training.
- Fine-tuning: not the route selected for Phase 4A1.
- Compute requirements: original training uses TensorFlow/TFLearn and parallel agents; not appropriate to clone as-is for a Python 3.12 CPU-first TFG.

## Data and evaluation

- Datasets / traces: FCC broadband traces, Norway HSDPA mobile traces, synthetic traces, and real-world/system experiments.
- Train split: paper reports training on trace corpus; exact split is not reused here.
- Validation split: not reused here.
- Test split: trace-driven and real-world experiments.
- OOD split: reports generalization to unseen network conditions/video properties, but later literature weakens any universal generalization claim.
- Baselines: rate-based, buffer-based/BBA, MPC, RobustMPC, offline optimal, tabular RL variants.
- Evaluation type: trace-driven simulation/emulation plus real-world/system experiments.
- Real-world evidence: present, but later Puffer/Fugu and Into-the-Wild style work warns that gains may not generalize broadly.

## Relevance to DashClientModular4

### What this source justifies

- Neural ABR can be formulated cleanly as state -> action -> reward.
- State should include observable client context: throughput/download history, buffer, previous action, chunk-size information if available without leakage.
- Action must be a valid representation/bitrate level, not an arbitrary bitrate.
- Reward should explicitly balance quality, rebuffering and smoothness.
- Action masking is relevant when the available ladder differs by video.

### What this source does NOT justify

- It does not justify choosing PPO/A3C by inertia.
- It does not justify using TensorFlow/TFLearn legacy code.
- It does not justify claiming SOTA.
- It does not justify training on DashClientModular4 dry-runs.
- It does not prove that a neural controller beats BBA/MPC in real deployments.

### Risks for this TFG

- Leakage risk: medium if chunk-size or future information is mishandled.
- Future-information risk: medium; next chunk sizes may be valid only if available from MPD/media metadata.
- Reward hacking risk: high for direct RL if reward is optimized without behavioral sanity gates.
- Overfitting risk: high if trace corpus is narrow.
- Hardware risk: medium/high if copied as RL training rather than used as conceptual reference.
- Dependency risk: high if attempting to reuse the original stack.

## Decision impact

- Method score: high as conceptual foundation.
- Feasibility score: medium/low as direct implementation.
- Defense strength: high.
- Implementation consequence: use its state/action/reward framing, action masking and history length ideas; do not clone its RL pipeline.

## Memory / thesis usage

- Chapter: Estado del arte; diseño de IA ABR; reward/QoE.
- Figure/table candidate: neural ABR loop state -> policy -> action -> reward.
- Defense point: Pensieve is seminal, but the project chooses a safer CPU-first design after later evidence.

## Phase 4 decision status

This card is part of Phase 4A1 Package 1. It is evidence for method selection, not an implementation order.

Current gate:

- no neural ABR implementation yet;
- no training yet;
- no controller/player/runtime/media changes;
- no benchmark or ranking;
- no dry-run legacy data for training.

