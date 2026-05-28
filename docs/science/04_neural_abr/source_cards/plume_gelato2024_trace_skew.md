# Source card: plume_gelato2024_trace_skew

## Bibliographic data

- Title: Practically High Performant Neural Adaptive Video Streaming
- Authors: Sagar Patel, Junyang Zhang, Nina Narodystka, Sangeetha Abdu Jyothi
- Year: 2024
- Venue: Proceedings of the ACM on Networking, CoNEXT4, Article 30
- DOI / stable URL: https://doi.org/10.1145/3696401
- Local PDF: C:\Users\danie\Documents\TFG\_literature\phase4_AI\01_wave1_core_decision\pdfs\Gelato.pdf
- Code URL: not adopted in Phase 4A1.
- Dataset URL: Puffer-related public data may be investigated later; not adopted until training data contract.

## Method family

- Family: DRL ABR + trace distribution balancing framework.
- Client-side / server-side / hybrid: ABR controller evaluated on Puffer platform.
- Learning type: deep RL controller Gelato trained with Plume trace skew balancing/prioritization.
- Relation to ABR: current frontier evidence that trace distribution skew can dominate DRL training behavior.

## State / action / reward

### State

Gelato uses rich application-level features. The appendix reports frame-stacking with 10 past values for client data and 5 future values of chunk sizes and SSIMs at every encoded bitrate. Plume operates above the controller by characterizing traces with features such as central tendency and spread:

- mean and quantiles;
- truncated means;
- spectral centroid;
- coefficient of variation;
- mean absolute change;
- autocorrelation at multiple lags;
- ratios beyond standard-deviation thresholds.

For DashClientModular4, the reusable part is trace characterization and balanced sampling, not Gelato's full feature set.

### Action

Discrete ABR bitrate/representation decision.

### Reward / QoE

Optimizes SSIM-based QoE with reward coefficients from Fugu: quality, stalls and delta-quality/smoothness. Rewards are normalized/clipped in training. DashClientModular4 keeps Phase 3.5 `reward_n` instead.

## Model and training

- Architecture: Gelato neural ABR controller; Plume is a generalized framework for trace skew identification, clustering and prioritization.
- Training method: DRL with trace cluster prioritization; dynamic/static Plume variants.
- Expert / teacher: not imitation learning.
- Online interaction: evaluated on Puffer live platform over long period.
- Offline data: trace datasets / Puffer logs.
- Fine-tuning: not selected as base.
- Compute requirements: direct reproduction is too heavy for CPU-first TFG; inference is reported as cheap, but training scale is not acceptable as a base gate.

## Data and evaluation

- Datasets / traces: Puffer plus trace datasets; paper reports over a year on Puffer, 59 stream-years and over 280,000 users.
- Train split: skew-aware training distribution.
- Validation split: not reused directly.
- Test split: simulated and real-world Puffer evaluation.
- OOD split: trace-distribution robustness focus.
- Baselines: state-of-the-art ABR controllers on Puffer and simulation.
- Evaluation type: real-world and simulated.
- Real-world evidence: very strong for Puffer environment.

## Relevance to DashClientModular4

### What this source justifies

- Trace distribution skew is a first-class problem, not a minor nuisance.
- Training/validation splits must be stratified or at least audited by trace regime.
- NeuralABR-Lite should use a trace-regime balancing plan inspired by Plume, but scaled down.
- Inference of a neural controller can be fast; training is the bottleneck.

### What this source does NOT justify

- It does not justify cloning Gelato.
- It does not justify DRL training with hundreds of millions of steps in a TFG.
- It does not justify requiring Puffer-scale data.
- It does not justify using SSIM/VMAF in DashClientModular4 runtime while VMAF remains deferred.

### Risks for this TFG

- Leakage risk: medium if trace clusters are computed using test/OOD data during training decisions.
- Future-information risk: high if future SSIM/chunk-size inputs are used online without availability contract.
- Reward hacking risk: high in full DRL reproduction.
- Overfitting risk: high without trace balancing; reduced by Plume-like sampling.
- Hardware risk: BLOCK for full training reproduction; low for small trace clustering.
- Dependency risk: medium/high for full reproduction.

## Decision impact

- Method score: high as trace-balancing evidence.
- Feasibility score: high for mini-Plume trace audit; low for full Gelato.
- Defense strength: very high.
- Implementation consequence: add a CPU-first mini-Plume trace characterization/sampling layer to future specs; do not adopt full Gelato DRL.

## Memory / thesis usage

- Chapter: frontera reciente; distribución de trazas; diseño experimental.
- Figure/table candidate: trace clustering features and balanced split diagram.
- Defense point: the project uses the latest evidence where it matters most: data distribution, not huge models.

## Phase 4 decision status

This card is part of Phase 4A1 Package 1. It is evidence for method selection, not an implementation order.

Current gate:

- no neural ABR implementation yet;
- no training yet;
- no controller/player/runtime/media changes;
- no benchmark or ranking;
- no dry-run legacy data for training.

