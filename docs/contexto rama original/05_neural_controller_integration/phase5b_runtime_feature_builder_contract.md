# Phase 5B runtime feature builder contract

## Purpose

The future runtime feature builder converts existing controller feedback into the context and candidate features expected by the Phase 4 bundle. It must use only information available before requesting the next segment.

## Feedback mapping

| Feedback key / source | Runtime feature | Rule |
|---|---|---|
| `queued_time` | `buffer_s` | Read before decision. |
| `level` | `last_representation_index` | Use the last executed representation index. |
| `rates` | candidate ladder | Current MPD/client rates only. |
| `last_fragment_size` and `last_download_time` | throughput sample | Add only after a completed download. |
| `fragment_duration` | segment duration | Use only if exposed before decision. |
| `segment_index` | segment index | Use only if known before decision. |

## Throughput history

Throughput history is built only from previous completed downloads:

```text
throughput_bps = 8 * last_fragment_size_bytes / last_download_time_s
```

Invalid or missing samples must not be invented. Missing required samples trigger fallback or a documented cold-start fallback policy.

## Optional features

Optional features require availability flags:

- candidate chunk size;
- chunks remaining;
- media duration;
- fragment duration if not always available.

If an optional feature is unavailable, the builder must either set its availability flag or fallback if the bundle declares it required.

## Forbidden information

The builder must not use future throughput, future download time, future rebuffer, future reward/QoE, teacher labels, trace id, dataset label, benchmark result or controller identity as model input.

## Failure behavior

Missing required feature, schema mismatch or feature build exception must trigger fallback. The failure must be recorded as diagnostic-only telemetry.
