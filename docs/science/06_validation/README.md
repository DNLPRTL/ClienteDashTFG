# Phase 6 Validation Documentation

Phase 6A2 protocol freeze is complete.

This directory is the active validation documentation path for DashClientModular4:

```text
docs/science/06_validation/
```

Phase 6A0/A1 opened the validation documentation scaffold and consolidated literature/source evidence. Phase 6A2 freezes the final experimental protocol for the next technical readiness phase.

Phase 6A2 still does not authorize benchmark execution, controller ranking, plots, result CSVs, winner declarations, retraining, or any claim that `neural_abr_lite` improves QoE over a baseline.

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
