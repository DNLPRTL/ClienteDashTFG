# Phase 3.4A Dataset Converters

Phase 3.4A adds raw-dataset-to-`normalized_trace_schema_v1` conversion infrastructure for the first three real trace candidates:

1. `hsdpa_norway_mmsys2013`
2. `ghent_4g_lte_bandwidth_logs`
3. `lancaster_abr_throughput_traces`

This is conversion infrastructure only. It does not implement replay, connect traces to DashClientModular4 runtime, modify controllers, modify player or media-engine behavior, define final QoE/reward, rank controllers, run benchmarks, freeze final splits, execute Mahimahi or `tc/netem`, or open IA/RL work.

## Architecture

Converter code lives under `core/trace_replay/converters/`.

| module | responsibility |
| --- | --- |
| `base.py` | Shared `ConversionError`, `ConvertedTrace` and `ConversionBatchResult` types. |
| `common.py` | Stable file discovery, ZIP text-source iteration, numeric parsing helpers, normalized CSV writing, manifest writing, checksums and validation. |
| `hsdpa_norway.py` | HSDPA Norway / Riiser MMSys 2013 converter. |
| `ghent_4g.py` | Ghent 4G/LTE bandwidth-log converter. |
| `lancaster_abr.py` | Lancaster ABR throughput-trace converter. |
| `__init__.py` | `convert_dataset(...)` dispatcher for accepted dataset ids. |

The CLI wrapper is `scripts/convert_trace_dataset.py`.

All converters:

- recursively discover likely text trace files in stable order;
- support `.zip` archives when entries are practical text trace files;
- derive stable trace ids and output filenames from dataset id plus source path;
- write normalized CSVs with required columns `timestamp_s`, `duration_s`, `throughput_kbps`;
- preserve safe optional metadata such as `source_dataset`, `source_file`, `scenario_label`, `mobility_label`, `network_type`, `latitude`, `longitude` and `source_timestamp` when available;
- validate every emitted CSV with `validate_normalized_trace_csv`;
- write one local `trace_manifest_v1` JSON per converted trace;
- fail on existing outputs unless `overwrite=True` is requested.

Normalized real traces and generated manifests are local artifacts outside the repository. They are not benchmark results and must not be committed.

## API

Dataset-specific entry points:

```python
convert_hsdpa_norway(input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False)
convert_ghent_4g(input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False)
convert_lancaster_abr(input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False)
```

Dispatcher:

```python
convert_dataset(dataset_id, input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False)
```

Accepted dataset ids:

- `hsdpa_norway_mmsys2013`
- `ghent_4g_lte_bandwidth_logs`
- `lancaster_abr_throughput_traces`

## CLI

Expected local smoke-run shape:

```text
python scripts/convert_trace_dataset.py --dataset <dataset_id> --input-dir <path> --output-dir <path> --manifest-dir <path> --max-traces 5 --overwrite
```

The CLI prints dataset id, input directory, output directory, manifest directory, converted trace count, skipped input count and errors if any. It exits non-zero if no traces are converted or if converter errors occur.

## Dataset Assumptions

### HSDPA Norway / Riiser MMSys 2013

The converter supports two conservative numeric patterns:

1. Six-column interval-byte logs interpreted as:
   - absolute source timestamp in milliseconds;
   - elapsed milliseconds since trace start;
   - latitude;
   - longitude;
   - bytes delivered during the interval;
   - elapsed milliseconds represented by the interval.
2. Two-column cumulative timestamp/byte pairs when the byte column is non-decreasing.

For interval-byte rows:

```text
throughput_kbps = bytes * 8 / elapsed_ms
duration_s = elapsed_ms / 1000
timestamp_s = (elapsed_ms_since_start - first_elapsed_ms_since_start) / 1000
```

For cumulative timestamp/byte pairs, positive adjacent deltas are converted using the elapsed time between samples. Negative byte deltas and non-positive durations are ignored.

### Ghent 4G/LTE Bandwidth Logs

The audited common shape is:

```text
absolute_timestamp_ms elapsed_ms latitude longitude bytes interval_ms
```

The converter applies:

```text
throughput_kbps = bytes * 8 / interval_ms
duration_s = interval_ms / 1000
timestamp_s = (elapsed_ms - first_elapsed_ms) / 1000
```

Mobility labels are inferred from source paths when they contain `foot`, `bicycle`, `bike`, `bus`, `tram`, `train` or `car`. ZIP entries are treated as individual text sources.

### Lancaster ABR-Throughput-Traces

One numeric value per line is interpreted as `throughput_kbps` at a regular 1.0 s interval:

```text
timestamp_s = row_index
duration_s = 1.0
throughput_kbps = value
```

Two numeric columns are interpreted as:

```text
timestamp_s throughput_kbps
```

Timestamps are normalized so the first emitted sample starts at `0.0`. Each duration is inferred from the next timestamp. The last duration uses the previous positive delta, or 1.0 s if no positive delta exists.

## Boundary

Phase 3.4A still does not define final train/validation/test/OOD split, final QoE/reward, benchmark ranking, replay runner, Mahimahi execution, `tc/netem` execution, or IA/RL. The emitted CSVs are future replay inputs only after later phases approve runner and split policy.
