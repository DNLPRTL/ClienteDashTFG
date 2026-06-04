# Normalization implementation spec

## Rule

Normalization statistics are fitted on train samples only.

## Output

```json
{
  "schema_version": "neural_abr_lite_normalization_v1",
  "fit_split": "train",
  "feature_stats": {
    "buffer_s": {"mean": 3.2, "std": 1.1, "min": 0.0, "max": 8.0}
  }
}
```

## Gate

The normalizer must fail if validation or OOD samples are included during fit.

## Stability

Features with zero variance must use a safe denominator of 1.0 and must record `std_was_zero: true`.
