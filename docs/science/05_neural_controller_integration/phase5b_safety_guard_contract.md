# Phase 5B safety guard contract

## Purpose

The safety guard runs after neural inference and before executing the selected action. It turns `raw_action` into either a safe action or fallback.

## Required behavior

- Preserve `raw_action` when it is safe.
- If `raw_action` is unsafe, search downward on the ordered ladder.
- Execute the highest lower feasible representation if one exists.
- If no feasible action exists, fallback to the conservative fallback chain or lowest valid representation.
- Record whether the guard intervened.

## Initial safety rule

The initial guard can be conservative and simple:

```text
Do not choose a candidate whose estimated download time exceeds a buffer guard
when enough online signals exist.
```

If signals are insufficient, the guard must use fallback rather than inventing confidence.

## Inputs

The guard may use only online-observable data:

- current buffer / queued time;
- recent completed throughput samples;
- candidate bitrate or candidate chunk size if available before decision;
- fragment duration if available before decision;
- current valid ladder.

## Telemetry

Required future diagnostics:

- `neural_raw_action`;
- `neural_safe_action`;
- `neural_safety_intervened`;
- `neural_fallback_reason` when fallback occurs.

## Boundary

The safety guard is not a benchmark and cannot be used to claim neural success.
