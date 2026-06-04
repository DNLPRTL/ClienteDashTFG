# Phase 3.3B TraceLoader For Normalized Schema V1

Phase 3.3B implements a minimal loader for already-normalized `normalized_trace_schema_v1` CSV rows and files.

This block is not a replay runner, not a converter block, not a client/runtime integration, not a benchmark, and not an IA/RL block.

## Objective

Provide a small standard-library loader that turns validated normalized trace rows into typed Python objects for future converter and replay work.

The loader accepts only `normalized_trace_schema_v1`. It does not read raw HSDPA, Ghent or Lancaster datasets, and it does not perform unit conversion, interpolation, resampling, replay timing or QoE scoring.

## Scope

Implementation files:

- `core/trace_replay/loader.py`
- updated `core/trace_replay/__init__.py`

Test file:

- `tests/test_trace_loader.py`

Tests generate tiny CSV files inside `unittest` temporary directories. No CSV fixtures are committed.

## API

`core.trace_replay.loader` exposes:

- `TraceSample`
- `LoadedTrace`
- `TraceLoadError`
- `load_normalized_trace_rows(rows, trace_id="<memory>", source="<memory>", strict=True)`
- `load_normalized_trace_csv(path, trace_id=None, source=None, strict=True)`

`TraceSample` fields:

- `timestamp_s`
- `duration_s`
- `throughput_kbps`
- `metadata`

`LoadedTrace` fields:

- `trace_id`
- `source`
- `schema_version`
- `samples`
- `validation`

`LoadedTrace` also exposes `sample_count`, duration and throughput statistic properties, `has_zero_throughput`, and `iter_samples()`.

## Relationship To Validator

The loader reuses Phase 3.3A validation:

- row loading calls `validate_normalized_trace_rows`;
- CSV loading calls `validate_normalized_trace_csv`;
- `strict=True` raises `TraceLoadError` for invalid normalized traces;
- `strict=False` can return `LoadedTrace` with invalid validation only when required fields are structurally loadable.

Missing required columns raise `TraceLoadError` even with `strict=False`.

## Relationship To Future Converters

Converters are future work. They must produce `normalized_trace_schema_v1` rows before using this loader.

The loader does not:

- convert units;
- inspect raw dataset formats;
- read raw local dataset directories;
- infer timestamps;
- infer durations;
- normalize throughput.

## Relationship To Future Replay Runner

The loader may hold the full normalized trace for a future replay environment. It must not become a controller-facing API.

The future replay/network model may consume `LoadedTrace`, but it must reveal only observations that a real client would have at that moment. Controllers must not receive future samples directly.

## Tests

The test suite covers:

- valid in-memory rows;
- valid CSV rows;
- CSV trace id derivation from file stem;
- explicit trace id and source preservation;
- optional and unknown metadata preservation;
- row order preservation;
- statistic delegation to validation results;
- ordered sample iteration;
- strict and non-strict invalid loading;
- missing required columns;
- missing-file behavior;
- no real dataset paths;
- no committed CSV fixtures.

## Non-Goals

- no real datasets;
- no converters;
- no replay runner;
- no client/player/runtime integration;
- no controller changes;
- no media engine changes;
- no metric definition changes;
- no final QoE/reward;
- no benchmark/ranking;
- no Mahimahi/tc integration;
- no IA/RL;
- no committed CSV fixtures;
- no datasets, PDFs, ZIPs, logs, media or generated artifacts.
