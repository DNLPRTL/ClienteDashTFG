# Trace Schema Acceptance Tests

This document defines future acceptance tests for `normalized_trace_schema_v1`. It does not add tests or implement validators in Phase 3.2B.

Future tests must use `unittest`, not `pytest`.

## Required Acceptance Areas

| area | future assertion |
| --- | --- |
| required columns | A valid trace includes `timestamp_s`, `duration_s` and `throughput_kbps`. |
| numeric parsing | Required columns parse as numbers. |
| timestamp order | `timestamp_s` is monotonically non-decreasing. |
| positive duration | Every `duration_s` is greater than 0. |
| throughput range | Every `throughput_kbps` is greater than or equal to 0. |
| outage support | `throughput_kbps = 0` is accepted as an outage/no-delivery interval. |
| invalid missing throughput | Missing throughput is rejected unless a converter policy explicitly handles it before normalization. |
| optional columns | Optional context columns are accepted but not required. |
| controller isolation | Runner tests must prove controllers do not receive future samples or optional context fields directly. |
| manifest consistency | Trace manifest statistics match the normalized file. |

## Minimal Synthetic Test Fixtures

Future implementation may define tiny synthetic fixtures only if explicitly authorized by a later block.

Required shapes:

- `constant_high`
- `constant_low`
- `step_down`
- `step_up`
- `oscillating`
- `zero_gap`
- invalid negative throughput;
- invalid zero or negative duration;
- invalid decreasing timestamp.

Synthetic traces are schema and runner fixtures only. They are not benchmark evidence and do not define final QoE/reward.

## Implementation Gate

Replay implementation should not begin until future tests cover:

1. schema validation;
2. unit conversion;
3. manifest consistency;
4. split manifest uniqueness;
5. no future-sample exposure to controllers;
6. no optional context dependency for Phase 2 baselines.

## Phase 3.2C Local Acquisition Update

The next implementation block should be Phase 3.3A synthetic trace fixtures and schema validation.

Phase 3.3A should validate the schema using tiny synthetic fixtures before any real HSDPA, Ghent or Lancaster raw files are normalized.

Real acquired raw datasets are not test fixtures and must not be committed. Tests must use `unittest`, not `pytest`.

## Phase 3.3A Synthetic Validation Update

The first acceptance-test layer is implemented in `tests/test_trace_schema_validation.py`.

It covers valid traces, zero-throughput outage samples, missing columns, nonnumeric values, negative throughput, zero and negative durations, decreasing and negative timestamps, `NaN`, infinity, empty CSVs, optional columns, summary statistics and deterministic repeated validation.

Synthetic CSV files are created inside `tempfile.TemporaryDirectory` and are not committed.

## Phase 3.3B TraceLoader Update

`tests/test_trace_loader.py` adds loader acceptance coverage using temporary synthetic CSVs only.

Coverage includes row/CSV loading, trace id derivation, metadata preservation, row ordering, stats delegation, strict/non-strict invalid behavior, missing required columns, missing files, and no committed CSV fixtures.

## Phase 3.4B Network Model Update

`tests/test_trace_network_model.py` adds acceptance coverage for the first environment timing model.

Coverage includes constant throughput, zero-throughput intervals, gaps, non-zero starts, exhaustion, bounded looping, all-zero traces, invalid inputs, measured throughput consistency, adapter clock behavior and temporary CSV loading through TraceLoader.

This still does not prove controller behavior, runtime replay correctness, final QoE/reward or benchmark ranking.
