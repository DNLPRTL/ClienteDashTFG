# Phase 3 Defense Talking Points

## Core Position

Phase 3 exists because implemented ABR controllers cannot be compared scientifically without reproducible network conditions. The project therefore documents trace discovery, dataset selection, replay/emulation decisions and leakage controls before running benchmarks.

## Strong Answers

- The Phase 2 controllers are already implemented and validated as code, but not ranked.
- Phase 3 keeps controllers frozen and focuses on the environment around them.
- No dataset is downloaded into the repository; the project records provenance and selection criteria first.
- Puffer is valuable for methodology and statistical caution, but full raw Puffer data is deferred.
- FCC Measuring Broadband America is a broadband reference, not a replay input yet.
- Norway HSDPA is mandatory to card because it is classic, small and ABR-relevant.
- Modern 4G/5G datasets are likely OOD or generalization candidates.
- Lancaster traces are promising for live/HAS realism, subject to carding and terms.
- Mahimahi is a credible method reference, while a custom fake trace-driven runner may be more practical for deterministic Python tests.

## Boundary Statements

- No final QoE/reward is defined in Phase 3.1.
- No replay runner is implemented in Phase 3.1.
- No controller, player, media engine or metric definition changes are made.
- No GStreamer benchmark is claimed.
- No IA/RL work is introduced.

## Likely Questions

| question | answer direction |
| --- | --- |
| Why not use real network tests directly? | They are hard to reproduce and confound controller behavior with uncontrolled network variation. |
| Why not use only Mahimahi? | It is credible, but may be operationally heavier than needed for deterministic local Python tests. It remains a candidate. |
| Why keep Puffer raw data deferred? | It is large and statistically subtle; Phase 3.1 only records metadata and caution. |
| How do you avoid overfitting traces? | Split policy, OOD separation, synthetic development traces and parameter freeze rules. |
| When can controllers be ranked? | Only after trace/replay methodology, final QoE/reward and result interpretation are closed. |

## Phase 3.2A Source-Triage Update

Use these talking points after the source cards are added:

- Phase 3.2A intentionally does not implement code because dataset and replay choices must be defensible first.
- The first implementation should prioritize determinism and testability through a custom Python trace-driven fake/replay runner.
- Mahimahi and `tc/netem` are considered, carded and kept as candidates, but are not forced prematurely.
- CausalSim and Veritas are included as threats-to-validity references, not implementation targets.
- Puffer warns against overclaiming from trace-driven tests because real deployment effects and causal bias matter.
- No dataset becomes final benchmark material and no final split is closed in Phase 3.2A.

## Phase 3.2B Schema Update

Use these talking points after the common schema is defined:

- The common schema uses `timestamp_s`, `duration_s` and `throughput_kbps` so every dataset must pass through the same unit boundary.
- `throughput_kbps = 0` is allowed for outage/no-delivery intervals, but missing throughput is not silently treated as zero.
- The future runner must not expose future trace samples directly to controllers.
- Raw and normalized real traces stay outside the repository.
- HSDPA, Ghent and Lancaster are conversion priorities, not final benchmark material.
- Raca 5G and Lumos5G are held as OOD candidates for future generalization work.
- Phase 3.2B prepares trace inputs; Phase 3.5 still has to close QoE/reward.

## Phase 3.2C Local Acquisition Update

Use these talking points:

- The first three real trace candidates are now locally present outside the repository.
- HSDPA Norway, Ghent 4G/LTE and Lancaster are raw candidates, not normalized traces.
- Raw local availability is necessary but not sufficient for evaluation.
- No local JSON inventory, raw logs, ZIPs or generated artifacts are committed.
- The next step should be synthetic schema validation, not full replay.
- Final QoE/reward and controller ranking remain out of scope.

## Phase 3.3A Synthetic Validation Update

Use these talking points:

- The first trace code is only a schema validator.
- Tests create synthetic CSVs in temporary directories and do not read local raw datasets.
- The validator rejects missing columns, malformed numeric values, `NaN`, infinity, bad timing and negative throughput.
- Zero throughput is accepted because it represents outage/no-delivery intervals.
- This is a gate before converters and replay, not a replay runner.

## Phase 3.3B TraceLoader Update

Use these talking points:

- TraceLoader loads already-normalized traces only.
- It delegates validation to the Phase 3.3A validator.
- It preserves optional/extra columns as metadata.
- It does not convert raw datasets and does not read HSDPA/Ghent/Lancaster raw paths.
- `LoadedTrace` is for the future replay environment, not controller input.
- Future replay must reveal only observations that a real client would have.

## Phase 3.4B Network Model Update

Use these talking points:

- The network model is deterministic and consumes `LoadedTrace`, not raw datasets.
- It simulates segment download time from throughput intervals, zero-throughput intervals and gaps.
- It is not connected to controllers, player/runtime or media engines.
- The fake replay adapter only advances a synthetic clock.
- Controllers must not receive complete traces or future samples.
- This step is needed before IA/RL because learning needs a reproducible environment before rewards or policies can be defended.
- Final QoE/reward, benchmark ranking, Mahimahi and `tc/netem` remain deferred.

## Phase 3.4C Controlled Dry-Run Update

Use these talking points:

- The dry-run harness is the first controlled loop that calls existing controllers against trace-driven timing.
- Controllers are still unmodified and are called through the public registry/contract.
- The controller adapter blocks complete traces, future samples, raw metadata, split labels and OOD labels.
- Dry-run outputs are explicitly labeled non-benchmark, not final QoE/reward and not for ranking.
- This validates integration boundaries, not controller superiority.

## Phase 3.4D Mahimahi/tc Decision Update

Use these talking points:

- The external emulation decision is closed for the current phase.
- Python trace-driven execution remains primary because it is deterministic, testable and already integrated.
- Mahimahi remains valuable as a secondary Ubuntu validation candidate, not as the primary benchmark path.
- `tc/netem` remains a Linux fallback/sanity candidate because real qdisc changes have privilege, cleanup and host-contamination risks.
- Phase 3.5 can proceed without Mahimahi or `tc/netem` installed.
- No Mahimahi/tc output exists as benchmark evidence in Phase 3.4D.
