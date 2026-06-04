# Source card 03: A2BR domain priors and fallback

## Title

Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach.

## Authors

Tianchi Huang, Chao Zhou, Rui-Xiao Zhang, Chenglei Wu, Lifeng Sun.

## Year

2022.

## Venue/type

IEEE Journal on Selected Areas in Communications; research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

A2BR supports the idea that domain knowledge and heuristic safety rules remain useful around learned ABR systems.

## Runtime integration pattern

The original source combines offline meta-models with online adaptation. Phase 5 uses only the safer principle: classical ABR logic remains a fallback/domain prior.

## Runtime inputs

Network conditions and client playback state. DashClientModular4 should use only feedback available before the next segment request.

## Runtime action/output

The source targets ABR adaptation under heterogeneous network conditions. Phase 5 does not copy its action mechanism.

## Safety/fallback/action mask

Domain priors and heuristics motivate a classical fallback path when neural inference is missing, invalid or unsafe.

## Latency/compute/deployment assumptions

Online meta-adaptation is not adopted because Phase 5 must be a small CPU-first integration.

## What transfers to DashClientModular4

- Treat classical fallback as a safety prior.
- Avoid making the learned scorer the only control path.
- Keep online adaptation out of Phase 5.

## What must not be copied

- MAML.
- Few-shot online learning.
- Virtual player runtime.

## Phase 5 docs affected

- `phase5a1_safety_fallback_matrix.md`
- `phase5a2_rejected_alternatives.md`
- `phase5b_fallback_policy_contract.md`

## Memory/defense usage

Use A2BR to defend the conservative choice to preserve classical control logic around the neural scorer.

## Final decision

Transfer the domain-prior and fallback rationale. Do not implement online adaptation.
