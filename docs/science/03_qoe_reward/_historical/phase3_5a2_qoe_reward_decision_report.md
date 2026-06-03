# Phase 3.5A2 QoE/Reward Decision Report

Status: completed documentation block.

## Initial Repository State

- Expected initial HEAD: `475c2b2`
- Expected initial commit: `docs(science): distill Phase 3.5 QoE evidence`
- Branch: `main`
- Scope: Markdown-only scientific and methodological documentation.

## Documents Created

- `../qoe_selection.md`
- `../reward_definition.md`
- `../secondary_metrics.md`
- `../metric_formula_catalog.md`
- `../evaluation_gate_policy.md`
- `../benchmark_result_schema.md`
- `../_historical/phase3_5a2_qoe_reward_decision_report.md`

## Documents Updated

- `../README.md`
- `../qoe_formula_candidates.md`
- `../qoe_evidence_matrix.md`
- `../qoe_terms_crosswalk.md`
- `docs/science/07_memory/_historical/chapter_06_evaluation_methodology_notes.md`
- `docs/science/07_memory/_historical/tables_plan.md`
- `docs/science/07_memory/_historical/figures_plan.md`
- `docs/science/07_memory/figures_tables_register.md`
- `docs/science/07_memory/_historical/bibliography_plan.md`

## Decisions

| topic | A2 decision |
| --- | --- |
| primary QoE | `qoe_linear_v1` |
| primary session metric | `qoe_linear_mean` |
| accumulated auxiliary metric | `qoe_linear_sum` |
| segment reward | `reward_n = q_n - 4.3 * rebuffer_s_n - smoothness_n` |
| future IA reward status | future candidate only |
| log metric | `qoe_log_v1` retained as sensitivity |
| startup | `startup_delay_s` report-only, `startup_penalty_weight = 0.0` |
| VMAF/perceptual | deferred and artifact-dependent |
| failures/incomplete runs | handled by gates, not numeric punishment |
| dry-runs before A2 | not benchmarks and not automatically evaluable |

## Confirmation Of Boundaries

- No code was implemented.
- No `core/evaluation` package was created.
- No QoE tests were created.
- No controllers, player, runtime, media engines or trace scripts were modified.
- No dry-runs, Mahimahi or `tc/netem` experiments were executed.
- No CSVs, logs, zips, PDFs, datasets or media artifacts were generated.
- No IA/training was opened.
- No IA algorithm was selected.
- No ranking was produced.
- No formal benchmark was produced.

## Validator Boundary Markers

- no code: A2 is documentation only.
- no IA: A2 does not open training or algorithm selection.
- no ranking: A2 does not compare controllers.
- no benchmark: A2 does not produce formal benchmark evidence.

## What Remains For Phase 3.5B

- Implement a pure QoE calculator using `qoe_linear_v1`.
- Add synthetic unit tests for formula behavior and gates.
- Keep implementation isolated from controllers/player/runtime.
- Define small synthetic fixtures in tests only, without generated artifacts in the repository.
- Preserve `outputs_are_benchmark_results=false` until a later formal benchmark phase.


