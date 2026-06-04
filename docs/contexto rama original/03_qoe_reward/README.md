# Phase 3.5 - QoE, reward and final metric semantics

This directory contains the scientific and methodological documentation for Phase 3.5.

## Scope

Phase 3.5 closes the QoE/reward metric semantics needed before any formal evaluation, ranked controller comparison or IA/RL training.

## Subphase Status

| subphase | status | result |
| --- | --- | --- |
| Phase 3.5A0 | closed | evidence intake scaffold |
| Phase 3.5A1 | closed | source-card distillation and evidence matrix |
| Phase 3.5A2 | closed | QoE/reward decision docs, secondary metrics, formula catalog, gate policy and artifact schema boundary |
| Phase 3.5A2.1 | closed | schema marker validation hotfix |
| Phase 3.5B | closed | pure QoE calculator and synthetic `unittest` coverage |
| Phase 3.5C | closed | isolated QoE artifact post-processing from dry-run outputs |
| Phase 3.5D | closed | controlled QoE smoke runs and no-ranking validation |
| Phase 3.5E | closed | closure, memory integration and Phase 4 transition gate |

## A2 Decision Summary

- Primary QoE formula version: `qoe_linear_v1`.
- Primary future session metric: `qoe_linear_mean`.
- Segment reward candidate for future IA: `reward_n` from `qoe_linear_v1`.
- Sensitivity metric: `qoe_log_v1`.
- Startup: `startup_delay_s` report-only, with `startup_penalty_weight = 0.0`.
- VMAF/perceptual quality: deferred and artifact-dependent.
- Failures/incomplete runs: handled by `session_eval_gate` and `row_eval_gate`, not numeric punishment.

## Hard Boundaries

- No IA/RL training in Phase 3.5.
- No controller ranking in Phase 3.5.
- No benchmark claims in Phase 3.5.
- No generated CSV/log/run artifacts in Git.
- No raw PDFs, HTML captures or source captures in Git.
- No controller, player, runtime, trace-runner or media-engine changes.
- No Mahimahi or `tc/netem` experiments in Phase 3.5.

## Evidence And Decision Flow

1. Search notes and local source batch.
2. Source inventory.
3. Source triage.
4. Source cards distilled in Phase 3.5A1.
5. QoE evidence matrix.
6. QoE terms crosswalk.
7. QoE formula candidates.
8. Phase 3.5A2 decision documents:
   - `qoe_selection.md`
   - `reward_definition.md`
   - `secondary_metrics.md`
   - `metric_formula_catalog.md`
   - `evaluation_gate_policy.md`
   - `benchmark_result_schema.md`
9. Phase 3.5B pure calculator:
   - `core/evaluation/qoe.py`
   - `tests/test_qoe_metrics.py`
   - `qoe_calculator_implementation_spec.md`
   - `qoe_calculator_acceptance_tests.md`
10. Phase 3.5C isolated QoE artifact post-processor:
   - `core/evaluation/artifacts.py`
   - `scripts/compute_qoe_from_dry_run.py`
   - `tests/test_qoe_artifacts.py`
   - `dry_run_to_qoe_mapping.md`
   - `qoe_artifact_computation_spec.md`
   - `run_summary_schema.md`
   - `qoe_summary_schema.md`
11. Phase 3.5D controlled QoE smoke validation:
   - `scripts/run_qoe_smoke_scenarios.py`
   - `tests/test_qoe_smoke_scenarios.py`
   - `_historical/controlled_qoe_smoke_runbook.md`
   - `phase3_5_results_boundary.md`
   - `no_ranking_policy.md`
12. Phase 3.5E closure and transition:
   - `_historical/phase3_5_closure_report.md`
   - `_historical/phase3_5_open_limitations.md`
   - `_handoffs/phase3_5_transition_to_phase4.md`
   - `phase3_5_final_artifact_index.md`
   - `_historical/phase3_5_validation_summary.md`
   - `_historical/phase3_5_defense_talking_points.md`
   - `_handoffs/phase3_5_to_phase4_context_prompt.md`
   - `_handoffs/phase3_5_to_phase4_master_handoff.md`

## Phase 3.5B Implementation Summary

Phase 3.5B implements the A2 formulas as pure, deterministic functions:

- `compute_linear_qoe` for `qoe_linear_v1`.
- `compute_log_qoe` for `qoe_log_v1`.

The calculator is not integrated into dry-runs, runners, controllers, player, runtime or media engines.

## Phase 3.5C Artifact Summary

Phase 3.5C adds an isolated post-processor from dry-run artifacts to QoE artifacts:

- source: `trace_dry_run_segments.csv`, `trace_dry_run_summary.json`, `trace_dry_run_manifest.json`;
- output: `qoe_segment_rewards.csv`, `qoe_run_summary.json`, `qoe_artifact_manifest.json`;
- gates: legacy and non-evaluable dry-runs remain `do_not_use_for_eval`;
- flags: `outputs_are_benchmark_results=false` and `no_final_ranking=true`.

The post-processor is not a benchmark runner and does not rank controllers.

## Phase 3.5D Smoke Summary

Phase 3.5D adds a controlled smoke runner that generates synthetic dry-run-like artifacts outside the repository, invokes the Phase 3.5C QoE post-processor and writes an external `qoe_smoke_report.json`.

The smoke runner:

- uses only synthetic inputs;
- rejects output roots inside the repository;
- preserves `outputs_are_benchmark_results=false`;
- preserves `no_final_ranking=true`;
- validates gates for complete, legacy, incomplete and source-conflicting scenarios;
- performs no real dry-run, no controller ranking, no benchmark and no IA/RL.

## Next After D

Phase 3.5E closes this directory as the QoE/reward methodology block. It consolidates:

- final artifact index;
- open limitations;
- validation summary;
- defense talking points;
- transition gate to Phase 4.

## Next After E

The next expected block is Phase 4A0: IA/RL ABR literature intake and algorithm triage.


## Phase 6P2 Navigation

Phase 6P2 keeps canonical and support documents in this directory root, while older working material is grouped below:

- `_historical/`: preserved intermediate records and superseded notes.
- `_handoffs/`: closed prompts, handoffs, and transition instructions.
- `_templates/`: reusable templates, not current project state.

Use the phase README and `docs/science/CANONICAL_DOCUMENTS.md` before opening historical material.
