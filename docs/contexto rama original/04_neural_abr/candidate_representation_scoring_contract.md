# Candidate representation scoring contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Selected output design

Phase 4A2 selected a candidate scorer rather than a fixed-size policy head.

```text
score_r = f(context_features, candidate_features_r)
action = argmax(score_r over valid representation candidates)
```

## Why candidate scoring

Candidate scoring is selected because it:

- works with different MPD ladders;
- keeps the action tied to real representations;
- avoids predicting arbitrary bitrates;
- supports action masks naturally;
- aligns with real-world ABR designs that score available bitrates rather than assuming a fixed output layer.

## Context/candidate separation

At each decision:

```text
context_features: shared across all candidates
candidate_features_r: representation-specific features
score_r: scalar score for candidate r
```

The same scorer is applied to every representation candidate. This is a small architecture and is compatible with CPU-first inference.

## Candidate mask

```text
action_mask[r] = 1 if representation r is valid for the current MPD and segment
action_mask[r] = 0 otherwise
```

Rules:

- Invalid candidates must never be selected.
- Masking happens before argmax.
- If all candidates are invalid, the neural model is bypassed and fallback is used.

## Tie-breaking

If two or more valid candidates have exactly equal scores, tie-breaking is deterministic:

```text
1. minimize absolute change from last_representation_index;
2. if still tied, choose the lower representation index;
3. if no last representation exists, choose the lowest tied valid representation.
```

This conservative tie-breaker is chosen to reduce avoidable switching and rebuffer risk.

## Confidence is not a benchmark

A score gap may be used later as a diagnostic or fallback trigger, but it must not be used to claim benchmark superiority in Phase 4.

## Base model size constraint

The base scorer must remain small. A future implementation should target an MLP-style scorer with limited hidden units and no dependency on GPU-only training. Exact architecture is deferred to Phase 4C/4D specs.
