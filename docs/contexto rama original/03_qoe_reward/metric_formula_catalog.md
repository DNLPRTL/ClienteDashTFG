# Phase 3.5A2 Metric Formula Catalog

Status: closed_phase3_5a2_documentation_contract.

PHASE_3_5A2_FORMULA_CATALOG_VERSION: metric_formula_catalog_v1

This catalog defines formulas and units for later implementation. It does not implement code and does not compute any artifact.

## Primary Linear Formula

| formula name | definition | unit |
| --- | --- | --- |
| `quality_utility_mbps` | `q_n = bitrate_kbps_n / 1000.0` | Mbps utility |
| `segment_reward_linear` | `reward_n = q_n - 4.3 * rebuffer_s_n - smoothness_n` | QoE utility units |
| `smoothness_penalty` | `sum(smoothness_n)`, where `smoothness_1 = 0.0` and `smoothness_n = abs(q_n - q_(n-1))` for `n > 1` | Mbps utility |
| `rebuffer_penalty` | `4.3 * sum(rebuffer_s_n)` | QoE utility units |
| `qoe_linear_sum` | `sum(segment_reward_linear_n)` | QoE utility units |
| `qoe_linear_mean` | `qoe_linear_sum / N` for `N` evaluable segments | QoE utility units per segment |

## Log Sensitivity Formula

| formula name | definition | unit |
| --- | --- | --- |
| `q_log_n` | `log(bitrate_kbps_n / min_bitrate_kbps)` | log utility |
| `segment_reward_log` | `q_log_n - 2.66 * rebuffer_s_n - smoothness_log_n` | log-QoE utility units |
| `smoothness_log_n` | `0.0` if `n == 1`, else `abs(q_log_n - q_log_(n-1))` | log-utility delta |
| `qoe_log_sum` | `sum(q_log_n) - 2.66 * sum(rebuffer_s_n) - sum(abs(q_log_n - q_log_(n-1))) for n > 1` | log-QoE utility units |
| `qoe_log_mean` | `qoe_log_sum / N` for `N` evaluable segments | log-QoE utility units per segment |

`min_bitrate_kbps` must be positive and documented from the representation ladder or controlled scenario. `qoe_log_v1` is a sensitivity metric, not the primary metric.

## Rebuffering Metrics

| formula name | definition | unit |
| --- | --- | --- |
| `total_rebuffer_s` | `sum(rebuffer_s_n)` | seconds |
| `rebuffer_ratio` | `total_rebuffer_s / playback_duration_s` when playback duration is available | ratio |
| `stall_event_count` | count of stall/rebuffer events, using the later implementation's event boundary | count |

## Switching Metrics

| formula name | definition | unit |
| --- | --- | --- |
| `switch_magnitude` | `abs(bitrate_kbps_n - bitrate_kbps_(n-1))` for `n > 1` | kbps |
| `quality_switch_count` | count of `switch_magnitude > 0` | count |
| `up_switch_count` | count of `bitrate_kbps_n > bitrate_kbps_(n-1)` for `n > 1` | count |
| `down_switch_count` | count of `bitrate_kbps_n < bitrate_kbps_(n-1)` for `n > 1` | count |
| `total_switch_magnitude_kbps` | `sum(switch_magnitude)` for `n > 1` | kbps |
| `avg_switch_magnitude_kbps` | `total_switch_magnitude_kbps / quality_switch_count` if `quality_switch_count > 0`, else `0.0` | kbps |

## Startup Report-Only Metric

| formula name | definition | unit |
| --- | --- | --- |
| `startup_delay_s` | time from session start to first playable/rendered media, when measured homogeneously | seconds |

`startup_delay_s` is report-only in A2. It is not included in `qoe_linear_v1`; `startup_penalty_weight = 0.0`.

## Gate-Related Formula Rules

- If required columns for a formula are missing, the affected artifact must not be silently scored.
- If `N == 0`, no mean QoE metric is comparable.
- If the session-level gate is not `use_for_eval`, benchmark-level aggregation must exclude the session.
