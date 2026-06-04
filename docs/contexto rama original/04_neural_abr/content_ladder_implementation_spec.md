# Content ladder implementation spec

## Purpose

The model chooses a representation index. Therefore the offline environment needs a deterministic representation ladder and per-segment sizes.

## Minimal content ladder JSON

```json
{
  "schema_version": "neural_abr_lite_content_ladder_v1",
  "content_id": "synthetic_vod_ladder_v1",
  "segment_duration_s": 2.0,
  "representations": [
    {"representation_index": 0, "bitrate_bps": 300000},
    {"representation_index": 1, "bitrate_bps": 750000},
    {"representation_index": 2, "bitrate_bps": 1200000},
    {"representation_index": 3, "bitrate_bps": 1850000}
  ],
  "segments": [
    {"segment_index": 0, "sizes_bytes": [75000, 187500, 300000, 462500]}
  ]
}
```

## Leakage boundary

The current segment's candidate sizes may be used if they are available as manifest/MPD-derived metadata before the decision. Future throughput is never allowed. Future segment sizes beyond the current decision horizon are not model inputs in Phase 4D.
