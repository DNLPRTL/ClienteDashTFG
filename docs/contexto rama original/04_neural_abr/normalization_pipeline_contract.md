# Normalization pipeline contract

## Rule

All normalization statistics must be fitted on train samples only.

## Required stats

At minimum:

```text
throughput_bps_scale
download_time_s_scale
buffer_s_scale
bitrate_bps_scale
chunk_size_bytes_scale
recent_rebuffer_s_scale
recent_switch_abs_scale
```

## Robust scaling preference

For heavy-tailed throughput distributions, robust scaling may be used:

```text
clip at train p01/p99
log1p transform for throughput/chunk size if justified
median/IQR normalization
```

The selected rule must be deterministic and recorded in `normalization_stats.json`.

## No leakage

Validation and OOD data may be transformed with train stats, but must not contribute to stats.

## Manifest fields

```json
{
  "normalization_version": "phase4_norm_v1",
  "fit_split": "train",
  "feature_stats": {},
  "clipping_policy": "...",
  "created_from_dataset_manifest": "..."
}
```
