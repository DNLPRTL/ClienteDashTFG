# Trace Source To Internal Mapping

This document maps Phase 3.2A dataset/source cards to `normalized_trace_schema_v1`.

The mappings are conversion decisions for sources that now have Phase 3.4A converters, and planning decisions for later sources. They do not download data or authorize replay.

## Mapping Table

| dataset/source | source raw format if known | likely conversion input | target normalized columns | unit conversion | expected granularity | expected risks | storage risk | leakage risk | download authorized in next block |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HSDPA Norway / Riiser MMSys 2013 | plain ASCII logs | bytes/ms or equivalent per-sample throughput log | required columns plus `source_dataset`, `source_file`, `network_type`, `mobility_label`, `notes` | bytes/ms or source rate to `throughput_kbps`; time to seconds | about 1 sample/s | final-row duration, route metadata, exact source units | low | medium route leakage | yes, external-only future block after terms check |
| Ghent 4G/LTE Bandwidth Logs | logs | bytes/ms or equivalent throughput log | required columns plus `source_dataset`, `source_file`, `network_type`, `mobility_label`, `notes` | source bytes/rate to `throughput_kbps`; time to seconds | TBD, expected interval samples | mode labels, GPS/context optionality, exact units | low | medium trace/mode leakage | yes, external-only future block after terms check |
| Lancaster ABR-Throughput-Traces | throughput traces | per-trace reported throughput | required columns plus `source_dataset`, `source_file`, `network_type`, `scenario_label`, `notes` | kbps likely kept as-is after validation | TBD, 4 min traces reported | service/day grouping, repository terms, trace count | medium | medium-high service/day leakage | yes, external-only future block after terms check |
| Raca 4G LTE channel/context | KPI dataset files | throughput column plus optional KPI columns | required columns plus optional `network_type`, `operator_or_carrier`, `mobility_label`, `source_file`, `notes` | Mbit/s in paper to `throughput_kbps` | 1 sample/s | context field selection, missing KPI data, grouping | medium | medium operator/device/app leakage | no, second-wave/OOD candidate |
| Raca 5G channel/context | KPI dataset files, public GitHub noted in card | DL/UL bitrate fields and app/context metadata | required columns plus optional `network_type`, `operator_or_carrier`, `mobility_label`, `scenario_label`, `notes` | DL bitrate kbps can map directly after validation | 1 sample/s | license/schema review, app pattern separation, KPI complexity | medium | medium operator/device/app leakage | no, second-wave/OOD candidate |
| Lumos5G | throughput plus features TBD | throughput samples plus trajectory/context fields | required columns plus optional `network_type`, `latitude`, `longitude`, `mobility_label`, `source_file`, `notes` | Mbps/Gbps in paper to `throughput_kbps` | 1 sample/s | high variability, large source, repeated trajectories | medium | medium-high trajectory/location leakage | no, second-wave/OOD candidate |
| FCC Measuring Broadband America | raw releases, derived traces in prior methodology | no conversion input selected | no normalized trace in Phase 3.2B | TBD | TBD | not direct ABR trace source, conversion plan missing | high | medium-high if derived traces are reused naively | no, reference-only |
| Puffer data archive | daily raw/archive logs | no conversion input selected | no normalized trace in Phase 3.2B | chunk/log-derived fields would need causal plan | chunk/session | achieved-throughput bias, storage, schema complexity | high | high causal/log-derived leakage | no, metadata-only |

## Shared Target Columns

Every converted real trace must at least produce:

- `timestamp_s`
- `duration_s`
- `throughput_kbps`

Converters may preserve optional columns when available, but future Phase 3 runner behavior must only require the three mandatory columns.

## Download Meaning

`yes` in the final column means a future block may authorize external download outside the repository. It does not authorize any download in Phase 3.2B and never authorizes committing data to git.

## Phase 3.2C Local Acquisition Update

The audit changes the first three rows from future external candidates to local raw candidates outside the repository:

| dataset/source | local raw status | immediate mapping consequence |
| --- | --- | --- |
| HSDPA Norway / Riiser MMSys 2013 | acquired outside repo | Ready for later raw inspection and converter design after synthetic schema validation. |
| Ghent 4G/LTE Bandwidth Logs | acquired outside repo | Archive contents must be inspected outside repo before converter design. |
| Lancaster ABR-Throughput-Traces | acquired outside repo | Archive/README must be inspected outside repo before converter design. |

No normalized columns are produced in Phase 3.2C. No raw file is copied into the repository.

## Phase 3.3A Synthetic Validation Update

Source-to-internal mapping remains documentation only. The validator checks already-normalized rows; it does not map HSDPA, Ghent, Lancaster, Raca, Lumos5G, FCC or Puffer raw formats.

Future converters must map source data into the required columns before validation.

## Phase 3.3B TraceLoader Update

The loader starts after source-to-internal mapping is complete. It does not inspect source-specific HSDPA, Ghent, Lancaster, Raca, Lumos5G, FCC or Puffer formats.

Phase 3.4A remains responsible for converter implementation.

## Phase 3.4A Raw-To-Normalized Assumptions

| dataset/source | Phase 3.4A converter assumption | emitted metadata | unresolved risk |
| --- | --- | --- | --- |
| HSDPA Norway / Riiser MMSys 2013 | Supports six-column interval-byte rows: `absolute_timestamp_ms elapsed_ms latitude longitude bytes interval_ms`. Also supports conservative two-column cumulative timestamp/byte pairs when bytes are non-decreasing. | `source_timestamp`, `latitude`, `longitude`, `mobility_label`, `network_type=HSDPA`, `scenario_label`, `source_dataset`, `source_file`, `notes`. | Representative local `.log` rows still need smoke confirmation because the audit sample showed index HTML but not data lines. |
| Ghent 4G/LTE Bandwidth Logs | Uses audited six-column interval-byte rows: `absolute_timestamp_ms elapsed_ms latitude longitude bytes interval_ms`. Throughput is `bytes * 8 / interval_ms`. | `source_timestamp`, `latitude`, `longitude`, mobility inferred from path/file/archive name, `network_type=LTE`, `scenario_label`, `source_dataset`, `source_file`, `notes`. | Duplicate files can exist across expanded archives and aggregate archives; trace ids include source path hash to stay stable. |
| Lancaster ABR-Throughput-Traces | One numeric value per line is interpreted as 1.0 s `throughput_kbps`. Two numeric columns are interpreted as `timestamp_s throughput_kbps`; durations come from adjacent timestamps and the last row uses the previous positive delta or 1.0 s. | `scenario_label`, `source_dataset`, `source_file`, `notes`. | Two-column irregular gaps are preserved as irregular durations; final-row duration remains inferred. |

All generated real CSVs and manifests remain outside the repository. These outputs are not final split inputs or benchmark results until later phases define replay, split and evaluation policy.
