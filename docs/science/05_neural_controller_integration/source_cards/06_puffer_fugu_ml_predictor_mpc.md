# Source card 06: Puffer/Fugu ML predictor plus MPC

## Title

Learning in situ: a randomized experiment in video streaming.

## Authors

Francis Y. Yan, Hudson Ayers, Chenzhi Zhu, Sadjad Fouladi, James Hong, Keyi Zhang, Philip Levis, Keith Winstein.

## Year

2020.

## Venue/type

USENIX NSDI; real-world randomized evaluation source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

Puffer/Fugu shows that learned ABR components must be treated with humility. Sophisticated learned/control schemes may fail to beat simple buffer-based control in real settings.

## Runtime integration pattern

Fugu uses a neural predictor for transmission-time distribution, while a classical MPC-style controller makes the final decision.

## Runtime inputs

Candidate chunk size and deployment telemetry. DashClientModular4 should not copy low-level TCP features that are not available.

## Runtime action/output

The learned component predicts transmission time distribution. The classical controller selects the bitrate.

## Safety/fallback/action mask

The transfer is the hybrid boundary: ML is bounded by classical decision logic.

## Latency/compute/deployment assumptions

The original deployment is much larger than this TFG. Phase 5 should only use the caution and boundary, not the infrastructure.

## What transfers to DashClientModular4

- Bound ML with classical logic.
- Keep no-benchmark policy in Phase 5.
- Treat BBA/MPC/RobustMPC as serious fallbacks/baselines.

## What must not be copied

- Server-side Fugu architecture.
- Low-level TCP features.
- Transmission-time predictor.

## Phase 5 docs affected

- `phase5a1_telemetry_contamination_matrix.md`
- `phase5b_no_benchmark_policy.md`
- `phase5b_fallback_policy_contract.md`

## Memory/defense usage

Use this source to defend why local integration smokes are not evidence of superiority.

## Final decision

Transfer the ML-bounded-by-classical-control lesson. Do not implement Fugu.
