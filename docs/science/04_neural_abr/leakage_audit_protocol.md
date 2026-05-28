# Leakage audit protocol

## Purpose

Block invalid ML claims before training.

## Audit checks

The future dataset builder must check:

```text
no validation trace in train
no OOD trace in train
no split field exposed as feature
no trace_id exposed as feature
no teacher action exposed as feature
no future throughput exposed as feature
no future QoE/reward exposed as feature
no benchmark result exposed as feature
normalization fitted on train only
action label within action mask
candidate features available before request
```

## Future-information audit

For each feature, the audit must classify availability:

```text
online_observable_before_decision
manifest_available_before_decision
offline_metadata_not_model_feature
teacher_only
forbidden
```

Only the first two categories may enter model input.

## Report

The audit must produce:

```text
leakage_audit_report.json
leakage_audit_summary.md
```

## Gate

Any leakage audit failure is a hard block for training and for Phase 5 integration.
