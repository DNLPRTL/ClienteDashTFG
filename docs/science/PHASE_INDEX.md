# Science Phase Index

This file maps project phases to their effective documentation paths.

| path | effective phase | status | notes |
| --- | --- | --- | --- |
| `00_field_map/` | Field map | Canonical background | Scope, DASH references, research questions, and source inventory. |
| `01_baselines/` | Phase 2 | Closed | Baseline selection, implementation, tests, limitations, and closure. |
| `02_traces_replay/` | Phase 3 | Closed | Trace selection, replay methodology, leakage policy, schema, and dry-run path. |
| `03_qoe_reward/` | Phase 3.5 | Closed | QoE/reward contract and artifact boundary. |
| `04_neural_abr/` | Phase 4 | Closed as diagnostic/training trail | NeuralABR-Lite candidate scorer, dataset, teacher, training, and export work. |
| `05_neural_controller_integration/` | Phase 5 | Closed | Canonical effective path for guarded `neural_abr_lite` integration. Do not rename. |
| `06_validation/` | Phase 6A0-6D | Protocol frozen; trace materialization and media-profile freeze tooling | Active validation documentation, evidence scaffold, final experimental protocol, readiness gates, Phase 6C external trace materialization and Phase 6D MPD-derived media-profile freeze. No benchmark authorization. |
| `07_memory/` | Thesis/memory | Active reference | Thesis integration, defense, tables, figures, and memory notes. |

## Phase 6 Boundary

Phase 6P and Phase 6P2 are closed pre-validation hygiene. They were not benchmark phases.

Phase 6A0/A1 opened validation documentation and protocol intake. Phase 6A2 freezes the final experimental protocol. Phase 6B adds evaluation readiness gates, manifest schema validation and `canonical_content_fingerprint` audit hardening. Phase 6C automates public-source acquisition, extraction, normalization, manifest building, validation, eligibility audit and external manifest freeze. Phase 6C-H1 hardens live materialization with primary-only defaults, logs, bounded progress and resume controls. Phase 6D adds MPD-derived media-profile extraction, validation, compatibility checking and external freeze tooling. These phases do not open benchmark execution.

During Phase 6C/6D:

- no benchmark runs;
- no plots;
- no result CSVs;
- no rankings;
- no winner declaration;
- no claim that `neural_abr_lite` improves QoE;
- no manual source config or manifest creation is required;
- real datasets, normalized CSVs, receipts, local manifests and reports stay outside Git;
- real MPDs, segment files, media-profile outputs, logs and freeze reports stay outside Git;
- checksum and canonical content fingerprint leakage guardrails must be in place;
- `ready_for_benchmark=false` and `benchmark_authorized=false` remain mandatory.

Final trace IDs are frozen only when the external `phase6_trace_manifest_final.json` exists after Phase 6C acquisition, normalization, validation, eligibility audit and freeze.

The shared media profile is frozen only when the external `media_profile_phase6_v1.json` exists after Phase 6D MPD extraction, validation, compatibility check and freeze. Phase 6E planning requires both external artifacts.
