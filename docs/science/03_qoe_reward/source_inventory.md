# Phase 3.5A1 Source Inventory

This inventory records the source set for QoE/reward/final metric semantics. A row in this file does not close the QoE formula and does not authorize code changes.

## Selected sources

| id | triage status | distillation status | type | year | title | local file |
| --- | --- | --- | --- | --- | --- | --- |
| QOE-M01 | mandatory | distilled_phase3_5a1 | QoE survey | 2015 | A Survey on Quality of Experience of HTTP Adaptive Streaming | 01_2015_seufert_qoe_http_adaptive_streaming_survey.pdf |
| QOE-M02 | mandatory | distilled_phase3_5a1 | ABR QoE objective | 2015 | A Control-Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP | 02_2015_yin_mpc_control_theoretic_abr_http.pdf |
| QOE-M03 | mandatory | distilled_phase3_5a1 | ABR reward and QoE evaluation | 2017 | Neural Adaptive Video Streaming with Pensieve | 03_2017_mao_pensieve_neural_adaptive_video_streaming.pdf |
| QOE-M04 | mandatory | distilled_phase3_5a1 | Utility-based ABR | 2020 | BOLA: Near-Optimal Bitrate Adaptation for Online Videos | 04_2020_spiteri_bola_near_optimal_bitrate_adaptation_ton.pdf |
| QOE-M05 | mandatory | distilled_phase3_5a1 | Modern ABR smoothness/QoE | 2024 | SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming | 05_2024_chen_soda_consistent_high_quality_video_streaming.pdf |
| QOE-M06 | mandatory | distilled_phase3_5a1 | QoE methodology and pitfalls | 2024 | Quality of Experience in Video Streaming: Status Quo, Pitfalls, and Guidelines | 06_2024_peroni_qoe_status_quo_pitfalls_guidelines.pdf |
| QOE-M07 | mandatory | distilled_phase3_5a1 | Adaptive streaming quality assessment survey | 2022 | A brief survey on adaptive video streaming quality assessment | 07_2022_zhou_adaptive_video_streaming_quality_assessment_survey.htm |
| QOE-M08 | mandatory technical reference | distilled_phase3_5a1 | Official technical source | 2026 access | VMAF official Netflix repository reference | 08_netflix_vmaf_reference_source.md |
| QOE-R01 | recommended context | distilled_phase3_5a1 | HAS review | 2025 | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges | 09_2025_timmerer_has_review_current_advances_future_challenges.pdf |
| QOE-R02 | recommended context | distilled_phase3_5a1 | End-to-end pipeline survey | 2025 | An End-to-End Pipeline Perspective on Video Streaming in Best-Effort Networks | 10_2025_peroni_gorinsky_video_streaming_pipeline_survey.pdf |
| QOE-R03 | recommended context | distilled_phase3_5a1 | User preference QoE | 2022 | Adaptive Bitrate with User-level QoE Preference for Video Streaming | 11_2022_zuo_ruyi_user_level_qoe_preference.pdf |
| QOE-R04 | recommended context | distilled_phase3_5a1 | QoE-driven streaming survey | 2025 | QoE-Driven Adaptive Video Streaming: Architectures, Techniques, and Future Research Challenges Toward 6G Networks | 12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey.pdf |

## Distillation boundary

- Source cards were filled from the Phase 3.5A1 evidence pack and local-source identities.
- No source PDF, HTML capture, CSV, log, media file or raw artifact is committed to the repository.
- Final QoE/reward decisions are deferred until A2.
- VMAF is treated as perceptual-quality evidence and tooling context, not automatically as an evaluation formula.
- Dry-runs generated before the final metric contract remain non-benchmark evidence.

## Hard rules

- Every selected source has a source card.
- The evidence matrix must be used before writing A2 selection documents.
- Candidate formulas remain candidates until A2 closes the metric and gate policy.
- Incomplete or non-comparable sessions should be handled by explicit gates rather than hidden numeric blending unless A2 justifies otherwise.
