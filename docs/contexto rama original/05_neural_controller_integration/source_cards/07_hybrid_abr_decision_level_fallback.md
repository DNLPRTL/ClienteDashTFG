# Source card 07: Hybrid ABR decision-level fallback

## Title

Hybrid Adaptive Bitrate for Video Streaming.

## Authors

Not recorded in the provided Phase 5 distillation.

## Year

2024/2025 integration-delta source.

## Venue/type

Research source for decision-level fallback in ABR.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

The source supports explicit fallback from learned decisions to rule-based decisions, including RobustMPC-style fallback.

## Runtime integration pattern

The default policy can be RL-based, but runtime logic falls back to rule-based decisions when those are better or safer.

## Runtime inputs

Runtime state and fallback pattern detection signals. Phase 5 does not copy the detector.

## Runtime action/output

Either the learned ABR action or the fallback rule-based action is executed.

## Safety/fallback/action mask

Fallback types include UP, UP-OVERSHOOT, DOWN, DOWN-OVERSHOOT and REBUFFERING. Phase 5 uses this to justify enumerated fallback reasons.

## Latency/compute/deployment assumptions

The offline mapping and online detector are deferred. Phase 5 only needs explicit fallback reason handling.

## What transfers to DashClientModular4

- Fallback to RobustMPC is scientifically justified.
- Runtime fallback reasons should be enumerated.
- Fallback activation must be visible.

## What must not be copied

- Offline pattern detector implementation.
- Cosine similarity fallback detector.

## Phase 5 docs affected

- `phase5a1_safety_fallback_matrix.md`
- `phase5b_fallback_policy_contract.md`
- `phase5b_error_handling_contract.md`

## Memory/defense usage

Use this source to defend explicit fallback as a designed controller behavior, not an afterthought.

## Final decision

Transfer decision-level fallback rationale and fallback reason enumeration. Do not copy the detector.
