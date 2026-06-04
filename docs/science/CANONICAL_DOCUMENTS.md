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

## Phase 6P/P2 - Closed Pre-validation Hygiene

- `docs/maintenance/pre_phase6_cleanup_report.md`
- `docs/maintenance/pre_phase6_workspace_layout_policy.md`
- `docs/maintenance/pre_phase6_evidence_integrity_risks.md`
- `docs/maintenance/pre_phase6_trace_leakage_audit.md`
- `docs/maintenance/phase6p2_workspace_recohesion_report.md`
- `scripts/audit_phase6_trace_eligibility.py`
- `tests/test_phase6_trace_eligibility_audit.py`

## Phase 6A0 - Validation Documentation Scaffold

- `docs/science/06_validation/README.md`
- `docs/science/06_validation/phase6a0_no_benchmark_yet.md`
- `docs/science/06_validation/phase6a0_search_protocol.md`
- `docs/science/06_validation/phase6a0_source_inventory.md`
- `docs/science/06_validation/phase6a0_source_triage_decision.md`
- `docs/science/06_validation/evaluation_evidence_matrix.md`
- `docs/science/06_validation/dataset_evidence_matrix.md`
- `docs/science/06_validation/threats_matrix.md`
- `docs/science/06_validation/protocol_decision_traceability.md`
- `docs/science/06_validation/ubuntu_evidence_package_spec.md`
- `docs/science/06_validation/phase6a0_open_gaps_for_phase6b.md`

Phase 6A0 is documentation/protocol intake only. It does not run a benchmark, create rankings, produce plots, declare a winner, retrain NeuralABR-Lite, or claim QoE improvement.

## Phase 6A2 - Experimental Protocol Freeze

- `docs/science/06_validation/phase6a2_protocol_freeze.md`
- `docs/science/06_validation/evaluation_protocol.md`
- `docs/science/06_validation/controller_matrix.md`
- `docs/science/06_validation/trace_selection_policy.md`
- `docs/science/06_validation/media_profile_decision.md`
- `docs/science/06_validation/metrics_schema.md`
- `docs/science/06_validation/statistical_comparison.md`
- `docs/science/06_validation/results_tables_plan.md`
- `docs/science/06_validation/reproducibility_checklist.md`
- `docs/science/06_validation/threats_to_validity.md`
- `docs/science/06_validation/phase6_memory_and_defense_plan.md`

Phase 6A2 freezes the protocol for the next technical readiness phase. It still does not run a benchmark, create rankings, produce plots from real data, generate result CSVs, declare a winner, retrain NeuralABR-Lite, or claim QoE improvement.

## Phase 6B - Manifest Readiness Gates

- `docs/science/06_validation/phase6_manifest_schema.md`
- `docs/science/06_validation/phase6b_preflight_contract.md`
- `docs/science/06_validation/phase6b_evaluation_readiness_report.md`
- `scripts/validate_phase6_trace_manifest.py`
- `scripts/check_phase6_evaluation_readiness.py`
- `scripts/audit_phase6_trace_eligibility.py`
- `tests/test_phase6_trace_manifest_validation.py`
- `tests/test_phase6_evaluation_readiness.py`
- `tests/test_phase6_trace_eligibility_audit.py`

Phase 6B closes the `canonical_content_fingerprint` audit gap and adds structural readiness gates for Phase 6C. It still does not run a benchmark, create rankings, produce plots from real data, generate result CSVs, declare a winner, retrain NeuralABR-Lite, or claim QoE improvement. `ready_for_phase6c` is not `ready_for_benchmark`, and `benchmark_authorized` remains false.

## Phase 6C - Automated Trace Materialization

- `configs/phase6/phase6c_public_sources.json`
- `docs/science/06_validation/phase6c_automated_acquisition_runbook.md`
- `docs/science/06_validation/phase6c_public_source_registry.md`
- `docs/science/06_validation/phase6c_normalization_contract.md`
- `docs/science/06_validation/phase6c_trace_manifest_freeze_contract.md`
- `docs/science/06_validation/phase6c_no_benchmark_boundary.md`
- `docs/science/06_validation/phase6c_live_materialization_troubleshooting.md`
- `scripts/run_phase6c_trace_materialization.py`
- `scripts/download_phase6_trace_sources.py`
- `scripts/extract_phase6_trace_archives.py`
- `scripts/normalize_phase6_trace_sources.py`
- `scripts/build_phase6_reference_manifest.py`
- `scripts/build_phase6_candidate_manifest.py`
- `scripts/freeze_phase6_trace_manifest.py`
- `tests/test_phase6c_orchestrator.py`
- `tests/test_phase6c_downloader.py`
- `tests/test_phase6c_extract.py`
- `tests/test_phase6c_normalization.py`
- `tests/test_phase6_reference_manifest.py`
- `tests/test_phase6_candidate_manifest.py`
- `tests/test_phase6_manifest_freeze.py`

Phase 6C automates acquisition, extraction, normalization, manifest building, validation, audit and external manifest freeze. Phase 6C-H1 hardens live materialization with primary-only defaults, source filtering, bounded normalizer sniffing, per-step logs, bounded output tails, timeouts, resume, skip-existing and clean-derived recovery. It does not require manual user-created configs or manifests. It still does not run a benchmark, create rankings, produce plots from real data, generate result CSVs, declare a winner, retrain NeuralABR-Lite, or claim QoE improvement. `ready_for_benchmark=false` and `benchmark_authorized=false` remain mandatory.

## Phase 6D - MPD-Derived Media Profile Freeze

- `configs/phase6/media_profile_phase6_v1_policy.json`
- `docs/science/06_validation/phase6d_media_profile_contract.md`
- `docs/science/06_validation/phase6d_mpd_extraction_runbook.md`
- `docs/science/06_validation/phase6d_media_profile_freeze_report.md`
- `docs/science/06_validation/phase6d_no_benchmark_boundary.md`
- `scripts/extract_phase6_media_profile_from_mpd.py`
- `scripts/validate_phase6_media_profile.py`
- `scripts/check_phase6_media_profile_compatibility.py`
- `scripts/freeze_phase6_media_profile.py`
- `scripts/run_phase6d_media_profile_freeze.py`
- `tests/test_phase6_mpd_media_profile_extraction.py`
- `tests/test_phase6_media_profile_validation.py`
- `tests/test_phase6_media_profile_compatibility.py`
- `tests/test_phase6d_media_profile_freeze.py`
- `tests/test_phase6d_orchestrator.py`

Phase 6D extracts `media_profile_phase6_v1` from a real MPD and freezes it outside Git after validation and compatibility checking. It supports real segment sizes from a local content root or HTTP `Content-Length`, and documents bitrate-estimated sizes when real sizes are unavailable. The server/VM is an MPD/content/media_profile source, not benchmark network evidence. It still does not run a benchmark, controllers, QoE, plots, rankings or result CSVs. `ready_for_benchmark=false` and `benchmark_authorized=false` remain mandatory.

## Thesis Memory

- `docs/science/07_memory/memory_structure_professor.md`
- `docs/science/07_memory/chapter_06_pre_evaluation_boundary.md`
- `docs/science/07_memory/implementation_chapter_traceability.md`
- `docs/science/07_memory/figures_tables_register.md`
- `docs/science/07_memory/originality_and_citation_policy.md`
