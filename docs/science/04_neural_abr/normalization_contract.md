# Normalization contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

Normalization must be reproducible and must not leak validation/OOD/test information.

## Fit scope

Normalization statistics are fit on:

```text
train split only
```

Forbidden:

```text
fitting normalization on validation
fitting normalization on OOD diagnostic
fitting normalization on future benchmark/test traces
refitting normalization after looking at validation/OOD results
```

## Recommended transforms

### Rates and bitrates

Use robust scaling or log scaling. A valid future implementation may use:

```text
log1p(value) followed by train-only robust scale
```

or local ladder-relative normalization for candidate bitrates:

```text
candidate_bitrate_bps / max_bitrate_in_current_ladder
```

### Buffer and durations

Use clipping plus train-only scale:

```text
clip to documented maximum
scale by train-only maximum or robust percentile
```

### Representation indices

Use ladder-relative normalization:

```text
representation_index / (num_representations - 1)
```

If there is only one representation, define the normalized value as `0.0`.

## Missing values

Missing early history entries must be handled consistently:

```text
left pad numeric values with 0
use availability flags if the implementation exposes them
record padding policy in normalization_manifest.json
```

## Required artifact

A future dataset build must create:

```text
normalization_manifest.json
```

Containing:

```text
normalization_version
fit_split
fit_trace_ids
feature_names
transform_per_feature
clipping_policy
padding_policy
created_at
```

## Phase 4B decision

Normalization is train-only and manifest-backed. Any normalization computed from all traces is invalid.
