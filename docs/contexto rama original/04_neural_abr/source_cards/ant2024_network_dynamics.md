# Source card: ant2024_network_dynamics

## Bibliographic data

- Title: Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming
- Authors: Jiaoyang Yin, Hao Chen, Yiling Xu, Zhan Ma, Xiaozhong Xu
- Year: 2024
- Venue: IEEE Transactions on Broadcasting, Vol. 70, No. 3, September 2024
- DOI / stable URL: `10.1109/TBC.2024.3396698`
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\ANT.pdf`

## Method family

- Family: network-dynamics detection + condition-wise multi-model ABR.
- Learning type: 1D-CNN network-condition classifier + multiple RL ABR models.
- Main contribution: characterize temporal throughput dynamics more accurately than mean/std and dynamically switch among dedicated ABR models.

## State / action / reward

### State

ANT separates:

- network condition input:
  - historical raw-throughput sequence;
  - learned temporal dynamics;
  - distance to clustering centers / cluster label;
- player/ABR state:
  - network statistics;
  - client-side playback status such as buffer occupancy.

The paper states that the ABR model state input, neural network structure and reward function remain consistent with Pensieve.

### Action

- Bitrate decision via a selected condition-wise ABR model.

For DashClientModular4:

- action must be `representation_index`.

### Reward / QoE

- General QoE metric:
  - quality term;
  - rebuffering penalty;
  - smoothness/switching penalty.
- Pensieve-consistent training reward.

For this TFG:

- use `qoe_linear_v1 / reward_n`.

## Model and training

- Unsupervised K-means clustering generates network condition labels.
- A 1D-CNN detects current network condition from historical throughput.
- Multiple RL-based ABR models are trained separately for each condition.
- At inference, the detector selects the appropriate model.

## Data and evaluation

- Real-world trace segments.
- Simulations and field tests.
- Reported QoE improvement:
  - 20.8%–41.2% for VoD;
  - 67.4%–134.5% for live streaming.

## Relevance to DashClientModular4

### What this source justifies

- Mean/std throughput alone may be insufficient.
- Trace-regime detection or clustering should be in the TFG evidence matrix.
- Validation must include dynamic regime changes, not only average throughput.

### What this source does NOT justify

- It does not justify training multiple DRL controllers in this TFG.
- It does not justify a server-side ABR architecture for the local client project.
- It does not justify using a 1D-CNN detector as a required dependency.

### Risks for this TFG

- Multi-model RL is too heavy.
- Condition labels may be unstable with small trace sets.
- Detector errors can cause wrong policy selection.
- Server/client boundary may not match DashClientModular4.

## Decision impact

- Supports: explicit trace-regime features and stratified split.
- Blocks: single average train/test split as sufficient.
- Implementation consequence:
  - create a lightweight trace-regime analysis in specs;
  - do not implement full ANT.

## Memory / thesis usage

- Generalization/OOD discussion.
- Figure candidate: trace-regime clustering / condition detection.
- Defense: explains why the TFG will balance traces and evaluate difficult cases.
