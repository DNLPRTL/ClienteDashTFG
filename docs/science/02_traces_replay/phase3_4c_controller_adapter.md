# Phase 3.4C Controller Adapter Boundary

The Phase 3.4C controller adapter lets the dry-run harness call existing Phase 2 controllers without modifying them.

## Public Contract Used

The adapter uses the existing controller public surface:

- `core.controller.registry.create_controller(...)`;
- controller `setPlayerFeedback(dict)`;
- controller `calcControlAction()`;
- controller `getControlAction()` when a controller returns `None`;
- `core.controller.contract.quantize_rate_to_level(...)`.

Controllers remain frozen evaluation subjects. Phase 3.4C does not change controller implementations, controller names or registry entries.

## Safe Feedback Allowlist

`ExistingControllerAdapter` accepts the current required feedback keys from `core.controller.contract.REQUIRED_FEEDBACK_KEYS`, plus a tiny compatibility allowlist for non-trace client context.

The dry-run harness currently sends the required public feedback keys only. This keeps the adapter aligned with Phase 2 controller tests and avoids leaking trace-specific context.

## Explicitly Forbidden Inputs

The adapter rejects feedback containing future-looking or non-client fields such as:

- complete trace objects;
- loaded traces;
- sample arrays;
- future samples;
- future throughput;
- raw trace metadata;
- split/domain/OOD labels;
- leakage groups.

This is the Phase 3.4C anti-leakage boundary: the replay environment may hold a full `LoadedTrace`, but controllers only see measurements that would have been observed by that point.

## Output Normalization

Existing controllers usually return a target rate in bytes per second. The adapter quantizes that target rate to a representation index using the current ladder.

For compatibility with debug/future test doubles, mapping outputs may also include:

- `representation_index`;
- `quality_index`;
- `level`;
- `target_rate_Bps`;
- `target_rate`;
- `rate`;
- `bitrate`.

Index decisions outside the ladder are clamped by default and can be rejected with `invalid_decision_policy = "reject"`. Clamping is documented in the returned `ControllerDecision.reason`.

## Non-Benchmark Status

Adapter decisions are dry-run decisions, not benchmark results. They are not final QoE inputs, not controller rankings and not evidence that one controller outperforms another.
