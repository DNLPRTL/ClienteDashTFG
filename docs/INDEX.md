# Repository Documentation Index

This index is the human entry point for DashClientModular4 documentation. It is intentionally selective.

## Architecture

- `docs/architecture/client_readiness_report.md`: final client readiness record from Phase 1.
- `docs/architecture/phase1_acceptance.md`: Phase 1 acceptance boundary.
- `docs/architecture/baseline_entry_contract.md`: baseline-entry controller contract.
- `docs/architecture/telemetry_column_provenance.md`: runtime and evaluation telemetry provenance.
- `docs/architecture/output_artifact_contract.md`: generated run artifact contract.
- `docs/architecture/phase2_baseline_closure.md`: baseline implementation closure.
- `docs/architecture/phase3_trace_schema_contract.md`: trace schema contract.

## Runbooks

- `docs/runbooks/environment.md`: Windows host and Ubuntu environment setup.
- `docs/runbooks/run_client.md`: non-interactive and interactive client runs.
- `docs/runbooks/run_layout.md`: run directory layout.
- `docs/runbooks/gstreamer_playback.md`: GStreamer integration/demo path.

## Science By Phase

- `docs/science/README.md`: science documentation overview.
- `docs/science/PHASE_INDEX.md`: phase-to-directory map.
- `docs/science/CANONICAL_DOCUMENTS.md`: shortest path through the canonical scientific trail.
- `docs/science/HISTORICAL_DOCUMENT_POLICY.md`: how to interpret historical, handoff, closure, and template docs.
- `docs/science/06_validation/README.md`: active Phase 6A2 validation protocol freeze and evidence scaffold.

## Roadmap

- `docs/roadmap/gui_frontend_dashboard.md`: future GUI/operator dashboard roadmap.

## Maintenance

- `docs/maintenance/pre_phase6_cleanup_report.md`: Phase 6P cleanup summary and external manifest pointers.
- `docs/maintenance/pre_phase6_workspace_layout_policy.md`: expected TFG workspace layout and artifact policy.
- `docs/maintenance/pre_phase6_evidence_integrity_risks.md`: pre-Phase6 evidence risks and mitigations.
- `docs/maintenance/pre_phase6_trace_leakage_audit.md`: checksum leakage guardrail and script usage.
- `docs/maintenance/phase6p2_workspace_recohesion_report.md`: closed Phase 6P2 documentation re-cohesion, external cleanup, and manifest map.

## Tests And Scripts

- `tests/`: checked-in unit and smoke tests.
- `scripts/check_client_readiness.py`: strict readiness gate.
- `scripts/audit_phase6_trace_eligibility.py`: Phase 6 trace eligibility audit.
- `scripts/validate_neural_abr_bundle.py`: local-only bundle validation helper.
- `scripts/smoke_neural_abr_inference.py`: local-only structural inference smoke helper.

External `_scripts/` under the TFG root are local-only operational history, not canonical repo automation.
