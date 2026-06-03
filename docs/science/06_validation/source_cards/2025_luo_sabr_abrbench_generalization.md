# Source Card: SABR / ABRBench Generalization

## Identity

- Source ID: `2025_luo_sabr_abrbench_generalization`
- Title: SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning
- Authors: Pengcheng Luo, Yunyang Zhao, Bowen Zhang, Genke Yang, Boon-Hee Soong, Chau Yuen
- Year/status: 2025, arXiv preprint intake
- Intake origins:
  - `wave2_guardrails_secondary/2025_luo_sabr_abrbench_generalization.md`
  - `phase6a0_wave3_4_md/wave3_trace_dataset_sources/2025_luo_sabr_abrbench_generalization_revision.md`
- Phase 6A0 triage: `ACCEPTED_GUARDRAIL_SECONDARY`

## Consolidation Note

Wave 2 and wave 3 include the same logical SABR source, with the wave 3 card recording a different PDF hash for the later upload. Phase 6A0 keeps one canonical card and does not create a second SABR bibliography entry.

## Why It Matters

SABR is relevant because it discusses behavior cloning, RL fine-tuning and explicit train/test/OOD benchmark separation. It is handled cautiously because it is a preprint in the intake.

## Phase 6 Protocol Transfers

- Maintain dedicated OOD separation.
- Do not tune on OOD traces.
- Treat ABRBench as deferred until access, license, format and leakage checks exist.
- Explain NeuralABR-Lite as a modest guarded BC-lite scorer, not SOTA.

## What Does Not Transfer

- No PPO/DPO/RL fine-tuning.
- No ABRBench mixing without dataset cards.
- No SABR baseline unless implemented later under a new spec.
- No claim that SABR results imply `neural_abr_lite` generalization.

## Current Decision

Use as OOD discipline and learned-ABR context only.
