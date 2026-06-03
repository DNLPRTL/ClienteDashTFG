# Source card 10: Into the Wild real-world testing gap

## Title

Into the Wild: Real-World Testing for ML-Based ABR.

## Authors

Benjamin Hoffman, Alexander Dietmuller, Ayush Mishra, Laurent Vanbever.

## Year

2025.

## Venue/type

PACMI; real-world testing source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

The source warns that ML-based ABR often struggles to bridge simulation and reality, and that testing in one real-world environment may still fail to generalize.

## Runtime integration pattern

Not a controller implementation pattern for Phase 5. It is a validation and claims boundary.

## Runtime inputs

Real-world network environments and testing infrastructure. Phase 5 does not add ABR-Arena.

## Runtime action/output

Not applicable for controller action. The useful output is a warning about claims.

## Safety/fallback/action mask

No direct safety guard transfer, but it reinforces no premature real-world claims.

## Latency/compute/deployment assumptions

Broader real-world testing is deferred to future validation work.

## What transfers to DashClientModular4

- Phase 5 smoke is not a benchmark.
- No real-world claim.
- Phase 6 must be careful and explicit.

## What must not be copied

- ABR-Arena platform.

## Phase 5 docs affected

- `phase5b_no_benchmark_policy.md`
- `_historical/notes_for_memory.md`
- `_historical/phase5_remaining_roadmap.md`

## Memory/defense usage

Use this source to defend the TFG limitation that local validation is not real-world proof.

## Final decision

Transfer the real-world testing caution. Defer ABR-Arena-style validation.


