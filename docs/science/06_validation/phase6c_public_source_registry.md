# Phase 6C Public Source Registry

Status: committed metadata contract. No downloaded data is stored in Git.

The source registry is:

```text
configs/phase6/phase6c_public_sources.json
```

It is a small committed metadata file. It contains source IDs, public URLs, roles, default splits/gates, citation hints and expected hashes when known. It does not contain local machine paths, downloaded artifacts, normalized CSVs, real manifests, logs, zips, media or model bundles.

## Source Decisions

| Source ID | Role | Default split | Default gate |
| --- | --- | --- | --- |
| `raca_4g_lte` | Primary OOD candidate | `ood_final` | `use_for_eval` after acquisition, normalization and clean audit |
| `raca_5g` | Primary OOD candidate | `ood_final` | `use_for_eval` after acquisition, normalization and clean audit |
| `lumos5g` | Optional OOD candidate | `ood_final` | `use_for_eval` only if automatic acquisition, normalization and audit pass |
| `ghent_4g_lte` | Same-family diagnostic | `same_family_candidate` | `diagnostic_only` |
| `hsdpa_norway` | Same-family diagnostic | `same_family_candidate` | `diagnostic_only` |
| `lancaster_abr_throughput_traces` | Excluded pending source note and clean audit | `excluded` | `do_not_use_for_eval` |

## Source Notes

Raca 4G LTE uses Zenodo record 1219679 and `LTE_Dataset.zip`; the registry includes the expected md5:

```text
27da16b90a94ded3511bad9682f2e166
```

Raca 5G uses the public `uccmisl/5Gdataset` archive `5G-production-dataset.zip`.

Lumos5G uses a Google Drive file ID. The downloader implements best-effort confirmation-token handling. If Google Drive blocks with captcha, auth or rate limiting, Phase 6C records `blocked_by_provider_or_manual_confirmation_required` instead of inventing data. The pipeline fails on Lumos only when `--require-lumos` is passed.

Ghent defaults to `logs_all.zip` only. Do not combine `logs_all` and per-mobility archives unless a future explicit option deduplicates them by checksum/fingerprint before split.

HSDPA Norway is acquired by recursively scraping simple directory listings for `report.*` files.

Lancaster is not downloaded or normalized by Phase 6C automation and must not appear as `use_for_eval`.

## Benchmark Boundary

The source registry is not benchmark evidence. It does not authorize benchmark execution, result tables, plots, rankings, winner declarations or QoE improvement claims.
