# Baseline Selection

This folder defines the Phase 2 ABR baseline selection and implementation scaffold.

The scaffold now includes implemented sanity controllers, `rate_based`, `bba`, `bola`, `mpc`, and `robust_mpc`. It still does not implement SODA, Pensieve, DYNAMIC, FAST SWITCHING, replay, traces, QoE reward, datasets, or benchmark code.

## Phase 2.3 Closure Audit

The Phase 2.3 closure audit is documented in:

- `baseline_implementation_summary.md`
- `_historical/baseline_registry_audit.md`
- `_historical/baseline_testing_summary.md`
- `_historical/baseline_smoke_summary.md`
- `_historical/baseline_limitations.md`
- `baseline_phase2_3_closure_report.md`

## Phase 2.4 Formal Closure

The formal Phase 2 closure and transition package is documented in:

- `phase2_baseline_closure.md`
- `phase2_controller_inventory.md`
- `_historical/phase2_test_validation_summary.md`
- `phase2_academic_validity_statement.md`
- `_historical/phase2_open_limitations_and_deferred_work.md`
- `_handoffs/phase2_transition_to_phase3.md`

## Initial Baseline Set

| order | controller class | status |
| --- | --- | --- |
| 1 | sanity controllers: `min_rate`, `fixed_rate`, `max_rate` | implemented as plumbing sanity only |
| 2 | `rate_based` | implemented first academic baseline; throughput-based |
| 3 | `bba` | implemented second academic baseline; buffer-based BBA-0 |
| 4 | `bola` | implemented third academic baseline; BOLA-basic utility/buffer score |
| 5 | `mpc` | implemented fourth academic baseline; small-horizon enumerative MPC |
| 6 | `robust_mpc` | implemented fifth academic baseline; MPC with conservative prediction correction |
| 7 | optional candidates | only if later justified |

## Required Gate Before Code

For every academic baseline implementation, create and review:

- `paper_card.md`
- `implementation_spec.md`
- `controller_api_mapping.md`
- `acceptance_tests.md`
- `notes_for_memory.md`

Each implementation block must update the controller-specific docs, tests, traceability matrices and memory notes without creating benchmark claims.


## Phase 6P2 Navigation

Phase 6P2 keeps canonical and support documents in this directory root, while older working material is grouped below:

- `_historical/`: preserved intermediate records and superseded notes.
- `_handoffs/`: closed prompts, handoffs, and transition instructions.
- `_templates/`: reusable templates, not current project state.

Use the phase README and `docs/science/CANONICAL_DOCUMENTS.md` before opening historical material.
