# Source card - mao2017

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M03 |
| title | Neural Adaptive Video Streaming with Pensieve |
| authors | Hongzi Mao, Ravi Netravali, Mohammad Alizadeh |
| year | 2017 |
| venue | ACM SIGCOMM |
| DOI or URL | https://doi.org/10.1145/3098822.3098843 |
| local source file | 03_2017_mao_pensieve_neural_adaptive_video_streaming.pdf |
| source type | ABR reward and QoE evaluation |
| triage status | mandatory |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It is a central source for ABR reward/QoE in neural adaptive streaming.
- It uses a classical additive quality minus rebuffering minus smoothness formula family.
- It reports average QoE per chunk, which helps A2 distinguish reward and run-level evaluation summaries.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | strong yes | `q(R_n)` maps chunk bitrate to perceived quality utility. | bitrate, log utility or HD utility | Direct evidence for linear/log candidates. |
| rebuffering or stalling | strong yes | `T_n` is rebuffering time caused by chunk download/playback dynamics. | seconds weighted by `mu` | Strong evidence for rebuffer penalty. |
| switching or smoothness | strong yes | Penalizes adjacent quality changes `|q(R_{n+1}) - q(R_n)|`. | abs utility delta | Strong evidence for smoothness penalty. |
| startup delay | not in quoted core | The Phase 3.5 evidence pack does not list startup in the core Pensieve reward. | seconds if separately tracked | Startup support should come from Seufert/Yin. |
| perceptual quality or VMAF | no direct VMAF | Quality utility is bitrate/log/HD in the listed variants. | utility units | Does not require VMAF artifacts. |
| latency | not central | Not a live-latency source for A1. | not applicable locally | Defer live latency. |
| failure or incomplete session handling | not addressed directly | Does not define local gates for incomplete run artifacts. | categorical gate needed locally | A2 should handle gates separately. |

## Exact formula or model

```text
QoE = sum_n q(R_n) - mu * sum_n T_n - sum_n |q(R_{n+1}) - q(R_n)|
```

Variants listed in the Phase 3.5A1 evidence pack:

- `QoE_lin`: `q(R)=R`, rebuffer penalty `mu=4.3`.
- `QoE_log`: `q(R)=log(R/R_min)`, rebuffer penalty `mu=2.66`.
- `QoE_hd`: step utility for HD, rebuffer penalty `mu=8`.

## Weights and parameters

- `mu=4.3` for linear utility.
- `mu=2.66` for log utility.
- `mu=8` for HD-step utility.
- Smoothness coefficient is effectively one in the formula as listed in the evidence pack.
- These values are evidence inputs, not final local weights.

## What is optimized

- In Pensieve, the formula acts as a scalar reward for neural ABR training.
- The same formula family is also used for evaluation reporting, so DashClientModular4 must label any reuse precisely.

## What is measured or reported

- Average QoE per chunk: total QoE divided by number of chunks.
- Component behavior across quality, rebuffering and switching.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | adaptive video streaming; not used here to open live latency |
| simulator/emulator/real deployment | neural ABR evaluation/training context |
| traces/datasets | not selected here as a trace dataset source |
| baselines | Pensieve/neural ABR context |

## What it justifies for DashClientModular4

- `qoe_linear_candidate` and `qoe_log_candidate` should be considered in A2.
- A per-chunk average may be useful as an evaluation summary candidate if A2 defines comparable complete runs.
- Training reward and evaluation metric must be named separately.

## What it does not justify

- It does not imply opening IA/RL in Phase 3.5.
- It does not imply training Pensieve.
- It does not imply `QoE_hd` is appropriate if the local bitrate ladder does not match the HD utility assumptions.

## Practical decision candidate

- Carry linear and log Pensieve-style QoE into A2 as candidate formulas, with explicit role labels and no IA implementation.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Neural ABR/QoE reward reference |
| Chapter 6 | Candidate reward/evaluation formula family and average-per-chunk reporting |
| Tables | Evidence matrix, candidate formula table |
| Figures | Telemetry to reward/QoE term map |
| Defense | Explain why Pensieve is evidence, not an implementation step |
| Bibliography | Add as Pensieve reward reference |
