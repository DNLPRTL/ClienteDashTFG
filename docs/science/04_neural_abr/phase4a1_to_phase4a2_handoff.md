# Phase 4A1 to Phase 4A2 handoff

## Current flow position

```text
search
  -> PDFs
  -> source_cards
  -> evidence_matrix
  -> method_decision      <-- NEXT
  -> specs
  -> Codex
```

## Inputs available for Phase 4A2

- All three waves of source cards.
- Final evidence matrix.
- Methods crosswalk.
- Method feasibility matrix.
- Risk register.
- Hardware constraints:
  - Windows 11;
  - i5-14600KF;
  - 32 GB RAM;
  - AMD RX 7800 XT 16 GB;
  - Python 3.12.8;
  - PyTorch 2.6.0+cpu;
  - CUDA unavailable;
  - torch_directml not installed;
  - WSL not installed.

## Phase 4A2 deliverables

Planned documents:

- `neural_method_selection.md`
- `method_decision_record.md`
- `neural_abr_design_intent.md`
- `why_not_ppo_first.md`
- `why_not_meta_rl_full.md`
- `why_not_offline_rl_full.md`
- `why_not_reward_learning.md`
- `neural_abr_lite_candidate_scorer_decision.md`
- `phase4a2_method_decision_report.md`

## Decision expected

Unless a validation issue appears, Phase 4A2 should select:

```text
NeuralABR-Lite candidate-scoring imitation-learning controller.
```

With:

```text
Fugu-lite predictor+policy as backup/comparator.
Tiny PPO fine-tune as optional future extension only.
```

## Hard blockers carried into A2

- no implementation;
- no training;
- no Codex implementation prompt;
- no dry-runs legacy as dataset;
- no benchmark/ranking;
- no reward change without versioning.
