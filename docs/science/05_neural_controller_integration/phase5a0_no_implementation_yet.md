# Phase 5A0 no implementation yet

Phase 5A0, Phase 5A1, Phase 5A2 and Phase 5B are documentation-only in this block.

## Prohibited actions

The following actions are explicitly prohibited:

- no controller code;
- no changes to `core/controller/neural_abr_lite.py`;
- no changes to `core/controller/registry.py`;
- no changes to `player.py`;
- no changes to `main.py`;
- no runtime code;
- no media engine code;
- no `config/client.example.yaml` neural activation;
- no benchmark;
- no ranking;
- no retraining;
- no model artifacts in Git;
- no PDFs in Git;
- no logs, CSVs, datasets, checkpoints or run artifacts in Git.

## Allowed scope

Only Markdown documentation under:

```text
docs/science/05_neural_controller_integration/
```

## Gate

If any runtime file changes in this block, the block fails. A future implementation block must start from these docs after review.
