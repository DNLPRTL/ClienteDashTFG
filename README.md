# DashClientModular4

DashClientModular4 is the client repository for the TFG "ABR con IA para streaming DASH". The client is modular, testable, and prepared for controlled ABR validation work.

## Current Status

Phase 5 is closed at commit `0c1018d` with the final decision:

```text
ACCEPTED_AS_INTEGRATED_GUARDED_CONTROLLER
```

The controller `neural_abr_lite` is integrated as a guarded neural scorer controller:

```text
feedback runtime -> online features -> bundle/schema validation -> train stats normalization -> action mask -> CPU inference -> safety guard -> fallback -> diagnostic telemetry
```

Phase 5 was integration and hardening only. It did not run a benchmark, produce plots, rank controllers, retrain NeuralABR-Lite, or claim that `neural_abr_lite` improves QoE over any baseline.

The active validation documentation state is:

```text
Phase 6D - MPD-derived media profile freeze
```

Phase 6A2 freezes the final experimental protocol. Phase 6B adds manifest validation, structural readiness preflight and `canonical_content_fingerprint` audit hardening. Phase 6C automates source registry loading, public acquisition, safe extraction, normalization, reference/candidate manifest building, validation, eligibility audit and external final manifest freeze. Phase 6C-H1 hardens live materialization with primary-only defaults, live logs, bounded output tails, progress files, timeouts, resume and skip-existing behavior. Phase 6D extracts and freezes `media_profile_phase6_v1` from real MPDs and representation folders outside the repository, including media-profile validation and NeuralABR-Lite ladder/action-count compatibility checks. It still did not run a benchmark and does not authorize ranking, plots from real data, result CSVs, winner declaration, retraining, or QoE improvement claims.

The active validation documentation path is:

```text
docs/science/06_validation/
```

Phase 6P closed at commit `1a753f1` with trace eligibility audit and evidence hygiene. Phase 6P2 closed at commit `d3d45cc` with documentation re-cohesion and external workspace cleanup. Phase 6P2 is documented in `docs/maintenance/phase6p2_workspace_recohesion_report.md`.

## Workspace Layout

The expected TFG root is outside the repository:

```text
C:\Users\danie\Documents\TFG
```

External workspaces live there and must stay out of Git:

```text
_datasets/
_models/
_runs/
_scripts/
_literature/
_audits/
_archive/
```

The current local-only NeuralABR-Lite bundle is:

```text
_models/phase4_AI/neural_abr_lite/phase4F/bundle_20260529_091652
```

The local marker is:

```text
_models/phase4_AI/neural_abr_lite/phase4F/CURRENT_BUNDLE.txt
```

No datasets, models, run outputs, logs, PDFs, CSVs, JSONL files, archives, videos, segments, media files, real MPDs, Phase 6C normalized traces, Phase 6D media-profile outputs, receipts or external manifests belong in this repository.

## Run Path

The supported client path remains config-driven and non-interactive:

```powershell
Copy-Item config\client.example.yaml config\client.local.yaml
# Edit config\client.local.yaml and set mpd_url.
python main.py --config config\client.local.yaml
```

Manual demo prompts are still available with:

```powershell
python main.py --interactive
```

See `docs/runbooks/run_client.md` and `docs/runbooks/run_layout.md` for usage and run artifact layout.

## Validation Commands

Recommended local validation during Phase 6C/6D automation/protocol work:

```powershell
python -m unittest discover
python scripts\check_client_readiness.py --strict
python scripts\check_phase6_evaluation_readiness.py --strict
python -m py_compile scripts\audit_phase6_trace_eligibility.py scripts\validate_phase6_trace_manifest.py scripts\check_phase6_evaluation_readiness.py scripts\run_phase6c_trace_materialization.py scripts\extract_phase6_media_profile_from_mpd.py scripts\validate_phase6_media_profile.py scripts\check_phase6_media_profile_compatibility.py scripts\freeze_phase6_media_profile.py scripts\run_phase6d_media_profile_freeze.py
Get-ChildItem core,scripts,tests -Recurse -Filter *.py | ForEach-Object { python -m py_compile $_.FullName }
```

