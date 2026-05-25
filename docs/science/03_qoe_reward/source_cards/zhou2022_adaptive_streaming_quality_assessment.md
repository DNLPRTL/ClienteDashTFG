# Source card - zhou2022

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M07 |
| title | A brief survey on adaptive video streaming quality assessment |
| authors | Wei Zhou, Xiongkuo Min, Hong Li, Qiuping Jiang |
| year | 2022 |
| venue | Journal of Visual Communication and Image Representation |
| DOI or URL | https://doi.org/10.1016/j.jvcir.2022.103526 |
| local source file | 07_2022_zhou_adaptive_video_streaming_quality_assessment_survey.htm |
| source type | Adaptive streaming quality assessment survey |
| triage status | mandatory |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It surveys quality assessment for adaptive streaming, including subjective and objective models.
- It distinguishes QoS-driven, signal-fidelity and hybrid models.
- It explains why pure video quality assessment is insufficient for HAS because playback issues such as initial buffering and stalling matter.
- It supports VMAF/perceptual quality as secondary or deferred when artifacts are missing.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | yes | Quality can be represented through QoS-driven, signal-fidelity or hybrid models. | bitrate, PSNR/SSIM/VMAF or hybrid score | Supports quality term, but not bitrate-only QoE. |
| rebuffering or stalling | strong yes | HAS quality assessment must consider playback issues such as stalling. | seconds/events | Supports rebuffering as a QoE term. |
| switching or smoothness | yes | Adaptive streaming quality changes are part of the assessment problem. | quality delta or model-specific units | Supports smoothness context. |
| startup delay | yes | Initial buffering is named as a playback issue beyond pure VQA. | seconds | Candidate/report-only depending on measurement. |
| perceptual quality or VMAF | strong yes | Covers signal-fidelity/objective quality assessment and hybrid models. | VMAF, PSNR, SSIM or MOS proxy | Supports secondary/deferred perceptual candidate. |
| latency | limited | Not the main A1 use. | seconds if later scoped | Defer live-latency use. |
| failure or incomplete session handling | not addressed directly | Does not define local run gates. | categorical gate needed locally | A2 gate policy remains local. |

## Exact formula or model

- No single formula is selected from this survey.
- The useful model taxonomy is: QoS-driven models, signal-fidelity models and hybrid models.
- The survey indicates hybrid models often perform better than QoS-only or signal-fidelity-only models when compared with full-reference metrics.

## Weights and parameters

- No local QoE weights are selected by this source.
- Perceptual metrics have metric-specific scales and requirements.

## What is optimized

- This is an assessment survey, not a DashClientModular4 controller objective.
- It informs metric selection and limitation statements.

## What is measured or reported

- Subjective and objective quality assessment approaches for adaptive streaming.
- The insufficiency of pure video-quality metrics when playback issues exist.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | adaptive streaming quality assessment |
| simulator/emulator/real deployment | survey of assessment methods |
| traces/datasets | not selected here as a local dataset source |
| baselines | not a controller baseline source |

## What it justifies for DashClientModular4

- VMAF/perceptual quality should be discussed as scientifically relevant.
- The current pipeline should not pretend bitrate-only telemetry is perceptual QoE.
- Playback impairment terms remain necessary even if perceptual quality is added later.

## What it does not justify

- It does not justify VMAF as the only QoE metric.
- It does not justify calculating VMAF without reference/distorted artifacts.
- It does not justify transforming bitrate-only telemetry into perceptual QoE without data.

## Practical decision candidate

- Keep `qoe_perceptual_candidate` as secondary/deferred unless A2 finds usable artifacts and a reproducible measurement path.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Adaptive streaming quality assessment background |
| Chapter 6 | Justify perceptual metrics as deferred/secondary without artifacts |
| Tables | Evidence matrix row for VMAF/perceptual context |
| Figures | Telemetry-to-QoE map can show missing perceptual artifact branch |
| Defense | Explain why VMAF is attractive but not automatic |
| Bibliography | Add as adaptive streaming quality assessment survey |
