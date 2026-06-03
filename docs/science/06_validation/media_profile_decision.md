# Phase 6 Media Profile Decision

Status: final Phase 6A2 protocol decision. No media assets are added to Git.

## Frozen Policy

The primary Phase 6 media profile is:

```text
media_profile_phase6_v1
```

It must be deterministic and shared by all controllers.

## Required Constraints

- `segment_duration_s = 2.0` unless a real extracted MPD profile is frozen before execution.
- The representation ladder must be identical for all controllers.
- Segment count and expected segment duration must be identical for all controllers within a trace/session comparison.
- Any real MPD/segment-size profile may be used only if extracted, documented, checksummed and frozen before execution.
- The VM server may provide content/demo/media_profile support, but VM bridge networking is not the benchmark path.

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
