# Decision: NeuralABR-Lite Candidate Scorer

Status: **selected as primary Phase 4 method**

## Selected concept

NeuralABR-Lite will be specified as a candidate-scoring neural ABR method.
For each chunk decision, the model will score each currently valid representation candidate.
The controller will select the highest safe candidate after masking and fallback logic.

## Why candidate scoring is preferable to fixed softmax

A fixed softmax over `N` outputs assumes that all videos have the same number of representations and that each output index always maps to the same bitrate/quality semantics.
That is too brittle for a DASH client.

A candidate scorer can evaluate the actual representation ladder for the current MPD:

```text
score(context, candidate_0)
score(context, candidate_1)
...
score(context, candidate_n)
```

This is more reusable and closer to production ABR reasoning.

## Minimal future model family

The intended model is a small shared MLP:

```text
input = context_features + candidate_features
hidden = small MLP
output = scalar score
```

The exact hidden sizes, activations and normalization are not decided in A2.
They belong to Phase 4B/4C.

## Future training objective candidates

Phase 4B/4C may choose between:

```text
cross_entropy over candidate scores
pairwise ranking loss
margin ranking loss
hybrid CE + smoothness regularizer, if justified
```

Default for a TFG should be cross-entropy because it is simple and defensible.

## Future teacher label candidates

```text
teacher action = argmax expert QoE decision over candidate representations
```

The expert can be:

```text
MPC
robust_mpc
oracle-limited dynamic planner
consensus of multiple teachers
```

The teacher must be generated only from train traces for training.
Validation and OOD traces must remain unseen by training.

## Success criteria for method selection

The method is selected because it satisfies:

- feasible CPU-first training;
- action validity by construction;
- compatibility with `representation_index`;
- explainability in memory and defense;
- direct relation to the existing ABR/QoE stack;
- clear leakage prevention strategy;
- fallback path if the model fails.

## Non-goals

- It is not expected to be SOTA.
- It is not expected to beat all classical controllers in all conditions.
- It is not a real-world deployment claim.
- It is not an end-to-end neural streaming system.
