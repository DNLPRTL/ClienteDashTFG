# Source card 13: SODA deployable smoothness controller

## Title

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming.

## Authors

Tianyu Chen, Yiheng Lin, Nicolas Christianson, Zahaib Akhtar, Sharath Dharmaji, Mohammad Hajiesmaili, Adam Wierman, Ramesh K. Sitaraman.

## Year

2024.

## Venue/type

ACM SIGCOMM; deployable ABR controller research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

SODA emphasizes production deployment across low-end devices and avoids expensive prediction machinery.

## Runtime integration pattern

SODA is a controller design focused on smoothness and robust decisions under prediction error.

## Runtime inputs

Playback and throughput-related signals. Phase 5 does not copy the SODA solver.

## Runtime action/output

ABR decision from a dedicated controller, not a candidate scorer.

## Safety/fallback/action mask

No direct action-mask pattern. It supports keeping runtime complexity low and robust to prediction error.

## Latency/compute/deployment assumptions

SODA reduces runtime complexity and avoids sophisticated expensive throughput predictors. Phase 5 transfers the low-compute expectation.

## What transfers to DashClientModular4

- Strict CPU latency and low complexity.
- No heavy predictor.
- No expensive planning inside the neural scorer wrapper.

## What must not be copied

- SODA controller implementation.
- SOCO solver.

## Phase 5 docs affected

- `phase5b_cpu_inference_contract.md`
- `phase5a2_rejected_alternatives.md`
- `_historical/notes_for_memory.md`

## Memory/defense usage

Use this source to defend CPU-first design and the rejection of heavy planning in Phase 5.

## Final decision

Transfer deployability constraints. Do not implement SODA.

