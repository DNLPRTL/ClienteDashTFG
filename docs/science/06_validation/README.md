# Phase 6A0 Validation Documentation

Phase 6A0 is open.

This directory is the active validation documentation path for DashClientModular4:

```text
docs/science/06_validation/
```

Phase 6A0/A1 is documentation, literature intake, protocol consolidation and evidence-scaffold work only. It does not authorize benchmark execution, controller ranking, plots, winner declarations, retraining, or any claim that `neural_abr_lite` improves QoE over a baseline.

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
