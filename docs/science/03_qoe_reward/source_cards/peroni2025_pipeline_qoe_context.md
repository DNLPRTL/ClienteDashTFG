# Source card - peroni2025

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-R02 |
| title | An End-to-End Pipeline Perspective on Video Streaming in Best-Effort Networks: A Survey and Tutorial |
| authors | Leonardo Peroni, Sergey Gorinsky |
| year | 2025 |
| venue | ACM Computing Surveys |
| DOI or URL | https://doi.org/10.1145/3742472 |
| local source file | 10_2025_peroni_gorinsky_video_streaming_pipeline_survey.pdf |
| source type | End-to-end pipeline survey |
| triage status | recommended context |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It places QoE within the end-to-end video streaming pipeline over best-effort networks.
- It defines QoE models as functions from measurable influence factors, such as stall duration and video quality, to subjective experience.
- It helps keep DashClientModular4 focused on client-side ABR evaluation while acknowledging the larger system.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | yes | Video quality is a measurable influence factor for QoE models. | bitrate/perceptual/model-specific | Context support. |
| rebuffering or stalling | yes | Stall duration is an example measurable influence factor. | seconds | Strong context support. |
| switching or smoothness | contextual | Quality changes can be part of measured influence factors in ABR context. | quality delta | Not a direct formula source. |
| startup delay | contextual | Startup/join behavior can be an influence factor if measured. | seconds | Measurement-dependent. |
| perceptual quality or VMAF | contextual | Video quality may be objective/perceptual depending on model. | metric-specific | Does not create artifacts. |
| latency | contextual | End-to-end pipeline includes broader delay factors. | seconds | Not current A1 scope. |
| failure or incomplete session handling | not defined locally | Does not define local run gates. | categorical gate needed locally | A2 should define artifact policy. |

## Exact formula or model

- No local formula is selected.
- The relevant conceptual model is: QoE models express subjective experience as a function of measurable influence factors.

## Weights and parameters

- No DashClientModular4 weights are selected.
- Any future weights remain A2 decisions and should be documented as local choices.

## What is optimized

- This survey/tutorial does not optimize a local controller.
- It frames where QoE models sit in the complete pipeline.

## What is measured or reported

- Pipeline components and their relationship to measurable influence factors.
- It supports scope and terminology, not local scoring.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | long-form 2D streaming over best-effort Internet with client-side ABR and CDN context |
| simulator/emulator/real deployment | survey/tutorial |
| traces/datasets | not a local dataset source |
| baselines | pipeline context for client-side ABR |

## What it justifies for DashClientModular4

- QoE should be tied to measurable local factors.
- Chapter 6 can explain why the current evaluation scope is client-side ABR telemetry rather than ingestion/CDN/processing.
- It supports cautious pipeline boundaries.

## What it does not justify

- It does not close a primary formula.
- It does not mix ingestion, processing or CDN concerns into the Phase 3.5 evaluation pipeline.
- It does not authorize implementation.

## Practical decision candidate

- Use as context for A2 scope boundaries and terminology: measurable factors yes, full end-to-end pipeline expansion no.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | End-to-end streaming pipeline context |
| Chapter 6 | Methodology scope and measurable influence-factor framing |
| Tables | Evidence matrix context row |
| Figures | Telemetry-to-QoE mapping and pipeline boundary |
| Defense | Explain why evaluation focuses on client-side ABR signals |
| Bibliography | Add as pipeline survey/tutorial reference |
