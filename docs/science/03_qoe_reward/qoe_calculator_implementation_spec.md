# Phase 3.5B QoE Calculator Implementation Spec

Status: implemented_phase3_5b_pure_calculator.

PHASE_3_5B_IMPLEMENTATION: pure_qoe_calculator

## Scope

Phase 3.5B materializes the Phase 3.5A2 formula contract as a pure Python calculator. The implementation is intentionally small, deterministic and unit-testable.

The calculator does not read files, write files, open network connections, spawn subprocesses or depend on external libraries. It uses only dataclasses and simple functions.

## API

The public API is exported from `core.evaluation`:

- `SegmentQoEInput`
- `QoEWeights`
- `QoEResult`
- `compute_linear_qoe`
- `compute_log_qoe`

`SegmentQoEInput` contains:

- `bitrate_kbps`
- `rebuffer_s`

`QoEWeights` contains:

- `rebuffer_weight`
- `smoothness_weight`
- `startup_penalty_weight`

`startup_penalty_weight` is validated but not applied in Phase 3.5B, matching A2 where startup remains report-only.

## qoe_linear_v1

`compute_linear_qoe(segments, weights=None)` implements:

```text
q_n = bitrate_kbps_n / 1000.0
smoothness_n = 0.0 if n == 1 else abs(q_n - q_(n-1))
reward_n = q_n - 4.3 * rebuffer_s_n - smoothness_n
```

The result includes `qoe_sum`, `qoe_mean`, quality utility, rebuffering penalty, smoothness penalty, switch counts and segment rewards.

## qoe_log_v1

`compute_log_qoe(segments, min_bitrate_kbps, weights=None)` implements the A2 sensitivity metric:

```text
q_log_n = log(bitrate_kbps_n / min_bitrate_kbps)
reward_n = q_log_n - 2.66 * rebuffer_s_n - smoothness_log_n
```

`min_bitrate_kbps` is explicit and is never inferred silently from the segment list.

## Validation

The calculator raises `ValueError` for empty inputs, non-positive bitrates, negative rebuffering, non-finite values, non-positive `min_bitrate_kbps`, and negative or non-finite weights.

## Non-Integration Boundary

Phase 3.5B does not integrate QoE into dry-runs, runners, controllers, player, runtime or media engines. It does not produce artifacts, rankings or benchmark outputs.

## IA Boundary

The segment reward remains compatible with a future IA phase, but Phase 3.5B does not train IA, choose an IA algorithm or create a training loop.
