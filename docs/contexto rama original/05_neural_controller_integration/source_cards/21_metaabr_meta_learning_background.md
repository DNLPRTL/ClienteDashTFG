﻿# Source card 21: MetaABR meta-learning background

## Title

MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming.

## Authors

Wenzhong Li, Xiang Li, Yeting Xu, Yi Yang, Sanglu Lu.

## Year

2024.

## Venue/type

IEEE Transactions on Mobile Computing; background source.

## Phase 5 triage

BACKGROUND_ONLY.

## Why this source matters for integration

MetaABR discusses real-world deployment challenges for learning-based ABR and shows unseen environments can degrade task-specific DRL.

## Runtime integration pattern

Meta-learning adapts ABR behavior across environments. Phase 5 does not adopt meta-learning.

## Runtime inputs

Observations such as throughput, buffer and chunk sizes in a learned ABR setting.

## Runtime action/output

Next bitrate decision in a meta-learning framework.

## Safety/fallback/action mask

The source supports deployment caution, not a direct Phase 5 fallback implementation.

## Latency/compute/deployment assumptions

Meta-learning complexity is deferred.

## What transfers to DashClientModular4

- No online/meta-learning in Phase 5.
- OOD risk remains a limitation.

## What must not be copied

- Meta-RL framework.
- Meta-learning training loop.

## Phase 5 docs affected

- `phase5a2_rejected_alternatives.md`
- `_historical/notes_for_memory.md`

## Memory/defense usage

Use to explain why Phase 5 integration is intentionally narrower than modern meta-learning work.

## Final decision

Use as background only; defer meta-learning.
