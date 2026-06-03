# Pre-Phase6 Evidence Integrity Risks

This note records risks found before Phase 6A0. It does not reopen Phase 5 and does not convert Phase 4 diagnostics into benchmark evidence.

## Closed State

Phase 5 remains closed as structural integration of `neural_abr_lite`:

```text
ACCEPTED_AS_INTEGRATED_GUARDED_CONTROLLER
```

The controller is integrated as a guarded scorer with runtime features, bundle/schema validation, normalization, action mask, CPU inference, safety guard, fallback, and diagnostic telemetry.

## Main Risk

The Phase 4 final candidate manifest contains checksum duplicates across splits:

```text
_datasets/phase4_AI/neural_abr_lite/phase4E2_expanded_candidate_20260529_080755/dataset_manifest.json
```

Recorded values:

- `trace_records = 210`
- `unique_checksums = 170`
- `duplicate_checksum_groups = 40`
- `checksum_cross_split_overlap_count = 17`
- `trace_id_cross_split_overlap_count = 0`
- `leakage_group_cross_split_overlap_count = 0`

Interpretation:

- The split appears clean by `trace_id` and `leakage_group`.
- It is not clean by `checksum_sha256`.
- Ghent has duplicated trace payloads in `logs_all` and specific folders such as `logs_bus`, `logs_car`, and `logs_foot`.

## Impact

This does not invalidate Phase 5 integration. Phase 5 tested guarded runtime integration, not comparative performance.

It does limit Phase 4 claims:

- teacher agreement is diagnostic only;
- OOD diagnostics are diagnostic only;
- Phase 4 is not strong evidence of generalization;
- Phase 4 cannot be used as a formal Phase 6 performance result.

## Required Mitigation

Before evaluating `neural_abr_lite` in Phase 6, exclude every checksum seen in Phase 4 train, validation, or OOD from Phase 6 evaluation splits.

For classical baselines, overlapping traces may still be useful as a separate diagnostic, but not as the fair IA-vs-baseline comparison set.

## Guardrail

Use:

```text
scripts/audit_phase6_trace_eligibility.py
```

The script writes a JSON report with:

- `use_for_phase6_eval`;
- overlap checks by checksum, `trace_id`, and `leakage_group`;
- internal duplicate checks;
- detection of `logs_all` vs specific-folder duplicates.
