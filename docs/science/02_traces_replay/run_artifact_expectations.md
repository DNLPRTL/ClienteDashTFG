# Run Artifact Expectations

This document defines expected future artifacts. Phase 3.1 creates none of them.

## Future Artifact Types

| artifact | purpose | git policy |
| --- | --- | --- |
| run manifest | Record commit, controller, trace, split, config and method. | Generated; do not commit unless manually summarized. |
| normalized trace copy | Immutable input used for a run. | Keep outside repo. |
| telemetry CSV | Per-segment or per-event measurements. | Keep outside repo. |
| summary JSON/CSV | Aggregated run metrics. | Keep outside repo until final policy exists. |
| plots | Visual summaries. | Generated; do not commit without explicit thesis figure decision. |
| logs | Debug/runtime output. | Keep outside repo. |
| environment snapshot | Python version, OS, dependency info. | Generated; summarize manually if needed. |

## Required Manifest Fields

Future run manifests should include:

- repository commit;
- controller name;
- runner/emulator method;
- dataset ID;
- trace ID;
- split;
- trace version or checksum;
- config file path or digest;
- random seed if any;
- output directory;
- timestamp;
- metric definition version once metrics are finalized.

## Repository Hygiene

Do not commit:

- raw datasets;
- PDFs;
- generated logs;
- generated CSV files;
- ZIP archives;
- media files;
- benchmark run directories;
- `.venv`, `.idea`, `__pycache__`, `.pyc`.

Manual Markdown summaries may be committed later only when they are authored documentation, not raw generated artifacts.

## Phase 3.2A Source-Triage Update

Future trace/replay runs must include at least:

- `run_manifest.json`
- `config.resolved.json`
- `environment.json`
- `run.log`
- `segment_telemetry.csv`
- `evaluation_segments.csv`
- `trace_manifest.json` or equivalent trace provenance artifact
- `split_manifest.json` or embedded split metadata

No Phase 3.2A work creates these artifacts.

## Phase 3.2B Schema Update

Future trace/replay artifacts must include schema provenance:

- normalized traces follow `normalized_trace_schema_v1`;
- trace provenance follows `trace_manifest_v1`;
- split provenance follows `split_manifest_v1`;
- run manifests should include trace id, dataset id, converter version/commit, checksum and split label.

Raw traces, normalized real traces and generated manifests remain outside the repository unless a later block explicitly converts a tiny synthetic fixture for tests.

## Phase 3.2C Local Acquisition Update

The local raw acquisition audit is not a run artifact and not a benchmark artifact.

Do not commit:

- local JSON inventories;
- raw logs;
- ZIP archives;
- normalized trace files;
- generated manifests;
- benchmark telemetry;
- plots or run summaries produced by tools.

Authored Markdown summaries such as `phase3_2c_dataset_audit_summary.md` are allowed.

## Phase 3.3A Synthetic Validation Update

Schema validation tests create temporary CSV files during test execution only. These files are not run artifacts, not benchmark artifacts and are not committed.

No generated CSVs, logs, manifests or normalized real traces are added by Phase 3.3A.

## Phase 3.3B TraceLoader Update

TraceLoader tests create temporary CSVs during test execution only. They are not run artifacts and are not committed.

Loading a CSV does not create manifests, logs, benchmark telemetry or normalized output files.

## Phase 3.4B Network Model Update

Network-model tests create no persistent artifacts. Temporary synthetic CSVs used to verify loader-to-model behavior are not run artifacts and are not committed.

`SegmentDownloadResult` is an in-memory simulation result, not a benchmark artifact. Future runner work may decide how to persist segment telemetry, but Phase 3.4B creates no run directories, logs, CSV outputs, plots or summaries.

## Phase 3.4C Controlled Dry-Run Update

Phase 3.4C introduces explicit dry-run artifacts:

- `trace_dry_run_manifest.json`;
- `trace_dry_run_segments.csv`;
- `trace_dry_run_summary.json`.

They are generated artifacts and must stay outside the repository. They must include:

- `phase = phase3_4c_dry_run`;
- `outputs_are_benchmark_results = false`;
- `final_qoe_reward_defined = false`;
- `row_eval_gate = do_not_use_for_eval`;
- `no_final_ranking = true`.

These artifacts are controlled integration evidence only. They are not final benchmark artifacts and not final QoE/reward inputs.

## Phase 3.4D Mahimahi/tc Probe Update

Mahimahi and `tc/netem` environment probes, if run later, produce local/audit-only artifacts outside the repository. They are not benchmark artifacts, not Python dry-run artifacts and not final QoE/reward evidence.

Do not commit:

- probe logs;
- command dumps;
- screenshots;
- generated summaries;
- CSVs;
- ZIPs;
- PDFs;
- media.

Future Mahimahi/tc validation artifacts must carry method-specific labels and must not be mixed with Python dry-run outputs as equivalent benchmark results.
