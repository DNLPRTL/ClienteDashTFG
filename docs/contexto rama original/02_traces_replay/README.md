# Phase 3 Trace Replay Methodology

This folder is the Phase 3.1 documentation scaffold for trace, dataset, replay and emulation methodology.

Phase 1 closed the client hardening work. Phase 2 closed the baseline controller implementation set: `min_rate`, `fixed_rate`, `max_rate`, `rate_based`, `bba`, `bola`, `mpc` and `robust_mpc`. Phase 3 does not add a new controller. It defines how future evaluations can expose those existing controllers to reproducible network conditions without changing the player, media engines, metric definitions or controller APIs.

## Objective

Define the evidence base and decision gates for selecting throughput traces, replay tools, emulation tools and synthetic test scenarios before any benchmark ranking or final QoE/reward is attempted.

## Questions Phase 3 Must Close

1. Which trace datasets are scientifically relevant, available, legally usable and small enough to integrate without repository bloat?
2. Which datasets should be candidates for train, validation, test and out-of-distribution evaluation?
3. Which sources are only methodological references and which sources are actual trace candidates?
4. Is the project better served by Mahimahi, Linux `tc/netem`, a custom fake trace-driven runner, or a combination?
5. What conversion rules are required before a dataset can become a replay input?
6. How will trace leakage be prevented if later phases introduce tuning, learning or parameter selection?
7. Which synthetic traces are needed to test a future runner before real datasets are used?
8. Which run artifacts should exist in future experiments, and which artifacts must stay out of git?

## Relationship With Phase 2 Controllers

Phase 3 treats the Phase 2 controllers as frozen evaluation subjects. The trace/replay methodology may exercise their existing inputs, but it must not modify controller logic, controller names, player behavior, media engines or metric definitions.

The methodology must preserve the existing separation between parser, segment download, buffer, playback engine, ABR control, logging and evaluation. If a future runner is implemented, it must feed controlled network behavior through an approved boundary rather than embedding trace assumptions into controllers.

## Explicit Non-Goals

- no dataset download;
- no replay implementation;
- no final QoE/reward definition;
- no benchmark ranking;
- no IA/RL implementation;
- no controller changes;
- no player changes;
- no media engine changes;
- no GStreamer benchmark;
- no generated artifacts;
- no PDFs in the repository;
- no logs, CSVs, ZIPs or media in the repository;
- no `pytest`.

## Directory Map

