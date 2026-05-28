# Source card: nmoeabr2026_mixture_of_experts

## Bibliographic data

- Title: Generalizing Adaptive Video Streaming with Mixture of Experts in Heterogeneous Wireless Networks
- Authors: Shuoyao Wang, Boyuan Li, Xiaowen Cao, Lifeng Xie
- Year: 2026
- Venue: IEEE Transactions on Mobile Computing, accepted author version in uploaded PDF
- DOI / stable URL: `10.1109/TMC.2026.3665094`
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\NMoEABR.pdf`

## Method family

- Family: nonlinear mixture of experts + preference-aware meta-reinforcement learning.
- Learning type: actor-critic/PPO-based meta-RL with dynamic expert fusion.
- Main contribution: cross-network generalization under heterogeneous wireless conditions and user preference diversity.

## State / action / reward

### State

- Real-time network state and user preference context.
- State and preference inputs drive dynamic convolution/expert weighting.

For DashClientModular4:

- user preference embeddings are not part of the current scope;
- network-state conditioning is relevant only as trace-regime features.

### Action

- Bitrate decision.

For DashClientModular4:

- must be mapped to a valid MPD representation index.

### Reward / QoE

- Immediate reward/utility `v_i(s_i, a_i)` with entropy-regularized cumulative reward.
- Preference-aware QoE objective.

For this TFG:

- do not introduce preference-aware reward unless Phase 3.5 is explicitly versioned; use `qoe_linear_v1 / reward_n`.

## Model and training

- Actor-critic architecture.
- NMoE-based actor.
- Nonlinear expert fusion through dynamic convolution.
- Single dynamically fused inference path instead of evaluating all experts in parallel.
- Preference-aware meta-RL strategy.
- PPO-style actor/critic optimization.

## Data and evaluation

- Real-world traces and wireless testbed.
- Claims improved average QoE, stability and adaptability under unseen network conditions and diverse user preference distributions.

## Relevance to DashClientModular4

### What this source justifies

- Heterogeneity and user preference are active 2026 research directions.
- Expert specialization can improve generalization.
- Single-path expert fusion is one way to make MoE feasible for inference.

### What this source does NOT justify

- It does not justify a MoE/large model in this TFG.
- It does not justify adding user preference objectives.
- It does not justify PPO as a base.

### Risks for this TFG

- Too complex for CPU-first implementation.
- Too hard to validate with available traces.
- Preference-aware evaluation requires user QoE objectives not present in Phase 3.5.
- Dynamic convolution/MoE increases code and defense complexity.

## Decision impact

- Supports: discussion of frontier 2026 and the importance of heterogeneity.
- Blocks: NMoEABR clone.
- Implementation consequence:
  - use as future-work evidence;
  - keep NeuralABR-Lite single-small-model or simple candidate scorer.

## Memory / thesis usage

- Frontier recent work section.
- Future work: preference-aware ABR and MoE.
- Defense: justifies why the TFG is intentionally simpler.
