# Canonical Documents

This is the shortest reading path for understanding the project without opening every historical Markdown file.

## Repository Entry

- `README.md`
- `AGENTS.md`
- `docs/INDEX.md`

## Phase 1 - Client Hardening

- `docs/architecture/phase1_acceptance.md`
- `docs/architecture/client_readiness_report.md`
- `docs/architecture/telemetry_column_provenance.md`
- `docs/runbooks/run_client.md`
- `docs/runbooks/run_layout.md`

## Phase 2 - Baselines

- `docs/science/01_baselines/README.md`
- `docs/science/01_baselines/baseline_selection_matrix.md`
- `docs/science/01_baselines/baseline_implementation_summary.md`
- `docs/science/01_baselines/baseline_phase2_3_closure_report.md`
- `docs/science/01_baselines/phase2_baseline_closure.md`

## Phase 3 - Traces And Replay

- `docs/science/02_traces_replay/README.md`
- `docs/science/02_traces_replay/common_trace_schema.md`
- `docs/science/02_traces_replay/leakage_prevention_policy.md`
- `docs/science/02_traces_replay/generalization_protocol.md`
- `docs/architecture/phase3_trace_schema_contract.md`

## Phase 3.5 - QoE And Reward

- `docs/science/03_qoe_reward/README.md`
- `docs/science/03_qoe_reward/metric_formula_catalog.md`
- `docs/science/03_qoe_reward/reward_definition.md`
- `docs/science/03_qoe_reward/phase3_5_results_boundary.md`
- `docs/science/03_qoe_reward/phase3_5_final_artifact_index.md`

If a filename has changed inside Phase 3.5, use `docs/science/03_qoe_reward/README.md` as the canonical local index before opening older files.

## Phase 4 - NeuralABR-Lite

- `docs/science/04_neural_abr/README.md`
- `docs/science/04_neural_abr/neural_abr_lite_candidate_scorer_decision.md`
- `docs/science/04_neural_abr/training_data_contract.md`
- `docs/science/04_neural_abr/trace_split_contract.md`
- `docs/science/04_neural_abr/teacher_policy_contract.md`
- `docs/science/04_neural_abr/phase4f_export_inference_contract_report.md`
- `docs/science/04_neural_abr/phase4g_closure_report.md`

Phase 4 diagnostics are not formal Phase 6 performance evidence because checksum duplicates were found across Phase 4 splits.

## Phase 5 - Guarded Controller Integration

- `docs/science/05_neural_controller_integration/README.md`
- `docs/science/05_neural_controller_integration/phase5b_no_benchmark_policy.md`
- `docs/science/05_neural_controller_integration/phase5d_implementation_report.md`
- `docs/science/05_neural_controller_integration/phase5e_closure_report.md`
- `docs/science/05_neural_controller_integration/phase5f_closure_report.md`
- `docs/science/05_neural_controller_integration/phase5g_final_integration_closure_report.md`
- `docs/science/05_neural_controller_integration/phase5g_limitations_and_non_claims.md`

## Phase 6P - Pre-validation Hygiene

- `docs/maintenance/pre_phase6_cleanup_report.md`
- `docs/maintenance/pre_phase6_workspace_layout_policy.md`
- `docs/maintenance/pre_phase6_evidence_integrity_risks.md`
- `docs/maintenance/pre_phase6_trace_leakage_audit.md`
- `scripts/audit_phase6_trace_eligibility.py`
- `tests/test_phase6_trace_eligibility_audit.py`

## Thesis Memory

- `docs/science/07_memory/memory_structure_professor.md`
- `docs/science/07_memory/chapter_06_pre_evaluation_boundary.md`
- `docs/science/07_memory/implementation_chapter_traceability.md`
- `docs/science/07_memory/figures_tables_register.md`
- `docs/science/07_memory/originality_and_citation_policy.md`
