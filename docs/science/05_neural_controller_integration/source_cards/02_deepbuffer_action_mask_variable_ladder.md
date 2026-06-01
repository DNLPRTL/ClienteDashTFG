# Source card 02: DeepBuffer action mask and variable ladder

## Title

DeepBuffer action mask and variable ladder support.

## Authors

Not recorded in the provided Phase 5 distillation.

## Year

2025/2026 integration-delta source.

## Venue/type

Research source for learned ABR with variable bitrate ladders.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

DeepBuffer shows that learned ABR must handle ladders that change across content and sessions. Invalid actions must be masked before selection.

## Runtime integration pattern

A neural bitrate selection layer receives an action mask that removes representations not present in the current ladder.

## Runtime inputs

Relevant runtime features include past throughput, past download time, buffer occupancy, last quality/bitrate, video bitrate levels and remaining chunks.

## Runtime action/output

The learned module selects among valid bitrate/quality candidates.

## Safety/fallback/action mask

The action mask is mandatory. If no actions are valid, the neural model must be bypassed and fallback must run.

## Latency/compute/deployment assumptions

Masking must be a cheap runtime operation. The DCPPG training design is not part of Phase 5.

## What transfers to DashClientModular4

- Mask length equals current candidate count.
- Invalid representation indices must never be selected.
- Mask is applied before argmax.
- All-false mask triggers fallback.

## What must not be copied

- Maximum buffer action.
- Dual action space.
- DCPPG training.

## Phase 5 docs affected

- `phase5a1_runtime_feature_availability_matrix.md`
- `phase5a1_safety_fallback_matrix.md`
- `phase5b_action_mask_contract.md`
- `phase5b_acceptance_tests.md`

## Memory/defense usage

Use this source to explain why score-per-candidate plus action mask is safer than a fixed output head.

## Final decision

Transfer action-mask and variable-ladder handling. Do not transfer DeepBuffer's full action space or training setup.
