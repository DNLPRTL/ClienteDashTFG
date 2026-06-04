# Phase 3 Rebuild Trace Pipeline

This note records the rebuilt Phase 3 trace workflow. It is an operational contract for code and data handling, not a benchmark report.

## Scope

Phase 3 rebuild produces normalized traces, per-trace metadata and split manifests. It does not train NeuralABR-Lite, does not run final benchmark, does not rank controllers and does not claim QoE improvement.

Canonical normalized schema:

```csv
timestamp_s,duration_s,throughput_kbps
```

Controller visibility guardrail: controllers must not receive `trace_id`, `dataset_id`, `source_id`, `split`, `group_id`, `leakage_group`, OOD labels or future throughput.

## External Roots

Raw data remains read-only under:

```text
C:\Users\danie\Documents\TFG\dataset en bruto
```

Derived artifacts are external to Git:

```text
C:\Users\danie\Documents\TFG\auditorias_trazas
C:\Users\danie\Documents\TFG\datasets_normalizados
C:\Users\danie\Documents\TFG\manifests_trazas
C:\Users\danie\Documents\TFG\runs_trazas
```

## Scripts

Raw inventory:

```powershell
python scripts\audit_phase3_raw_datasets.py --hash-mode sample
```

Full hashing is available with `--hash-mode full`, but it reads the complete raw corpus.

Trace conversion:

```powershell
python scripts\convert_phase3_traces.py --datasets norway_hsdpa_umass ghent_4g_lte ucc_4g_lte_beyond_throughput ucc_5g_beyond_throughput oboe nyu_mets lumos5g fcc_measuring_broadband_america roma_4g_nbiot_5g_nsa gavist5g --max-traces-per-dataset 1
```

Puffer is implemented as a streaming `video_sent`/`video_acked` SQLite join, but the real raw files are large. Run it deliberately, not as part of a casual smoke.

Final split manifest:

```powershell
python scripts\build_phase3_trace_manifest.py
```

Splits are assigned by `leakage_group`, never by rows. The final manifest keeps `ready_for_benchmark=false` and `benchmark_authorized=false`.

## Dataset Semantics

- Norway HSDPA and Ghent LTE: `bytes_received / elapsed_ms * 8` to `throughput_kbps`.
- UCC 4G and UCC 5G: `DL_bitrate` is treated as `throughput_kbps`.
- Oboe: first column is milliseconds, second column is `throughput_kbps`.
- NYU-METS and Lumos5G: Mbps values are multiplied by 1000.
- FCC MBA: `curr_httpgetmt.csv`, `bytes_sec * 8 / 1000`, duration from `fetch_time`.
- Roma: `Current Netw. DL` is treated as `throughput_kbps`; gaps split traces.
- GAViST5G: packet `Length` is aggregated per second and marked as `observed_application_traffic`.
- Puffer: joined streaming delivery samples are marked as `real_streaming_delivery_rate`.

## Smoke Status

Windows smoke generated a sample-hash raw inventory and one normalized trace per non-Puffer dataset. The resulting external final manifest validated 10 traces with split counts:

```text
train=7, test=2, eval=1
```

Those outputs are technical smoke artifacts only.
