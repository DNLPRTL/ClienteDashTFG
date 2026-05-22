# Phase 3.4B Trace-Driven Network Model

Phase 3.4B adds a deterministic network model that consumes a `LoadedTrace` and simulates segment download durations. It does not connect to DashClientModular4 runtime, does not run controllers and does not create benchmark results.

## Position In The Trace Pipeline

| layer | role |
| --- | --- |
| converters | Convert raw HSDPA/Ghent/Lancaster files into `normalized_trace_schema_v1` CSVs and local manifests outside the repo. |
| TraceLoader | Loads already-normalized rows or CSVs into `TraceSample` and `LoadedTrace`. |
| TraceDrivenNetworkModel | Converts a `LoadedTrace` into deterministic segment download durations. |
| TraceDrivenFakeReplayAdapter | Owns a small fake replay clock around the network model. |
| future runtime runner | Later integration layer that may connect the model boundary to player/runtime behavior. Not implemented in Phase 3.4B. |

Controllers must not receive `LoadedTrace`, complete traces or future samples. The network model is an environment/replay component, not a controller API.

## API

`core.trace_replay.network_model` exposes:

- `TraceReplayError`
- `END_POLICY_FAIL = "fail"`
- `END_POLICY_LOOP = "loop"`
- `SegmentDownloadResult`
- `TraceDrivenNetworkModel`

Main call:

```python
model = TraceDrivenNetworkModel(loaded_trace)
result = model.download(segment_size_bytes, start_time_s=0.0)
```

`estimate_download_duration(...)` is an alias wrapper around `download(...)`.

## Network Semantics

Each `TraceSample` interval is treated as:

```text
[timestamp_s, timestamp_s + duration_s)
```

Throughput is converted as:

```text
bytes_per_second = throughput_kbps * 1000 / 8
```

Rules:

- `segment_size_bytes` must be a positive integer.
- `start_time_s` must be finite and non-negative.
- `throughput_kbps = 0` means no bytes are delivered during that interval.
- Gaps between samples are no-delivery time.
- Download duration includes waiting through gaps and zero-throughput intervals.
- Measured throughput is computed from delivered bytes and wall-clock download duration.
- `END_POLICY_FAIL` raises `TraceReplayError` if the trace cannot finish the segment.
- `END_POLICY_LOOP` may wrap to trace time `0.0`; `max_loops` bounds wrapping inside one download.
- All-zero positive-duration traces raise `TraceReplayError` for positive segment downloads.

The model is deterministic and purely local. It creates no run directories, logs, normalized CSVs or benchmark artifacts.

## Boundary

Phase 3.4B still does not define final QoE/reward, run benchmark rankings, implement IA/RL, execute Mahimahi, execute `tc/netem`, modify controllers, modify player/runtime behavior or modify media engines. QoE/reward remains Phase 3.5 work.
