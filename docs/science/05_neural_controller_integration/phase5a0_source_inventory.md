# Phase 5A0 source inventory

## Inventory

| Source title | Year | Type | Wave | Triage | Phase 5 use |
|---|---:|---|---|---|---|
| SafeSABR runtime safety auditor | 2025/2026 | research source | Phase 5 integration delta | ACCEPTED_FOR_SOURCE_CARD | Runtime safety auditor, raw action vs safe action, lower feasible fallback |
| DeepBuffer action mask and variable ladder | 2025/2026 | research source | Phase 5 integration delta | ACCEPTED_FOR_SOURCE_CARD | Mandatory action mask and invalid representation filtering |
| A2BR domain priors and fallback | 2022 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Classical fallback as domain safety prior; no online adaptation |
| Real-world Video Adaptation with Reinforcement Learning | 2019/2020 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Candidate scoring per representation and production humility |
| Ahaggar bitrate guidance | 2024 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Advisory ML guidance with client heuristic boundary |
| Puffer/Fugu Learning in situ | 2020 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | ML predictor bounded by classical MPC and no Phase 5 ranking |
| Hybrid Adaptive Bitrate for Video Streaming | 2024/2025 | research source | Phase 5 integration delta | ACCEPTED_FOR_SOURCE_CARD | Decision-level fallback to RobustMPC-style logic |
| BayesMPC | 2024/2025 | research source | Phase 5 integration delta | ACCEPTED_FOR_SOURCE_CARD | Conservative uncertainty-aware feasibility checks |
| CausalSim | 2023 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | No telemetry contamination and no dry-run labels |
| Into the Wild / ABR-Arena | 2025 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Real-world testing gap and no claims from smoke tests |
| Comyco | 2020 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Imitation learning support; lifelong learning deferred |
| Oboe | 2018 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Runtime network regime diagnostics as future analysis |
| SODA | 2024 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Low compute and deployability constraints |
| SABR | 2025/2026 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | BC pretraining context; no RL fine-tuning in Phase 5 |
| BETA | 2025 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Under-generalization risk and no model switching now |
| ANT | 2024 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Network dynamics warning and richer diagnostics |
| Gelato/Plume | 2024 | research source | inherited plus integration delta | ACCEPTED_FOR_SOURCE_CARD | Trace skew and real-world validation caution |
| On the (In)Security of Loading Machine Learning Models | 2025/2026 | security reference | Phase 5 integration delta | ACCEPTED_FOR_SOURCE_CARD | Model loading threat model |
| HTTP Adaptive Streaming review | 2025 | survey/background | Phase 5 background | BACKGROUND_ONLY | HAS/DASH placement and client-side ABR context |
| Review of Learning-Based HAS methods | 2025 | survey/background | Phase 5 background | BACKGROUND_ONLY | Learning-based ABR deployment challenges |
| MetaABR | 2024 | research background | inherited plus integration delta | BACKGROUND_ONLY | Meta-learning deployment caution |
| PyTorch 2.12 documentation | 2026 | technical reference | Phase 5 integration delta | TECHNICAL_REFERENCE_ONLY | Safe local CPU `state_dict` loading |
| ONNX Runtime Python API | 2026 | technical reference | Phase 5 integration delta | TECHNICAL_REFERENCE_ONLY / DEFERRED | Future migration option only |

## Rejected or deferred search candidates

| Candidate | Phase 5 decision | Rationale |
|---|---|---|
| eBandit | REJECTED_FOR_PHASE5 | Not needed for the accepted Candidate Scorer integration contract. |
| PivotSketch | REJECTED_FOR_PHASE5 | Not directly tied to client-side ABR controller integration. |
| CADENCE | REJECTED_FOR_PHASE5 | Outside the immediate guarded scorer integration surface. |
| ABUV | REJECTED_FOR_PHASE5 | Not needed for action mask, fallback, bundle loading or controller API contracts. |
| Edge-assisted secure streaming | DEFERRED_TO_PHASE6_OR_FUTURE_WORK | Useful for broader system design, but Phase 5 is local CPU client integration. |
| Cross-layer wireless tuning | DEFERRED_TO_PHASE6_OR_FUTURE_WORK | Requires lower-layer signals not available in DashClientModular4. |
| mmWave/3D streaming | DEFERRED_TO_PHASE6_OR_FUTURE_WORK | Interesting domain extension, not part of the current DASH client controller contract. |

## Pensieve note

Pensieve remains inherited context from the Phase 4 source cards. No new Pensieve PDF was provided in this Phase 5 wave, so Phase 5 does not rewrite the Phase 4 Pensieve card. Pensieve is relevant only as background for learned ABR and for comparison discipline in later Phase 6 evaluation.
