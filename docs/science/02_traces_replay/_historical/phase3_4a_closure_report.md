# Phase 3.4A Closure Report

## Closed

Phase 3.4A implements dataset converters for:

- `hsdpa_norway_mmsys2013`
- `ghent_4g_lte_bandwidth_logs`
- `lancaster_abr_throughput_traces`

The implementation adds:

- converter dataclasses and `ConversionError`;
- shared deterministic discovery, ZIP text-source handling, parsing, CSV writing, manifest writing, checksum and validation helpers;
- dataset-specific converters;
- `convert_dataset(...)` dispatcher;
- CLI script `scripts/convert_trace_dataset.py`;
- synthetic-only `unittest` coverage using temporary directories.

Each converted CSV is validated against `normalized_trace_schema_v1`. Each converted trace receives a local `trace_manifest_v1` JSON with checksum, counts, duration, throughput statistics, scenario tags, mobility tags, network tags, leakage group and `split_candidate = conversion_only_no_final_split`.

## Conversion Assumptions

HSDPA Norway supports the six-column interval-byte shape and conservative two-column cumulative timestamp/byte pairs. Ghent 4G/LTE uses the audited six-column interval-byte shape and preserves GPS plus mobility labels inferred from path names. Lancaster treats one-value lines as 1.0 s `throughput_kbps` samples and two-column lines as `timestamp_s throughput_kbps` with adjacent timestamp duration inference.

## Still Not Closed

Phase 3.4A does not define or implement:

- replay runner;
- DashClientModular4 runtime trace integration;
- player, controller or media-engine changes;
- final QoE/reward;
- benchmark ranking;
- final train/validation/test/OOD split;
- Mahimahi execution;
- Linux `tc/netem` execution;
- IA/RL.

Normalized real traces and generated manifests remain local artifacts outside the repository. They are not benchmark results and must not be committed.

## Residual Risks

- HSDPA raw logs need local smoke confirmation because the Phase 3.4A audit did not include representative `.log` data rows.
- Lancaster two-column durations are inferred from adjacent timestamps, so irregular gaps preserve irregular durations.
- Converter correctness depends on raw-unit assumptions recorded in the dataset docs and manifests.
- Future runner code must still prevent future-sample exposure to controllers.

## Validation

Validation for this phase is synthetic and standard-library only. Tests create raw inputs with `tempfile.TemporaryDirectory()` and do not add persistent CSV fixtures.
