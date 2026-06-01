# Source card 14: SABR BC pretraining and RL fine-tuning

## Title

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning.

## Authors

Pengcheng Luo, Yunyang Zhao, Bowen Zhang, Genke Yang, Boon-Hee Soong, Chau Yuen.

## Year

2025/2026 frontier source in the uploaded source set.

## Venue/type

Research source; final venue not recorded in the provided distillation.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

SABR supports behavior cloning pretraining as a reasonable foundation and warns about OOD generalization.

## Runtime integration pattern

The source combines BC pretraining with RL fine-tuning. Phase 5 uses only the BC support and OOD caution.

## Runtime inputs

ABR state/features from training and runtime. Phase 5 must restrict inputs to online-available features.

## Runtime action/output

ABR bitrate decision from a learned policy.

## Safety/fallback/action mask

The source does not replace Phase 5 masks and fallback. It reinforces the need for careful stabilization before deployment.

## Latency/compute/deployment assumptions

RL fine-tuning and benchmark datasets are not adopted in this integration block.

## What transfers to DashClientModular4

- Phase 4 behavior cloning foundation remains defensible.
- OOD/generalization risk remains open.
- No RL fine-tuning in Phase 5.

## What must not be copied

- DPO/PPO.
- ABRBench pipeline.
- RL fine-tuning.

## Phase 5 docs affected

- `phase5a2_rejected_alternatives.md`
- `notes_for_memory.md`
- `phase5_remaining_roadmap.md`

## Memory/defense usage

Use this source to explain that Phase 4 chose a smaller BC subset rather than trying to reproduce a full RL pipeline.

## Final decision

Transfer BC and OOD context only. Do not add RL fine-tuning.
