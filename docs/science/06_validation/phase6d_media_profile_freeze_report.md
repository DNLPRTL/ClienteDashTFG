# Phase 6D Media Profile Freeze Report

Status: committed Phase 6D report template and contract summary. The real frozen media-profile JSON belongs outside Git.

## Current State

Phase 6C-H1 is closed. The external primary OOD trace materialization has passed acquisition, normalization, candidate manifest validation, strict validation, eligibility audit and final trace manifest freeze outside the repository.

Phase 6D adds MPD-derived media-profile freeze tooling. It does not report benchmark results.

## Implemented Tooling

Committed tooling:

- `configs/phase6/media_profile_phase6_v1_policy.json`;
- `scripts/extract_phase6_media_profile_from_mpd.py`;
- `scripts/validate_phase6_media_profile.py`;
- `scripts/check_phase6_media_profile_compatibility.py`;
- `scripts/freeze_phase6_media_profile.py`;
- `scripts/run_phase6d_media_profile_freeze.py`.

The orchestrator writes external outputs under:

```text
<external-root>/media_profiles/
<external-root>/reports/
<external-root>/logs/
```

## MPD-Derived Source Material

The expected source MPD has:

- 60 s media duration;
- 4 s SegmentTemplate duration from `61440 / 15360`;
- 15 segments;
- six representations at `300/750/1200/1850/2850/4300` kbps after ascending-bitrate normalization.

`representation_index` is independent of MPD id order. The original MPD id is retained as `mpd_representation_id`.

## Size Evidence

Real segment sizes are preferred when the MPD content is available through:

- a local `--content-root`; or
- HTTP-accessible segments through `--base-url` and `--size-policy http_head`.

When real sizes are not available, the profile uses and records the deterministic bitrate estimate. Estimated sizes are acceptable for a frozen pre-benchmark profile only when documented.

## Compatibility Evidence

The compatibility report checks whether all controllers can share the same primary `representation_index` ladder. For `neural_abr_lite`, JSON bundle metadata is inspected when a bundle path is provided.

If the bundle supports 6 candidates, the full ladder can be primary. If it supports only 5 candidates, the primary profile must be the MPD-derived subset:

```text
300/750/1200/1850/2850 kbps
```

The full 6-representation profile can be retained as diagnostic-only metadata in the frozen external profile.

## External Freeze Preconditions

Before using the frozen media profile for future Phase 6E planning:

- validation report must be `valid=true`;
- compatibility report must have no hard failures;
- frozen profile must include `frozen_profile_sha256`;
- all benchmark flags must remain false;
- real MPDs, media, segments and logs must remain outside Git.

## Non-Results

No benchmark, controller run, QoE computation, result CSV, plot, ranking, winner declaration or NeuralABR-Lite QoE improvement claim is produced by this report.
