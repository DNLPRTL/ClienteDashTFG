# Source card 20: Learning-based HAS review 2025 background

## Title

A Review of Learning-Based Methods for Adaptive Video Streaming over HTTP.

## Authors

Hala Amer, Mohamed S. Hassan, Mahmoud H. Ismail.

## Year

2025 context.

## Venue/type

IEEE Access author version / accepted publication; survey/background.

## Phase 5 triage

BACKGROUND_ONLY.

## Why this source matters for integration

The review summarizes learning-based ABR methods and practical deployment challenges.

## Runtime integration pattern

It provides background on how HAS/DASH uses MPDs, representations and segment URLs, but it does not define the Phase 5 controller.

## Runtime inputs

MPD representations, client state and learning-based ABR features at a survey level.

## Runtime action/output

ABR selects bitrate level for each segment.

## Safety/fallback/action mask

The survey supports general deployment caution but is not a direct safety contract.

## Latency/compute/deployment assumptions

Deployment gaps and real-world degradation are relevant background.

## What transfers to DashClientModular4

- General learning-based ABR context.
- Practical deployment challenge framing.
- No overclaiming.

## What must not be copied

- Treating the survey as an implementation recipe.

## Phase 5 docs affected

- `notes_for_memory.md`
- `phase5a0_literature_delta_report.md`

## Memory/defense usage

Use in the state-of-the-art chapter and limitations discussion.

## Final decision

Use as background only.
