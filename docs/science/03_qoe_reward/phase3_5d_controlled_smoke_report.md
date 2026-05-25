# Phase 3.5D Controlled QoE Smoke Report

## Initial HEAD

Expected initial HEAD: `50dd3aa feat(qoe): add dry-run artifact QoE post-processor`.

## Files Created

- `scripts/run_qoe_smoke_scenarios.py`
- `tests/test_qoe_smoke_scenarios.py`
- `docs/science/03_qoe_reward/controlled_qoe_smoke_runbook.md`
- `docs/science/03_qoe_reward/phase3_5_results_boundary.md`
- `docs/science/03_qoe_reward/no_ranking_policy.md`
- `docs/science/03_qoe_reward/phase3_5d_controlled_smoke_report.md`

## Files Updated

- `docs/science/03_qoe_reward/README.md`
- `docs/science/07_memory/chapter_06_evaluation_methodology_notes.md`
- `docs/science/07_memory/tables_plan.md`
- `docs/science/07_memory/figures_plan.md`
- `docs/science/07_memory/figures_tables_register.md`

## Smoke Scenarios Defined

- `complete_use_for_eval`: synthetic complete session with `row_eval_gate=use_for_eval`, expected `qoe_linear_sum=2.0` and `session_eval_gate=use_for_eval`.
- `legacy_do_not_use_for_eval`: synthetic legacy/non-evaluable source rows, expected `session_eval_gate=do_not_use_for_eval`.
- `incomplete_session`: three completed segments with expected count four, expected `incomplete_session` gate reason.
- `source_claims_benchmark`: source rows claim benchmark output, while QoE outputs keep `outputs_are_benchmark_results=false`.

## Script Created

`scripts/run_qoe_smoke_scenarios.py` creates synthetic dry-run-like sources outside the repository and invokes the Phase 3.5C QoE post-processor through `compute_qoe_artifacts_from_dry_run`.

The script rejects output roots inside the repository and writes a top-level external `qoe_smoke_report.json`.

## Synthetic Tests

`tests/test_qoe_smoke_scenarios.py` covers report creation, no-benchmark/no-ranking flags, scenario outcomes, per-scenario QoE artifact files, CLI execution and rejection of repository-internal output roots.

## External Artifacts

Phase 3.5D smoke outputs are generated outside Git. They are validation artifacts only and are not part of the repository.

## No Runner Integration

No dry-run runner, trace replay runner, controller adapter, controller, player, runtime or media engine is modified.

## No IA, Ranking Or Benchmark

Phase 3.5D does not train IA/RL, does not select an IA algorithm, does not rank controllers and does not produce benchmark results.

## Next Phase

Phase 3.5E should close Phase 3.5 with a transition gate: what is now safe to use, what remains diagnostic, and which conditions must hold before formal evaluation.

## Validation markers

- HEAD_EXPECTED: 50dd3aa
- PHASE_3_5D_STATUS: controlled_smoke_defined
- no runner integration
- no dry-run real execution
- no benchmark
- no ranking
- no IA
- qoe_smoke_report.json
- qoe_run_summary.json
- qoe_segment_rewards.csv
- qoe_artifact_manifest.json
