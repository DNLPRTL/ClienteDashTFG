# Source card: metaabr2024_meta_learning

## Bibliographic data

- Title: MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming
- Authors: Wenzhong Li, Xiang Li, Yeting Xu, Yi Yang, Sanglu Lu
- Year: 2024
- Venue: IEEE Transactions on Mobile Computing, Vol. 23, No. 3
- DOI / stable URL: https://doi.org/10.1109/TMC.2023.3260086
- Local PDF: MetaABR.pdf
- Code URL: not used as implementation dependency
- Dataset URL: not used as implementation dependency

## Method family

- Family: meta-reinforcement learning ABR.
- Client-side / server-side / hybrid: client-side ABR decision model in emulation/testbed context.
- Learning type: A3C-style DRL with a meta-learning framework and shared meta-critic.
- Relation to ABR: direct bitrate selection.

## State / action / reward

### State

MetaABR formulates ABR as a DRL task with state:

```text
s_t = (x_t, tau_t, n_t, b_t, c_t, l_t)
```

where:

- `x_t`: network throughput measurements for the past `k` video chunks;
- `tau_t`: download time of the past `k` chunks;
- `n_t`: vector of available sizes for the next video chunk;
- `b_t`: current buffer level;
- `c_t`: number of chunks remaining;
- `l_t`: bitrate of the last downloaded chunk.

### Action

The action is the bitrate selected for the next chunk.

### Reward / QoE

Reward is a comprehensive QoE metric. The paper evaluates multiple QoE objectives, including a standard QoE metric, a fluency-oriented metric with higher rebuffering penalty and an HD-oriented metric.

## Model and training

- Architecture: task-config network, critic network and actor network; three-layer fully connected networks with ReLU.
- Training method: meta-RL with multiple actors and shared meta-critic; A3C-like learning.
- Expert / teacher: none.
- Online interaction: evaluated in emulation and wireless testbed; few-shot adaptation concept.
- Offline data: 3G, WiFi, 4G Sydney and hybrid traces for training; 4G New York and 5G traces used as unseen environments.
- Fine-tuning: meta-adaptation to unseen environment.
- Compute requirements: TensorFlow 1.13.1 in the paper; not aligned with Python 3.12 / PyTorch CPU-first as an implementation base.

## Data and evaluation

- Datasets / traces: 3G, WiFi, 4GSyd, hybrid, 4GNY and 5G throughput traces.
- Train split: 80% train / 20% test by default for generated traces.
- Validation split: 20% of the train set for hyperparameter tuning.
- Test split: 20% test plus unseen 4GNY/5G sets.
- OOD split: 4GNY and 5G used for adaptivity and knowledge transfer.
- Baselines: BBA, RobustMPC, Pensieve and related state-of-the-art ABR algorithms.
- Evaluation type: Mahimahi emulation plus wireless testbed.
- Real-world evidence: testbed evidence, not global real-world production.

## Relevance to DashClientModular4

### What this source justifies

- A serious Phase 4 design needs explicit OOD/generalization splits.
- State features similar to Pensieve remain useful: throughput history, download time history, next chunk sizes, buffer, chunks remaining and last bitrate.
- Multiple QoE objectives can expose different behavior; Phase 3.5 reward must be fixed/versioned.
- Stable high-throughput networks can produce trivial solutions; IA may add little under near-perfect connectivity.

### What this source does NOT justify

- It does not justify implementing full meta-RL in this TFG.
- It does not justify TensorFlow 1.x or old stacks.
- It does not justify online adaptation in the player before a safe contract exists.
- It does not justify using test traces for hyperparameter tuning.

### Risks for this TFG

- Leakage risk: medium if train/test/OOD are not separated.
- Future-information risk: medium due to next-chunk size vectors; acceptable only if available from MPD/media metadata.
- Reward hacking risk: medium/high for direct RL.
- Overfitting risk: high under mixed datasets without regime-aware validation.
- Hardware risk: medium/high.
- Dependency risk: high if cloned.

## Decision impact

- Method score: 3/3 for generalization/OOD design; 1/3 for direct implementation.
- Feasibility score: 1/3 as base method, 3/3 as source of state/split design.
- Defense strength: 3/3.
- Implementation consequence: trace split contract must include held-out regime/OOD diagnostics.

## Memory / thesis usage

- Chapter: Estado del arte; Diseño experimental; Amenazas.
- Figure/table candidate: train/validation/OOD split by network family.
- Defense point: IA can fail to generalize unless the evaluation deliberately tests unseen regimes.
