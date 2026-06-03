# Phase 4A1 Package 3 report

## Status

Package 3 â€” frontera reciente â€” is completed as repo-ready Markdown.

Generated source cards:

- `sabr2025_bc_rl_finetuning.md`
- `fortuna2025_offline_meta_rl.md`
- `eastream2026_environment_aware.md`
- `nmoeabr2026_mixture_of_experts.md`
- `ant2024_network_dynamics.md`
- `beta2025_spatial_temporal_generalization.md`
- `airl2025_inverse_rl.md`
- `http_adaptive_streaming_review2025.md`
- `ababr_search_note.md`
- `ppo_abr_search_note.md`

Updated final A1 files:

- `../neural_evidence_matrix.md`
- `../neural_methods_crosswalk.md`
- `../method_feasibility_matrix.md`
- `../risk_register.md`
- `../_historical/phase4a1_closure_report.md`
- `../_handoffs/phase4a1_to_phase4a2_handoff.md`
- `../_handoffs/package3_next_steps.md`

## Package 3 scientific conclusion

The frontier papers reinforce, rather than overturn, the prior decision path.

SABR supports behavior cloning before PPO and provides recent OOD benchmark evidence. Fortuna, EAStream, NMoEABR, ANT and BETA all demonstrate that generalization is the hard problem, but their full systems are too complex for the Phase 4 base. AIRL reinforces expert-demonstration learning and action masking, but learned reward is not compatible with the already closed Phase 3.5 reward contract.

## A1 final hypothesis

```text
NeuralABR-Lite Candidate Scorer
  = small CPU-first candidate-scoring neural ABR
  + behavior cloning / imitation learning
  + teacher MPC / robustMPC / oracle-limited labels
  + trace-regime balancing
  + action mask over valid MPD representations
  + fallback to a classical controller
```

## Still blocked

- No IA implementation.
- No Codex implementation prompt.
- No training.
- No dataset generation.
- No dry-runs legacy as training data.
- No benchmark/ranking.
- No PPO by inertia.



