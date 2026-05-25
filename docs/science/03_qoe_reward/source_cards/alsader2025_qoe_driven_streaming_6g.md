# Source card - alsader2025

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-R04 |
| title | QoE-Driven Adaptive Video Streaming: Architectures, Techniques, and Future Research Challenges Toward 6G Networks |
| authors | Moner Alsader, Alcardo Alex Barakabitze, Is-Haka Mkwawa |
| year | 2025 |
| venue | IEEE Access |
| DOI or URL | https://doi.org/10.1109/ACCESS.2025.3597058 |
| local source file | 12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey.pdf |
| source type | QoE-driven streaming survey |
| triage status | recommended context |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It provides modern QoE-driven streaming context toward 6G networks.
- It classifies architectures and techniques involving SDN/NFV/MEC, AI/ML, cloud/edge and 6G.
- It is useful for future-work framing and for explaining why these topics are outside A1.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | contextual yes | QoE-driven streaming includes video quality. | model-specific | Context only for A1. |
| rebuffering or stalling | contextual yes | Playback impairments are part of QoE-driven streaming concerns. | seconds/events | Context only for A1. |
| switching or smoothness | contextual yes | Adaptive streaming techniques may consider quality variation. | quality delta | Not a direct formula source. |
| startup delay | contextual | Can be part of QoE in broader systems. | seconds | Use stronger sources for A2. |
| perceptual quality or VMAF | contextual | Broader QoE-driven systems may use perceptual metrics. | metric-specific | Does not create local artifacts. |
| latency | contextual strong | 6G/network-assisted settings emphasize latency and future network capabilities. | seconds | Out of current Phase 3.5 scope unless later reopened. |
| failure or incomplete session handling | not defined locally | Does not define DashClientModular4 gates. | categorical gate needed locally | A2 remains responsible. |

## Exact formula or model

- No local QoE formula is selected from this survey.
- It is a taxonomy and future-challenges source for QoE-driven adaptive streaming architectures.

## Weights and parameters

- No DashClientModular4 weights are selected.
- 6G/network-assisted parameters are future-work context only.

## What is optimized

- The survey classifies QoE-driven techniques and architectures rather than optimizing the local client.
- AI/ML topics are context, not A1 implementation scope.

## What is measured or reported

- Architecture families and future research challenges for QoE-driven streaming.
- The A1 use is context and limitation framing.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | broad QoE-driven streaming toward 6G |
| simulator/emulator/real deployment | survey of architectures and techniques |
| traces/datasets | not a local dataset source |
| baselines | broad future-work context |

## What it justifies for DashClientModular4

- Future-work discussion for QoE-driven, network-assisted and AI/ML streaming.
- Clear boundary that the TFG current phase remains client-side, trace-driven and documentation-first.

## What it does not justify

- It does not define the local metric formula.
- It does not pull Phase 3.5 toward network slicing, XR, metaverse or 6G implementation.
- It does not open IA/RL.

## Practical decision candidate

- Use as future-work context only; do not use as a candidate formula source.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Modern QoE-driven streaming context |
| Chapter 6 | Scope and future-work boundary |
| Tables | Evidence matrix context row |
| Figures | Optional future-work positioning figure if created |
| Defense | Explain why 6G/AI topics remain outside the current phase |
| Bibliography | Add as QoE-driven streaming survey reference |
