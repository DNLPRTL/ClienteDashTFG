# Phase 3.5A0 Source Inventory

This inventory records the source set for QoE/reward/mÃ©tricas finales. A row in this file does not close the QoE formula and does not authorize code changes.

## Selected sources

| id | status | type | year | title | local file |
| --- | --- | --- | --- | --- | --- |
| QOE-M01 | mandatory | QoE survey | 2015 | A Survey on Quality of Experience of HTTP Adaptive Streaming | 01_2015_seufert_qoe_http_adaptive_streaming_survey.pdf |
| QOE-M02 | mandatory | ABR QoE objective | 2015 | A Control-Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP | 02_2015_yin_mpc_control_theoretic_abr_http.pdf |
| QOE-M03 | mandatory | ABR reward and QoE evaluation | 2017 | Neural Adaptive Video Streaming with Pensieve | 03_2017_mao_pensieve_neural_adaptive_video_streaming.pdf |
| QOE-M04 | mandatory | Utility-based ABR | 2020 | BOLA: Near-Optimal Bitrate Adaptation for Online Videos | 04_2020_spiteri_bola_near_optimal_bitrate_adaptation_ton.pdf |
| QOE-M05 | mandatory | Modern ABR smoothness/QoE | 2024 | SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming | 05_2024_chen_soda_consistent_high_quality_video_streaming.pdf |
| QOE-M06 | mandatory | QoE methodology and pitfalls | 2024 | Quality of Experience in Video Streaming: Status Quo, Pitfalls, and Guidelines | 06_2024_peroni_qoe_status_quo_pitfalls_guidelines.pdf |
| QOE-M07 | mandatory | Adaptive streaming quality assessment survey | 2022 | A brief survey on adaptive video streaming quality assessment | 07_2022_zhou_adaptive_video_streaming_quality_assessment_survey.htm |
| QOE-M08 | mandatory technical reference | Official technical source | 2026 access | VMAF official Netflix repository reference | 08_netflix_vmaf_reference_source.md |
| QOE-R01 | recommended context | HAS review | 2025 | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges | 09_2025_timmerer_has_review_current_advances_future_challenges.pdf |
| QOE-R02 | recommended context | End-to-end pipeline survey | 2025 | An End-to-End Pipeline Perspective on Video Streaming in Best-Effort Networks | 10_2025_peroni_gorinsky_video_streaming_pipeline_survey.pdf |
| QOE-R03 | recommended context | User preference QoE | 2022 | Adaptive Bitrate with User-level QoE Preference for Video Streaming | 11_2022_zuo_ruyi_user_level_qoe_preference.pdf |
| QOE-R04 | recommended context | QoE-driven streaming survey | 2025 | QoE-Driven Adaptive Video Streaming: Architectures, Techniques, and Future Research Challenges Toward 6G Networks | 12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey.pdf |

## Hard rules

- No source file is committed to the repository.
- Every mandatory source must receive a source card.
- Final QoE/reward decisions are deferred until the evidence matrix is complete.
- VMAF is considered a perceptual-quality reference, not automatically the primary QoE metric.
- Dry-runs generated before the final metric contract remain non-benchmark evidence.