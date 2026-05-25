# Source card - timmerer2025

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-R01 |
| title | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges |
| authors | Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, Hermann Hellwagner |
| year | 2025 |
| venue | ACM Transactions on Multimedia Computing, Communications, and Applications |
| DOI or URL | https://doi.org/10.1145/3736306 |
| local source file | 09_2025_timmerer_has_review_current_advances_future_challenges.pdf |
| source type | HAS review |
| triage status | recommended context |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It is a modern HAS survey covering encoding, delivery/networking, consumption/player, ABR, QoE and energy.
- It helps position the TFG in the current state of the art.
- It provides context for VMAF-aware and energy-aware directions without making them A1 requirements.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | yes | QoE/ABR context includes delivered video quality. | model-specific | Context support, not formula closure. |
| rebuffering or stalling | yes | HAS QoE context includes playback impairments. | seconds/events | Context support. |
| switching or smoothness | yes | ABR context includes adaptation behavior. | quality delta | Context support. |
| startup delay | contextual | Startup/join effects can be part of HAS QoE context. | seconds | Use Seufert/Yin for stronger A2 evidence. |
| perceptual quality or VMAF | contextual yes | Mentions modern VMAF-aware/GreenABR-type context in the evidence pack. | VMAF or model-specific | Future-work/context support. |
| latency | contextual | Modern HAS includes broader consumption/player challenges. | seconds | Not a current local metric requirement. |
| failure or incomplete session handling | not addressed for local artifacts | Does not define DashClientModular4 gate policy. | categorical gate needed locally | A2 remains responsible. |

## Exact formula or model

- No A1 QoE formula is selected from this survey.
- It provides state-of-the-art context rather than a local metric equation.

## Weights and parameters

- No local QoE weights are selected.
- Energy-aware and VMAF-aware details remain context/future-work unless later scoped.

## What is optimized

- This review does not optimize a DashClientModular4 controller.
- It surveys current advances and future challenges.

## What is measured or reported

- Broad HAS research areas, including QoE and ABR context.
- It should be used for framing, not numeric scoring.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | broad HAS context |
| simulator/emulator/real deployment | survey/review |
| traces/datasets | not a local dataset source |
| baselines | broad ABR context |

## What it justifies for DashClientModular4

- Chapter 2 state-of-the-art framing.
- A future-work note that modern HAS includes energy-aware and VMAF-aware directions.
- Scope discipline: not every modern topic enters Phase 3.5.

## What it does not justify

- It does not define the local QoE metric.
- It does not bring energy-aware ABR into A1 except as future work.
- It does not authorize IA/RL.

## Practical decision candidate

- Use as context source only; do not use as a formula source for A2 unless the later selection document explicitly motivates a narrow point.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Modern HAS state-of-the-art context |
| Chapter 6 | Evaluation scope and future-work boundary |
| Tables | Evidence matrix context row |
| Figures | Optional state-of-the-art positioning figure if created |
| Defense | Explain what is in scope versus future work |
| Bibliography | Add as modern HAS review reference |
