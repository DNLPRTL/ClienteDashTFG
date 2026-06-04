# Phase 6C Normalization Contract

Status: Phase 6C normalization contract. Normalized CSVs are external artifacts.

Phase 6C converts acquired/extracted public traces into:

```text
normalized_trace_schema_v1
```

Output location:

```text
<external_root>/normalized/<dataset_family>/<trace_id>.csv
<external_root>/manifests/per_trace/<dataset_family>/<trace_id>.json
```

These files are not committed.

## Phase 6C-H1 Operational Bounds

The normalizer is source-filtered and bounded for live materialization:

- default source selection is `primary`, meaning Raca 4G LTE and Raca 5G only;
- Lumos5G is included only with `--include-lumos` or an explicit source list;
- Ghent and HSDPA are included only with `--include-diagnostic`, `--sources all` or an explicit source list;
- Lancaster remains excluded;
- candidate input scanning is limited to selected `extracted/<source_id>/` and `raw/<source_id>/` trees;
- `archives/`, `normalized/`, `manifests/`, `reports/`, `receipts/` and `logs/` are not candidate input roots;
- delimiter/header sniffing uses bounded byte samples instead of full-file reads;
- binary, media, archive, HTML and unsupported files are skipped quickly;
- `--max-files-per-source`, `--max-file-size-mb`, `--max-sniff-bytes` and `--progress-every` bound and expose work.

The normalizer prints source start/end summaries and writes `reports/phase6c_normalization_progress.json` during the run. If a live run is interrupted, rerun the orchestrator with `--resume --skip-existing --clean-derived` so selected-source derived outputs are rebuilt without redownloading archives.

## Required Columns

Normalized CSVs contain:

- `timestamp_s`
- `duration_s`
- `throughput_kbps`

Optional preserved columns:

- `latitude`
- `longitude`
- `mobility_tag`
- `source_dataset`
- `source_file`

Optional context columns are metadata/context only. They are not controller features and are not benchmark claims.

## Validity Rules

- `duration_s` must be positive.
- `throughput_kbps` must be non-negative.
- Empty or invalid traces are excluded with an `exclusion_reason`.
- Throughput is never invented.

## Normalizers

Ghent and HSDPA six-column whitespace logs are parsed as:

```text
timestamp_or_timestamp_ms elapsed_ms latitude longitude bytes_received_since_previous milliseconds_since_previous
```

Throughput is:

```text
throughput_kbps = bytes_received_since_previous * 8 / milliseconds_since_previous
```

Raca 4G, Raca 5G and Lumos5G use robust CSV/TSV detection. The normalizer searches for throughput aliases such as `throughput_mbps`, `dl_throughput_kbps`, `download_bitrate_mbps`, `speed_mbps`, `bitrate_mbps` and related variants. Mbps and bps units are converted to kbps.

If only bytes and elapsed milliseconds are available, the normalizer uses the same bytes/time formula. If no throughput or bytes/time identity can be detected, the file is excluded with:

```text
unable_to_detect_throughput_column
```

## Fingerprints

Each normalized trace gets two separate identities:

- `checksum_sha256`: SHA-256 over the normalized CSV bytes.
- `canonical_content_fingerprint`: SHA-256 over normalized semantic rows only: `timestamp_s`, `duration_s`, `throughput_kbps`.

`canonical_content_fingerprint` is designed to detect the same trace content even when source paths, archive layout or optional context columns differ.

`trace_id` is deterministic:

```text
<dataset_family>_<canonical_content_fingerprint_prefix>
```

`leakage_group` is deterministic from dataset family and canonical content identity.

## Boundary

Normalization does not run the client, controllers, QoE computation or benchmarks. Normalized CSVs are preparation artifacts for future evaluation phases, not results.
