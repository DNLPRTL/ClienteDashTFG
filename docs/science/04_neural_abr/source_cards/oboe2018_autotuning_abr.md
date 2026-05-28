# Source card: oboe2018_autotuning_abr

## Bibliographic data

- Title: Oboe: Auto-tuning Video ABR Algorithms to Network Conditions
- Authors: Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, Hui Zhang
- Year: 2018
- Venue: ACM SIGCOMM 2018
- DOI / stable URL: https://doi.org/10.1145/3230543.3230558
- Local PDF: C:\Users\danie\Documents\TFG\_literature\phase4_AI\01_wave1_core_decision\pdfs\Oboe.pdf
- Code URL: not used by this TFG.
- Dataset URL: not adopted directly in Phase 4A1.

## Method family

- Family: auto-tuning / network-regime adaptation / non-neural tuning wrapper.
- Client-side / server-side / hybrid: tuning system for ABR behavior; conceptually compatible with client-side selection.
- Learning type: offline parameter search + online network-state detection.
- Relation to ABR: tunes parameters of existing ABR algorithms such as BOLA, MPC, HYB and RobustMPC to network conditions.

## State / action / reward

### State

Oboe characterizes the current network state, especially throughput level and throughput variability, using the observation that TCP/video sessions often traverse piecewise-stationary network regimes.

### Action

The action is not a bitrate directly. Oboe chooses/tunes a configuration of an underlying ABR algorithm for the current network state.

### Reward / QoE

The objective is composite video QoE, with results reported for QoE-lin and underlying metrics such as bitrate, rebuffering and switching/change magnitude.

## Model and training

- Architecture: no neural ABR controller required.
- Training method: offline search/precomputation of best ABR parameters for network states; online adaptation to detected state.
- Expert / teacher: not a teacher-policy method.
- Online interaction: online state detection and parameter selection.
- Offline data: throughput/network traces for tuning.
- Fine-tuning: parameter tuning, not neural fine-tuning.
- Compute requirements: far lighter than full neural RL; compatible as an inspiration for trace-regime features and split design.

## Data and evaluation

- Datasets / traces: throughput traces and testbed experiments; commercial ABR setting included.
- Train split: offline tuning data.
- Validation split: not reused directly.
- Test split: evaluation across multiple algorithms and network conditions.
- OOD split: not the same as modern OOD, but addresses broad network-state variation.
- Baselines: BOLA, HYB, MPC/RobustMPC, commercial ABR, Pensieve.
- Evaluation type: testbed/trace-driven style experiments.
- Real-world evidence: industrial/commercial context, but not a full replacement for benchmark validation in this TFG.

## Relevance to DashClientModular4

### What this source justifies

- Network regime matters; a single averaged policy can underperform because it does not specialize.
- Trace splits should be stratified by throughput level and variability, not random only.
- NeuralABR-Lite should include regime-aware validation and possibly regime features.
- Existing DashClientModular4 baselines BOLA/MPC/RobustMPC are strong and must not be treated as weak baselines.

### What this source does NOT justify

- It does not require implementing Oboe as the final IA controller.
- It does not justify an overly complex runtime parameter tuner in Phase 4.
- It does not justify claiming that ML always beats tuned classical methods.

### Risks for this TFG

- Leakage risk: low/medium if network regime is computed using future trace statistics at inference time.
- Future-information risk: medium; offline trace clusters must be separated from online runtime features.
- Reward hacking risk: low.
- Overfitting risk: medium if clusters are tuned to validation/test traces.
- Hardware risk: low.
- Dependency risk: low.

## Decision impact

- Method score: high as design constraint.
- Feasibility score: high for trace-regime stratification; medium for full Oboe implementation.
- Defense strength: high.
- Implementation consequence: add trace-regime balancing/splits to Phase 4B/C; do not use a naive random split only.

## Memory / thesis usage

- Chapter: estado del arte ABR clásico/auto-tuning; diseño experimental; amenazas de generalización.
- Figure/table candidate: table of regimes slow/medium/fast x stable/variable.
- Defense point: the proposed IA is not one-size-fits-all; it is trained/validated with regime awareness.

## Phase 4 decision status

This card is part of Phase 4A1 Package 1. It is evidence for method selection, not an implementation order.

Current gate:

- no neural ABR implementation yet;
- no training yet;
- no controller/player/runtime/media changes;
- no benchmark or ranking;
- no dry-run legacy data for training.