| document | purpose |
| --- | --- |
| `source_inventory.md` | Initial source categories and decisions for trace/replay literature and datasets. |
| `search_protocol.md` | Repeatable literature and dataset search methodology. |
| `trace_dataset_selection.md` | Dataset selection criteria and decision workflow. |
| `trace_dataset_matrix.md` | Candidate dataset matrix with risk and split columns. |
| `_templates/trace_dataset_card_template.md` | Template for future per-dataset cards. |
| `_templates/method_card_template.md` | Template for future replay/emulation method cards. |
| `replay_emulation_decision.md` | Decision criteria for replay, emulation and fake trace-driven execution. |
| `mahimahi_or_alternatives.md` | Comparison of Mahimahi, `tc/netem` and a custom fake runner. |
| `generalization_protocol.md` | Generalization and OOD evaluation planning rules. |
| `evaluation_network_scenarios.md` | Scenario taxonomy for later evaluation design. |
| `train_validation_test_ood_policy.md` | Split policy for future tuning, learning and reporting. |
| `leakage_prevention_policy.md` | Controls against trace, parameter and artifact leakage. |
| `_historical/replay_runner_requirements.md` | Requirements for a future runner without implementing it. |
| `_historical/synthetic_trace_test_plan.md` | Synthetic trace plan for future runner validation. |
| `run_artifact_expectations.md` | Expected future run artifacts and repository hygiene. |
| `_historical/phase3_memory_notes.md` | Thesis memory and defense usage notes. |
| `common_trace_schema.md` | Phase 3.2B normalized trace schema v1. |
| `trace_units_and_normalization.md` | Unit conversion and normalization policy. |
| `trace_manifest_schema.md` | `trace_manifest_v1` metadata schema. |
| `trace_directory_layout.md` | External raw/normalized/manifest storage policy. |
| `_historical/trace_conversion_plan.md` | Conversion priority and implementation readiness gate. |
| `_historical/dataset_download_plan.md` | Future external download policy; no downloads in Phase 3.2B. |
| `trace_source_to_internal_mapping.md` | Dataset/source card mapping to the internal schema. |
| `trace_split_manifest_policy.md` | `split_manifest_v1` schema and split leakage rules. |
| `trace_schema_acceptance_tests.md` | Future `unittest` acceptance plan for schema validation. |
| `trace_schema_risks_and_open_decisions.md` | Remaining schema and conversion risks. |
| `_historical/phase3_2b_closure_report.md` | Phase 3.2B closure record. |
| `phase3_2c_local_dataset_acquisition.md` | Local raw acquisition status for first real trace candidates. |
| `_historical/phase3_2c_dataset_audit_summary.md` | Audit summary and risks from local acquisition. |
| `_historical/phase3_2c_closure_report.md` | Phase 3.2C closure record. |
| `phase3_3a_synthetic_trace_schema_validation.md` | Synthetic-only implementation of normalized trace schema validation. |
| `_historical/phase3_3a_closure_report.md` | Phase 3.3A closure record. |
| `phase3_3b_trace_loader.md` | Minimal loader for already-normalized schema-v1 traces. |
| `_historical/phase3_3b_closure_report.md` | Phase 3.3B closure record. |
| `phase3_4a_dataset_converters.md` | Dataset converter architecture, assumptions, API and CLI. |
| `_historical/phase3_4a_local_conversion_smoke_runbook.md` | Local outside-repo smoke procedure for real raw candidates. |
| `_historical/phase3_4a_closure_report.md` | Phase 3.4A closure record. |
| `phase3_4b_trace_driven_network_model.md` | Deterministic network model semantics and API. |
| `phase3_4b_fake_replay_adapter.md` | Small fake replay adapter boundary around the network model. |
| `_historical/phase3_4b_local_model_smoke_runbook.md` | Local outside-repo smoke procedure for the model. |
| `_historical/phase3_4b_closure_report.md` | Phase 3.4B closure record. |
| `phase3_4c_controlled_dry_runs.md` | Controlled dry-run harness semantics and artifact boundary. |
| `phase3_4c_controller_adapter.md` | Existing-controller adapter contract and anti-leakage boundary. |
| `_historical/phase3_4c_local_dry_run_smoke_runbook.md` | Local outside-repo smoke procedure for dry-run artifacts. |
| `_historical/phase3_4c_closure_report.md` | Phase 3.4C closure record. |
| `phase3_4d_mahimahi_tc_decision.md` | Mahimahi/tc decision: Python primary, Mahimahi secondary, tc fallback. |
| `_historical/phase3_4d_mahimahi_runbook.md` | Ubuntu-only Mahimahi probe/runbook boundary. |
| `_historical/phase3_4d_tc_netem_runbook.md` | Linux-only `tc/netem` probe/runbook boundary. |
| `phase3_4d_environment_probe_policy.md` | Local/audit-only probe policy and artifact boundary. |
| `phase3_4d_validation_boundaries.md` | Smoke, dry-run, validation, benchmark and final-evaluation boundaries. |
| `_historical/phase3_4d_closure_report.md` | Phase 3.4D closure record. |
| `trace_dataset_cards/` | Placeholder for later dataset cards. |
| `method_cards/` | Placeholder for later method cards. |

## Current Decision Boundary

No dataset is final until `trace_dataset_selection.md` is completed. No dataset is downloaded into the repository. Full Puffer raw data remains metadata-only in Phase 3.1. FCC raw data remains reference-only until a conversion and storage plan exists. Mahimahi is a method candidate, not a mandatory implementation. `tc/netem` is a fallback or complementary method candidate. A custom fake trace-driven runner is the primary likely implementation candidate for reproducible Python tests, but this phase only documents requirements.

## Phase 3.2B Trace Schema Update

Phase 3.2B defines `normalized_trace_schema_v1` as a CSV-like time series with required columns `timestamp_s`, `duration_s` and `throughput_kbps`. It also defines `trace_manifest_v1`, `split_manifest_v1`, external storage paths and the conversion priority.

