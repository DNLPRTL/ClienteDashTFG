# Source card 01: SafeSABR runtime safety auditor

## Title

SafeSABR runtime safety auditor.

## Authors

Not recorded in the provided Phase 5 distillation.

## Year

2025/2026 integration-delta source.

## Venue/type

Research source for safe learned ABR integration.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

SafeSABR gives the clearest Phase 5 pattern for separating a neural `raw_action` from the action actually executed by the client.

## Runtime integration pattern

A learned ABR policy proposes `raw_action`. A runtime safety auditor checks the action before execution.

## Runtime inputs

The auditor uses feasibility evidence such as conservative capacity and ladder ordering. DashClientModular4 should translate this only into online-available buffer and throughput feasibility checks.

## Runtime action/output

The output is `safe_action`, which may equal `raw_action` or a safer lower representation.

## Safety/fallback/action mask

If `raw_action` is unsafe, the auditor searches downward on the ordered bitrate ladder and executes the highest lower feasible action. If no action satisfies the guard, it falls back to the lowest representation.

## Latency/compute/deployment assumptions

The transferable element is a lightweight runtime guard. Starlink-specific predictors and heavy training machinery are not adopted.

## What transfers to DashClientModular4

- Safety guard after neural inference.
- `raw_action` and `safe_action` telemetry.
- `safety_intervened` indicator.
- Lower feasible downshift rule.
- Final fallback if no feasible action exists.

## What must not be copied

- Starlink-specific assumptions.
- CVaR-PPO training.
- BG-CFQS predictor implementation.

## Phase 5 docs affected

- `phase5a1_safety_fallback_matrix.md`
- `phase5a2_neural_as_guarded_scorer_decision.md`
- `phase5b_safety_guard_contract.md`
- `phase5b_telemetry_contract.md`

## Memory/defense usage

Use this source to defend why the neural model is not the final authority. The safety layer is part of responsible integration, not a benchmark trick.

## Final decision

Transfer the runtime safety-auditor pattern only. Do not transfer the training method or domain-specific predictor.
