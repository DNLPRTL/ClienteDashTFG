# Phase 6D Media Profile Contract

Status: Phase 6D contract. This freezes the media profile input for future evaluation planning; it does not authorize benchmark execution.

## Purpose

Phase 6D materializes `media_profile_phase6_v1` from a real MPEG-DASH MPD. The user already has real MPDs and representation folders on the Ubuntu server, so the Phase 6D source is MPD/content evidence, not a generic synthetic ladder.

The VM/server role is:

- MPD source;
- representation and segment-size source when local files or HTTP-accessible segments are available;
- demo/integration support.

The VM/server is not the benchmark network. Future benchmark network conditions remain Python trace-driven through normalized traces and `TraceDrivenNetworkModel`.

## Frozen Profile Fields

The extracted profile schema is `phase6_media_profile_extracted_v1`. The frozen profile schema is `phase6_media_profile_frozen_v1`.

Every profile must include:

- `media_profile_id`;
- `source_mpd`;
- `mpd_duration_s`;
- `segment_duration_s`;
- `segment_count`;
- `representations`;
- `segments`;
- `segment_template`;
- `size_policy`;
- `checksum_sha256` and, after freeze, `frozen_profile_sha256`;
- `benchmark_authorized=false`;
- `ready_for_benchmark=false`;
- `phase6d_freeze_only=true`;
- `vmaf_available=false`;
- `perceptual_metrics_available=false`.

No real MPDs, `.m4s`, `.mp4`, logs, receipts, result CSVs, plots or media files are committed to Git.

## Provided MPD-Derived Profile

The expected MPD structure for the current source material is:

- `mediaPresentationDuration = PT0H1M0.000S`;
- `SegmentTemplate timescale = 15360`;
- `SegmentTemplate duration = 61440`;
- `startNumber = 1`;
- `segment_duration_s = 4.0`;
- `segment_count = 15`;
- `media = chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s$Number$.m4s`;
- `initialization = chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s.mp4`.

The MPD representation order can be high-to-low, but controller-facing `representation_index` is canonical ascending bitrate:

| representation_index | MPD id | bitrate_kbps | resolution |
| --- | --- | ---: | --- |
| 0 | 6 | 300 | 256x144 |
| 1 | 5 | 750 | 426x240 |
| 2 | 4 | 1200 | 640x360 |
| 3 | 3 | 1850 | 854x480 |
| 4 | 2 | 2850 | 1280x720 |
| 5 | 1 | 4300 | 1920x1080 |

## Segment Size Policy

Real segment sizes are preferred when available:

- `--content-root` with `--size-policy file_size` reads local segment sizes;
- `--base-url` with `--size-policy http_head` reads HTTP `Content-Length`;
- `--prefer-real-segment-sizes` selects file size first, then HTTP HEAD when the corresponding source is provided.

If real sizes are unavailable, the profile records a bitrate estimate:

```text
size_bytes = round((bitrate_kbps * 1000 / 8) * segment_duration_s)
```

The per-segment `size_source_by_representation` records `file_size`, `http_head`, `bitrate_estimate` or `missing_estimated`.

## NeuralABR-Lite Compatibility

`neural_abr_lite` is a guarded neural scorer controller that uses `representation_index`, an action mask and fallback. Phase 6D does not retrain it and does not run inference.

When a bundle path is provided, `scripts/check_phase6_media_profile_compatibility.py` inspects JSON metadata such as:

- `bundle_manifest.json`;
- `ladder_schema.json`;
- `inference_contract.json`.

If metadata supports 6 candidates, the full MPD ladder can be the primary profile. If metadata supports only 5 candidates, the primary profile must use the MPD-derived compatible subset:

```text
300/750/1200/1850/2850 kbps
```

The full 6-representation ladder may be retained only as diagnostic metadata. Controllers must not see different primary ladders in the same future benchmark.

## Phase 6E Inputs

Future Phase 6E planning requires both external inputs:

- Phase 6C `phase6_trace_manifest_final.json`;
- Phase 6D frozen `media_profile_phase6_v1.json`.

Together they still do not authorize benchmark execution. `benchmark_authorized=false` and `ready_for_benchmark=false` remain mandatory until a later explicit phase opens execution.
