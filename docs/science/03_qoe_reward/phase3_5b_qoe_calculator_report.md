# Phase 3.5B QoE Calculator Report

Status: completed_phase3_5b_pure_calculator.

## Initial Repository State

- Initial HEAD: `02c0695`
- Context: final Phase 3.5A2.1 hotfix immediately after `8970fd4`.
- Branch: `main`

## Files Created

- `core/evaluation/__init__.py`
- `core/evaluation/qoe.py`
- `tests/test_qoe_metrics.py`
- `docs/science/03_qoe_reward/qoe_calculator_implementation_spec.md`
- `docs/science/03_qoe_reward/qoe_calculator_acceptance_tests.md`
- `docs/science/03_qoe_reward/phase3_5b_qoe_calculator_report.md`

## Files Updated

- `docs/science/03_qoe_reward/README.md`
- `docs/science/07_memory/chapter_06_evaluation_methodology_notes.md`
- `docs/science/07_memory/tables_plan.md`
- `docs/science/07_memory/figures_plan.md`
- `docs/science/07_memory/figures_tables_register.md`

## API Implemented

- `SegmentQoEInput`
- `QoEWeights`
- `QoEResult`
- `compute_linear_qoe`
- `compute_log_qoe`

## Formulas Implemented

- `qoe_linear_v1` primary formula from Phase 3.5A2.
- `qoe_log_v1` sensitivity formula from Phase 3.5A2.

## Synthetic Tests

The test suite covers linear QoE without rebuffering, linear QoE with rebuffering, one-segment behavior, invalid inputs, non-finite inputs, negative weights, log QoE sensitivity, invalid log minimum and immutable segment rewards.

## Purity Confirmation

- No IO.
- No pandas.
- No numpy.
- No subprocess.
- No network.
- No generated CSV/log/PDF/zip/media artifacts.

## Boundary Confirmation

- No runner integration.
- No dry-run execution.
- No controller changes.
- No player changes.
- No runtime changes.
- No media-engine changes.
- No IA/training.
- No ranking.
- No benchmark.

## What Remains For Phase 3.5C

- Decide how the pure calculator will be wired into future run summaries.
- Preserve gate semantics from A2 before any artifact promotion.
- Keep `outputs_are_benchmark_results=false` until a formal benchmark phase.
- Define any integration tests without producing benchmark claims.
