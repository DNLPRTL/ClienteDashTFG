# Pre-Phase6 Cleanup Report

Phase:

```text
Phase 6P - Pre-validation workspace normalization, documentation hygiene and evidence-integrity audit
```

This report records maintenance work only. It is not a benchmark, result report, plot record, ranking, or QoE claim.

## Inventory

The Phase 6P0 inventory was generated outside the repository:

```text
C:\Users\danie\Documents\TFG\_audits\pre_phase6_workspace_audit\pre_phase6_workspace_audit.json
C:\Users\danie\Documents\TFG\_audits\pre_phase6_workspace_audit\pre_phase6_workspace_audit.md
C:\Users\danie\Documents\TFG\_audits\pre_phase6_workspace_audit\pre_phase6_cleanup_plan.draft.json
```

Inventory summary:

- Files: 15,011
- Directories: 860
- Empty directories before cleanup: 102
- Total size: 547.04 MiB
- `_datasets`: 9,048 files, 379,108,802 bytes
- `_models`: 27 files, 912,457 bytes
- `_runs`: 109 files, 1,067,814 bytes
- `_scripts`: 33 files, 143,510 bytes
- Duplicate SHA-256 groups: 564

The inventory includes the Git repository, local virtualenv, and external workspaces. The only dangerous-artifact candidate reported inside the repo was an ignored `.venv` Python `.pth` file, not a tracked model artifact.

## Cleanup Applied

The Phase 6P1 cleanup manifest is outside the repository:

```text
C:\Users\danie\Documents\TFG\_archive\pre_phase6_cleanup_20260603_094913\cleanup_manifest.json
```

Applied actions:

- Archive moves: 4
- Empty external directories removed: 107
- Remaining empty external directories: 0
- Local scripts README created: `_scripts/README_LOCAL_DO_NOT_COMMIT.md`
- Current bundle marker created: `_models/phase4_AI/neural_abr_lite/phase4F/CURRENT_BUNDLE.txt`

Archived paths:

```text
_models/phase4_AI/neural_abr_lite/phase4F/bundle_20260529_080755
_datasets/phase4_AI/neural_abr_lite/phase4E2_expanded_candidate
_datasets/phase4_AI/neural_abr_lite/phase4E2_expanded_candidate_20260529_073732
_datasets/phase4_AI/neural_abr_lite/phase4E1_external_trace_smoke_TEST
```

All non-empty archived paths were moved under:

```text
_archive/pre_phase6_cleanup_20260603_094913/
```

## Bundle Declaration

Current local-only bundle:

```text
_models/phase4_AI/neural_abr_lite/phase4F/bundle_20260529_091652
```

Current model state hash:

```text
657a5fae58a1eda82e7769861b365bf7dc2eda0f6ae0fd97f41b70305fec1770
```

`bundle_20260529_080755` was archived after confirming that the payload matched `bundle_20260529_091652`; only `bundle_manifest.json` and `export_log.json` differed.

## Preserved Provenance

Final Phase 4 dataset provenance remains outside Git:

```text
_datasets/phase4_AI/neural_abr_lite/phase4E2_expanded_candidate_20260529_080755
```

No raw datasets, model artifacts, runs, PDFs, CSVs, JSONL files, logs, zips, media files, or external scripts were moved into the repository.

## Non-Goals Respected

- No benchmark was executed.
- No plots were generated.
- No ranking was created.
- No controller winner was declared.
- No QoE improvement claim was made.
- No NeuralABR-Lite retraining was performed.
- No runtime code was changed.

## Phase 6P2 Follow-up

The later workspace re-cohesion and strong cleanup pass is recorded in:

```text
docs/maintenance/phase6p2_workspace_recohesion_report.md
```

That follow-up keeps this Phase 6P1 report as provenance and records its own external audit and cleanup manifests.
