# Leakage Prevention Policy

Leakage occurs when information from validation, test or OOD data influences implementation, parameter selection or interpretation before the final evaluation. This policy applies to future Phase 3 and later work.

## Leakage Types

| leakage type | example | prevention |
| --- | --- | --- |
| Trace reuse leakage | Same route/session appears in train and test. | Split by trace/session/source identity. |
| Parameter leakage | Controller thresholds adjusted after inspecting test results. | Freeze parameters before test execution. |
| Scenario leakage | Test scenarios are repeatedly used as development fixtures. | Use synthetic development traces and reserve real test traces. |
| OOD leakage | OOD traces guide parameter changes. | Run OOD after choices are frozen. |
| Metadata leakage | Context fields unavailable to controllers influence adaptation logic. | Keep context fields out of controller inputs unless later explicitly approved. |
| Artifact leakage | Generated CSV/logs from test runs are used as training data. | Separate artifact folders and label split provenance. |
| Manual inspection leakage | Human review of test traces changes selection policy. | Document all inspection before split freeze. |

## Controls

1. Create dataset cards before download or conversion.
2. Record split assignment before benchmark execution.
3. Use synthetic traces for runner development.
4. Freeze controller parameters before final test and OOD runs.
5. Keep raw traces and generated artifacts outside git.
6. Record checksums or stable external identifiers for selected traces.
7. Label every run artifact with dataset ID, trace ID, split, method and commit.
8. Do not redefine metrics after seeing comparative results.

## Phase 3.1 Boundary

Because Phase 3.1 downloads no datasets and runs no benchmark, there is no experimental leakage yet. The risk begins when later phases inspect, convert, tune or execute trace-driven runs.

## Phase 3.2A Source-Triage Update

### New Leakage Risks Recognized

- Sliding-window leakage: windows from the same original trace must not cross train/validation/test/OOD boundaries.
- Route leakage: repeated commute routes must be grouped.
- Service/day leakage: Lancaster traces from a single service/day require careful grouping.
- Operator/device/app leakage: Raca 4G/5G must be grouped by available metadata.
- Trajectory leakage: Lumos5G repeated passes over same locations/trajectories must not be split naively.
- Causal trace leakage: Puffer/log-derived traces may reflect choices of deployed ABR algorithms and are not automatically exogenous capacity traces.

### Required Policy

Every dataset conversion plan must produce a manifest with:

- source dataset id;
- original file id;
- route/session/day/operator/app metadata when available;
- split assignment;
- reason for split assignment;
- conversion version;
- unit normalization.

## Phase 3.2B Schema Update

`trace_manifest_v1` and `split_manifest_v1` make leakage controls explicit.

Required additions:

- every trace has a `leakage_group`;
- every split entry records `trace_id`, `dataset_id`, `source_file`, `domain_label` and reason;
- optional context/KPI fields may be preserved but must not become baseline-controller inputs;
- runner tests must ensure controllers never receive future trace samples directly.

Phase 3.2B does not create final split files or inspect real traces.

## Phase 3.2C Local Acquisition Update

Acquired raw files introduce concrete grouping concerns:

- HSDPA route folders require route/report-level leakage grouping.
- Ghent mobility-mode archives require grouping by original archive, trace and mode.
- Lancaster archive contents require grouping by original trace and any service/day metadata discovered later.

The local acquisition audit does not create split manifests. No acquired raw file may be windowed or assigned to train/validation/test/OOD before a split policy is produced.

## Phase 3.3A Synthetic Validation Update

The validator reduces malformed-input risk but does not solve split leakage by itself.

Important boundary: tests use synthetic temporary CSVs only and do not inspect real raw HSDPA, Ghent or Lancaster files. This avoids accidental leakage from real traces into development fixtures.

## Phase 3.3B TraceLoader Update

`LoadedTrace` can contain all samples, but that object is intended for the replay environment, not controllers.

Future runner code must enforce observation timing so controllers cannot inspect future samples. The loader itself does not implement any controller-facing API.

## Phase 3.4C Controlled Dry-Run Update

The dry-run harness enforces the first controller-facing anti-leakage boundary.

Allowed controller inputs are limited to current client/controller feedback such as buffer level, previous measured download rate, previous level, segment duration, downloaded bytes and the representation ladder.

Forbidden controller inputs include complete traces, `LoadedTrace`, sample arrays, future samples, future throughput, raw optional trace metadata, split labels, domain labels, OOD labels and leakage groups.

Dry-run artifacts are marked `do_not_use_for_eval` and `no_final_ranking = true` so they cannot become accidental benchmark, tuning or final-report inputs.

## Phase 3.4D Mahimahi/tc Decision Update

External-emulator leakage risk is now explicitly bounded.

Controls:

- Mahimahi/tc probes are local/audit-only and outside-repo;
- failed probes cannot force method changes before Phase 3.5;
- external validation outputs must not be used to tune controllers unless a later split and tuning policy allows it;
- Mahimahi/tc outputs must not be mixed with Python dry-run outputs as equivalent benchmark rows;
- controller ranking remains prohibited until final metrics and split rules are closed.
