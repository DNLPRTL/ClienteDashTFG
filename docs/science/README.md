# Science Documentation

This directory contains the scientific documentation trail for DashClientModular4.

The current state is:

- Phase 5 is closed.
- `neural_abr_lite` is integrated as a guarded neural scorer controller.
- Phase 5 did not run benchmarks, create rankings, or claim QoE improvement.
- Phase 6P and Phase 6P2 are closed as pre-validation workspace and evidence hygiene.
- Phase 6A0/A1 opened the validation documentation scaffold.
- Phase 6A2 freezes the final experimental protocol for the next technical readiness phase.
- `docs/science/06_validation/` is the active validation documentation path.
- No Phase 6A2 benchmark, ranking, plot from real data, result CSV, winner or QoE improvement claim exists.

## Entry Points

- `PHASE_INDEX.md`: map from project phases to documentation directories.
- `CANONICAL_DOCUMENTS.md`: shortest canonical reading path.
- `HISTORICAL_DOCUMENT_POLICY.md`: how to interpret historical, handoff, closure, template, memory-feed, and local-only references.

## Phase 6P2 Navigation

Phase directories keep canonical and support documents in their root. Closed-phase working material is grouped into `_historical/`, `_handoffs/`, and `_templates/` folders inside the same phase.

Read `CANONICAL_DOCUMENTS.md` and the phase `README.md` first. Open historical folders only for provenance, reconstruction, or thesis traceability.

## Directory Map

| path | phase | purpose |
| --- | --- | --- |
| `00_field_map/` | Field map | DASH background, scope, source inventory, and positioning. |
| `01_baselines/` | Phase 2 | baseline selection, implementation specs, source cards, validation summaries, and closure. |
| `02_traces_replay/` | Phase 3 | trace datasets, replay methodology, leakage prevention, and trace schema. |
| `03_qoe_reward/` | Phase 3.5 | QoE/reward definition and artifact boundary. |
| `04_neural_abr/` | Phase 4 | NeuralABR-Lite dataset, teacher, training, export, and diagnostic records. |
| `05_neural_controller_integration/` | Phase 5 | canonical integration path for `neural_abr_lite`. |
| `06_validation/` | Phase 6A2 | active validation protocol freeze and evidence scaffold; no benchmark authorization. |
| `07_memory/` | Thesis | memory, defense, figures, tables, and thesis integration notes. |

## Source Handling Rules

- Do not add raw PDFs to the repository.
- Do not implement from raw PDFs or pasted paper text.
- Do not copy long passages, paper figures, or datasets into Git.
- Keep implementation decisions traceable to source cards, specs, matrices, and closure reports.
- Keep generated artifacts outside the repository.

## Evidence Boundary

Phase 4 teacher agreement and OOD diagnostics are diagnostic evidence only. Because the Phase 4 candidate dataset has checksum duplicates across splits, Phase 6 must exclude all Phase 4 checksums from any fair `neural_abr_lite` evaluation split.
