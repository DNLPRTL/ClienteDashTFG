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
| `06_validation/` | Phase 6 | Not opened | Future validation path. It should not exist before Phase 6A0 opens it. |
| `07_memory/` | Thesis/memory | Active reference | Thesis integration, defense, tables, figures, and memory notes. |

## Phase 6 Boundary

Phase 6P is pre-validation hygiene. It is not a benchmark phase.

Before Phase 6A0 opens:

- no benchmark runs;
- no plots;
- no rankings;
- no winner declaration;
- no claim that `neural_abr_lite` improves QoE;
- checksum leakage guardrails must be in place.
