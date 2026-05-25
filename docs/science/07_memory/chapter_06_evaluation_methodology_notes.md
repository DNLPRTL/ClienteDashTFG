# Chapter 06 Evaluation Methodology Notes

These notes extend the pre-evaluation boundary with Phase 3 trace/replay methodology. They are not final LaTeX prose.

## Chapter Role

Chapter 6 should explain the evaluation ladder:

1. Phase 1 client readiness and output hygiene.
2. Phase 2 controller implementation and unit/fake-smoke validation.
3. Phase 3 trace, replay, emulation and dataset methodology.
4. Later final QoE/reward and benchmark ranking.

## Phase 3 Message

The key message is that a DASH ABR comparison needs controlled network conditions before performance claims are meaningful. Phase 3 therefore documents dataset provenance, replay/emulation choices, train/test/OOD boundaries, leakage prevention and future artifact expectations.

## What Phase 3.1 Adds

- Source inventory for trace/replay literature and datasets.
- Dataset selection criteria.
- Replay/emulation decision criteria.
- Mahimahi, `tc/netem` and fake-runner comparison.
- Split and OOD policy.
- Leakage prevention policy.
- Synthetic trace plan.
- Run artifact expectations.

## What Remains Deferred

- dataset downloads;
- replay implementation;
- final QoE/reward;
- benchmark ranking;
- IA/RL;
- controller/player/media/metric changes;
- GStreamer benchmark claims.

## Defense Wording

Use careful verbs: documented, scoped, classified, deferred, selected as candidate, requires carding, requires later validation.

Avoid: proved, outperformed, reproduced, optimized, trained, deployed, benchmarked.

## Phase 3.2A Source-Triage Update

Chapter 6 can now cite the Phase 3.2A card set and triage matrix as methodology evidence, not as experimental results.

New material available:

- dataset selection rationale table;
- replay/emulation method comparison table;
- threats to validity: exogenous trace assumption, log-derived trace bias, split leakage, storage risk and format risk;
- OOD/generalization policy;
- explanation that unit tests, smoke tests and fake traces are not benchmark evidence.

Important wording:

- first integration candidates: HSDPA Norway, Ghent 4G/LTE and Lancaster HAS traces;
- modern mobile/OOD candidates: Raca 4G, Raca 5G and Lumos5G;
- reference-only: FCC Measuring Broadband America;
- metadata-only: Puffer data archive;
- primary likely implementation path: custom Python trace-driven fake/replay runner, not implemented in Phase 3.2A;
- secondary validation candidate: Mahimahi;
- Linux fallback candidate: `tc/netem`;
- threats-to-validity references: CausalSim and Veritas.

## Phase 3.2B Schema Update

Chapter 6 can now introduce the common trace input contract:

- normalized traces are CSV-like time series;
- required columns are `timestamp_s`, `duration_s` and `throughput_kbps`;
- throughput is normalized to `kbps`;
- time is normalized to seconds;
- trace provenance is recorded by `trace_manifest_v1`;
- split provenance is recorded by `split_manifest_v1`;
- raw datasets, normalized datasets and local manifests are stored outside the repository;
- replay/converter implementation, final QoE/reward and benchmark ranking remain deferred.

This supports the methodological claim that the project has prepared reproducible trace inputs. It does not support a performance claim.

## Phase 3.2C Local Acquisition Update

Chapter 6 can now distinguish three states:

1. source triage and cards are closed;
2. common schema and conversion plan are closed;
3. first raw candidates are locally acquired outside the repository.

The acquired candidates are HSDPA Norway, Ghent 4G/LTE and Lancaster ABR traces. They are raw local files only. They are not normalized, not split, not replayed and not benchmark evidence.

Use this phase to explain storage hygiene and the next gate: Phase 3.3A synthetic trace fixtures and schema validation before converter or replay work.

## Phase 3.3A Synthetic Validation Update

Chapter 6 can now include a small implementation milestone: the project validates `normalized_trace_schema_v1` using synthetic traces generated in `unittest` temporary directories.

This evidence supports:

- schema boundary enforcement;
- rejection of malformed normalized traces;
- deterministic validation behavior;
- no real dataset reads during schema tests.

It does not support replay, conversion, QoE, ranking, IA/RL or real-network claims.

## Phase 3.3B TraceLoader Update

