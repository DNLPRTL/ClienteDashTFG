# Phase 3.5A2 Benchmark Result Schema Boundary

Status: closed_phase3_5a2_documentation_contract.

PHASE_3_5A2_SCHEMA: segment_telemetry_run_summary_benchmark_aggregate
PHASE_3_5A2_BENCHMARK_STATUS: no_formal_benchmark_yet
PHASE_3_5A2_RANKING_STATUS: no_controller_ranking_yet

This document separates telemetry, run summaries and future benchmark aggregates. It does not create or validate artifacts.

## Validator Marker Summary

The schema boundary uses these exact layer names:

- segment-level telemetry: per-segment rows are not benchmark results by themselves.
- run-level summary: per-session summaries do not imply ranking.
- benchmark-level aggregate: cross-run aggregation will be closed in a later formal phase.

Dry-runs generated before the A2 contract do not pass automatically to benchmark status. Evaluable summaries must include `qoe_formula_version` and `eval_phase`; `outputs_are_benchmark_results` remains `false` until a formal benchmark phase, and `no_final_ranking=true` remains required until a formal ranking phase.

## Layer 1 - Segment-Level Telemetry

Segment-level telemetry records per-segment facts and derived row fields.

Expected future fields include:

- `segment_index`
- `bitrate_kbps`
- `quality_utility_mbps`
- `rebuffer_s`
- `smoothness_mbps`
- `segment_reward_linear`
- `row_eval_gate`
- `row_eval_gate_reason`
- `qoe_formula_version`
- `eval_phase`

Segment-level telemetry is not a benchmark. It is input evidence for run-level summaries once generated under a valid contract.

## Layer 2 - Run-Level Summary

Run-level summary aggregates one session/run.

Expected future fields include:

- `qoe_formula_version`
- `qoe_linear_sum`
- `qoe_linear_mean`
- `quality_utility_sum`
- `rebuffer_penalty`
- `smoothness_penalty`
- `total_rebuffer_s`
- `avg_bitrate_kbps`
- `avg_quality_mbps`
- `total_switch_magnitude_kbps`
- `quality_switch_count`
- `startup_delay_s`
- `completed_segment_count`
- `expected_segment_count`
- `session_completed`
- `failure_reason`
- `trace_id`
- `trace_split`
- `controller_name`
- `session_eval_gate`
- `session_eval_gate_reason`
- `eval_phase`
- `outputs_are_benchmark_results`
- `no_final_ranking`

A run-level summary does not imply ranking. It is only eligible for later aggregation if `session_eval_gate == use_for_eval` and the future benchmark protocol allows it.

## Layer 3 - Benchmark-Level Aggregate

Benchmark-level aggregate is a later-phase artifact that combines comparable run summaries across declared controllers, traces, splits and repetitions.

This layer is not closed in A2. A later phase must define:

- aggregation groups;
- confidence/statistical reporting policy;
- allowed trace splits;
- controller scope;
- regenerated artifact provenance;
- final benchmark naming;
- final ranking policy, if any.

## Required Boundary Fields

| field | required meaning |
| --- | --- |
| `qoe_formula_version` | must be present in evaluable summaries and set to the formula actually used |
| `eval_phase` | must identify the phase or protocol that generated the artifact |
| `outputs_are_benchmark_results` | must remain `false` until a formal benchmark phase |
| `no_final_ranking` | must remain `true` until a formal ranking phase |
| `session_eval_gate` | must control whether a run summary is eligible for aggregation |
| `row_eval_gate` | must control whether a segment row contributes to metrics |

## Legacy Dry-Run Rule

Dry-runs generated before this A2 contract do not pass automatically to benchmark status. They must remain diagnostic or `do_not_use_for_eval` unless regenerated under a later controlled contract.

## Explicit Non-Claims

- Segment-level telemetry is not benchmark evidence by itself.
- Run-level summary does not imply ranked comparison.
- Benchmark-level aggregate will be closed in a later phase.
- `outputs_are_benchmark_results` remains `false` until a formal benchmark phase.
- `no_final_ranking=true` until a formal ranking phase.
