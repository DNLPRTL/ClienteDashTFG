# Phase 6D MPD Extraction Runbook

Status: operational Phase 6D runbook. Use it to freeze `media_profile_phase6_v1` outside the repository.

## Boundary

Phase 6D uses real MPDs and representation folders as media-profile source material. It does not run the client, controllers, trace replay, QoE computation, plots, rankings or result generation.

The server/VM provides MPD and content information only. Future benchmark network conditions remain normalized trace replay through `TraceDrivenNetworkModel`.

## One-Command Freeze

Example Windows command:

```powershell
python -u scripts\run_phase6d_media_profile_freeze.py ^
  --external-root C:\Users\danie\Documents\TFG\_datasets\phase6_validation ^
  --mpd C:\path\to\content\Paseo_Almunecar.mpd ^
  --content-root C:\path\to\content ^
  --prefer-real-segment-sizes ^
  --size-policy file_size ^
  --neural-bundle-root C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652 ^
  --strict
```

Example HTTP-backed command:

```powershell
python -u scripts\run_phase6d_media_profile_freeze.py ^
  --external-root C:\Users\danie\Documents\TFG\_datasets\phase6_validation ^
  --mpd http://server.example/content/Paseo_Almunecar.mpd ^
  --base-url http://server.example/content/ ^
  --prefer-real-segment-sizes ^
  --size-policy http_head ^
  --strict
```

If the neural bundle path is omitted, the compatibility step warns `bundle_not_checked` and still keeps `benchmark_authorized=false`.

## Expected External Outputs

The orchestrator creates:

```text
<external-root>/media_profiles/media_profile_phase6_v1_extracted.json
<external-root>/media_profiles/media_profile_phase6_v1.json
<external-root>/reports/phase6d_media_profile_validation.json
<external-root>/reports/phase6d_media_profile_compatibility.json
<external-root>/reports/phase6d_media_profile_freeze_summary.json
<external-root>/reports/phase6d_media_profile_freeze_summary.md
<external-root>/reports/commands_used.ps1
<external-root>/reports/commands_used.sh
<external-root>/logs/phase6d_media_profile_freeze.log
```

No external output is committed to Git.

## Individual Commands

Extract:

```powershell
python scripts\extract_phase6_media_profile_from_mpd.py ^
  --mpd <path-or-url> ^
  --output <external-root>\media_profiles\media_profile_phase6_v1_extracted.json ^
  --content-root <local-content-dir> ^
  --prefer-real-segment-sizes ^
  --size-policy file_size ^
  --profile-id media_profile_phase6_v1 ^
  --strict
```

Validate:

```powershell
python scripts\validate_phase6_media_profile.py ^
  --profile <external-root>\media_profiles\media_profile_phase6_v1_extracted.json ^
  --output <external-root>\reports\phase6d_media_profile_validation.json ^
  --strict ^
  --fail-on-error
```

Check compatibility:

```powershell
python scripts\check_phase6_media_profile_compatibility.py ^
  --media-profile <external-root>\media_profiles\media_profile_phase6_v1_extracted.json ^
  --neural-bundle-root <bundle-root> ^
  --output <external-root>\reports\phase6d_media_profile_compatibility.json ^
  --strict
```

Freeze:

```powershell
python scripts\freeze_phase6_media_profile.py ^
  --extracted-profile <external-root>\media_profiles\media_profile_phase6_v1_extracted.json ^
  --validation-report <external-root>\reports\phase6d_media_profile_validation.json ^
  --compatibility-report <external-root>\reports\phase6d_media_profile_compatibility.json ^
  --output <external-root>\media_profiles\media_profile_phase6_v1.json ^
  --strict
```

## Review Checklist

- Confirm `segment_duration_s = 4.0` for the provided MPD.
- Confirm `segment_count = 15` for the 60 s source.
- Confirm the ladder is `300/750/1200/1850/2850/4300` kbps in ascending bitrate order.
- Confirm `mpd_representation_id` preserves the original MPD ids.
- Confirm size sources are `file_size` or `http_head` when real segments are available.
- Confirm estimated sizes are explicitly marked if real sizes are unavailable.
- Confirm compatibility with the NeuralABR-Lite action count or freeze the common compatible subset.
- Confirm `ready_for_benchmark=false` and `benchmark_authorized=false` in every report.
