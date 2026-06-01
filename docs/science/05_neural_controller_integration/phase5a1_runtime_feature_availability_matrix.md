# Phase 5A1 runtime feature availability matrix

## Valid online features

| Feature | Source | Availability rule | Phase 5 status |
|---|---|---|---|
| `throughput_history_bps` | Previous completed downloads | Built only after segment download completes | ONLINE_REQUIRED if history exists; otherwise fallback or cold-start policy |
| `download_time_history_s` | Previous completed downloads | Built only from measured completed downloads | ONLINE_REQUIRED if history exists; otherwise fallback or cold-start policy |
| `buffer_s` / queued time | Feedback `queued_time` before decision | Read before requesting next segment | ONLINE_REQUIRED |
| `last_representation_index` / `level` | Feedback `level` | Last executed representation | ONLINE_REQUIRED if previous action exists |
| `last_bitrate_bps` / current selected rate | Feedback `rates[level]` or last selected rate | Derived from current ladder | ONLINE_REQUIRED if previous action exists |
| representation ladder / rates | Feedback `rates` and MPD state | Current candidates only | ONLINE_REQUIRED |
| candidate representation index | Candidate enumeration | Built from current ladder indices | ONLINE_REQUIRED |
| candidate bitrate | Candidate `rates[index]` | Built from current ladder | ONLINE_REQUIRED |
| `segment_index` | Feedback/media state | Must be known before decision | ONLINE_REQUIRED if exposed |
| `fragment_duration` | Feedback or media metadata | Use only if available before decision | ONLINE_OPTIONAL with availability flag |
| `candidate_chunk_size_bytes` | MPD/client media metadata | Use only if provided before decision | ONLINE_OPTIONAL with availability flag |
| `chunks_remaining_norm` | MPD/media list | Use only if known before decision | ONLINE_OPTIONAL with availability flag |

## Forbidden features

The following must never be model inputs:

- future throughput;
- future download time;
- future rebuffer;
- future reward or QoE;
- `teacher_action`;
- `teacher_reward`;
- split label;
- trace id;
- source dataset;
- benchmark rank or result;
- final run QoE;
- controller identity as model input;
- dry-run legacy labels.

## Rule

Any feature not proven to be available before the decision is forbidden unless it is explicitly optional and paired with an availability flag. Missing required features trigger fallback. Diagnostic-only fields are not benchmark evidence.
