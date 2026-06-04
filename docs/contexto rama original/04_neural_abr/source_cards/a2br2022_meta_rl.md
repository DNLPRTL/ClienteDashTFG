# Source card: a2br2022_meta_rl

## Bibliographic data

- Title: Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach
- Authors: Tianchi Huang, Chao Zhou, Rui-Xiao Zhang, Chenglei Wu, Lifeng Sun
- Year: 2022
- Venue: IEEE Journal on Selected Areas in Communications, Vol. 40, No. 8
- DOI / stable URL: https://doi.org/10.1109/JSAC.2022.3180804
- Local PDF: C:\Users\danie\Documents\TFG\_literature\phase4_AI\01_wave1_core_decision\pdfs\A2BR.pdf
- Code URL: not adopted in Phase 4A1.
- Dataset URL: not adopted yet.

## Method family

- Family: meta-reinforcement learning / IMDP / domain-specific priors.
- Client-side / server-side / hybrid: ABR policy intended for personalized network conditions.
- Learning type: offline meta-learning plus online few-shot adaptation.
- Relation to ABR: adapts policy to heterogeneous network conditions and user preferences.

## State / action / reward

### State

A2BR first trains a teacher with many possible features and prunes using a lightweight model. Its final state uses 5 metrics and 17 critic features:

- past video quality;
- current buffer occupancy;
- past `k` chunk throughputs;
- past `k` chunk download times;
- past `k` chunk response times.

The paper sets `k = 5` to reduce state size and normalizes statistics to improve generalization.

### Action

Discrete action space: an `n`-dimensional actor output giving the probability of selecting each bitrate level. Critic output is a scalar state value.

### Reward / QoE

Uses accumulated QoE/reward in a meta-RL/PPO formulation with entropy. The exact paper reward does not replace DashClientModular4 `reward_n`.

## Model and training

- Architecture: actor-critic neural network; Conv1D layers for throughput/download/response-time sequences; fully connected layers for quality/buffer; softmax actor output and scalar critic output.
- Training method: meta-RL with MAML-style offline meta-model and online adaptation; maximum-entropy PPO / dual-clip PPO variant.
- Expert / teacher: teacher network and feature pruning are part of design, not the final TFG teacher policy.
- Online interaction: explicit online stage for continual adaptation.
- Offline data: heterogeneous network environments/traces.
- Fine-tuning: central to paper, but not selected for base TFG implementation.
- Compute requirements: too complex as direct implementation under CPU-first constraints.

## Data and evaluation

- Datasets / traces: trace-driven experiments across vehicles, users, network types and heterogeneous preferences; testbed experiments for unseen environments.
- Train split: multiple network conditions/tasks for meta-training.
- Validation split: not reused directly.
- Test split: unseen/environments in trace/testbed.
- OOD split: strong conceptual relevance.
- Baselines: recent ABR approaches including heuristic and learning-based methods.
- Evaluation type: trace-driven plus testbed.
- Real-world evidence: testbed-level, not broad global deployment.

## Relevance to DashClientModular4

### What this source justifies

- Heterogeneous networks should be treated as a core design problem.
- A compact state with `k = 5` is defensible for CPU-first NeuralABR-Lite.
- Normalization of state features is required.
- Meta-RL literature supports regime-aware validation and adaptation discussion.

### What this source does NOT justify

- It does not justify implementing MAML/meta-RL as the base TFG method.
- It does not justify online gradient adaptation in the player.
- It does not justify adding PPO before the evidence matrix is closed.

### Risks for this TFG

- Leakage risk: medium due to feature engineering/teacher pipeline.
- Future-information risk: medium if bitrate/chunk maps are used incorrectly.
- Reward hacking risk: high for direct RL/fine-tuning.
- Overfitting risk: medium/high despite meta-learning.
- Hardware risk: high for full reproduction.
- Dependency risk: medium/high.

## Decision impact

- Method score: medium/high as generalization evidence.
- Feasibility score: low as direct implementation; high as source of state-design constraints.
- Defense strength: high.
- Implementation consequence: use `k = 5`/normalized temporal features as a candidate; do not implement full A2BR.

## Memory / thesis usage

- Chapter: generalización, redes heterogéneas, meta-RL.
- Figure/table candidate: methods crosswalk showing why meta-RL is scientifically relevant but not base implementation.
- Defense point: the TFG consciously limits scope while preserving the key insight: adaptation/generalization matters.

## Phase 4 decision status

This card is part of Phase 4A1 Package 1. It is evidence for method selection, not an implementation order.

Current gate:

- no neural ABR implementation yet;
- no training yet;
- no controller/player/runtime/media changes;
- no benchmark or ranking;
- no dry-run legacy data for training.
