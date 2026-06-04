# Phase 6 Validation Documentation

Phase 6A2 protocol freeze is complete. Phase 6B added evaluation readiness gates, manifest schema validation and canonical content fingerprint audit hardening. Phase 6C adds automated trace acquisition, normalization and manifest freeze tooling. Phase 6D adds MPD-derived media-profile extraction, validation, compatibility checking and external freeze tooling.

This directory is the active validation documentation path for DashClientModular4:

```text
docs/science/06_validation/
```

Phase 6A0/A1 opened the validation documentation scaffold and consolidated literature/source evidence. Phase 6A2 freezes the final experimental protocol. Phase 6B added readiness/audit code. Phase 6C automates real dataset materialization outside the repository. Phase 6D freezes the shared media profile from real MPD/content evidence outside the repository.

Phase 6D still does not authorize benchmark execution, controller ranking, plots, result CSVs, winner declarations, retraining, or any claim that `neural_abr_lite` improves QoE over a baseline.

## Current Boundary

- Primary evaluation path remains Python trace-driven.
- The VM server is for content/demo/media_profile work, not benchmark network evaluation.
- `qoe_linear_v1` remains the primary QoE formula.
- `qoe_linear_mean` is the future primary session aggregate.
- `qoe_log_v1` remains a sensitivity metric.
- Startup is report-only until measured homogeneously.
- VMAF and MOS claims are deferred until the required artifacts exist.
- Gates remain mandatory: `use_for_eval`, `diagnostic_only`, `do_not_use_for_eval`.
- Phase 4E2 teacher agreement/OOD material remains diagnostic history, not strong generalization evidence.
- Phase 6B closes the `canonical_content_fingerprint` audit gap while continuing to report `checksum_sha256` separately.
- Phase 6C is automated; the user should not manually create source configs or manifests.
- Phase 6C-H1 makes live materialization primary-only by default and adds per-step logs, bounded output tails, progress files, timeouts, resume, skip-existing and clean-derived recovery.
- Phase 6D uses the user's real Ubuntu-server MPDs and representation folders as media-profile source material.
- The VM server is an MPD/content/media_profile source and demo/integration surface, not the benchmark network.
- Future benchmark network conditions remain Python trace-driven from normalized traces through `TraceDrivenNetworkModel`.
- The provided MPD-derived profile is 60 s long, uses 4 s segments, yields 15 segments, and exposes a canonical ascending-bitrate ladder `300/750/1200/1850/2850/4300` kbps.
- `representation_index` is canonical ascending bitrate and independent of MPD id order.
- Real segment sizes are preferred via `--content-root` or `--base-url`; otherwise a documented bitrate estimate is used.
- NeuralABR-Lite bundle compatibility is checked by JSON metadata/action count when a bundle path is provided.
- If the full 6-representation ladder is incompatible with a 5-action bundle, the primary profile must use the common MPD-derived subset and retain the full ladder as diagnostic only.
- Real datasets, normalized CSVs, receipts, local manifests, media-profile outputs, MPDs, segments, logs and reports live outside the repo.
- `ready_for_phase6c` is not `ready_for_benchmark`; `benchmark_authorized` remains false.
- Final Phase 6 trace IDs are frozen only by the external `phase6_trace_manifest_final.json` after acquisition, normalization, validation, eligibility audit and freeze.
- Future Phase 6E planning requires both the external Phase 6C trace manifest and the external Phase 6D frozen media profile.

## Frozen Phase 6A2 Protocol

- `evaluation_protocol.md`: final experimental protocol boundary.
- `controller_matrix.md`: controllers in scope and classification.
- `trace_selection_policy.md`: trace groups, leakage gates and final manifest rule.
- `media_profile_decision.md`: frozen media profile policy.
- `metrics_schema.md`: primary/secondary metrics and gates.
- `statistical_comparison.md`: statistical unit, summaries, CI and pairwise plan.
- `results_tables_plan.md`: planned figures/tables, not generated outputs.
- `reproducibility_checklist.md`: future evidence checklist.
- `threats_to_validity.md`: final threats narrative.
- `phase6a2_protocol_freeze.md`: protocol-freeze decision.
- `phase6_memory_and_defense_plan.md`: thesis and defense integration plan.

## Phase 6B Readiness Contracts

- `phase6_manifest_schema.md`: manifest fields, gate aliases, fingerprint aliases and strict-final requirements.
- `phase6b_preflight_contract.md`: structural readiness checks and non-benchmark boundary.
- `phase6b_evaluation_readiness_report.md`: JSON report semantics for `ready_for_phase6c`, `ready_for_benchmark` and `benchmark_authorized`.

## Phase 6C Automation Contracts

- `phase6c_automated_acquisition_runbook.md`: one-command external materialization runbook.
- `phase6c_public_source_registry.md`: committed public-source metadata and source roles.
- `phase6c_normalization_contract.md`: normalized CSV schema and fingerprint contract.
- `phase6c_trace_manifest_freeze_contract.md`: final external manifest freeze preconditions.
- `phase6c_no_benchmark_boundary.md`: explicit non-execution boundary.
- `phase6c_live_materialization_troubleshooting.md`: live-output, timeout and interrupted-normalization recovery guidance.

## Phase 6D Media Profile Contracts

- `phase6d_media_profile_contract.md`: MPD-derived media-profile schema, ladder order, size policy and NeuralABR-Lite compatibility contract.
- `phase6d_mpd_extraction_runbook.md`: one-command external media-profile freeze runbook.
- `phase6d_media_profile_freeze_report.md`: committed report template and external freeze preconditions.
- `phase6d_no_benchmark_boundary.md`: explicit non-execution boundary for media-profile freeze work.

## Entry Documents

- `phase6a0_search_protocol.md`: intake process, source handling and no-PDF implementation rule.
- `phase6a0_source_inventory.md`: classified Phase 6A0 source inventory.
- `phase6a0_literature_delta_report.md`: what changed relative to Phase 6P/P2.
- `phase6a0_source_triage_decision.md`: accepted, deferred and not-used decisions.
- `phase6a0_no_benchmark_yet.md`: explicit non-results boundary.

## Evidence Scaffold

- `source_cards/`: canonical source cards for methodology, guardrails and QoE/reporting.
- `dataset_cards/`: dataset cards for first candidates and future OOD candidates.
- `evaluation_evidence_matrix.md`: source-to-protocol evidence mapping.
- `dataset_evidence_matrix.md`: dataset readiness and leakage matrix.
- `threats_matrix.md`: threats to validity and mitigation plan.
- `protocol_decision_traceability.md`: source, decision, document and future gate map.
- `ubuntu_evidence_package_spec.md`: future evidence ZIP contract.
- `phase6a0_open_gaps_for_phase6b.md`: hardening and protocol gaps for later phases.

## Non-Claim Boundary

Generated documents in this directory are protocol evidence only. They are not run outputs, benchmark evidence, rankings, plots, or performance results.

Raca 4G and Raca 5G are the primary OOD candidates. Lumos5G is optional and may be blocked by Google Drive. Ghent and HSDPA are same-family diagnostic by default. Lancaster remains excluded from primary final evaluation unless a source note/card and eligibility audit authorize it. Ghent must use `logs_all` OR per-mobility folders, not both, unless deduplicated by checksum/fingerprint.
