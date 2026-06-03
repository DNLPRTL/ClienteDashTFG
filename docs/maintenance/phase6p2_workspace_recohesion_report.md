# Phase 6P2 Workspace Re-cohesion Report

Status: maintenance_only_pre_validation_hygiene.

Phase 6P2 reorganized documentation and local-only workspaces before Phase 6A0. It did not change runtime logic, controllers, `player.py`, `core/trace_replay`, `core/evaluation`, training, benchmarks, plots, rankings, or QoE claims.

## External Audit

Primary Phase 6P2 audit workspace:

```text
C:\Users\danie\Documents\TFG\_audits\phase6p2_workspace_recohesion_20260603_135527
```

Important local-only manifests:

- `phase6p2_workspace_audit.json`: updated inventory, duplicate SHA-256 groups, documentation buckets, and guardrails.
- `phase6p2_doc_move_plan.json`: planned documentation moves.
- `phase6p2_doc_move_manifest.final.json`: final old_path to new_path documentation mapping.
- `phase6p2_external_cleanup_plan.json`: planned external archive/delete actions.
- `phase6p2_external_cleanup_manifest.json`: applied external cleanup actions.

## Documentation Layout

Canonical and support documents remain in each phase directory root. Phase 6P2 groups older working material inside each phase:

- `_historical/`: intermediate reports, closure trail fragments, local runbooks, notes, and superseded plans.
- `_handoffs/`: prompts, handoffs, transition notes, and next-step records from closed blocks.
- `_templates/`: reusable templates.

Use this order before opening deep historical files:

1. `docs/INDEX.md`
2. `docs/science/PHASE_INDEX.md`
3. `docs/science/CANONICAL_DOCUMENTS.md`
4. the phase `README.md`
5. `_historical/`, `_handoffs/`, or `_templates/` only when provenance is needed

## External Workspace Map

Expected local root:

```text
C:\Users\danie\Documents\TFG
```

Current external workspaces:

- `_datasets/`: local raw, normalized, and training/provenance datasets; not Git content.
- `_models/`: local model bundles and validation outputs; not Git content.
- `_runs/`: local run outputs; may be empty after cleanup.
- `_scripts/`: local operational scripts not promoted through a repo spec.
- `_literature/`: local PDF/source batches; not Git content.
- `_audits/`: local audit JSON/Markdown/manifests.
- `_archive/`: reversible cleanup archive with manifests and hashes.

Current protected NeuralABR-Lite paths:

```text
_models/phase4_AI/neural_abr_lite/phase4F/bundle_20260529_091652
_datasets/phase4_AI/neural_abr_lite/phase4E2_expanded_candidate_20260529_080755
```

## External Cleanup Applied

Archive root:

```text
C:\Users\danie\Documents\TFG\_archive\pre_phase6p2_strong_cleanup_20260603_140329
```

Applied actions:

- Documentation moves: 182
- Archive moves: 10
- Duplicate file deletes: 22
- Empty directory removals: 4

Duplicate deletes were limited to byte-identical files under ad-hoc `_literature/fase 5` and `_literature/fase 6` paths when at least one retained copy with the same SHA-256 existed elsewhere.

## Guardrails Respected

- No benchmark was executed.
- No plot was generated.
- No ranking was created.
- No controller winner was declared.
- No QoE improvement claim was made.
- No NeuralABR-Lite retraining was performed.
- No runtime, player, controller, trace replay, or evaluation logic was changed.
- `docs/science/06_validation/` remains unopened.