This update still does not implement replay or converters, download datasets, define final QoE/reward, run benchmarks, rank controllers, open IA/RL, or change runtime code.

## Phase 3.2C Local Acquisition Update

Phase 3.2C records that the first three real trace candidates are locally acquired outside the repository:

1. HSDPA Norway / Riiser MMSys 2013;
2. Ghent 4G/LTE Bandwidth Logs;
3. Lancaster ABR-Throughput-Traces.

The local raw files are not normalized traces, final split inputs, benchmark artifacts or QoE evidence. The next recommended implementation block is Phase 3.3A synthetic trace fixtures and schema validation, not full replay.

## Phase 3.3A Synthetic Validation Update

Phase 3.3A adds a minimal standard-library validation layer for `normalized_trace_schema_v1` under `core/trace_replay/`. Tests generate tiny synthetic CSVs inside `unittest` temporary directories.

This validates the schema only. It does not read real raw datasets, implement converters, implement TraceLoader, implement replay, define QoE/reward, run benchmarks, rank controllers or change client runtime behavior.

## Phase 3.3B TraceLoader Update

Phase 3.3B adds a minimal `TraceLoader` for already-normalized `normalized_trace_schema_v1` rows and CSV files. It preserves row order and metadata, and delegates validity checks to the Phase 3.3A validator.

This is still not replay, conversion, client integration, QoE/reward, benchmark ranking or IA/RL.

## Phase 3.4A Dataset Converter Update

Phase 3.4A adds standard-library converters for HSDPA Norway / Riiser MMSys 2013, Ghent 4G/LTE Bandwidth Logs and Lancaster ABR-Throughput-Traces. The converters emit validated `normalized_trace_schema_v1` CSVs and local `trace_manifest_v1` JSON files.

Normalized real traces and generated manifests are local artifacts outside the repository, not benchmark results. This update still does not implement replay, connect traces to runtime, define final QoE/reward, rank controllers, freeze final splits, execute Mahimahi or `tc/netem`, change controllers/player/media engines, or open IA/RL.

## Phase 3.4B Trace-Driven Network Model Update

Phase 3.4B adds a deterministic `TraceDrivenNetworkModel` and a small `TraceDrivenFakeReplayAdapter`. They consume `LoadedTrace` objects and simulate segment download durations while treating gaps and zero-throughput intervals as no-delivery time.

This is not runtime integration and not a benchmark runner. Controllers must not receive complete traces or future samples. QoE/reward remains deferred to Phase 3.5, and Mahimahi/`tc/netem` remain later optional validation/runbook work.

## Phase 3.4C Controlled Dry-Run Update

Phase 3.4C adds a controlled dry-run harness that can execute existing Phase 2 controllers through the public controller contract against a normalized trace and the Phase 3.4B network model.

The dry-run writes artifacts only when explicitly invoked and only to the requested output directory. All artifacts are labeled `phase3_4c_dry_run`, `outputs_are_benchmark_results = false`, `final_qoe_reward_defined = false`, `row_eval_gate = do_not_use_for_eval` and `no_final_ranking = true`.

This remains outside final benchmark, QoE/reward, IA/RL, Mahimahi, `tc/netem`, player/runtime integration, media-engine changes and controller changes.

## Phase 3.4D Mahimahi/tc Decision Update

Phase 3.4D closes the method decision for external emulation tools. The custom Python trace-driven pipeline remains the primary reproducible path for Phase 3.5 and future IA work.

Mahimahi is retained as a secondary Ubuntu-only validation/runbook candidate. Linux `tc/netem` is retained as a Linux fallback/sanity/runbook candidate. Neither tool is required for Phase 3.5, and neither produces benchmark evidence in Phase 3.4D.

This update is documentation only: no installation, no emulation execution, no qdisc or namespace changes, no final QoE/reward, no ranking and no runtime/controller/player/media changes.


## Phase 6P2 Navigation

Phase 6P2 keeps canonical and support documents in this directory root, while older working material is grouped below:

- `_historical/`: preserved intermediate records and superseded notes.
- `_templates/`: reusable templates, not current project state.

Use the phase README and `docs/science/CANONICAL_DOCUMENTS.md` before opening historical material.
