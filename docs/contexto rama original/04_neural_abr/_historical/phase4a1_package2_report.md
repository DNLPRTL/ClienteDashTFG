# Phase 4A1 Package 2 report — Generalization, deployment and surveys

## Status

Package 2 source cards are completed for:

```text
metaabr2024_meta_learning
ahaggar2024_bitrate_guidance
abrl_facebook2020_real_world_rl
into_the_wild2025_real_world_testing
soda2024_smoothness_controller
survey_learning_has2025
survey_pipeline2025
http_adaptive_streaming_review2025
```

This package extends the Package 1 core decision sources. It does not implement IA, train models or choose the final method.

## Main decision deltas

### 1. Candidate scoring becomes the preferred model output shape

ABRL/Facebook provides the most useful architecture for DashClientModular4: the model scores each valid bitrate/representation using shared weights, then selects among the valid candidates. This avoids a brittle fixed output head and maps naturally to MPD ladders.

### 2. Guidance/fallback becomes a first-class design pattern

Ahaggar shows that learning can provide guidance while a lightweight client remains responsible for local adaptation. In this TFG, the local equivalent is:

```text
neural scorer/advisor
+ action mask
+ classical fallback
+ safety caps
```

### 3. Smoothness is now a hard evaluation and safety requirement

SODA shows that a strong non-ML ABR can optimize video quality, rebuffering and switching with theoretical and production evidence. NeuralABR-Lite must not optimize average reward while causing avoidable switching.

### 4. Real-world claims are blocked

Into the Wild shows that even real-world platforms can have regional bias and survivorship bias. The thesis must say "trace-driven controlled validation", not "general Internet deployment proof".

### 5. Surveys are for framing, not method authority

The 2025 surveys and HAS review are excellent for the memory, taxonomy and pipeline diagrams. They do not replace primary method papers for A2 method selection.

## Current method hypothesis

```text
NeuralABR-Lite Candidate Scorer

Input:
  context features observable online
  + candidate representation features

Output:
  score per valid representation
  or conservative guidance such as max_allowed_representation

Training:
  behavior cloning / imitation learning from teacher decisions
  train traces only
  regime-balanced sampling

Safety:
  action mask
  no future info in features
  fallback to robust_mpc/MPC/BBA-like controller
  smoothness sanity checks

Hardware:
  CPU-first
  PyTorch CPU
  no CUDA/ROCm/Ray/TensorFlow legacy as requirement
```

## Not yet allowed

- No implementation.
- No Codex.
- No training.
- No dataset generation.
- No dry-runs legacy as training data.
- No controller/player/runtime/media changes.
- No benchmark/ranking.
- No final method decision until Package 3 and final evidence matrix.
