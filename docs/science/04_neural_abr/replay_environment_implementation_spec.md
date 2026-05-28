# Replay environment implementation spec

## Replay state

The offline replay state must track:

```text
trace_id
segment_index
wall_time_s
buffer_s
last_representation_index
last_bitrate_bps
last_download_time_s
last_fragment_size_bytes
throughput_history_bps[K_CONTEXT]
download_time_history_s[K_CONTEXT]
recent_rebuffer_s
recent_switch_abs
chunks_remaining
```

## Buffer update

For a selected representation at a segment:

```text
download_time_s = network_model.download(size_bytes, wall_time_s).duration_s
rebuffer_s = max(download_time_s - buffer_s, 0)
buffer_s = max(buffer_s - download_time_s, 0) + segment_duration_s
buffer_s = min(buffer_s, max_buffer_s)
wall_time_s += download_time_s
```

## Reward computation

For Phase 4D training samples, reward metadata must use the Phase 3.5 QoE definition:

```text
qoe_linear_v1 / reward_n basis
quality utility = bitrate_kbps / 1000
rebuffer penalty = 4.3 * rebuffer_s
smoothness penalty = 1.0 * abs(current_quality - previous_quality)
```

This reward is metadata for teacher replay/sample validation. It must not be used to claim final benchmark superiority.
