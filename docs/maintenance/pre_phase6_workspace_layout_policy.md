# Pre-Phase6 Workspace Layout Policy

The TFG workspace root is expected to be:

```text
C:\Users\danie\Documents\TFG
```

The Git repository is:

```text
C:\Users\danie\Documents\TFG\DashClientModular4
```

## Expected External Workspaces

These directories live beside the repository, not inside it:

```text
_datasets/
_models/
_runs/
_scripts/
_literature/
_audits/
_archive/
```

`_local_configs/` may be recreated locally when needed, but it is not required after Phase 6P cleanup.

## Artifact Boundary

Keep these artifacts outside Git:

- raw datasets and converted datasets;
- model bundles and weights;
- run outputs and smoke outputs;
- logs;
- CSV, JSONL, and generated JSON evaluation outputs;
- PDFs and literature batches;
- archives and zips;
- DASH media, MPDs, segments, and videos;
- local operational scripts not promoted through a spec.

Small checked-in JSON or CSV fixtures may be added in future phases only when they are explicitly scoped as tests and are not generated evaluation artifacts.

## Current Bundle

The current local-only NeuralABR-Lite bundle is:

```text
_models/phase4_AI/neural_abr_lite/phase4F/bundle_20260529_091652
```

The marker file is:

```text
_models/phase4_AI/neural_abr_lite/phase4F/CURRENT_BUNDLE.txt
```

## Git Hygiene

- Use explicit `git add` paths.
- Do not use `git add .`.
- Do not commit external workspaces.
- Do not use local run outputs as Phase 6 results unless Phase 6A0+ explicitly defines the protocol.
- Do not create `docs/science/06_validation/` before Phase 6A0 opens.
