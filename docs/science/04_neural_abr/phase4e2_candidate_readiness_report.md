# Phase 4E.2 Candidate Readiness Report

Decision: `PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F`

This report is an offline diagnostic gate for NeuralABR-Lite. It is not a formal benchmark, ranking, SOTA claim, or real-world validation.

## Corpus and dataset

- Trace count: `210`
- Dataset families: `3`
- Regime buckets: `10`
- Split policy: `phase4e2_regime_balanced_trace_v1`

## Validation

- Offline validation status: `PASS`
- Validation valid action rate: `1.0`
- OOD diagnostic valid action rate: `1.0`
- Validation teacher agreement: `0.9613788700925631`
- OOD teacher agreement: `0.9583333333333334`

## Distribution sanity

- Validation TVD prediction vs teacher: `0.0054261091605489874`
- OOD TVD prediction vs teacher: `0.0052966101694914905`
- Validation entropy ratio: `0.9977732022653799`
- OOD entropy ratio: `0.9940127060352608`

## Gates

- `unit_tests_pass`: `UNKNOWN`
- `readiness_pass`: `UNKNOWN`
- `dataset_validation_pass`: `PASS`
- `offline_validation_pass`: `PASS`
- `validation_valid_action_rate_is_1`: `PASS`
- `ood_valid_action_rate_is_1`: `PASS`
- `no_nan_inf`: `PASS`
- `no_invalid_labels`: `PASS`
- `no_trace_overlap`: `PASS`
- `no_leakage_group_overlap`: `PASS`
- `train_only_normalization`: `PASS`
- `cpu_execution`: `PASS`
- `no_forbidden_repo_artifacts`: `PASS`
- `no_controller_runtime_media_changes`: `PASS`
- `trace_count_at_least_30`: `PASS`
- `dataset_family_count_at_least_2`: `PASS`
- `regime_bucket_count_at_least_3`: `PASS`
- `model_card_exists`: `PASS`
- `limitations_doc_exists`: `PASS`

## Warnings

- dataset family hsdpa_norway_mmsys2013 is below 5% of trace count
- regime bucket low_variable is below 5% of trace count
- regime bucket very_high_variable is below 5% of trace count

## Boundary

OOD remains diagnostic-only. Phase 4F is allowed only when the decision is `PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F`; this report does not integrate a neural controller into the client.
