# Phase 5B action mask contract

## Purpose

The action mask prevents NeuralABR-Lite from selecting a representation that is not valid for the current MPD/client ladder and segment.

## Mask construction

- Mask length equals the number of current candidates in `rates`.
- Valid candidates are current MPD representations available for the segment.
- Each valid candidate is `true`.
- Invalid or unavailable candidates are `false`.
- The mask must contain at least one `true`.

## Selection rule

The mask is applied before argmax:

```text
valid_scores = scores where action_mask[index] is true
raw_action = argmax(valid_scores)
```

The selected index must be validated after selection:

- index is within ladder bounds;
- mask at index is true;
- mapped rate exists in `feedback["rates"]`;
- score is finite.

## Failure behavior

- All-false mask -> fallback.
- Invalid mask shape -> fallback.
- Selected action masked out -> fallback and telemetry.
- Invalid selected index -> fallback and telemetry.

## Benchmark boundary

Mask validity is an integration correctness requirement. It is diagnostic-only and not benchmark evidence.
