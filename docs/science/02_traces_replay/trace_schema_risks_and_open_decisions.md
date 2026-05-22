# Trace Schema Risks And Open Decisions

This document records risks that remain after defining `normalized_trace_schema_v1`.

## Risks

| risk | impact | mitigation |
| --- | --- | --- |
| Source unit ambiguity | Wrong throughput conversion can invalidate all later results. | Require dataset-specific converter notes and manifest fields. |
| Inferred duration ambiguity | Last-row or irregular sampling duration may be unclear. | Document per-dataset duration policy before conversion. |
| Achieved-throughput bias | Logs may reflect decisions made by a deployed ABR algorithm. | Treat Puffer and similar logs as causal-risk sources until a causal plan exists. |
| Future-sample leakage | A runner could accidentally let controllers see future throughput. | Acceptance tests must check controller signal boundaries. |
| Context leakage | KPI/location/app metadata could leak into baseline controller decisions. | Preserve optional context only as metadata unless later approved for IA. |
| Split leakage | Windows from the same route/session/day could cross splits. | Use `leakage_group` in trace and split manifests. |
| Storage creep | Real traces or generated manifests could enter git. | Keep raw, normalized and generated manifest files outside the repository. |
| Benchmark overclaiming | Schema validation could be mistaken for performance evidence. | Keep QoE/reward and ranking deferred to Phase 3.5 and later. |

## Open Decisions

- Final synthetic fixture storage policy.
- Dataset-specific rules for irregular sampling and final-row duration.
- Whether Lancaster traces should be grouped by service/day, trace source or another metadata field.
- Whether Raca 4G/5G context fields should be retained verbatim or reduced to safe labels.
- Whether Lumos5G trajectory metadata is sufficient for OOD grouping.
- Whether any external Mahimahi or `tc/netem` validation is needed after the Python runner exists.
- Final QoE/reward, explicitly deferred to Phase 3.5.
- Final IA/RL method choices, explicitly deferred.

## Closure Requirement

These risks must be revisited before:

- converter implementation;
- replay runner implementation;
- dataset download;
- train/validation/test/OOD split freeze;
- final QoE/reward definition;
- benchmark ranking.

## Phase 3.2C Local Acquisition Update

New risks from the acquisition audit:

| dataset | observed risk | required follow-up |
| --- | --- | --- |
| HSDPA Norway | Many route/report log files | Define route and report-level grouping before any split. |
| Ghent 4G/LTE | Mobility-mode ZIP archives | Inspect/extract outside repo and define archive handling policy. |
| Lancaster | ZIP archive plus README | Inspect archive contents and terms outside repo before conversion. |
| all acquired datasets | Raw file names include logs/ZIPs | Keep raw files outside repo and commit only authored Markdown summaries. |

Open decisions now include exact archive inspection procedure, converter implementation order and whether any raw source pages should be represented only by dataset-card prose.

## Phase 3.3A Synthetic Validation Update

Closed risk:

- basic schema validation now rejects malformed normalized traces before converter or replay work.

Remaining risks:

- validator does not inspect real raw datasets;
- validator does not convert source units;
- validator does not prove replay correctness;
- validator does not prevent all future leakage unless later converter and runner code preserve the same boundaries.

Open decision: decide whether Phase 3.3B adds converter preflight logic or additional manifest validation before any real dataset normalization.

## Phase 3.3B TraceLoader Update

Closed risk:

- normalized rows can now be loaded into typed objects after validation.

Remaining risks:

- the loader can hold a full trace for a future replay environment, so future runner code must prevent future-sample exposure to controllers;
- the loader does not validate manifests or split manifests;
- the loader does not prove converter correctness;
- non-strict loading must remain a diagnostic path, not benchmark input.

## Phase 3.4A Dataset Converter Update

Closed risks:

- converter implementation paths and synthetic-only tests are now defined for HSDPA Norway, Ghent 4G/LTE and Lancaster;
- emitted converter CSVs are validated with `validate_normalized_trace_csv`;
- local manifests include checksum, statistics, tags, leakage group and `split_candidate = conversion_only_no_final_split`;
- ZIP text-source handling is covered by synthetic tests.

Remaining risks:

| risk | status after Phase 3.4A | mitigation |
| --- | --- | --- |
| HSDPA raw-format uncertainty | Still open because the audit did not show representative HSDPA `.log` data rows. | Run local smoke outside repo and inspect skipped/error counts before treating outputs as usable replay candidates. |
| Lancaster final-row duration | Still inferred from previous positive delta or 1.0 s. | Keep assumption in manifest notes and revisit before final benchmark. |
| Duplicate archive/plain inputs | Managed by stable source-path-derived trace ids, but duplicates may still represent the same measurement. | Use `leakage_group` and later split review to avoid duplicate leakage. |
| Benchmark overclaiming | Still open. Converter outputs are not QoE evidence. | Keep docs and manifests marked `conversion_only_no_final_split`. |

Phase 3.4A still does not define final QoE/reward, replay runner, benchmark ranking, final split, Mahimahi or `tc/netem` execution, controller changes, runtime changes or IA/RL.
