# Source card: puffer_fugu2020_learning_in_situ

## Bibliographic data

- Title: Learning in situ: a randomized experiment in video streaming
- Authors: Francis Y. Yan, Hudson Ayers, Chenzhi Zhu, Sadjad Fouladi, James Hong, Keyi Zhang, Philip Levis, Keith Winstein
- Year: 2020
- Venue: USENIX NSDI 2020
- DOI / stable URL: https://www.usenix.org/conference/nsdi20/presentation/yan
- Local PDF: C:\Users\danie\Documents\TFG\_literature\phase4_AI\01_wave1_core_decision\pdfs\Learning_in_situ_Fugu_Puffer.pdf
- Code URL: Puffer publishes data/results; this TFG does not depend on deploying to Puffer.
- Dataset URL: Puffer public data can be investigated later, but no dataset is adopted until `training_data_contract.md`.

## Method family

- Family: supervised predictor + classical control / Fugu / real-world randomized evaluation.
- Client-side / server-side / hybrid: player-side ABR informed by learned transmission-time prediction.
- Learning type: supervised learning in situ for a probabilistic transmission time predictor; MPC-style controller uses the prediction.
- Relation to ABR: learned component is deliberately narrow and checkable soon after prediction.

## State / action / reward

### State

Fugu's learned predictor uses deployment telemetry. Important reported signal types include:

- candidate chunk file size;
- low-level TCP/congestion-control statistics such as RTT-style information;
- information available soon enough to predict upcoming chunk transmission time.

The exact Fugu feature set is not adopted directly because DashClientModular4 does not currently depend on low-level TCP telemetry.

### Action

The predictor does not output a bitrate action directly. It outputs a probabilistic prediction of upcoming chunk transmission time; an MPC-like classical policy chooses the bitrate/representation.

### Reward / QoE

The paper evaluates practical QoE metrics including SSIM quality, stall fraction, SSIM variation and time-on-site/session duration.

## Model and training

- Architecture: supervised neural predictor for transmission time distribution.
- Training method: supervised learning on in-situ deployment data.
- Expert / teacher: no behavior cloning expert; the learned module is a predictor.
- Online interaction: real randomized deployment on Puffer.
- Offline data: deployment data from Puffer; not equivalent to replaying arbitrary traces.
- Fine-tuning: continuous in-situ learning is a theme, but not adopted here.
- Compute requirements: realistic for a deployed platform; not directly reproducible as a TFG deployment.

## Data and evaluation

- Datasets / traces: Puffer deployment data; over 38.6 years of video to 63,508 users overall; primary experiment includes 637,189 streams, 54,612 client IP addresses and 13.1 stream-years.
- Train split: in-situ deployment data.
- Validation split: real randomized/blinded experiment rather than simple offline validation.
- Test split: production randomized trial.
- OOD split: real traffic variation; still geographically/platform limited.
- Baselines: BBA, MPC-HM, RobustMPC-HM, Pensieve, Fugu.
- Evaluation type: real-world randomized controlled trial.
- Real-world evidence: very strong for Puffer's environment.

## Relevance to DashClientModular4

### What this source justifies

- Learned ABR should be humble: ML can fail to beat simple buffer-based control in real settings.
- A narrow supervised module plus a classical controller can be more defensible than end-to-end RL.
- Representative training data is the central challenge.
- ML predictions should be checkable soon after use.
- BBA/MPC/RobustMPC must be treated as serious baselines.

### What this source does NOT justify

- It does not justify claiming `real-world validation` for DashClientModular4 unless we deploy globally, which we will not do in Phase 4.
- It does not justify using Puffer-style in-situ claims from local dry-runs.
- It does not justify using legacy dry-runs as a training dataset.
- It does not force us to implement Fugu; it gives a strong alternative design pattern.

### Risks for this TFG

- Leakage risk: medium if deployment-style telemetry is simulated incorrectly.
- Future-information risk: low/medium for predictor features, but high if future chunk outcomes are used as inputs.
- Reward hacking risk: low for predictor-only module, medium for MPC objective tuning.
- Overfitting risk: high if training traces are narrow.
- Hardware risk: low for predictor; low/medium for full real-world pipeline.
- Dependency risk: medium if trying to reproduce Puffer infrastructure.

## Decision impact

- Method score: high as alternative design path.
- Feasibility score: high for `predictor + policy` as a fallback candidate; medium for full Fugu reproduction.
- Defense strength: very high.
- Implementation consequence: keep Fugu-lite as an alternative in method decision; use this source to block exaggerated claims.

## Memory / thesis usage

- Chapter: estado del arte real-world; amenazas a la validez; diseño alternativo predictor+policy.
- Figure/table candidate: comparison of direct RL vs predictor+MPC vs imitation learning.
- Defense point: the project is academically stronger because it accepts that IA may lose to BBA/MPC in some regimes.

## Phase 4 decision status

This card is part of Phase 4A1 Package 1. It is evidence for method selection, not an implementation order.

Current gate:

- no neural ABR implementation yet;
- no training yet;
- no controller/player/runtime/media changes;
- no benchmark or ranking;
- no dry-run legacy data for training.

