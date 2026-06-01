# Source card 08: BayesMPC uncertainty predictor plus MPC

## Title

BayesMPC.

## Authors

Not recorded in the provided Phase 5 distillation.

## Year

2024/2025 integration-delta source.

## Venue/type

Research source for uncertainty-aware ABR.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

BayesMPC reinforces conservative feasibility checks by feeding lower-confidence predictions into robust MPC.

## Runtime integration pattern

A Bayesian neural network predicts a distribution of future throughput. A lower confidence bound feeds robust MPC.

## Runtime inputs

Throughput history and uncertainty-related features. Phase 5 does not implement a BNN predictor.

## Runtime action/output

The learned module produces a conservative prediction; MPC owns the final action.

## Safety/fallback/action mask

The transferable safety idea is conservative lower-bound reasoning before accepting a risky high representation.

## Latency/compute/deployment assumptions

BNN inference and a new MPC implementation are deferred. The Phase 5 guard must stay simple and CPU-first.

## What transfers to DashClientModular4

- Safety guard may later use conservative throughput estimates if available.
- Unsafe high actions should be rejected when buffer/throughput evidence is insufficient.

## What must not be copied

- BNN predictor.
- New MPC implementation.

## Phase 5 docs affected

- `phase5a1_safety_fallback_matrix.md`
- `phase5b_safety_guard_contract.md`
- `phase5a2_rejected_alternatives.md`

## Memory/defense usage

Use this source to explain the conservative safety-guard philosophy.

## Final decision

Transfer uncertainty-aware caution. Do not implement BayesMPC in Phase 5.
