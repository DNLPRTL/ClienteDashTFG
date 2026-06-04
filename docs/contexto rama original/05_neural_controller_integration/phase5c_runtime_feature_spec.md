# Phase 5C runtime feature spec

## Purpose

The future runtime feature builder converts current dict-based controller feedback into Phase 4 NeuralABR-Lite context and candidate features. It must use only pre-decision information.

## Feedback to context mapping

| Runtime feature | Current feedback/source | Rule |
|---|---|---|
| `buffer_s` | `feedback["queued_time"]` | Use current queued seconds before decision. |
| `last_representation_index` | `feedback["level"]` | Clamp to current valid range. |
| `last_bitrate_bps` | `feedback["rates"][level] * 8.0` | Convert bytes/s ladder rate to bits/s. |
| `throughput_history_bps` | previous completed downloads | `8.0 * last_fragment_size / last_download_time`; left-pad to `K_CONTEXT`. |
| `download_time_history_s` | previous completed downloads | Use `last_download_time`; left-pad to `K_CONTEXT`. |
| `segment_index` | `feedback["segment_index"]` | Use only as runtime context, not a forbidden trace id. |
| segment duration | `feedback["fragment_duration"]` | Required for safety and candidate-size estimate. |
| `recent_switch_abs` | internal last selected levels | Compute absolute level change history. |
| `recent_rebuffer_s` | unavailable in current feedback | Default `0.0` with documented limitation unless added later. |
| `chunks_remaining_norm` | optional total segment count | If unavailable, set `0.0`. |
| `has_chunks_remaining` | optional total segment count | If unavailable, set `0.0`. |

Throughput history uses completed downloads only. Do not include the segment about to be requested.

## Candidate mapping

For each `index, rate_Bps` in `feedback["rates"]`:

| Candidate feature | Mapping |
|---|---|
| `candidate_representation_index` | `float(index)` |
| `candidate_bitrate_bps` | `float(rate_Bps) * 8.0` |
| `candidate_ladder_position_norm` | `index / max(n - 1, 1)` |
| `candidate_bitrate_norm_ladder` | `(candidate_bitrate_bps - min_bitrate_bps) / max(max_bitrate_bps - min_bitrate_bps, 1.0)` |
| `candidate_delta_from_last_bitrate_norm` | `(candidate_bitrate_bps - last_bitrate_bps) / max(max_bitrate_bps, 1.0)` |
| `candidate_chunk_size_bytes` | explicit pre-decision size if known; otherwise `rate_Bps * fragment_duration_s` estimate |
| `candidate_chunk_size_available` | `1.0` only for explicit pre-decision size; `0.0` for bitrate-duration estimate |

## Forbidden runtime inputs

Runtime feature building must not use:

- future throughput;
- future download time;
- future rebuffer;
- future QoE/reward;
- teacher action/reward;
- split label;
- trace id;
- source dataset;
- benchmark result/rank;
- final run QoE;
- controller identity as input;
- dry-run legacy labels.

Missing required features trigger fallback. Optional features require availability flags. All telemetry remains diagnostic-only and not benchmark evidence.
