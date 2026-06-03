# Source card 05: Ahaggar bitrate guidance and hybrid boundary

## Title

Bitrate Adaptation and Guidance With Meta Reinforcement Learning.

## Authors

Abdelhak Bentaleb, May Lim, Mehmet N. Akcay, Ali C. Begen, Roger Zimmermann.

## Year

2024.

## Venue/type

IEEE Transactions on Mobile Computing; research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

Ahaggar supports a hybrid boundary: learning can provide guidance while the client keeps lightweight heuristic ABR behavior.

## Runtime integration pattern

The source uses learning to provide bitrate guidance, with metadata/guidance carried to the client. The client boundary remains lightweight.

## Runtime inputs

Guidance metadata and client playback state. DashClientModular4 Phase 5 does not add CMCD/CMSD signaling.

## Runtime action/output

Bitrate guidance rather than an unconditional final client action.

## Safety/fallback/action mask

The client-side heuristic/fallback remains necessary because learning-based systems can be difficult to deploy on low-resource devices.

## Latency/compute/deployment assumptions

The source highlights low-resource deployment concerns. Phase 5 therefore keeps local CPU inference small and fallback-protected.

## What transfers to DashClientModular4

- Treat NeuralABR-Lite as advisory/scoring.
- Keep classical fallback inside the client.
- Avoid server-side protocol changes in Phase 5.

## What must not be copied

- Server-side CMCD/CMSD implementation.
- Multi-client meta-RL.

## Phase 5 docs affected

- `phase5a2_neural_as_guarded_scorer_decision.md`
- `phase5b_fallback_policy_contract.md`
- `_historical/phase5_remaining_roadmap.md`

## Memory/defense usage

Use this source to explain why the future controller is a bounded scorer instead of an unguarded neural controller.

## Final decision

Transfer the advisory boundary. Defer server guidance and protocol-level metadata.

