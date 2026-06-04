# Supervised sample generation contract

## Sample unit

One supervised sample corresponds to one ABR decision point:

```text
sample_id = dataset_id + trace_id + episode_id + segment_index
```

## Required sample fields

```text
sample_id
trace_id
episode_id
segment_index
split
context_features
candidate_features[]
action_mask[]
teacher_representation_index
teacher_name
reward_version
normalization_version
```

## Context features inherited from Phase 4B

```text
throughput_history_bps[5]
download_time_history_s[5]
buffer_s
last_representation_index
last_bitrate_bps
recent_rebuffer_s
recent_switch_abs
chunks_remaining_norm
has_chunks_remaining
```

## Candidate features inherited from Phase 4B

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

## Action mask

Each sample must include an action mask marking valid representation candidates. Invalid actions must never be selected as labels or model outputs.

## Prohibited fields

```text
future throughput not observable at decision time
future reward
future QoE
final QoE
teacher action as input feature
split as input feature
trace_id as input feature
controller name as input feature
benchmark rank
```

## Sample manifest

Generated samples must be accompanied by a manifest that records sample counts per split, trace, regime and teacher.
