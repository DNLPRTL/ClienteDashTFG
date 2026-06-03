# Source card 11: Comyco lifelong imitation learning

## Title

Quality-aware Neural Adaptive Video Streaming with Lifelong Imitation Learning.

## Authors

Tianchi Huang, Chao Zhou, Xin Yao, Rui-Xiao Zhang, Chenglei Wu, Bing Yu, Lifeng Sun.

## Year

2020.

## Venue/type

IEEE Journal on Selected Areas in Communications / Comyco research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

Comyco supports imitation learning from expert trajectories, which is consistent with the Phase 4 behavior cloning decision.

## Runtime integration pattern

The source includes inner-loop and outer-loop systems. The inner-loop can be deployed without continuous updates if lifelong learning is not needed.

## Runtime inputs

Client playback features and expert-derived behavior. Phase 5 uses only online-observable features.

## Runtime action/output

The model outputs ABR decisions based on learned expert behavior.

## Safety/fallback/action mask

The source supports behavior cloning as a foundation but does not remove the need for fallback or masks in DashClientModular4.

## Latency/compute/deployment assumptions

Server-side update loops and model servers are not adopted. Phase 5 stays local-only.

## What transfers to DashClientModular4

- Phase 4 behavior cloning remains defensible.
- No online training is needed in Phase 5.
- Model update loops are future work.

## What must not be copied

- VMAF-specific quality-aware model.
- Lifelong update loop.
- Model server download path.

## Phase 5 docs affected

- `phase5a2_rejected_alternatives.md`
- `phase5b_artifact_policy.md`
- `_historical/notes_for_memory.md`

## Memory/defense usage

Use this source to connect the Phase 4 imitation learning choice to a known neural ABR family.

## Final decision

Transfer imitation learning support. Defer lifelong/online training.

