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
| `06_validation/` | Phase 6A0-A2 | Protocol frozen | Active validation documentation, evidence scaffold and final experimental protocol. No benchmark authorization. |
| `07_memory/` | Thesis/memory | Active reference | Thesis integration, defense, tables, figures, and memory notes. |

## Phase 6 Boundary

Phase 6P and Phase 6P2 are closed pre-validation hygiene. They were not benchmark phases.

Phase 6A0/A1 opened validation documentation and protocol intake. Phase 6A2 freezes the final experimental protocol and authorizes the next technical readiness phase, but it does not open benchmark execution.

During Phase 6A2:

- no benchmark runs;
- no plots;
- no result CSVs;
- no rankings;
- no winner declaration;
- no claim that `neural_abr_lite` improves QoE;
- checksum leakage guardrails must be in place.
