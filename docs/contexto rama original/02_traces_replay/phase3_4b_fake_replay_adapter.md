# Phase 3.4B Fake Replay Adapter Boundary

`TraceDrivenFakeReplayAdapter` is a tiny boundary around `TraceDrivenNetworkModel`. It owns a current replay time and advances it after each simulated segment download.

## API

```python
adapter = TraceDrivenFakeReplayAdapter(network_model, initial_time_s=0.0)
result = adapter.download_segment(segment_size_bytes)
adapter.reset(current_time_s=0.0)
```

The adapter:

- stores `current_time_s`;
- calls `network_model.download(..., start_time_s=current_time_s)`;
- sets `current_time_s` to `SegmentDownloadResult.end_time_s`;
- can reset its clock to a finite non-negative value.

## Explicit Non-Integration

This adapter is not connected to:

- `core.media_engine.fake`;
- player/runtime code;
- controllers;
- benchmark artifacts;
- QoE/reward computation.

Its purpose is to keep a clean boundary ready for later Phase 3.4C/3.4D integration work. The later runner must still decide how simulated download timing maps to runtime events and controller observations.

## Controller Isolation

The adapter returns segment-level download results to the environment layer. Controllers must not receive complete traces, `LoadedTrace.samples`, future throughput samples or optional metadata columns such as GPS or scenario labels.

Mahimahi and Linux `tc/netem` remain optional later validation/runbook work, not part of this implementation.
