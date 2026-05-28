# Model and training implementation spec

## Model family

```text
NeuralABR-Lite Candidate Scorer
```

## Required architecture

A small shared MLP scores each candidate representation:

```text
score_r = MLP(concat(normalized_context, normalized_candidate_features_r))
action = argmax(score_r over valid candidates)
```

The same weights are used for every candidate.

## Phase 4D training scope

Phase 4D may implement a training CLI and may run a tiny synthetic smoke only. It must not perform formal training, benchmark ranking, or claim final QoE results.

## Loss

Primary loss:

```text
cross_entropy(masked_candidate_scores, teacher_action)
```

Invalid candidates must be masked before loss/argmax.

## CPU-first

The default device is CPU. The CLI may accept `--device cpu` only in Phase 4D. Do not require CUDA/ROCm/DirectML/WSL.

## Checkpoint policy

Any checkpoint produced by a smoke run must be outside the repository, under:

```text
C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4D_smoke
```

Checkpoint files are not repo artifacts.
