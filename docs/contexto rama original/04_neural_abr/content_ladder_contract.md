# Content ladder and segment table contract

## Purpose

Define the video/content side of the replay environment.

## Representation ladder

Each replay episode must have a representation ladder:

```text
representation_index
bitrate_bps
optional_width
optional_height
optional_codec
```

The action space is always the set of valid representation indices.

## Segment/chunk table

If available, the environment may use per-segment/per-representation sizes:

```text
segment_index
representation_index
chunk_size_bytes
duration_s
```

If a real segment size table is not available, Phase 4D must use a documented synthetic or derived size policy and mark it clearly.

## Candidate features

Allowed candidate features:

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

## Future leakage boundary

Using `candidate_chunk_size_bytes` is allowed only if that value is available before requesting the segment under the dataset/client assumptions. It must never include realized download time or future QoE.
