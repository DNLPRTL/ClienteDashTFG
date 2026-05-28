# Source card: beta2025_spatial_temporal_generalization

## Bibliographic data

- Title: A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming
- Authors: Guanghui Zhang, Ziming Wang, Huaren Wei, Mengbai Xiao, Hui Yuan, Dongxiao Yu, Xiuzhen Cheng
- Year: 2025
- Venue: IEEE Transactions on Mobile Computing, Vol. 24, No. 12, December 2025
- DOI / stable URL: `10.1109/TMC.2025.3588135`
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\BETA.pdf`

## Method family

- Family: spatial-temporal DRL for ABR generalization.
- Learning type: DRL with spatial underperformance detection and temporal sequence learning.
- Main contribution: defines and addresses "ABR Under-Generalization".

## State / action / reward

### State

The uploaded paper describes five categories of environmental state:

- measured throughput of the past 8 segments;
- download durations of the past 8 segments;
- bitrate of the most recently downloaded segment;
- current buffer occupancy;
- number of remaining segments.

This is highly compatible with a small CPU-first TFG state candidate.

### Action

- Discrete bitrate level as the output decision action.

For DashClientModular4:

- map to MPD `representation_index`.

### Reward / QoE

- State-action-reward tuples are recorded per segment.
- The temporal module samples sequences of consecutive segments and uses discounted actual reward plus expected reward to train longer-horizon behavior.
- The abstract reports average QoE gains of 19.4%–50.9% and up to 244.1% under severely fluctuating conditions.

For this TFG:

- use Phase 3.5 `qoe_linear_v1 / reward_n`;
- sequence-level diagnostics can be used later, but not as a different reward.

## Model and training

- Spatial Module:
  - trains a base ABR model;
  - compares performance to offline optimum;
  - labels traces as normal vs difficult;
  - trains a classifier and complementary ABR models.
- Temporal Module:
  - stores state-action-reward sequences;
  - samples multi-segment sequences;
  - minimizes discrepancy between discounted actual reward and expected reward.
- Builds on DRL methods and compares against several families.

## Data and evaluation

- Extensive real-world network traces.
- Evaluates under heterogeneous and severely fluctuating network conditions.
- Reports "ABR Under-Generalization": DRL ABR methods may reach only 43.1% to 48.9% of optimal QoE under highly diverse conditions.

## Relevance to DashClientModular4

### What this source justifies

- The TFG state should probably use `k = 8` or a similar short history window.
- Validation must include difficult/underperforming traces.
- OOD and regime-specific diagnostics are mandatory for honest claims.
- A single global model may be a compromise.

### What this source does NOT justify

- It does not justify implementing BETA's full multi-model DRL framework.
- It does not justify using offline optimum labels unless teacher leakage is controlled.
- It does not justify formal benchmark/ranking in Phase 4.

### Risks for this TFG

- Offline optimum can leak future if used incorrectly.
- Multi-model training is too complex.
- Measuring "% optimum" requires a clear oracle contract.
- High risk of overfitting to the difficult-trace detector.

## Decision impact

- Strongly supports: state window with recent throughput/download times/buffer/last bitrate/remaining chunks.
- Supports: difficult-trace diagnostics and trace stratification.
- Blocks: naive random train/test split.
- Implementation consequence:
  - include BETA-style "difficult trace" category in the data/spec plan, not full BETA.

## Memory / thesis usage

- State representation justification.
- OOD/generalization chapter.
- Defense: explains why "average QoE" alone is misleading.
