# Phase 6 Metrics Schema

Status: final Phase 6A2 protocol decision. No metrics are computed in this document.

## Primary Metric

| Metric | Formula/source | Statistical unit | Role |
| --- | --- | --- | --- |
| `qoe_linear_mean` | Mean session QoE using `qoe_linear_v1` segment/session values | Session/trace | Primary Phase 6 metric |

`qoe_linear_v1` remains the primary QoE formula. `reward_n` is not changed in this block.

## Secondary Metrics

| Metric | Type | Notes |
| --- | --- | --- |
| `qoe_linear_sum` | QoE aggregate | Sum over completed/evaluable session segments. |
| `qoe_log_mean` | Sensitivity metric | Mean using `qoe_log_v1`; not primary. |
| `avg_bitrate_kbps` | Quality component | Average selected bitrate. |
| `total_rebuffer_s` | Rebuffer component | Total session rebuffering. |
| `rebuffer_ratio` | Rebuffer component | Rebuffer time normalized by session duration where defined. |
| `stall_event_count` | Rebuffer component | Count of stall/rebuffer events. |
| `quality_switch_count` | Switching component | Total quality-switch count. |
| `up_switch_count` | Switching component | Count of upward switches. |
| `down_switch_count` | Switching component | Count of downward switches. |
| `total_switch_magnitude_kbps` | Switching component | Sum of absolute bitrate switch magnitudes. |
| `avg_switch_magnitude_kbps` | Switching component | Mean absolute switch magnitude where switches exist. |
| `startup_delay_s` | Report-only | Report only unless measured homogeneously. |
| `completed_segment_count` | Completion/gate | Number of completed segments. |
| `expected_segment_count` | Completion/gate | Frozen expected segment count for the profile/session. |
| `session_completed` | Completion/gate | Boolean/session status. |
| `failure_reason` | Completion/gate | Reason for failure/exclusion if any. |
| `session_eval_gate` | Gate | Session-level `use_for_eval`, `diagnostic_only` or `do_not_use_for_eval`. |
| `row_eval_gate` | Gate | Row/segment-level `use_for_eval`, `diagnostic_only` or `do_not_use_for_eval`. |

## Gate Semantics

- `use_for_eval`: included in final statistical summaries.
- `diagnostic_only`: kept for debugging/explanation, excluded from final claims.
- `do_not_use_for_eval`: excluded from evaluation and diagnostic claims.

## Reporting Boundary

Metrics are reported at session/trace level for statistical comparison. Segment rows may support decomposition and selected trace figures, but they are not independent statistical units.
