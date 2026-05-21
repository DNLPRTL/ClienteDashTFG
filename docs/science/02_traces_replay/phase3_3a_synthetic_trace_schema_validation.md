# Phase 3.3A Synthetic Trace Schema Validation

Phase 3.3A implements the first minimal validation layer for `normalized_trace_schema_v1` using synthetic traces only.

This block is not a replay runner, not a dataset converter, not a production TraceLoader, not a benchmark, and not an IA/RL block.

## Scope

Implementation files:

- `core/trace_replay/__init__.py`
- `core/trace_replay/schema.py`
- `core/trace_replay/validation.py`

Test file:

- `tests/test_trace_schema_validation.py`

Synthetic CSV inputs are generated inside `unittest` temporary directories. No CSV trace fixtures are committed. No real raw HSDPA, Ghent or Lancaster directories are read by tests.

## Validator API

`core.trace_replay.schema` exposes:

- `TRACE_SCHEMA_VERSION = "normalized_trace_schema_v1"`
- `REQUIRED_TRACE_COLUMNS = ("timestamp_s", "duration_s", "throughput_kbps")`
- `OPTIONAL_TRACE_COLUMNS`

`core.trace_replay.validation` exposes:

- `TraceValidationResult`
- `validate_normalized_trace_rows(rows, source="<memory>")`
- `validate_normalized_trace_csv(path)`

`TraceValidationResult` records:

- validity;
- sample count;
- total duration;
- minimum, mean and maximum throughput;
- nominal granularity when durations are uniform;
- zero-throughput presence;
- human-readable errors and warnings.

## Validation Semantics

The validator checks:

- required columns exist;
- empty traces are invalid;
- `timestamp_s`, `duration_s` and `throughput_kbps` are numeric and finite;
- `timestamp_s >= 0`;
- `timestamp_s` is monotonically non-decreasing;
- `duration_s > 0`;
- `throughput_kbps >= 0`;
- `throughput_kbps = 0` is valid outage/no-delivery evidence;
- `NaN` and infinity are rejected;
- extra optional columns are accepted and ignored.

Missing files may raise `FileNotFoundError`. Malformed trace contents return `is_valid=False` with errors.

## Test Coverage

The synthetic test suite covers:

1. valid constant-throughput trace;
2. valid variable-throughput trace with a zero-throughput outage sample;
3. missing required column;
4. non-numeric value;
5. negative throughput;
6. zero duration;
7. negative duration;
8. decreasing timestamp;
9. negative timestamp;
10. `NaN`;
11. infinity;
12. empty CSV/no rows;
13. extra optional columns accepted;
14. summary statistics for a valid trace;
15. repeated validation determinism.

Additional tests cover schema version, in-memory row validation and missing-file behavior.

## Boundaries

- HSDPA, Ghent and Lancaster remain raw local candidates outside the repository.
- No real raw dataset is read by tests.
- No dataset conversion is implemented.
- No production TraceLoader or replay runner is implemented.
- No final QoE/reward or controller ranking is defined.
- No controller, player/runtime, media engine or metric definition is changed.

## Gate Created

Phase 3.3A creates the validation gate before Phase 3.3B and Phase 3.4A. Later converter or runner work must consume this schema validation boundary rather than reading raw dataset formats directly.