The Phase 6C materialization path is automated. The user should not manually create source config JSON files or manifests:

```powershell
python -u scripts\run_phase6c_trace_materialization.py ^
  --external-root C:\Users\danie\Documents\TFG\_datasets\phase6_validation ^
  --phase4-dataset-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate_20260529_080755\dataset_manifest.json ^
  --sources primary ^
  --download ^
  --extract ^
  --normalize ^
  --build-reference ^
  --build-candidate ^
  --validate ^
  --audit ^
  --freeze ^
  --strict ^
  --resume ^
  --skip-existing ^
  --clean-derived ^
  --progress-every 10
```

The Phase 6D media-profile freeze path is also automated and writes only to the external root:

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

The server/VM is a source for MPD/content/media_profile data and demo/integration support. It is not the benchmark network; future benchmark network conditions remain normalized traces through `TraceDrivenNetworkModel`.

The Phase 6 trace eligibility guardrail can be run with external manifests:

```powershell
python scripts\audit_phase6_trace_eligibility.py `
  --phase4-dataset-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate_20260529_080755\dataset_manifest.json `
  --phase6-candidate-manifest C:\path\to\phase6_candidate_manifest.json `
  --output C:\Users\danie\Documents\TFG\_audits\phase6_trace_eligibility.json
```

The Phase 6B structural preflight can be run without manifests:

```powershell
python scripts\check_phase6_evaluation_readiness.py --strict
```

Without manifests it reports `manifest_audit_not_run`. With manifests, it validates the Phase 6 candidate schema and audits Phase 4 overlap by `trace_id`, `leakage_group`, `checksum_sha256` and `canonical_content_fingerprint`. In Phase 6C, `ready_for_benchmark=false` and `benchmark_authorized=false` always remain in force.

## Main Repository Structure

- `core/controller`: controller interface, registry, baselines, and NeuralABR-Lite controller integration.
- `core/parser`: MPD parsing.
- `core/media_engine`: fake and GStreamer playback engines.
- `core/downloader.py`: segment downloader.
- `core/runtime_feedback.py`: controller feedback payload helper used by `Player`.
- `core/dataset_schema.py`: telemetry and evaluation segment CSV schema helpers.
- `scripts`: checked-in validation, conversion, training, export, and audit utilities.
- `tests`: unit and smoke tests.
- `docs/architecture`: client contracts and implementation architecture.
- `docs/runbooks`: operator and environment runbooks.
- `docs/science`: phase-indexed scientific documentation.
- `configs/phase6`: committed Phase 6C source registry and Phase 6D media-profile policy metadata only.
- `docs/science/06_validation`: active Phase 6 validation protocol plus Phase 6C automation and Phase 6D media-profile freeze contracts.
- `docs/maintenance`: workspace hygiene and pre-validation guardrails.
- `docs/roadmap`: future work.

## Evidence Boundary

Phase 4 teacher agreement and OOD diagnostics are not formal performance evidence because the final Phase 4 dataset contains identity leakage risk across splits. That does not invalidate Phase 5 integration. It does mean Phase 6 must exclude every trace seen by Phase 4 by `trace_id`, `leakage_group`, `checksum_sha256` and `canonical_content_fingerprint` when evaluating `neural_abr_lite` against baselines.

Final Phase 6 trace IDs are frozen only when the external `phase6_trace_manifest_final.json` exists after Phase 6C acquisition, normalization, validation, eligibility audit and freeze. The shared media profile is frozen only when the external `media_profile_phase6_v1.json` exists after Phase 6D MPD extraction, validation, compatibility check and freeze. Both artifacts still keep `ready_for_benchmark=false` and `benchmark_authorized=false`.
