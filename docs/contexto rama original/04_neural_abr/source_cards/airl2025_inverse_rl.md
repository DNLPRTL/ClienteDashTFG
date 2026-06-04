# Source card: airl2025_inverse_rl

## Bibliographic data

- Title: Learning Robust Adaptive Bitrate Algorithms with Adversarial Inverse Reinforcement Learning
- Authors: Ling Yi, Yongbin Qin
- Year: 2025
- Venue: Chinese Journal of Electronics, Vol. 34, No. 4, pp. 1309–1320
- DOI / stable URL: `10.23919/cje.2024.00.202`
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\AIRL.pdf`

## Method family

- Family: adversarial inverse reinforcement learning.
- Learning type: expert demonstrations + adversarial discriminator + policy update.
- Main contribution: learn a robust reward function and ABR policy from expert behavior while decoupling reward from dynamics.

## State / action / reward

### State

The paper's training methodology lists six state variables:

- throughput;
- chunk download time;
- next chunk sizes;
- buffer size;
- remaining chunks;
- chunk bitrate.

These match the core Phase 4 state candidates, but the next chunk sizes must be available through a valid artifact/MPD contract to avoid future-information leakage.

### Action

- Bitrate of the next video chunk.
- The paper uses a final-softmax action mask so that only bitrates supported by the video receive probability mass.

For DashClientModular4:

- this supports a hard action mask over valid `representation_index` values.

### Reward / QoE

- AIRL learns/infer rewards from the discriminator.
- The paper modifies the GAIL/AIRL discriminator to reduce undesired reward shaping and disentangle rewards from video dynamics.
- It then updates the policy using a duel-PPO-style policy optimization step.

For this TFG:

- reward learning is not selected because Phase 3.5 already fixed `qoe_linear_v1 / reward_n`.

## Model and training

- Generator/policy and discriminator.
- Same network structure for generator and discriminator:
  - one hidden layer;
  - 128 convolution kernels;
  - fully connected network;
  - kernel size 4;
  - stride 1.
- Alternates:
  - collect trajectories;
  - train discriminator to distinguish expert from generated samples;
  - infer reward;
  - update policy.

## Data and evaluation

- Heterogeneous network environments.
- Expert demonstrations are required.
- Experiments across network conditions.

## Relevance to DashClientModular4

### What this source justifies

- Expert demonstrations are a valid scientific input for ABR learning.
- Action masks are important for valid bitrate/representation choices.
- Reward-shaping and reward-learning risks are real and must be documented.

### What this source does NOT justify

- It does not justify replacing Phase 3.5 reward with a learned reward.
- It does not justify AIRL as the base implementation.
- It does not justify duel-PPO as a required dependency.
- It does not justify using future data in model features.

### Risks for this TFG

- Conflicts with the already closed QoE/reward contract.
- High implementation complexity.
- Harder to explain and reproduce than behavior cloning.
- More opportunities for reward hacking.

## Decision impact

- Supports: imitation/expert-demonstration direction.
- Strongly blocks: learned reward as Phase 4 base.
- Implementation consequence:
  - use AIRL as evidence in the risk register and future work, not as the selected method.

## Memory / thesis usage

- State of the art: inverse RL branch.
- Risk register: reward hacking, reward shaping and expert leakage.
- Defense: explains why fixing reward before training was correct.
