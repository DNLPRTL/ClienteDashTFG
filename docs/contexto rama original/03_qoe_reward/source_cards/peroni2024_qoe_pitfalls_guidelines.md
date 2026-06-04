# Source card - peroni2024

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M06 |
| title | Quality of Experience in Video Streaming: Status Quo, Pitfalls, and Guidelines |
| authors | Leonardo Peroni, Sergey Gorinsky |
| year | 2024 |
| venue | COMSNETS |
| DOI or URL | https://doi.org/10.1109/COMSNETS59351.2024.10427330 |
| local source file | 06_2024_peroni_qoe_status_quo_pitfalls_guidelines.pdf |
| source type | QoE methodology and pitfalls |
| triage status | mandatory |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It is the main methodological caution source for QoE modeling.
- It emphasizes that QoE is subjective and depends on user, device, content, connectivity and context.
- It warns against proposing or using QoE models without adequate validation.
- It supports using a transparent, classical and limited formula candidate instead of inventing a new subjective model.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | yes | Video quality is one measurable influence factor among many. | model-specific | Must not be overclaimed as human satisfaction by itself. |
| rebuffering or stalling | yes | Playback impairment is a measurable influence factor. | seconds/events | Valid as an objective term, with scope limits. |
| switching or smoothness | yes | Quality variation can be an influence factor. | quality delta or model-specific units | Include transparently if used. |
| startup delay | yes | Contextual influence factor if measured. | seconds | Measurement contract matters. |
| perceptual quality or VMAF | yes, with caution | Objective models can scale, but model validity is not automatic. | metric-specific | Supports caution for VMAF/perceptual claims. |
| latency | context-dependent | QoE factors vary by service context. | seconds | Do not add latency unless scoped and measured. |
| failure or incomplete session handling | methodological relevance | Failed/non-comparable runs need explicit treatment. | categorical gate and reason | Supports gate transparency, not hidden blending. |

## Exact formula or model

- No new QoE formula should be adopted from this source.
- The key model distinction is methodological: test conducting, model building and model using must not be collapsed.

## Weights and parameters

- No local weights are provided.
- Fixed weights in the TFG, if selected later, should be framed as reproducible engineering choices with limited claims.

## What is optimized

- This paper does not optimize a DashClientModular4 controller.
- It critiques QoE-model construction and use.

## What is measured or reported

- Methodological pitfalls and guidelines for QoE in video streaming.
- Reasons to avoid overclaiming objective QoE scores.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | video streaming broadly |
| simulator/emulator/real deployment | methodology/guidelines |
| traces/datasets | not a local trace/dataset source |
| baselines | not a controller baseline source |

## What it justifies for DashClientModular4

- Use a transparent candidate formula instead of inventing an unvalidated subjective model.
- Keep training reward, controller objective and evaluation metric separately named.
- Document gates and limitations before comparisons.

## What it does not justify

- It does not justify a new QoE model without subjective validation.
- It does not justify claiming computed QoE equals real human satisfaction.
- It does not justify rankings without closed gates and methodology.

## Practical decision candidate

- Use as a methodology guardrail in A2: prefer classic transparent candidates; document limitations and gates.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | QoE modeling caution and subjectivity |
| Chapter 6 | Threats to validity and metric-claim limits |
| Tables | Evidence matrix row for methodology limits |
| Figures | Evaluation pipeline/gate figure can show model-using boundary |
| Defense | Explain why the project does not invent subjective QoE |
| Bibliography | Add as QoE pitfalls/guidelines reference |
