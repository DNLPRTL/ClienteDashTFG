# Phase 4E.2 trace corpus requirements

## Allowed sources

```text
Phase 3 normalized external trace CSVs
Phase 3 external manifests
Phase 3 expanded raw external trace candidates if safely parseable
```

## Prohibited sources

```text
Phase 3 dry-run outputs
player/runtime logs
benchmark outputs
QoE smoke outputs
any test/future benchmark data
```

## Required normalized schema

```text
timestamp_s,duration_s,throughput_kbps
```

## Required manifest fields

```text
trace_id
dataset_id
leakage_group
sample_count
source_kind
converter
mean_throughput_kbps
min_throughput_kbps
max_throughput_kbps
coefficient_of_variation
regime_bucket
checksum_or_source_fingerprint
```
