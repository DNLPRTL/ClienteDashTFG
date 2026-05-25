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

## Phase 3.5B Implementation Summary

Phase 3.5B implements the A2 formulas as pure, deterministic functions:

- `compute_linear_qoe` for `qoe_linear_v1`.
- `compute_log_qoe` for `qoe_log_v1`.

The calculator is not integrated into dry-runs, runners, controllers, player, runtime or media engines.

## Next After B

The next expected block is Phase 3.5C: controlled integration planning or run-summary wiring around the pure calculator, while preserving A2 gates and avoiding benchmark/ranking claims.
