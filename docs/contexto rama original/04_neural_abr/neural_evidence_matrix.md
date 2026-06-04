# Neural ABR evidence matrix

Phase: Phase 4A1 — source cards + evidence matrix
Status: final A1 matrix after Package 1 + Package 2 + Package 3
Marker: NEURALABR_LITE_HYPOTHESIS

Scoring:

- `0`: no evidence / not applicable.
- `1`: weak.
- `2`: medium.
- `3`: strong.
- `BLOCK`: blocks direct implementation as Phase 4 base.
- `DIAG`: useful as diagnostic/future-work evidence.

| source_id | method_family | state/action/reward clarity | sample efficiency | CPU-first feasibility | data requirements | leakage/future-info risk | OOD/generalization evidence | real-world evidence | DashClientModular4 fit | implementation complexity | defense strength | decision impact |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| pensieve2017_neural_abr | RL/A3C | 3 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | BLOCK | 3 | Seminal formulation only; do not clone |
| oboe2018_autotuning_abr | auto-tuning / regime adaptation | 2 | 3 | 3 | 2 | 1 | 3 | 2 | 3 | 2 | 3 | Justifies regime-aware split/tuning |
| puffer_fugu2020_learning_in_situ | predictor + MPC / real-world RCT | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | Strong caution against simulator-only claims |
| causalsim2023_unbiased_trace_simulation | causal trace simulation | 2 | 1 | 1 | 3 | BLOCK | 3 | 3 | 3 | BLOCK | 3 | Blocks dry-runs legacy as training data |
| comyco2020_lifelong_imitation_learning | imitation learning | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | Main support for behavior cloning/IL |
| a2br2022_meta_rl | meta-RL | 3 | 1 | 1 | 3 | 2 | 3 | 2 | 2 | BLOCK | 2 | Generalization source; not base |
| merina2022_meta_rl_generalization | latent/meta-RL | 3 | 1 | 1 | 3 | 2 | 3 | 1 | 2 | BLOCK | 2 | Supports context/OOD; not base |
| plume_gelato2024_trace_skew | DRL + trace balancing | 3 | 1 | 1 | 3 | 2 | 3 | 3 | 2 | BLOCK | 3 | Trace balancing mandatory; no Gelato clone |
| metaabr2024_meta_learning | meta-RL | 3 | 1 | 1 | 3 | 2 | 3 | 2 | 2 | BLOCK | 2 | Generalization evidence; not base |
| ahaggar2024_bitrate_guidance | server-side guidance/meta-RL | 2 | 2 | 1 | 3 | 2 | 3 | 2 | 1 | BLOCK | 2 | Inspires guidance/fallback, not client base |
| abrl_facebook2020_real_world_rl | real-world RL / candidate scoring | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 3 | Strong support for candidate-scoring output |
| into_the_wild2025_real_world_testing | real-world testing critique | 1 | 0 | 3 | 3 | 2 | 3 | 3 | 2 | 1 | 3 | Blocks real-world claims from local traces |
| soda2024_smoothness_controller | non-IA deployable ABR | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 2 | 2 | 3 | Strong non-IA comparator and smoothness lesson |
| survey_learning_has2025 | survey learning-based HAS | 1 | 0 | 3 | 0 | 1 | 2 | 1 | 2 | 0 | 3 | Taxonomy/memory |
| survey_pipeline2025 | survey/tutorial pipeline | 1 | 0 | 3 | 0 | 1 | 2 | 1 | 2 | 0 | 3 | Pipeline/memory |
| http_adaptive_streaming_review2025 | HAS review | 1 | 0 | 3 | 0 | 1 | 2 | 1 | 2 | 0 | 3 | DASH/HAS/QoE context |
| sabr2025_bc_rl_finetuning | BC + PPO fine-tuning | 3 | 3 for BC / 2 for PPO | 3 for BC / 2 for PPO | 2 | 2 | 3 | 1 | 3 | 2 | 3 | Supports BC base; PPO only optional extension |
| fortuna2025_offline_meta_rl | offline RL + meta-RL | 3 | 2 | 1 | 3 | 3 | 3 | 2 | 2 | BLOCK | 2 | Frontier; too complex for base |
| eastream2026_environment_aware | VAE + meta-RL | 3 | 2 | 2 inference / 1 training | 3 | 2 | 3 | 1 | 2 | BLOCK | 2 | Supports environment context; not base |
| nmoeabr2026_mixture_of_experts | MoE + preference-aware meta-RL | 2 | 1 | 1 | 3 | 2 | 3 | 2 | 1 | BLOCK | 2 | Frontier/future work only |
| ant2024_network_dynamics | network condition detection + multi-model RL | 2 | 2 | 2 detector / 1 full | 3 | 2 | 3 | 2 | 2 | 3 | 3 | Supports trace-regime clustering, not multi-model DRL |
| beta2025_spatial_temporal_generalization | spatial-temporal DRL | 3 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | BLOCK | 3 | Supports k-history state and difficult-trace diagnostics |
| airl2025_inverse_rl | adversarial inverse RL | 3 | 1 | 1 | 3 | 3 | 2 | 1 | 2 | BLOCK | 2 | Supports demonstrations/action masks; blocks reward learning base |
| ababR_search_note | not full PDF | 0 | 0 | 0 | 0 | DIAG | 0 | 0 | 0 | 0 | 0 | Surveillance only |
| ppo_abr_search_note | not full PDF | 0 | 0 | 0 | 0 | DIAG | 0 | 0 | 0 | 0 | 0 | PPO not chosen by inertia |

## Matrix conclusion

The evidence supports the following Phase 4A2 hypothesis:

```text
NeuralABR-Lite Candidate Scorer
  = small CPU-first candidate-scoring neural ABR
  + behavior cloning / imitation learning
  + teacher MPC / robustMPC / oracle-limited labels
  + trace-regime balancing
  + action mask over valid MPD representations
  + fallback to a classical controller
```

The evidence does not support as base:

```text
PPO/A3C from scratch,
full meta-RL,
full offline RL,
MoE/NMoE,
AIRL reward learning,
transformer/LLM ABR,
real-world/SOTA claims.
```
