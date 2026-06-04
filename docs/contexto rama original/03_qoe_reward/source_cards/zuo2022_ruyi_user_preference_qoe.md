# Source card - zuo2022

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-R03 |
| title | Adaptive Bitrate with User-level QoE Preference for Video Streaming |
| authors | Xutong Zuo, Jiayu Yang, Mowei Wang, Yong Cui |
| year | 2022 |
| venue | video streaming / QoE preference paper; venue not provided in Phase 3.5 evidence pack |
| DOI or URL | not provided in Phase 3.5 evidence pack |
| local source file | 11_2022_zuo_ruyi_user_level_qoe_preference.pdf |
| source type | User preference QoE |
| triage status | recommended context |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It shows that QoE preferences vary between users.
- It uses additive preference models with quality, rebuffering and smoothness meta-metrics.
- It supports documenting fixed local weights as reproducible assumptions rather than universal human preferences.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | strong yes | Uses `v_k`, with VMAF as quality meta-metric. | VMAF in [0,100] | Perceptual quality is part of the preference vector. |
| rebuffering or stalling | strong yes | Uses `r_k` as rebuffer meta-metric. | frame numbers in evidence pack | Supports rebuffer term and unit caution. |
| switching or smoothness | strong yes | Uses `s_k` as quality-switch/smoothness meta-metric. | switch/quality-change metric | Supports smoothness term. |
| startup delay | not central | Startup is not listed in the A1 evidence pack formula. | seconds if later scoped | Use Seufert/Yin for startup. |
| perceptual quality or VMAF | strong yes | VMAF appears as the quality meta-metric. | VMAF [0,100] | Requires VMAF artifacts if reused. |
| latency | not central | Not a live-latency source for A1. | not applicable locally | Defer. |
| failure or incomplete session handling | not addressed directly | Does not define local run gates. | categorical gate needed locally | A2 gate policy remains local. |

## Exact formula or model

```text
QoE_ij = w_i dot q_j
QoE_ij = sum_k (w_iv, w_ir, w_is) dot (v_k, r_k, s_k)
```

Where `v_k` is VMAF, `r_k` is rebuffering and `s_k` is quality switching/smoothness.

## Weights and parameters

- User-specific weights `w_i`.
- Component weights include quality, rebuffering and smoothness preferences.
- The source supports variability of weights, not fixed local closure.

## What is optimized

- A preference-aware ABR objective for user-level QoE.
- This is not opened as an implementation or IA task in A1.

## What is measured or reported

- User-preference-weighted QoE using VMAF, rebuffering and smoothness meta-metrics.
- The key A1 takeaway is weight variability.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | video streaming preference-aware ABR |
| simulator/emulator/real deployment | preference-model context |
| traces/datasets | not selected here as a local dataset source |
| baselines | Ruyi/preference-aware ABR context |

## What it justifies for DashClientModular4

- Fixed weights should be presented as a reproducible local decision if selected in A2.
- VMAF can be a quality component only if artifacts exist.
- Quality, rebuffering and smoothness are again a common additive core.

## What it does not justify

- It does not open preference-aware ABR now.
- It does not justify training models in Phase 3.5.
- It does not justify VMAF as a primary metric without artifacts.
- It does not convert Phase 3.5 into a user study.

## Practical decision candidate

- Use as evidence that A2 weights require explicit rationale and limitation wording.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | User-preference QoE context |
| Chapter 6 | Weight-choice limitations and reproducibility framing |
| Tables | Evidence matrix row for preference weights |
| Figures | Optional mapping showing weights as configurable assumptions |
| Defense | Explain why weights are not universal |
| Bibliography | Add as preference-aware QoE reference |
