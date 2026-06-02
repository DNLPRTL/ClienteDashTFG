# Phase 5 neural controller integration documentation

This directory contains the Phase 5A0, Phase 5A1, Phase 5A2 and Phase 5B documentation package for integrating the accepted NeuralABR-Lite Candidate Scorer into DashClientModular4 in a later implementation block.

This block is documentation-only. It does not implement a controller, does not register a controller, does not touch playback/runtime code, and does not run a benchmark.

## Inherited Phase 4 decision

Phase 4 closed with NeuralABR-Lite accepted for controlled Phase 5 integration:

- method: behavior cloning / imitation learning;
- teacher: `robust_mpc`;
- action: `representation_index`;
- output: score per valid candidate representation;
- action mask: mandatory;
- inference: CPU-first PyTorch;
- normalization: train split only;
- bundle: local-only and outside the repository;
- benchmark status: no benchmark, no ranking, no SOTA claim, no real-world claim.

The inherited bundle contract contains:

```text
bundle_manifest.json
model_card.json
feature_schema.json
normalization_stats.json
ladder_schema.json
inference_contract.json
fallback_policy.json
model_state.pt
```

## Final integration target

The selected future integration target is a guarded neural scorer controller:

1. The controller receives online feedback before requesting the next segment.
2. Runtime features are built only from information available before the decision.
3. Bundle schema, feature schema and normalization schema are checked.
4. Normalization uses train-only `normalization_stats.json`.
5. An action mask is built from the current valid MPD representations.
6. CPU inference scores candidate representations.
7. `raw_action` is the best valid candidate.
8. A runtime safety guard checks `raw_action`.
9. Safe actions are executed.
10. Unsafe actions are downshifted to the highest lower feasible representation.
11. If no feasible action exists, or any runtime failure occurs, a classical fallback is used.
12. Diagnostic telemetry is emitted.
13. Telemetry remains diagnostic-only and not benchmark evidence.

## Documents created

Phase 5A0:

- `phase5a0_search_protocol.md`
- `phase5a0_source_inventory.md`
- `phase5a0_literature_delta_report.md`
- `phase5a0_source_triage_decision.md`
- `phase5a0_no_implementation_yet.md`
- `phase5a0_closure_report.md`

Phase 5A1:

- `phase5a1_source_card_index.md`
- `phase5a1_integration_evidence_matrix.md`
- `phase5a1_runtime_feature_availability_matrix.md`
- `phase5a1_safety_fallback_matrix.md`
- `phase5a1_model_loading_matrix.md`
- `phase5a1_telemetry_contamination_matrix.md`
- `source_cards/`

Phase 5A2:

- `phase5a2_integration_method_decision.md`
- `phase5a2_neural_as_guarded_scorer_decision.md`
- `phase5a2_rejected_alternatives.md`

Phase 5B:

- `phase5b_controller_integration_contract.md`
- `phase5b_runtime_feature_builder_contract.md`
- `phase5b_action_mask_contract.md`
- `phase5b_safety_guard_contract.md`
- `phase5b_fallback_policy_contract.md`
- `phase5b_bundle_loading_contract.md`
- `phase5b_model_loading_security_contract.md`
- `phase5b_cpu_inference_contract.md`
- `phase5b_telemetry_contract.md`
- `phase5b_error_handling_contract.md`
- `phase5b_artifact_policy.md`
- `phase5b_no_benchmark_policy.md`
- `phase5b_acceptance_tests.md`
- `phase5b_codex_implementation_readiness_gate.md`

Phase 5C:

- `phase5c_scope_and_gate.md`
- `phase5c_current_code_mapping.md`
- `phase5c_offline_runtime_boundary_spec.md`
- `phase5c_file_change_plan.md`
- `phase5c_controller_api_mapping.md`
- `phase5c_bundle_runtime_spec.md`
- `phase5c_runtime_feature_spec.md`
- `phase5c_action_mask_safety_fallback_spec.md`
- `phase5c_telemetry_hook_decision.md`
- `phase5c_test_plan_phase5d.md`
- `phase5c_phase5d_codex_prompt.md`
- `phase5c_closure_report.md`

Memory and roadmap:

- `notes_for_memory.md`
- `phase5_remaining_roadmap.md`

## Gates before implementation

Implementation may only start after:

- source cards exist and are reviewed;
- integration evidence matrices exist and are reviewed;
- the guarded scorer decision is accepted;
- all Phase 5B contracts exist;
- all Phase 5C implementation specs exist;
- the Phase 5D Codex prompt is ready;
- no runtime code has been touched in this documentation block;
- `python -m unittest discover` passes;
- `python scripts/check_client_readiness.py --strict` passes;
- the future implementation prompt explicitly preserves the diagnostic-only and not benchmark boundary.
