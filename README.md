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
Phase 6A0 - Validation documentation scaffold and evidence consolidation
```

Phase 6A0 is open as documentation/protocol intake only. No benchmark, ranking, plots, results table, winner declaration, retraining, or QoE improvement claim is allowed yet.

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

No datasets, models, run outputs, logs, PDFs, CSVs, JSONL files, archives, videos, segments, or media files belong in this repository.

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

Recommended local validation during Phase 6A0 documentation work:

```powershell
python -m unittest discover
python scripts\check_client_readiness.py --strict
python -m py_compile scripts\audit_phase6_trace_eligibility.py
Get-ChildItem core,scripts,tests -Recurse -Filter *.py | ForEach-Object { python -m py_compile $_.FullName }
```

The Phase 6 trace eligibility guardrail can be run with external manifests:

```powershell
python scripts\audit_phase6_trace_eligibility.py `
  --phase4-dataset-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate_20260529_080755\dataset_manifest.json `
  --phase6-candidate-manifest C:\path\to\phase6_candidate_manifest.json `
  --output C:\Users\danie\Documents\TFG\_audits\phase6_trace_eligibility.json
```

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
- `docs/science/06_validation`: active Phase 6A0 validation documentation and evidence scaffold.
- `docs/maintenance`: workspace hygiene and pre-validation guardrails.
- `docs/roadmap`: future work.

## Evidence Boundary

Phase 4 teacher agreement and OOD diagnostics are not formal performance evidence because the final Phase 4 dataset contains checksum duplicates across splits. That does not invalidate Phase 5 integration. It does mean Phase 6 must exclude, by checksum, every trace seen by Phase 4 when evaluating `neural_abr_lite` against baselines.
