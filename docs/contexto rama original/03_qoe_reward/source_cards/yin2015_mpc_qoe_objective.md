# Source card - yin2015

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M02 |
| title | A Control-Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP |
| authors | Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, Bruno Sinopoli |
| year | 2015 |
| venue | ACM SIGCOMM |
| DOI or URL | https://doi.org/10.1145/2785956.2787486 |
| local source file | 02_2015_yin_mpc_control_theoretic_abr_http.pdf |
| source type | ABR QoE objective |
| triage status | mandatory |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It is a classical ABR source for a multi-term QoE objective.
- It explicitly separates average video quality, quality variation, rebuffering and startup delay.
- It helps distinguish controller objective, evaluation metric and user-preference weight choices.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | strong yes | Positive utility `q(R_k)` for selected representation bitrate/quality. | utility units per segment/chunk | Direct candidate-family evidence. |
| rebuffering or stalling | strong yes | Penalizes predicted rebuffering from download time and buffer state. | seconds transformed by weight `mu` | Strong support for a rebuffer penalty. |
| switching or smoothness | strong yes | Penalizes absolute changes in quality utility across adjacent chunks. | abs utility delta weighted by `lambda` | Strong support for smoothness. |
| startup delay | yes | Explicit startup term `T_s` with weight `mu_s`. | seconds weighted by `mu_s` | Candidate only if measured homogeneously. |
| perceptual quality or VMAF | no direct VMAF | `q()` can map bitrate to quality, but VMAF is not required by the A1 evidence. | utility units | Does not require perceptual artifacts. |
| latency | not central | Objective targets HAS adaptation, not live-latency scoring for A1. | seconds if later scoped | Defer unless A2 expands scope. |
| failure or incomplete session handling | not addressed directly | Does not define local run gates. | categorical gate needed locally | Use A2 gate policy for incomplete runs. |

## Exact formula or model

```text
QoE_1^K =
  sum_{k=1..K} q(R_k)
  - lambda * sum_{k=1..K-1} |q(R_{k+1}) - q(R_k)|
  - mu * sum_{k=1..K} (d_k(R_k) / C_k - B_k)^+
  - mu_s * T_s
```

## Weights and parameters

- `lambda`, `mu` and `mu_s` are non-negative weights.
- The paper provides the structure; it does not fix the final DashClientModular4 weights.

## What is optimized

- A model-predictive ABR controller objective over a horizon.
- The objective is not automatically the same as the local run-level evaluation metric.

## What is measured or reported

- QoE components and aggregate objective values in the ABR evaluation context.
- The source can inform candidate run summaries, but A2 must name the evaluation role.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | HAS/VoD-style adaptive streaming |
| simulator/emulator/real deployment | control-theoretic ABR evaluation context |
| traces/datasets | not selected here as a dataset source |
| baselines | MPC/RobustMPC family context |

## What it justifies for DashClientModular4

- Additive candidate formula with quality utility, rebuffering penalty and smoothness penalty.
- Optional startup penalty candidate if `startup_delay_s` is measured consistently.
- Clear separation between a controller objective and later evaluation reporting.

## What it does not justify

- It does not fix the final weights for the TFG.
- It does not force startup into a score if startup is not measured homogeneously.
- It does not authorize code changes in A1.

## Practical decision candidate

- Carry the additive MPC structure into A2 as evidence for `qoe_linear_candidate` and `startup_penalty_candidate`.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Classical ABR/QoE objective reference |
| Chapter 6 | Explain candidate formula terms and role separation |
| Tables | Evidence matrix and formula-candidate table |
| Figures | Mapping from segment telemetry to quality/rebuffer/smoothness/startup terms |
| Defense | Explain why weights are methodological choices |
| Bibliography | Add as MPC QoE objective reference |
