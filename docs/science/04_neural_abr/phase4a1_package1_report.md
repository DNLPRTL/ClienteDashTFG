# Phase 4A1 Package 1 report — core-decision source cards

## Status

Package 1 source cards have been filled for the core-decision sources:

- pensieve2017_neural_abr
- oboe2018_autotuning_abr
- puffer_fugu2020_learning_in_situ
- causalsim2023_unbiased_trace_simulation
- comyco2020_lifelong_imitation_learning
- a2br2022_meta_rl
- merina2022_meta_rl_generalization
- plume_gelato2024_trace_skew

The first filled version of `neural_evidence_matrix.md` and `method_feasibility_matrix.md` has been produced.

## Package 1 decision signal

The package strongly favors a small CPU-first design:

```text
NeuralABR-Lite candidate scorer / guidance policy
  trained by imitation learning / behavior cloning
  using expert labels from existing MPC/robustMPC/oracle-limited teacher
  with trace-regime balancing
  with action masking and fallback
```

This remains a hypothesis, not the formal method decision.

## Non-negotiable gates extracted from Package 1

1. No PPO/A3C by inertia.
2. No dry-runs legacy as training data.
3. No future information in model inputs.
4. No real-world/SOTA claims from local trace-driven validation.
5. No full meta-RL/Gelato-scale DRL as CPU-first base implementation.
6. Regime-aware trace split/balancing is mandatory.
7. BBA/MPC/RobustMPC remain serious baselines.

## Next package

Proceed to Package 2 source cards:

- metaabr2024_meta_learning
- ahaggar2024_bitrate_guidance
- abrl_facebook2020_real_world_rl
- into_the_wild2025_real_world_testing
- soda2024_smoothness_controller
- survey_learning_has2025
- survey_pipeline2025
- http_adaptive_streaming_review2025

No implementation is allowed yet.
