# Replay engine contract

## Purpose

Define how the offline environment converts trace throughput and selected representation into transition dynamics.

## Required transition inputs

```text
current buffer_s
selected representation_index
chunk_size_bytes or derived chunk size
segment_duration_s
current trace throughput interval(s)
```

## Transition outputs

```text
download_time_s
new_buffer_s
rebuffer_s
measured_throughput_bps
completed_segment_index
history updates
```

## Conceptual download model

The future implementation must document one of these policies:

```text
single-interval throughput approximation
multi-interval byte-drain model
dataset-provided download time model
```

The default preferred model is a byte-drain replay over trace intervals because it is more explicit than assuming one throughput sample equals one full segment download.

## Buffer update

Conceptual update:

```text
rebuffer_s = max(0, download_time_s - buffer_s)
buffer_after_download = max(0, buffer_s - download_time_s) + segment_duration_s
buffer_s = min(buffer_after_download, max_buffer_s)
```

Any startup handling must remain aligned with the Phase 3.5 reward contract: startup is report-only unless a later versioned contract changes it.

## Determinism

For fixed trace, selected actions, chunk table and parameters, transitions must be deterministic.

## Not benchmark-grade

Replay output is valid for training and sanity validation under documented assumptions. It is not a final benchmark authority.
