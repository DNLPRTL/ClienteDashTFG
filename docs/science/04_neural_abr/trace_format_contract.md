# Trace format contract

## Purpose

Define the minimum trace representation accepted by the Phase 4 training environment.

## Trace unit

A trace represents exogenous network conditions for one replay episode/session. It must not be generated from DashClientModular4 legacy dry-runs unless a later explicit contract proves it is valid and non-contaminated.

## Required trace fields

Preferred canonical fields:

```text
trace_id: stable string
source_dataset: stable string
time_s: monotonically increasing timestamp or interval boundary
throughput_bps: available network throughput estimate/capacity for the interval
```

Alternative accepted fields if converted reproducibly:

```text
time_ms
bandwidth_kbps
bandwidth_mbps
download_rate_bytes_per_s
capacity_bps
```

All alternatives must be converted to canonical SI units before sample generation.

## Optional trace fields

```text
rtt_ms
loss_rate
cwnd_bytes
network_type
region
mobility_label
```

Optional fields may be stored in metadata and used for diagnostics/clustering only if they are available without future leakage. They are not automatically model features.

## Units

```text
throughput: bits per second
chunk size: bytes
time: seconds
buffer: seconds
bitrate: bits per second
representation index: integer index in ladder
```

## Disallowed trace fields as model features

```text
split name
future average throughput
future reward
teacher action
final QoE
controller name used for data collection
trace_id as categorical feature
benchmark result
```

## Missing data

Missing or invalid throughput values must be handled by a documented conversion rule. Silent interpolation without manifest entry is forbidden.
