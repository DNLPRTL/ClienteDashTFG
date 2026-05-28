# Dataset schema contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This file defines the conceptual schema for future training samples. It is not an implementation file.

## Sample-level fields

Each decision sample must be representable with:

```text
sample_id
trace_id
source_dataset_id
split
regime_label
segment_index
decision_time_s
context_features
candidate_features
action_mask
teacher_action
teacher_id
teacher_reward_n
feature_availability_flags
normalization_version
schema_version
```

## Context feature schema

```text
context_features = {
  throughput_history_bps: array[K_CONTEXT],
  download_time_history_s: array[K_CONTEXT],
  buffer_s: float,
  last_representation_index: int_or_sentinel,
  last_bitrate_bps: float,
  recent_rebuffer_s: float,
  recent_switch_abs: float,
  chunks_remaining_norm: float,
  has_chunks_remaining: bool
}
```

## Candidate feature schema

```text
candidate_features = [
  {
    representation_index: int,
    ladder_position_norm: float,
    bitrate_bps: float,
    bitrate_norm_ladder: float,
    delta_from_last_bitrate_norm: float,
    chunk_size_bytes: float,
    chunk_size_available: bool
  }
]
```

## Action mask schema

```text
action_mask = array[num_candidates] of bool
```

Rules:

- Length equals number of candidate representations in `candidate_features`.
- At least one valid action is required for neural inference.
- If no valid action exists, the sample is invalid for training and fallback is required at runtime.

## Label schema

```text
teacher_action = representation_index
```

Rules:

- Must be valid under the action mask.
- Must belong to the same candidate list.
- Must not be inferred from validation/OOD/test outcomes.

## Versioning

The dataset schema version for this contract is:

```text
neural_abr_dataset_schema_v1
```

A future implementation must refuse to train on unversioned or incompatible datasets.
