# Source card - chen2024

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M05 |
| title | SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming |
| authors | Tianyu Chen, Yiheng Lin, Nicolas Christianson, Zahaib Akhtar, Sharath Dharmaji, Mohammad Hajiesmaili, Adam Wierman, Ramesh K. Sitaraman |
| year | 2024 |
| venue | ACM SIGCOMM |
| DOI or URL | not provided in Phase 3.5 evidence pack |
| local source file | 05_2024_chen_soda_consistent_high_quality_video_streaming.pdf |
| source type | Modern ABR smoothness/QoE |
| triage status | mandatory |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It is modern evidence that QoE is not only high bitrate; consistency and bitrate switching matter.
- It states that QoE is maximized by high quality, minimum rebuffering and minimum bitrate switching.
- It is especially useful to justify smoothness as a core term, while avoiding direct formula reuse outside its scope.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | strong yes | Includes a video quality term. | utility/time-based expression | Supports quality as part of the common core. |
| rebuffering or stalling | yes | Rebuffering is minimized, but the objective uses buffer cost rather than direct rebuffer time. | buffer/time cost | Useful but not direct current-pipeline formula evidence. |
| switching or smoothness | strong yes | Bitrate switching/smoothness is one of the key components. | switching cost `c(r_n, r_{n-1})` | Strong evidence for smoothness. |
| startup delay | not central | Startup delay is not the A1 focus of this source. | seconds if separately measured | Use Seufert/Yin for startup. |
| perceptual quality or VMAF | no direct VMAF | Quality term is not presented in the evidence pack as VMAF. | utility units | Does not require VMAF. |
| latency | contextually important | Particularly relevant to live streaming and short buffers. | seconds/time-based factors | Live-specific elements should be deferred unless A2 scopes them in. |
| failure or incomplete session handling | not addressed directly | Does not define local run comparability gates. | categorical gate needed locally | A2 gate policy remains needed. |

## Exact formula or model

The A1 evidence pack lists the SODA time-based form:

```text
sum_n [ v(r_n) * omega_n * Delta_t / r_n + beta * b(x_n) + gamma * c(r_n, r_{n-1}) ]
```

## Weights and parameters

- `beta` weights buffer cost.
- `gamma` weights switching/smoothness cost.
- `omega_n` and `Delta_t` appear in the time-based quality term.
- These are SODA objective parameters, not final local QoE weights.

## What is optimized

- SODA optimizes consistent high-quality streaming with explicit attention to switching and buffer-related costs.
- It is a controller objective, not a direct run-level metric for the current segment-level trace-driven pipeline.

## What is measured or reported

- Quality, rebuffering/buffer-related behavior and bitrate-switching consistency.
- The A1 use is evidentiary, especially for smoothness.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | especially strong for live/short-buffer streaming context |
| simulator/emulator/real deployment | ABR controller evaluation context |
| traces/datasets | not selected here as a local dataset source |
| baselines | SODA/SOCO context; not selected for implementation in A1 |

## What it justifies for DashClientModular4

- Smoothness/switching should be treated as a core QoE candidate term.
- Modern literature supports consistency, not only average quality.
- Direct SODA formula reuse should be deferred unless A2 aligns scope and telemetry.

## What it does not justify

- It does not convert Phase 3.5 into live streaming.
- It does not require SOCO/SODA implementation.
- It does not provide a direct primary formula for the current trace-driven VoD/smoke pipeline.

## Practical decision candidate

- Use as strong support for `smoothness` in A2; do not copy the SODA objective directly without scope alignment.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Modern smoothness/QoE context |
| Chapter 6 | Justify switching/smoothness as a candidate evaluation component |
| Tables | Evidence matrix row for smoothness |
| Figures | Telemetry-to-QoE term map can include quality-change deltas |
| Defense | Explain why high average bitrate alone is not enough |
| Bibliography | Add as SODA smoothness/QoE reference |
