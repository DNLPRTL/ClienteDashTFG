# Phase 6A0 Source Inventory

Status: canonical inventory from the Phase 6A0 Markdown intake waves.

## Mandatory Methodology

| Source | Year | Canonical card | Phase 6A0 role |
| --- | ---: | --- | --- |
| Yan et al., Learning in situ / Puffer Fugu | 2020 | `source_cards/2020_yan_learning_in_situ_puffer_fugu.md` | uncertainty, distributions, claims discipline |
| Alomar et al., CausalSim | 2023 | `source_cards/2023_alomar_causalsim_unbiased_trace_driven_simulation.md` | trace-driven exogeneity assumption, leakage guardrails |
| Chen et al., SODA | 2024 | `source_cards/2024_chen_soda_consistent_high_quality_video_streaming.md` | modern non-neural ABR context, switching and smoothness reporting |
| Hoffman et al., Into the Wild / ABR-Arena | 2025 | `source_cards/2025_hoffman_into_the_wild_abr_arena.md` | sim-to-real caution and no global deployment claim |
| Peroni and Gorinsky survey | 2025 | `source_cards/2025_peroni_gorinsky_end_to_end_pipeline_video_streaming_survey.md` | end-to-end streaming taxonomy and scope |
| Timmerer et al. HAS review | 2025 | `source_cards/2025_timmerer_has_review_current_advances_future_challenges.md` | HAS/DASH and QoE state-of-the-art framing |

## Guardrails And Secondary Sources

| Source | Year | Canonical card | Phase 6A0 role |
| --- | ---: | --- | --- |
| Netravali et al., Mahimahi | 2015 | `source_cards/2015_netravali_mahimahi_record_replay_http.md` | secondary emulation reference, not primary benchmark |
| Bothra et al., Veritas | 2022 | `source_cards/2022_bothra_veritas_causal_queries_video_streaming.md` | causal-query and counterfactual caution |
| Patel et al., Plume | 2023 | `source_cards/2023_patel_plume_prioritized_trace_sampling.md` | trace skew, tail traces and stratified reporting |
| Luo et al., SABR / ABRBench | 2025 | `source_cards/2025_luo_sabr_abrbench_generalization.md` | OOD split discipline and BC/RL context with caution |
| Sentosa et al., CellReplay | 2025 | `source_cards/2025_sentosa_cellreplay_record_replay_cellular.md` | cellular emulation limits and diagnostic-only demos |

## Dataset And Trace Sources

| Source | Year | Canonical card | Phase 6A0 role |
| --- | ---: | --- | --- |
| Riiser et al., Norway HSDPA / MMSys dataset | 2013 | `dataset_cards/2013_riiser_hsdpa_norway_dataset.md` | first materialization candidate |
| van der Hooft et al., Ghent 4G/LTE logs | 2016 | `dataset_cards/2016_van_der_hooft_ghent_4g_lte_dataset.md` | first materialization candidate with duplicate guardrail |
| Raca et al., Beyond Throughput 4G LTE | 2018 | `dataset_cards/2018_raca_4g_lte_dataset.md` | future/OOD 4G candidate |
| Raca et al., Beyond Throughput 5G | 2020 | `dataset_cards/2020_raca_5g_dataset.md` | future/OOD 5G candidate |
| Narayanan et al., Lumos5G | 2020 | `dataset_cards/2020_narayanan_lumos5g_dataset.md` | future/OOD 5G mmWave candidate |

## QoE And Reporting Sources

| Source | Year | Canonical card | Phase 6A0 role |
| --- | ---: | --- | --- |
| Duanmu et al., Streaming QoE Index | 2017 | `source_cards/2017_duanmu_streaming_qoe_index.md` | limits of linear/objective QoE and perceptual claims |
| Barman and Martini QoE survey | 2019 | `source_cards/2019_barman_martini_qoe_modeling_has_survey.md` | QoE influence factors and MOS/VMAF caution |
| Taraghi et al., heuristic ABR QoE | 2021 | `source_cards/2021_taraghi_understanding_qoe_heuristic_abr.md` | component reporting and objective/subjective gap |

## Optional Or Future

| Candidate | Status | Reason |
| --- | --- | --- |
| ABRBench from SABR | Deferred candidate | Needs dataset card, access/license/format check and leakage audit before any use. |
| Raca 4G, Raca 5G, Lumos5G | Recommended future OOD | Useful for modern OOD, but not required before first protocol closure. |
| Mahimahi/tc/netem/CellReplay style emulation | Secondary diagnostic/demo | May support Ubuntu demos, but primary evaluation remains Python trace-driven. |
| VMAF, P.1203, MOS-like reporting | Deferred/artifact-dependent | Requires media/perceptual artifacts and a documented metric version change. |

## Deferred Or Not Used

| Candidate | Decision | Reason |
| --- | --- | --- |
| Raw PDFs as implementation sources | Not used | Codex must use Markdown intake/source cards/specs first. |
| VM bridge network as benchmark | Not used | VM server is for content/demo/media_profile, not benchmark network. |
| Phase 4E2 as strong generalization evidence | Not used | Phase 4E2 remains diagnostic because of checksum leakage history. |
| Lancaster dataset | Gap, not authorized | Intended Phase 6C candidate needs a source note/card in this validation pack before use. |
| SODA, SABR, ABR-Arena, Veritas, CausalSim implementations | Not implemented | They inform protocol and threats only in Phase 6A0. |
