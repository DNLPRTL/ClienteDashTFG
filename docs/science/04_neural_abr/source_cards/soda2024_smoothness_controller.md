# Source card: soda2024_smoothness_controller

## Bibliographic data

- Title: SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
- Authors: Tianyu Chen, Yiheng Lin, Nicolas Christianson, Zahaib Akhtar, Sharath Dharmaji, Mohammad Hajiesmaili, Adam Wierman, Ramesh K. Sitaraman
- Year: 2024
- Venue: ACM SIGCOMM 2024
- DOI / stable URL: https://doi.org/10.1145/3651890.3672260
- Local PDF: SODA.pdf
- Code URL: not used as an implementation dependency for this TFG
- Dataset URL: not used as an implementation dependency for this TFG

## Method family

- Family: non-neural theoretical/control ABR.
- Client-side / server-side / hybrid: client-side controller.
- Learning type: no ML controller; smoothed online convex optimization (SOCO) and efficient horizon planning.
- Relation to ABR: practical ABR controller focused on smoothness, deployability and robustness.

## State / action / reward

### State

SODA uses a time-based formulation rather than a conventional segment-only formulation. Relevant variables include:

- predicted or observed throughput over time intervals;
- selected bitrate for each time interval;
- buffer level after the interval;
- previous bitrate for switching cost;
- available bitrate set.

### Action

Select a bitrate from the available bitrate set for each interval.

### Reward / QoE

SODA formulates a cost with three QoE components:

```text
distortion / video quality cost
+ buffer stability cost
+ bitrate switching cost
```

It deliberately steers the buffer toward a target level instead of directly optimizing a rebuffering-duration term. The switching term explicitly penalizes changes in selected bitrate.

## Model and training

- Architecture: no neural model.
- Training method: no training.
- Expert / teacher: theoretical controller.
- Online interaction: deployable online controller.
- Offline data: used for evaluation, not for training a neural policy.
- Fine-tuning: not applicable.
- Compute requirements: designed for production feasibility; efficient approximate solver searches monotonic bitrate sequences and reduces computational cost versus brute force.

## Data and evaluation

- Datasets / traces: numerical simulations, prototype evaluation and Amazon Prime Video production experiments.
- Train split: not applicable.
- Validation split: not applicable.
- Test split: simulation/prototype/production evaluation.
- OOD split: not an ML split.
- Baselines: includes BOLA, MPC/Fugu-like baselines, RL-based CausalSimRL and production baseline.
- Evaluation type: simulation, prototype and production deployment.
- Real-world evidence: Amazon Prime Video production live streaming experiments; the paper reports up to 88.8% reduction in bitrate switching and up to 5.91% increase in average stream viewing duration compared with a tuned production baseline.

## Relevance to DashClientModular4

### What this source justifies

- Smoothness/switching cannot be treated as an afterthought.
- A non-IA ABR can be highly competitive and deployable.
- NeuralABR-Lite must be evaluated for switching behavior and not just average reward.
- A fallback classical controller is academically justified.
- The IA controller should not hide QoE trade-offs behind an opaque black box.

### What this source does NOT justify

- It does not justify implementing SODA as Phase 4 IA.
- It does not prove that IA is superior.
- It does not justify a benchmark/ranking in Phase 4.
- It does not justify changing Phase 3.5 reward; it reinforces the need to report switching and smoothness.

### Risks for this TFG

- Leakage risk: low.
- Future-information risk: low/medium depending on throughput prediction usage.
- Reward hacking risk: medium if a neural model optimizes reward but causes unstable switching.
- Overfitting risk: low for SODA itself; relevant as a warning for neural ABR.
- Hardware risk: low.
- Dependency risk: low.

## Decision impact

- Method score: 3/3 as comparator and design constraint; 0/3 as IA implementation target.
- Feasibility score: high for using its smoothness insights; not chosen as Phase 4 IA.
- Defense strength: 3/3.
- Implementation consequence: Phase 4 specs must include switching sanity checks and fallback behavior.

## Memory / thesis usage

- Chapter: Estado del arte; Diseño QoE; Evaluación y amenazas.
- Figure/table candidate: QoE trade-off table showing quality/rebuffer/switching.
- Defense point: the TFG does not assume that neural ABR is automatically better than modern control-based ABR.
