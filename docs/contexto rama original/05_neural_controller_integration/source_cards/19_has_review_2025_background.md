﻿# Source card 19: HAS review 2025 background

## Title

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges.

## Authors

Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, Hermann Hellwagner.

## Year

2025.

## Venue/type

ACM Transactions on Multimedia Computing, Communications, and Applications; survey/background.

## Phase 5 triage

BACKGROUND_ONLY.

## Why this source matters for integration

The review provides HAS/DASH context: manifests expose multiple representations and clients decide which segments to request.

## Runtime integration pattern

ABR logic belongs at the client decision point. The review is not a neural implementation spec.

## Runtime inputs

Manifest/representation information and client playback state.

## Runtime action/output

Client chooses a representation/segment request.

## Safety/fallback/action mask

The source supports why action validity must be tied to available representations.

## Latency/compute/deployment assumptions

No direct CPU model loading contract.

## What transfers to DashClientModular4

- Explain why controller integration belongs in the client.
- Explain MPD representation context for the TFG memory.

## What must not be copied

- Treating the survey as a direct neural controller spec.

## Phase 5 docs affected

- `README.md`
- `_historical/notes_for_memory.md`
- `phase5b_controller_integration_contract.md`

## Memory/defense usage

Use in the background chapter to place ABR inside HAS/DASH.

## Final decision

Use as background only.
