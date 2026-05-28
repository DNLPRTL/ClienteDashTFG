# Feature builder implementation spec

## Context features

`K_CONTEXT = 5`.

Required context features:

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

## Candidate features

For each representation candidate:

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

## Forbidden feature inputs

The feature builder must reject or ignore any attempt to include:

```text
future throughput
future download time
teacher_action
teacher_reward
qoe_total
split
trace_id
source_dataset as numeric input
regime label as numeric input
benchmark result
controller name as target leakage
```

Trace/regime metadata may be kept in sample metadata for audits, never as model input in Phase 4D.
