# Phase 3.4C Controlled Trace Dry-Runs

Phase 3.4C adds a deterministic dry-run harness that can execute existing Phase 2 controllers against a loaded normalized trace through the Phase 3.4B network model.

This is a controlled integration dry-run only. It is not the final benchmark, does not define final QoE/reward, does not rank controllers and does not connect to the DashClientModular4 player/runtime or media engines.

## Pipeline

The dry-run loop is:

1. load a `normalized_trace_schema_v1` CSV with `TraceLoader`;
2. create `TraceDrivenNetworkModel`;
3. wrap it in `TraceDrivenFakeReplayAdapter`;
4. build a synthetic representation ladder from kbps values;
5. ask a controller adapter for one representation index per synthetic segment;
6. estimate the selected segment size from bitrate and segment duration;
7. download through the trace-driven model;
8. update a simple buffer model;
9. record one `SegmentDryRunRecord` per synthetic segment.

## API

`core.trace_replay.dry_run` exposes:

- `TraceDryRunError`;
- `Representation`;
- `SegmentDryRunRecord`;
- `TraceDryRunResult`;
- `TraceDryRunConfig`;
- `build_representations_from_kbps(...)`;
- `estimate_segment_size_bytes(...)`;
- `run_trace_dry_run(...)`;
- `write_trace_dry_run_artifacts(...)`.

## Buffer Model

For each segment:

```text
rebuffer_s = max(download_duration_s - buffer_before_s, 0)
buffer_after_s = max(buffer_before_s - download_duration_s, 0) + segment_duration_s
```

This is intentionally minimal. It is sufficient for controller-interface and network-model integration checks, but it is not a replacement for final playback, QoE or reward semantics.

## Controller Feedback Boundary

Controllers receive only current public controller feedback:

- representation ladder rates;
- current buffer estimate;
- previous level;
- previous measured download timing and size;
- previous measured bandwidth estimate;
- segment duration and current segment index.

Controllers do not receive `LoadedTrace`, complete sample arrays, future trace samples, future throughput, optional trace metadata, split labels, OOD labels or leakage groups.

## Artifact Boundary

Artifacts are written only by explicit CLI/function invocation to an explicit output directory. They are labeled:

- `phase = phase3_4c_dry_run`;
- `outputs_are_benchmark_results = false`;
- `final_qoe_reward_defined = false`;
- `row_eval_gate = do_not_use_for_eval`;
- `no_final_ranking = true`.

The artifacts are dry-run integration evidence only and must stay outside the repository unless a later authored Markdown summary explicitly refers to them.

## Non-Goals

Phase 3.4C does not implement:

- final QoE/reward;
- benchmark ranking;
- IA/RL;
- Mahimahi or `tc/netem`;
- player/runtime integration;
- media-engine changes;
- controller changes;
- real dataset fixtures or generated run outputs in git.
