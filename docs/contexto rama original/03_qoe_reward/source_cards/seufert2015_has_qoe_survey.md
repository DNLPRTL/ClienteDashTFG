# Source card - seufert2015

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M01 |
| title | A Survey on Quality of Experience of HTTP Adaptive Streaming |
| authors | Michael Seufert, Sebastian Egger, Martin Slanina, Thomas Zinner, Tobias Hossfeld, Phuoc Tran-Gia |
| year | 2015 |
| venue | IEEE Communications Surveys & Tutorials |
| DOI or URL | not provided in Phase 3.5 evidence pack |
| local source file | 01_2015_seufert_qoe_http_adaptive_streaming_survey.pdf |
| source type | QoE survey |
| triage status | mandatory |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It is a survey specific to QoE in HTTP Adaptive Streaming.
- It identifies initial delay, stalling/rebuffering and adaptation/quality variation as QoE influence factors.
- It distinguishes startup/initial delay from stalling: startup wait is expected and normally less severe, while stalling is unexpected and perceived more negatively.
- It supports treating `startup_delay_s` as secondary or report-only unless A2 confirms homogeneous measurement.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | yes | Video quality and quality adaptation affect QoE. | representation quality, bitrate-derived quality or subjective score | Survey evidence, not a numeric utility choice. |
| rebuffering or stalling | strong yes | Stalling/rebuffering is a major HAS impairment and worse than expected startup wait. | seconds, events or ratio | Strong support for inclusion in a candidate QoE score. |
| switching or smoothness | yes | Adaptation and variable quality influence perceived experience. | quality/bitrate variation | Supports a smoothness term, but not a specific weight. |
| startup delay | strong yes | Initial delay before playback is a separate influence factor. | seconds | Relevant, but measurement-dependent for the local pipeline. |
| perceptual quality or VMAF | indirect | Discusses subjective QoE and video quality, not VMAF tooling. | model-specific | Does not justify VMAF by itself. |
| latency | limited | Low-latency/live-specific delay is not the central A1 contribution. | seconds | Defer unless live telemetry enters A2. |
| failure or incomplete session handling | not addressed directly | Survey does not define artifact gates for failed runs. | categorical gate needed locally | Local gate policy remains for A2. |

## Exact formula or model

- No single universal QoE formula is adopted from this survey.
- The useful model contribution is an influence-factor taxonomy: initial delay, stalling/rebuffering, quality level and quality adaptation.

## Weights and parameters

- No final weights are provided for DashClientModular4.
- The source supports term selection, not weight closure.

## What is optimized

- The survey does not define a controller objective for DashClientModular4.
- It reviews factors that ABR systems and QoE models commonly account for.

## What is measured or reported

- QoE influence factors and their subjective relevance in HAS literature.
- Initial delay and stalling are conceptually separated.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | HTTP Adaptive Streaming broadly; useful for VoD and general HAS context |
| simulator/emulator/real deployment | survey over prior studies |
| traces/datasets | not a local trace/dataset source |
| baselines | not a controller baseline source |

## What it justifies for DashClientModular4

- Rebuffering/stalling should be considered in the A2 QoE/reward candidate.
- Startup delay should be tracked separately and only included in a score if measured consistently.
- Bitrate-only quality is incomplete without playback impairment terms.

## What it does not justify

- It does not provide a universal final formula.
- It does not justify using only bitrate as complete QoE.
- It does not justify mixing incomplete sessions into numeric comparisons.

## Practical decision candidate

- Use as evidence for `rebuffering`, `startup_delay` and `smoothness` terms.
- Treat startup as `should be considered in A2`; likely report-only unless measured homogeneously.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | HAS QoE influence-factor background |
| Chapter 6 | Justify separating startup delay, rebuffering and smoothness in evaluation methodology |
| Tables | Evidence matrix row for QoE influence factors |
| Figures | Telemetry-to-QoE term mapping |
| Defense | Explain why stalling matters more than a simple bitrate average |
| Bibliography | Add as HAS QoE survey reference |
