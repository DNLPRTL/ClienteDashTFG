# Replay Runner Requirements

This file defines requirements for a future trace-driven runner. It does not implement that runner.

## Required Properties

| property | requirement |
| --- | --- |
| Determinism | Same controller, trace, config and commit should produce the same future run artifacts. |
| Controller neutrality | Runner must not require controller-specific code paths. |
| Unit clarity | Trace input units must be explicit and converted before execution. |
| Time model clarity | Runner must document how trace time maps to segment download time. |
| Synthetic-first validation | Runner must pass synthetic trace tests before real trace use. |
| Artifact manifest | Future runs must record controller, trace ID, commit, config and method. |
| Repository hygiene | Raw traces, logs, CSVs, ZIPs and media stay outside git. |
| Python compatibility | Future code must remain compatible with the project Python version policy. |

## Candidate Normalized Trace Schema

The Phase 3.1/3.2A draft below is superseded by the Phase 3.2B decision in `../common_trace_schema.md`.

| field | meaning |
| --- | --- |
| `trace_id` | Stable external or local identifier. |
| `sample_time_s` | Monotonic seconds from trace start. |
| `throughput_bps` | Available throughput in bits per second. |
| `source_dataset` | Dataset ID from `../trace_dataset_matrix.md`. |
| `split` | train, validation, test, OOD or synthetic. |
| `notes` | Optional non-controller metadata. |

## Forbidden Shortcuts

- Do not infer final QoE/reward in the runner.
- Do not pass GPS, RSRP, RSRQ, SINR or other context fields into existing controllers.
- Do not change parser, downloader, buffer, player or media engines to fit a dataset.
- Do not write generated artifacts into tracked documentation folders.
- Do not use `pytest` for this project.

## Future Acceptance Evidence

Before real traces are used, a future runner should have:

1. unit tests based on synthetic traces;
2. deterministic output checks;
3. schema validation checks;
4. artifact manifest checks;
5. documentation of unsupported trace features;
6. client readiness check passing in strict mode.

## Phase 3.2A Source-Triage Update

The future runner must not be implemented in this block. Requirements now fixed:

- accept an internal trace schema rather than raw dataset formats;
- support deterministic synthetic traces;
- emit canonical run artifacts;
- record trace id, source dataset id, converter version and split label;
- run with `unittest` without external network;
- avoid requiring root/admin privileges;
- keep Mahimahi/netem behind optional runbooks;
- separate trace replay from final QoE/reward calculation until Phase 3.5.

## Phase 3.2B Schema Update

The active runner input contract is now `normalized_trace_schema_v1`.

Required columns:

| column | unit | requirement |
| --- | --- | --- |
| `timestamp_s` | seconds | Numeric seconds from trace start; monotonically non-decreasing. |
| `duration_s` | seconds | Numeric interval duration; strictly positive. |
| `throughput_kbps` | kbps | Numeric available/application-level downlink throughput; greater than or equal to 0. |

Future runner requirements:

- consume normalized traces rather than raw dataset formats;
- use `trace_manifest_v1` to record provenance and statistics;
- use `split_manifest_v1` to prevent leakage;
- never expose future trace samples directly to controllers;
- never require optional context/KPI columns for Phase 2 baseline controllers;
- keep final QoE/reward outside runner scope until Phase 3.5.

## Phase 3.2C Local Acquisition Update

Local raw acquisition does not authorize runner implementation.

Before replay runner implementation:

1. Phase 3.2C documentation must close;
2. Phase 3.3A must validate schema behavior with synthetic fixtures;
3. converter or loader boundaries must be documented separately;
4. no future-sample leakage must be covered by tests;
5. final QoE/reward must remain deferred to Phase 3.5.

The acquired HSDPA, Ghent and Lancaster files are raw candidates only. The future runner must consume normalized traces, not raw logs or archives.

## Phase 3.3A Synthetic Validation Update

The future runner now has a concrete precondition: it must only consume traces that pass `validate_normalized_trace_csv` or equivalent row validation.

This does not implement the runner. It adds a schema gate that future runner work must call or preserve.

## Phase 3.3B TraceLoader Update

The future runner may consume `LoadedTrace`, but `LoadedTrace` is not a controller-facing API.

Runner requirements now include:

- accept only loaded normalized traces or equivalent validated rows;
- reveal only time-appropriate observations to controllers;
- never pass `LoadedTrace.samples` or future throughput values directly to controllers;
- preserve row order from the normalized trace.

## Phase 3.4B Network Model Update

`TraceDrivenNetworkModel` implements the deterministic network timing core that a future runner can use, but it is not the runner itself.

Additional runner requirements now include:

- consume network-model results as environment timing, not as controller input;
- keep controllers isolated from complete traces and future samples;
- decide later how `SegmentDownloadResult` maps into player/runtime events;
- keep final QoE/reward in Phase 3.5;
- keep Mahimahi and `tc/netem` as later optional validation/runbook paths.

## Phase 3.4C Controlled Dry-Run Update

The first controller-facing runner boundary is a controlled dry-run harness, not a benchmark runner.

Additional requirements now enforced:

- build controller feedback from observed state only;
- call existing controllers through the public registry/contract adapter;
- reject future-looking feedback keys such as complete traces, future samples, raw metadata, split labels and OOD labels;
- write artifacts only to an explicit output directory;
- label every artifact as `phase3_4c_dry_run`, `outputs_are_benchmark_results = false`, `final_qoe_reward_defined = false`, `row_eval_gate = do_not_use_for_eval` and `no_final_ranking = true`;
- keep generated dry-run outputs outside git.

## Phase 3.4D Mahimahi/tc Decision Update

Runner requirements now treat external emulation as optional validation, not as a prerequisite:

- the Python trace-driven pipeline remains the primary Phase 3.5 path;
- Mahimahi is a secondary Ubuntu-only validation/runbook candidate;
- Linux `tc/netem` is a fallback/sanity/runbook candidate;
- environment probes are local/audit-only and outside-repo;
- probe failures do not block Phase 3.5;
- Mahimahi/tc outputs must not be mixed with Python dry-run outputs as equivalent benchmark results;
- final QoE/reward and ranking remain deferred.
