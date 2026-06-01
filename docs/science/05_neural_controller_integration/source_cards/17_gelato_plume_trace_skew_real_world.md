# Source card 17: Gelato/Plume trace skew and real-world caution

## Title

Practically High Performant Neural Adaptive Video Streaming.

## Authors

Sagar Patel, Junyang Zhang, Nina Narodystka, Sangeetha Abdu Jyothi.

## Year

2024.

## Venue/type

Proceedings of the ACM on Networking / CoNEXT; research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

Gelato/Plume emphasizes skewed trace distributions, confidence intervals and real-world testing.

## Runtime integration pattern

The source addresses DRL training and validation under trace skew. Phase 5 does not retrain from it.

## Runtime inputs

Trace distributions and deployment/evaluation data. Phase 5 does not treat local telemetry as a training corpus.

## Runtime action/output

ABR policy/evaluation output in the original work. No direct Phase 5 action transfer.

## Safety/fallback/action mask

No direct fallback pattern. It reinforces no premature generalization claims.

## Latency/compute/deployment assumptions

Real-world validation scale is outside Phase 5.

## What transfers to DashClientModular4

- Training-data skew remains a risk.
- Phase 5 must not claim generalization.
- Phase 6 must define evaluation carefully.

## What must not be copied

- Plume trace prioritization.
- Gelato controller.
- Retraining pipeline.

## Phase 5 docs affected

- `phase5b_no_benchmark_policy.md`
- `notes_for_memory.md`
- `phase5_remaining_roadmap.md`

## Memory/defense usage

Use this source in limitations and threats to validity.

## Final decision

Transfer trace-skew caution. Do not implement Gelato/Plume.
