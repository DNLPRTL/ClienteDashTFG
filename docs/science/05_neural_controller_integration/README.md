# Phase 5 NeuralABR-Lite controller integration

This directory records Phase 5 of the NeuralABR-Lite work: integration of the Phase 4 Candidate Scorer as a guarded controller in DashClientModular4.

Phase 5 is integration work only. It does not benchmark, rank controllers, claim QoE improvement, retrain, or claim real-world superiority.

## Final Phase 5 status

Phase 5G decision:

```text
ACCEPTED_PENDING_FINAL_POST_HARDENING_SMOKE
```

The final post-hardening real-bundle regression smoke for HEAD `72681b6` was not provided in the Phase 5G input and is recorded as:

```text
PENDING_USER_EXECUTION
```

No later phase is opened by this directory update.

## Controller result

- Controller key: `neural_abr_lite`.
- Role: guarded neural scorer controller.
- Model: Phase 4 NeuralABR-Lite Candidate Scorer.
- Action space: `representation_index`.
- Return value: existing MPD ladder rate in bytes per second.
- Runtime: CPU-first PyTorch.
- Bundle: optional local-only artifact outside Git.
- Model loading: `torch.load(..., map_location="cpu", weights_only=True)`.
- Safety: action mask, runtime safety guard, classical fallback, emergency representation.
- Telemetry: diagnostic-only `feedback_neural_*` fields in `segment_telemetry.csv`.
- Evaluation artifact boundary: `evaluation_segments.csv` remains free of neural diagnostics.
- Config: disabled/commented example only; default behavior unchanged.

## Phase status

| Block | Status | Notes |
| --- | --- | --- |
| Phase 5A0 | Closed | Search protocol, source inventory, literature delta, triage, and no-implementation gate. |
| Phase 5A1 | Closed | Evidence/source cards and integration matrices. |
| Phase 5A2 | Closed | Guarded scorer decision and rejected alternatives. |
| Phase 5B | Closed | Controller, feature, action-mask, safety, fallback, bundle, security, CPU, telemetry, error, artifact, no-benchmark, and acceptance-test contracts. |
| Phase 5C | Closed | Implementation specifications and Phase 5D prompt finalized. |
| Phase 5D | Closed | `neural_abr_lite` implemented and registered with focused tests. |
| Phase 5E | Closed | Structural smokes recorded: no-bundle fake, real-bundle fake, optional Ubuntu/GStreamer structural/demo. |
| Phase 5F | Closed locally | Fallback/error/telemetry hardening validated with 471 tests and readiness strict. |
| Phase 5G | Accepted pending final smoke | Documentation-only closure; final post-hardening real-bundle regression smoke pending user execution. |

## Key documents

Phase 5A0/A1/A2/B/C documents remain as the evidence, contract, and implementation-specification trail.

Phase 5D/E/F/G closure documents:

- `phase5d_implementation_report.md`
- `phase5d_structural_smoke_runbook.md`
- `phase5e_closure_report.md`
- `phase5e_artifact_inspection_checklist.md`
- `phase5f_scope_and_gate.md`
- `phase5f_fault_injection_plan.md`
- `phase5f_error_fallback_matrix.md`
- `phase5f_telemetry_hardening_matrix.md`
- `phase5f_hardening_report.md`
- `phase5f_closure_report.md`
- `phase5g_scope_and_gate.md`
- `phase5g_final_integration_closure_report.md`
- `phase5g_validation_register.md`
- `phase5g_controller_status_summary.md`
- `phase5g_safety_fallback_closure.md`
- `phase5g_telemetry_artifact_closure.md`
- `phase5g_limitations_and_non_claims.md`
- `phase5g_memory_notes.md`
- `phase5g_repository_release_checklist.md`
- `phase5g_closed_phase_handoff_stub.md`

## Artifact policy

No model files, run outputs, logs, CSVs, datasets, zips, PDFs, or media artifacts belong in Git for this phase.

## Non-claim boundary

Phase 5 proves structural integration and safety hardening only. It does not establish comparative performance.
