# Phase 4E.1 defense talking points

- Phase 4E.1 extends the existing offline pipeline to consume Phase 3 normalized external trace CSVs.
- It still does not register a neural ABR controller and does not touch player, runtime, downloader, parser, media engine or classical controllers.
- The input schema remains `normalized_trace_schema_v1` with required `timestamp_s`, `duration_s` and `throughput_kbps`.
- Matching trace manifests preserve provenance such as `trace_id`, `dataset_id`, `leakage_group`, throughput stats, tags, converter and checksum metadata.
- If a manifest is missing, the code creates conservative metadata with `manifest_missing=true`; this is covered by unit tests.
- Splitting uses `phase4e1_trace_level_regime_v1`: split by `leakage_group` if present, otherwise by `trace_id`.
- No row-level random split is used. Validation checks both trace ID and leakage group disjointness.
- OOD diagnostic traces are marked as not for tuning.
- Normalization remains train-only through the existing Phase 4D normalizer.
- Teacher labels are generated offline by the `robust_mpc` teacher over a fixed 5-level ladder: 300, 750, 1200, 1850 and 2850 kbps.
- Model inputs do not include trace ID, split, source dataset, teacher action, teacher reward, future throughput or future download time.
- The smoke passed dataset build, validation, CPU training, offline validation, unit tests and strict readiness.
- The smoke is diagnostic-only. It is not a benchmark, ranking, real-world validation or Phase 4F export decision.