Chapter 6 can now describe the second implementation step in the trace pipeline: validated normalized rows can be loaded into `TraceSample` and `LoadedTrace` objects.

This supports typed representation of already-normalized traces, metadata preservation, strict and diagnostic non-strict loading, and row-order preservation.

It still does not support replay, conversion, client integration, final QoE/reward, ranking or IA/RL.

## Phase 3.4B Network Model Update

Chapter 6 can now describe a deterministic trace-driven network model that converts loaded normalized traces into segment download durations.

This supports:

- reproducible timing from `timestamp_s`, `duration_s` and `throughput_kbps`;
- explicit handling of zero throughput and gaps as no-delivery time;
- bounded end-of-trace behavior through fail or loop policy;
- a fake adapter clock boundary for later integration.

It still does not support ranked controller comparison, final QoE/reward, player/runtime integration, media-engine changes, Mahimahi/`tc/netem` execution or IA/RL. The methodological value is that deterministic environment behavior is established before any future IA or tuning loop can be defended.

## Phase 3.4C Controlled Dry-Run Update

Chapter 6 can now describe the first controlled controller execution loop over trace-driven timing.

This supports:

- exercising existing registered controllers without modifying them;
- using only current client/controller feedback;
- recording per-segment dry-run telemetry;
- writing artifacts explicitly marked as non-benchmark and not final QoE/reward.

It still does not support final ranked controller comparison, final reward design, player/runtime integration, Mahimahi/`tc/netem` execution, media-engine changes or IA/RL.

## Phase 3.4D Mahimahi/tc Decision Update

Chapter 6 can now close the external emulation decision for this stage:

- the Python trace-driven pipeline is the primary reproducible route into Phase 3.5;
- Mahimahi is a secondary Ubuntu-only validation/runbook candidate;
- Linux `tc/netem` is a fallback/sanity/runbook candidate;
- Phase 3.5 does not depend on either external tool being operational.

This supports a clear methodology claim, not an experimental claim. No Mahimahi or `tc/netem` benchmark was run, and no ranked controller comparison or final QoE/reward is implied.

## Phase 3.5A1 QoE/Reward Evidence Update

Chapter 6 can now cite Phase 3.5A1 as scientific evidence for later QoE/reward/gate decisions:

- the common QoE core across the distilled sources is quality utility, rebuffering/stalling and smoothness/switching;
- startup delay is relevant but measurement-dependent;
- VMAF/perceptual quality is relevant but artifact-dependent;
- user preference weights vary, so fixed weights require careful wording;
- Peroni 2024 supports avoiding an ad hoc QoE model without validation.

This does not close `qoe_selection.md`, `reward_definition.md`, secondary metrics, result schema or gate policy. It also does not support code changes, IA/RL, ranked controller comparison or a formal benchmark.

## Phase 3.5A2 QoE/Reward Contract Update

Chapter 6 can now cite Phase 3.5A2 as the documentation closure for QoE/reward semantics and evaluation gates:

- primary formula version: `qoe_linear_v1`;
- primary future session metric: `qoe_linear_mean`;
- future segment-level IA reward candidate: `reward_n` from `qoe_linear_v1`, without opening IA/training;
- sensitivity formula: `qoe_log_v1`;
- startup delay: report-only with `startup_penalty_weight = 0.0`;
- VMAF/perceptual quality: deferred and artifact-dependent;
- incomplete/non-comparable artifacts: handled by `row_eval_gate` and `session_eval_gate`, not numeric punishment;
- benchmark schema boundary: segment telemetry, run-level summary and later benchmark aggregate are separate layers.

This supports Phase 3.5B implementation of a pure QoE calculator and synthetic tests. It still does not support controller ranking, formal benchmark claims, dry-run promotion, runner integration, media-engine changes or IA/RL training.

## Phase 3.5B Pure QoE Calculator Update

Chapter 6 can now describe a small implementation milestone: the A2 formulas are materialized as a pure Python calculator with synthetic `unittest` coverage.

This supports:

- deterministic calculation of `qoe_linear_v1`;
- deterministic calculation of `qoe_log_v1` as sensitivity;
- validation of invalid inputs before scoring;
- immutable segment reward output;
- no IO, pandas, numpy, runner integration or artifact generation.

It still does not support dry-run integration, controller ranking, formal benchmark claims, player/runtime/media changes or IA/RL training.
