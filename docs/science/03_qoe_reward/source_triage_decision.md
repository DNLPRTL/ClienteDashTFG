# Phase 3.5A0 Source Triage Decision

## Decision

The Phase 3.5 source batch is closed for the current QoE/reward decision. No additional PDFs are needed before source-card distillation.

## Triage table

| id | decision | action | target source card | reason |
| --- | --- | --- | --- | --- |
| QOE-M01 | mandatory | card now | seufert2015_has_qoe_survey.md | HAS QoE influence factors: initial delay, stalling, adaptation and subjective QoE. |
| QOE-M02 | mandatory | card now | yin2015_mpc_qoe_objective.md | Classical MPC QoE objective and evaluation methodology. |
| QOE-M03 | mandatory | card now | mao2017_pensieve_qoe_reward.md | Reward definitions for neural ABR and comparison of QoE objectives. |
| QOE-M04 | mandatory | card now | spiteri2020_bola_utility_qoe.md | Utility maximization, quality utility, rebuffering trade-off and switching discussion. |
| QOE-M05 | mandatory | card now | chen2024_soda_smoothness_qoe.md | Modern evidence for bitrate switching, smoothness and rebuffering/QoE trade-off. |
| QOE-M06 | mandatory | card now | peroni2024_qoe_pitfalls_guidelines.md | Methodological warnings against careless QoE modeling and overclaiming. |
| QOE-M07 | mandatory | card now | zhou2022_adaptive_streaming_quality_assessment.md | Objective and subjective quality assessment, perceptual quality and streaming-specific impairments. |
| QOE-M08 | mandatory technical reference | card now | netflix_vmaf_perceptual_quality.md | Official implementation/tooling reference for VMAF and libvmaf. |
| QOE-R01 | recommended context | card now | timmerer2025_has_review_qoe_context.md | Modern HAS/QoE context for state of the art and memory. |
| QOE-R02 | recommended context | card now | peroni2025_pipeline_qoe_context.md | Holistic pipeline context and QoE placement in distribution-stage ABR. |
| QOE-R03 | recommended context | card now | zuo2022_ruyi_user_preference_qoe.md | Evidence that QoE weights/preferences vary across users. |
| QOE-R04 | recommended context | card now | alsader2025_qoe_driven_streaming_6g.md | Future-work context for QoE-driven adaptive streaming and network-assisted settings. |

## Deferred sources

The following families are deferred unless the tutor explicitly requests them or Phase 4/6 re-opens the topic:

- edge-collaboration RL ABR;
- wireless-only DRL surveys;
- low-latency live-only surveys;
- sustainable/energy-aware ABR;
- 360/VR/XR-specific QoE papers;
- CDN/cache-only QoE papers without a usable ABR metric contribution.

## Non-actions

- No Codex implementation.
- No formula closure.
- No ranking.
- No benchmark.
- No IA/RL.