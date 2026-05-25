# Phase 3.5C Run Summary Schema

Status: implemented_phase3_5c_schema.

PHASE_3_5C_RUN_SUMMARY_SCHEMA: qoe_run_summary_v1

## Purpose

`qoe_run_summary.json` is a run-level QoE summary generated from one dry-run artifact directory. It is not a benchmark-level aggregate and does not imply ranking.

## Required Fields

| field | meaning |
| --- | --- |
| `artifact_type` | always `qoe_run_summary` |
| `eval_phase` | always `phase3_5c_qoe_artifact_computation` |
| `qoe_formula_version` | primary formula, `qoe_linear_v1` |
| `primary_session_metric` | `qoe_linear_mean` |
| `outputs_are_benchmark_results` | always `false` in Phase 3.5C |
| `no_final_ranking` | always `true` in Phase 3.5C |
| `trace_id` | source trace identifier |
| `controller_name` | source controller identifier |
| `completed_segment_count` | number of segment rows used |
| `expected_segment_count` | expected count from parameter or source summary, or null |
| `session_completed` | whether completed and expected segment counts match when expected is known |
| `session_eval_gate` | `use_for_eval`, `diagnostic_only`, or `do_not_use_for_eval` |
| `gate_reasons` | list of gate reasons |
| `qoe_linear_sum` | accumulated primary QoE |
| `qoe_linear_mean` | primary session metric |
| `quality_utility_sum` | sum of Mbps quality utility |
| `avg_quality_mbps` | average Mbps quality utility |
| `avg_bitrate_kbps` | average selected bitrate |
| `total_rebuffer_s` | accumulated rebuffering seconds |
| `rebuffer_penalty` | linear rebuffer penalty |
| `smoothness_penalty` | linear smoothness penalty |
| `stall_event_count` | rows with positive rebuffering |
| `quality_switch_count` | bitrate switch count |
| `up_switch_count` | upward switch count |
| `down_switch_count` | downward switch count |
| `total_switch_magnitude_kbps` | accumulated switch magnitude |
| `avg_switch_magnitude_kbps` | average magnitude over switches |
| `source_segments_filename` | source dry-run segment CSV filename |
| `source_summary_filename` | source dry-run summary JSON filename |
| `source_manifest_filename` | source dry-run manifest JSON filename |

## Optional Log Fields

When `--min-bitrate-kbps` is supplied:

- `log_qoe_computed=true`
- `qoe_log_sum`
- `qoe_log_mean`
- `qoe_log_min_bitrate_kbps`

When it is absent:

- `log_qoe_computed=false`

The post-processor never infers `min_bitrate_kbps` silently from the input.

## Boundary

This schema is a run-level summary only. Future benchmark-level aggregation remains a later phase.
