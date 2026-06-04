# Source card: merina2022_meta_rl_generalization

## Bibliographic data

- Title: Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning
- Authors: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, Hongkai Xiong
- Year: 2022
- Venue: ACM Multimedia 2022
- DOI / stable URL: https://doi.org/10.1145/3503161.3548331
- Local PDF: C:\Users\danie\Documents\TFG\_literature\phase4_AI\01_wave1_core_decision\pdfs\MERINA.pdf
- Code URL: not adopted in Phase 4A1.
- Dataset URL: not adopted yet.

## Method family

- Family: context-based meta-RL / latent dynamics inference.
- Client-side / server-side / hybrid: policy is for ABR decisions; training/adaptation is research-system oriented.
- Learning type: model-free meta-RL with latent encoder and latent-conditioned policy; policy can be trained via policy-gradient RL or imitation learning.
- Relation to ABR: handles changing throughput dynamics as latent context.

## State / action / reward

### State

MERINA treats the adaptive video streaming problem as a POMDP-like setting with latent throughput dynamics. The policy state includes the normal video streaming features, while an inference network uses recent throughput context to infer a latent variable `z`.

Implementation details report:

- throughput context from previous `p = 8` chunks;
- average throughput values and time intervals of throughput measurements;
- policy features including available bitrate versions, last measured average throughput, last download duration, current buffer, previous selected bitrate and chunks remaining.

### Action

Discrete bitrate/representation selection through an actor policy conditioned on state and latent variable `z`.

### Reward / QoE

Uses ABR QoE reward in meta-RL evaluation. It does not override DashClientModular4 `reward_n`.

## Model and training

- Architecture: probabilistic latent encoder for throughput dynamics; latent-conditioned actor and critic networks.
- Training method: model-free meta-RL; mutual-information regularization to make latent variable informative for policy; adaptation epochs in new dynamics.
- Expert / teacher: can use on-policy RL or imitation learning; not fixed to a simple teacher policy.
- Online interaction: adaptation to new throughput dynamics with few trials/epochs.
- Offline data: multiple trace datasets with varying dynamics.
- Fine-tuning: meta-adaptation is central.
- Compute requirements: paper implementation uses PyTorch 1.9, 40-core Intel Xeon Silver 4114, 64GB RAM, NVIDIA RTX 2080; GPU used for efficiency, though CPU training is stated possible.

## Data and evaluation

- Datasets / traces: multiple datasets including Puffer slices; real-world platform evaluation is reported.
- Train split: throughput-dynamics tasks for meta-training.
- Validation split: adaptation curves and dataset-specific evaluation.
- Test split: different datasets/throughput patterns.
- OOD split: strong generalization focus.
- Baselines: RobustMPC, BOLA, Comyco and other neural/classical baselines.
- Evaluation type: trace-driven plus real-world/platform-style validation.
- Real-world evidence: limited but present.

## Relevance to DashClientModular4

### What this source justifies

- ABR is partially observable: recent throughput samples may not fully reveal network dynamics.
- Context windows of 5-8 chunks are defensible candidates.
- OOD/generalization validation is mandatory.
- A small policy can be conditioned on temporal context, but a full latent meta-RL system is not required.

### What this source does NOT justify

- It does not justify implementing MERINA full meta-RL under CPU-first constraints.
- It does not justify online adaptation inside DashClientModular4 player.
- It does not justify using GPU-dependent training as a TFG gate.

### Risks for this TFG

- Leakage risk: medium if context or evaluation tasks are mixed incorrectly.
- Future-information risk: medium.
- Reward hacking risk: high for direct RL.
- Overfitting risk: medium/high; mitigated by OOD design, not eliminated.
- Hardware risk: high for full reproduction.
- Dependency risk: medium.

## Decision impact

- Method score: high as OOD/generalization evidence.
- Feasibility score: low as direct implementation, medium as design inspiration.
- Defense strength: high.
- Implementation consequence: include OOD diagnostics and temporal context; do not build full latent meta-RL in base Phase 4.

## Memory / thesis usage

- Chapter: generalización; POMDP/partial observability; límites del diseño.
- Figure/table candidate: latent-context idea vs simplified NeuralABR-Lite context features.
- Defense point: the project knows why meta-RL exists and deliberately chooses a smaller reproducible approximation.

## Phase 4 decision status

This card is part of Phase 4A1 Package 1. It is evidence for method selection, not an implementation order.

Current gate:

- no neural ABR implementation yet;
- no training yet;
- no controller/player/runtime/media changes;
- no benchmark or ranking;
- no dry-run legacy data for training.
