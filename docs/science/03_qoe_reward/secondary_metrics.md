# Phase 3.5A2 Secondary Metrics

Status: closed_phase3_5a2_documentation_contract.

PHASE_3_5A2_SECONDARY_METRICS_DEFINED: true

Secondary metrics support interpretation, diagnostics and later schema design. They do not replace the primary session metric `qoe_linear_mean`.

## Required Secondary Metrics

| metric | definition | unit/type | evaluation role |
| --- | --- | --- | --- |
| `avg_bitrate_kbps` | `mean(bitrate_kbps_n)` over evaluable segments | kbps | quality diagnostic |
| `avg_quality_mbps` | `mean(bitrate_kbps_n / 1000.0)` | Mbps utility | quality diagnostic aligned with `qoe_linear_v1` |
| `total_rebuffer_s` | `sum(rebuffer_s_n)` | seconds | impairment diagnostic |
| `rebuffer_ratio` | `total_rebuffer_s / playback_duration_s` when duration is available | ratio | impairment diagnostic |
| `stall_event_count` | count of rebuffer/stall events | count | impairment diagnostic |
| `quality_switch_count` | count of adjacent segments with changed bitrate | count | smoothness diagnostic |
| `up_switch_count` | count where `bitrate_kbps_n > bitrate_kbps_(n-1)` for `n > 1` | count | adaptation diagnostic |
| `down_switch_count` | count where `bitrate_kbps_n < bitrate_kbps_(n-1)` for `n > 1` | count | adaptation diagnostic |
| `total_switch_magnitude_kbps` | `sum(abs(bitrate_kbps_n - bitrate_kbps_(n-1)))` for `n > 1` | kbps | smoothness diagnostic |
| `avg_switch_magnitude_kbps` | `total_switch_magnitude_kbps / quality_switch_count` if switches exist, else `0.0` | kbps | smoothness diagnostic |
| `startup_delay_s` | time from session start to first playable media when measured homogeneously | seconds | report-only in A2 |
| `completed_segment_count` | number of completed/evaluable segments | count | comparability diagnostic |
| `expected_segment_count` | expected number of segments for the session/scenario | count | completion diagnostic |
| `session_completed` | whether the session completed as expected | boolean | gate input |
| `failure_reason` | reason string/code for failed or non-comparable run | categorical string | gate input |
| `trace_id` | trace identity/provenance identifier | string | grouping/provenance |
| `trace_split` | split label such as train/validation/test/OOD once defined | categorical string | leakage and evaluation boundary |
| `controller_name` | canonical controller identifier | string | grouping/provenance |
| `qoe_formula_version` | formula version used for metrics | string | must be `qoe_linear_v1` for primary A2-compatible summaries |
| `session_eval_gate` | session-level comparability gate | categorical | controls use of run summary |
| `row_eval_gate` | segment-row-level comparability gate | categorical | controls use of row telemetry |

## Report-Only And Deferred Metrics

- `startup_delay_s` is report-only in A2 and has `startup_penalty_weight = 0.0`.
- VMAF/perceptual metrics are deferred unless reproducible per-segment artifacts exist.
- Latency/live-specific metrics remain deferred unless a later phase scopes live or low-latency evaluation.

## Required Context Fields

Future evaluable run summaries should include at least:

- `qoe_formula_version`
- `eval_phase`
- `outputs_are_benchmark_results`
- `no_final_ranking`
- `session_eval_gate`
- `trace_id`
- `trace_split`
- `controller_name`

These fields prevent dry-runs, diagnostics and formal benchmark artifacts from being blurred together.
