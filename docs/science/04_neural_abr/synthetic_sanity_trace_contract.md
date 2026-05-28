# Synthetic sanity trace contract

## Purpose

Synthetic traces may be used only to sanity-check the environment and model behavior. They are not final benchmark traces.

## Allowed synthetic sanity traces

```text
constant_high_throughput
constant_low_throughput
step_down_throughput
step_up_throughput
oscillating_throughput
short_trace_edge_case
zero_or_missing_value_rejection_case
```

## Expected behavior examples

```text
constant_high:
  model should not be forced to min representation.

constant_low:
  model should avoid persistent high-bitrate rebuffering.

step_down:
  model should eventually reduce selected representation.

step_up:
  model may increase cautiously.

oscillating:
  model should not switch pathologically every segment without reason.
```

## Gate

Synthetic sanity traces are for debugging and safety checks only. They must not be used to claim final QoE performance.
