# Phase 6 Media Profile Decision

Status: final Phase 6A2 protocol decision extended by Phase 6D MPD-derived freeze tooling. No media assets are added to Git.

## Frozen Policy

The primary Phase 6 media profile is:

```text
media_profile_phase6_v1
```

It must be deterministic and shared by all controllers.

Phase 6D resolves this profile from a real MPEG-DASH MPD when the external freeze is run. The user already has real MPDs and representation folders on the Ubuntu server; that server is a media-profile/content source and demo/integration surface, not the benchmark network.

## Required Constraints

- `segment_duration_s = 2.0` only remains a fallback if no real extracted MPD profile is frozen before execution planning.
- The representation ladder must be identical for all controllers.
- Segment count and expected segment duration must be identical for all controllers within a trace/session comparison.
- Any real MPD/segment-size profile may be used only if extracted, documented, checksummed and frozen before execution.
- The VM server may provide content/demo/media_profile support, but VM bridge networking is not the benchmark path.
- Future benchmark network conditions remain Python trace-driven through normalized traces and `TraceDrivenNetworkModel`.

## Phase 6D MPD-Derived Profile

The current MPD-derived profile candidate has:

- `mpd_duration_s = 60.0`;
- `segment_duration_s = 4.0`;
- `segment_count = 15`;
- canonical bitrate ladder `300/750/1200/1850/2850/4300` kbps.

The MPD ids are preserved, but controller-facing `representation_index` is sorted by ascending bitrate:

| representation_index | MPD id | bitrate_kbps |
| --- | --- | ---: |
| 0 | 6 | 300 |
| 1 | 5 | 750 |
| 2 | 4 | 1200 |
| 3 | 3 | 1850 |
| 4 | 2 | 2850 |
| 5 | 1 | 4300 |

Real segment sizes are preferred from `--content-root` or `--base-url`. If they are unavailable, the profile records deterministic bitrate-estimated sizes and labels their source.

## NeuralABR-Lite Compatibility

The Phase 6D compatibility report checks NeuralABR-Lite bundle metadata when a bundle path is provided. It inspects JSON files such as `bundle_manifest.json`, `ladder_schema.json` and `inference_contract.json` without running inference or importing torch.

If the bundle supports 6 candidates, the full MPD ladder can be primary. If it supports only 5 candidates, the primary profile must use the shared MPD-derived subset `300/750/1200/1850/2850` kbps. The full 6-representation profile may be retained as diagnostic only.

## Representation Ladder Rule

The future resolved media profile must expose:

- representation index;
- bitrate in bps/kbps;
- segment duration;
- expected segment count;
- segment-size model or extracted segment sizes;
- checksum/fingerprint of the frozen profile file.

## VMAF Boundary

VMAF remains deferred and artifact-dependent. No Phase 6 result may claim perceptual quality, VMAF or MOS unless a later metric decision freezes the required artifacts and computation path.

## Non-Authorization

This document does not create MPDs, segments, media files, plots, benchmark outputs or result tables.
