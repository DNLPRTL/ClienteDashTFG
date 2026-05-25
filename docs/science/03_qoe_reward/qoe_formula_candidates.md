# QoE Formula Candidates

Status: resolved_phase3_5a2.

PHASE_3_5A2_CANDIDATES_RESOLVED: true

This document records how the A1 candidates were resolved in A2. It is no longer an open selection document.

## Candidate Resolution

| candidate | A2 resolution | reason |
| --- | --- | --- |
| `qoe_linear_candidate` | `selected_as_qoe_linear_v1_primary` | Pensieve/MPC support additive quality, rebuffering and smoothness; current telemetry supports bitrate-derived Mbps utility |
| `qoe_log_candidate` | `retained_as_qoe_log_v1_sensitivity` | Pensieve/BOLA support concave/log utility and diminishing returns, but it is kept secondary |
| `qoe_perceptual_candidate` | `deferred_artifact_dependent` | Zhou/Netflix/Ruyi support relevance, but per-segment perceptual artifacts are not part of the current contract |
| `startup_penalty_candidate` | `report_only_weight_0` | Seufert/Yin support startup as an influence factor, but measurement homogeneity is not closed for primary scoring |
| `failure_gate_candidate` | `selected_as_gate_policy` | Incomplete/non-comparable artifacts should be gated instead of numerically punished |

## Selected Primary Candidate

`qoe_linear_candidate` is closed as `qoe_linear_v1`.

For each segment:

```text
q_n = bitrate_kbps_n / 1000.0
smoothness_n = 0.0 if n == 1 else abs(q_n - q_(n-1))
reward_n = q_n - 4.3 * rebuffer_s_n - smoothness_n
```

For each session:

```text
qoe_linear_sum = sum(reward_n)
qoe_linear_mean = qoe_linear_sum / N
```

`qoe_linear_mean` is the primary future session metric.

## Retained Sensitivity Candidate

`qoe_log_candidate` is retained as `qoe_log_v1` sensitivity:

```text
q_log_n = log(bitrate_kbps_n / min_bitrate_kbps)
qoe_log_sum = sum(q_log_n) - 2.66 * sum(rebuffer_s_n) - sum(abs(q_log_n - q_log_(n-1)))
qoe_log_mean = qoe_log_sum / N
```

It must not be used as the primary metric unless a later versioned decision changes the contract.

## Deferred Candidates

- VMAF/perceptual quality remains deferred and artifact-dependent.
- Startup remains report-only in A2 with `startup_penalty_weight = 0.0`.
- Failure handling is closed as gate policy through `evaluation_gate_policy.md`.

## Implementation Boundary

The candidate resolution is documentation only. A later Phase 3.5B may implement a pure calculator and synthetic tests.
