# Source card - spiteri2020

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M04 |
| title | BOLA: Near-Optimal Bitrate Adaptation for Online Videos |
| authors | Kevin Spiteri, Rahul Urgaonkar, Ramesh K. Sitaraman |
| year | 2020 |
| venue | IEEE/ACM Transactions on Networking |
| DOI or URL | https://doi.org/10.1109/TNET.2020.2996964 |
| local source file | 04_2020_spiteri_bola_near_optimal_bitrate_adaptation_ton.pdf |
| source type | Utility-based ABR |
| triage status | mandatory |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It formulates bitrate adaptation as utility maximization.
- It supports concave/log utility and diminishing returns from higher bitrates.
- It reinforces the quality-versus-rebuffering trade-off while showing that controller objectives are not automatically universal evaluation metrics.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | strong yes | Utility can be defined by content, provider or device; example log utility. | utility units | Strong evidence for `qoe_log_candidate`. |
| rebuffering or stalling | strong yes | Rebuffer avoidance is central to the buffer/utility trade-off. | seconds or buffer-derived objective units | Supports rebuffering as a candidate penalty. |
| switching or smoothness | partial | BOLA can be adapted to reduce frequent switches, but switching is not the central Lyapunov term. | quality/bitrate delta if added | Does not justify omitting smoothness in evaluation. |
| startup delay | not central | Startup delay is not the main A1 contribution from this source. | seconds if separately measured | Use Seufert/Yin for startup evidence. |
| perceptual quality or VMAF | indirect | Utility may be chosen flexibly, but the A1 evidence gives log bitrate/size utility. | utility units | Does not require VMAF. |
| latency | not central | Online video ABR context, not a live-latency formula for A1. | not applicable locally | Defer live latency. |
| failure or incomplete session handling | not addressed directly | Does not define local artifact gates. | categorical gate needed locally | A2 should define gates. |

## Exact formula or model

- Example utility from the A1 evidence pack:

```text
v_m = ln(S_m / S_1)
```

- BOLA uses a buffer-aware utility-maximization objective with parameters such as `V` and `gamma`.

## Weights and parameters

- `gamma` controls how much the controller avoids rebuffering.
- `V` controls the relationship with buffer level.
- Utility values `v_m` can be defined for the representation ladder.
- These are controller-objective parameters, not final DashClientModular4 evaluation weights.

## What is optimized

- BOLA optimizes a buffer-aware utility objective for representation selection.
- It is a controller objective, not a direct metric for all controllers.

## What is measured or reported

- Video utility/bitrate quality and rebuffering behavior in BOLA evaluation context.
- Switching may be discussed or mitigated, but it is not the core objective component.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | online video / HAS ABR |
| simulator/emulator/real deployment | controller evaluation context |
| traces/datasets | not selected here as a trace dataset source |
| baselines | BOLA baseline/objective context |

## What it justifies for DashClientModular4

- A log/concave quality utility should be considered in A2.
- Diminishing returns are scientifically defensible as a sensitivity candidate.
- BOLA's internal objective should not be copied as the single metric for all controllers.

## What it does not justify

- It does not justify omitting smoothness from later evaluation.
- It does not justify using BOLA's internal objective as the only cross-controller score.
- It does not close local weights.

## Practical decision candidate

- Carry `qoe_log_candidate` into A2, with BOLA cited for concave utility and diminishing returns.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Utility-based ABR and BOLA background |
| Chapter 6 | Candidate log utility and objective-vs-evaluation distinction |
| Tables | Evidence matrix and candidate formula table |
| Figures | Utility curve/diminishing returns concept if a local original figure is created |
| Defense | Explain why log utility is considered but not automatically selected |
| Bibliography | Add as BOLA utility reference |
