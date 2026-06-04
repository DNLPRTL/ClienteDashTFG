# Phase 4E.1 external trace model card

## Model

- Name: NeuralABR-Lite Candidate Scorer
- Phase: 4E.1 external trace smoke
- Status: diagnostic smoke checkpoint only
- Decision: `PHASE4E1_EXTERNAL_TRACE_SMOKE_PASS_NOT_CANDIDATE`

## Intended use

This checkpoint is intended to validate the offline training pipeline on Phase 3 normalized external trace CSVs:

- external trace ingestion;
- manifest metadata preservation;
- trace/leakage-group split;
- train-only normalization;
- CPU behavior-cloning training;
- action-mask validity;
- validation and OOD diagnostic reporting.

## Not intended use

- Client integration.
- Controller registration.
- Phase 4F export.
- Production deployment.
- Benchmark ranking.
- Real-world or SOTA claim.

## Training data

- Source: Phase 3 normalized trace CSV smoke subset.
- Trace schema: `normalized_trace_schema_v1`.
- Trace count: 15.
- Train samples: 1367.
- Validation samples: 407.
- OOD diagnostic samples: 427.
- Split policy: `phase4e1_trace_level_regime_v1`.
- OOD use: diagnostic-only, not tuning.

No legacy dry-runs, controller actions, QoE smoke outputs or benchmark artifacts were used as training data.

## Features

Context features:

```text
throughput_history_bps[5]
download_time_history_s[5]
buffer_s
last_representation_index
last_bitrate_bps
recent_rebuffer_s
recent_switch_abs
chunks_remaining_norm
has_chunks_remaining
```

Candidate features:

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

Forbidden model inputs include future throughput, future download time, teacher action, teacher reward, split, trace ID, source dataset, regime label and benchmark result.

## Training

- Objective: masked cross entropy over valid candidate scores.
- Teacher: `robust_mpc`.
- Reward context: `qoe_linear_v1 / reward_n`.
- Epochs: 5.
- Batch size: 16.
- Seed: 123.
- Device: CPU.
- Final loss: 0.6211519241333008.
- Mean loss: 0.5170281020772838.

## Validation

| split | valid action rate | teacher agreement | prediction distribution |
|---|---:|---:|---|
| validation | 1.0 | 0.941031941031941 | `{"0": 9, "1": 15, "2": 36, "3": 20, "4": 327}` |
| ood_diagnostic | 1.0 | 0.9133489461358314 | `{"0": 16, "1": 21, "2": 36, "3": 57, "4": 297}` |

The no-fixed-action-collapse diagnostic passed for this smoke. The highest representation remains dominant, so broader external validation is still required.

## Limitations

This checkpoint is not selected for Phase 4F. The external trace subset is small, no runtime inference/export contract was exercised, no CPU latency budget was measured, and no formal benchmark comparison was run.
