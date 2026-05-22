# Phase 3 Trace Schema Contract

This architecture contract records the Phase 3.2B trace schema boundary for DashClientModular4.

## Contract

Future trace/replay work must use `normalized_trace_schema_v1` as the internal trace input contract.

Required normalized trace columns:

| column | unit | rule |
| --- | --- | --- |
| `timestamp_s` | seconds | Numeric seconds from trace start; monotonically non-decreasing. |
| `duration_s` | seconds | Numeric interval duration; strictly positive. |
| `throughput_kbps` | kilobits per second | Numeric available/application-level downlink throughput; greater than or equal to 0. |

Optional context columns may be preserved, but Phase 2 baseline controllers must not require them.

## Runtime Boundary

The future runner must not expose future trace samples directly to controllers. Controllers may only receive normal client/controller signals produced by the playback loop.

This contract does not authorize:

- replay implementation;
- dataset download;
- QoE/reward definition;
- benchmark ranking;
- IA/RL implementation;
- controller changes;
- player/runtime changes;
- media-engine changes;
- metric-definition changes.

Phase 3.4A separately authorizes limited converter implementation for HSDPA Norway, Ghent 4G/LTE and Lancaster under `core/trace_replay/converters/` and `scripts/convert_trace_dataset.py`. That converter authorization does not change the runtime boundary above.

## Storage Boundary

Raw datasets, normalized traces and generated manifests must stay outside the repository:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_raw_candidates
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_manifests
```

The repository contains authored documentation and may contain future tiny synthetic fixtures only if a later implementation block explicitly authorizes them.

## Method Boundary

The likely primary runner is a custom Python trace-driven fake/replay runner because it can be deterministic, tested with `unittest`, compatible with Windows/Ubuntu, and usable in future IA training loops.

Mahimahi is a secondary Ubuntu validation candidate. Linux `tc/netem` is a Linux fallback/runbook candidate. Neither is implemented or selected as the final benchmark path by this contract.

## Phase 3.3B TraceLoader Boundary

`core.trace_replay.loader` can load already-normalized schema-v1 rows and CSV files into `LoadedTrace`.

This is not the replay runner. `LoadedTrace` may hold all samples for the future replay environment, but it must not be passed to controllers as a future-looking decision source.

The future replay/network model must consume `LoadedTrace` and reveal only observations that a real client would have at the current point in playback.

## Phase 3.4A Converter Boundary

Dataset converters may read raw local sources and write normalized CSV plus manifest JSON outside the repository. They must validate emitted CSVs against `normalized_trace_schema_v1`.

Converter outputs are not benchmark results, final split inputs, QoE evidence or controller-ranking evidence. Phase 3.4A still does not implement the replay runner, Mahimahi, `tc/netem`, final QoE/reward, final train/validation/test/OOD split, IA/RL, controller changes, player/runtime changes, media-engine changes or metric-definition changes.

