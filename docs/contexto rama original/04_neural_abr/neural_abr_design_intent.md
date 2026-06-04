# NeuralABR-Lite design intent

This document captures the **design intent** selected in Phase 4A2.
It is not an implementation specification yet.

## One-sentence design

NeuralABR-Lite is a small CPU-first neural component that scores valid DASH representations using observable client context and candidate representation features, trained by behavior cloning from expert decisions and protected by action masks and classical fallback.

## Intended future architecture

```text
                     observable client state
                              |
                              v
                      context feature builder
                              |
                              v
             +----------------+----------------+
             |                                 |
             v                                 v
    representation candidate 0        representation candidate n
             |                                 |
             v                                 v
       shared neural scorer             shared neural scorer
             |                                 |
             +--------------+------------------+
                            |
                            v
                   score per representation
                            |
                            v
               action mask + safety/fallback
                            |
                            v
                 selected representation_index
```

## Intended observable context

Final features are not closed in A2, but Phase 4B should decide among:

```text
throughput_history_k
download_time_history_k
buffer_s
last_representation_index
last_bitrate_kbps
last_chunk_download_time_s
recent_rebuffer_s
recent_switch_magnitude
chunks_remaining, if valid for VoD and available online
```

## Intended candidate features

Phase 4B should decide among:

```text
candidate_representation_index
candidate_ladder_position
candidate_bitrate_kbps
candidate_chunk_size_bytes, only if available without leakage
bitrate_delta_from_last
relative_bitrate_to_estimated_throughput, only if defined online
```

## Intended output

```text
score(candidate_representation)
```

The action is not a free bitrate.
The action is:

```text
representation_index in valid MPD ladder
```

## Intended training family

```text
behavior cloning / imitation learning
```

The future dataset will contain pairs:

```text
(observable_state, valid_candidate_representations) -> expert_representation_index
```

## Intended teacher family

The final teacher is not closed in A2. Phase 4B must compare:

```text
MPC teacher
robust_mpc teacher
oracle-limited teacher
consensus teacher
```

If any teacher uses future information to label an action, that future information must never enter model inputs.

## Intended safety pattern

```text
action mask:
  exclude invalid representations
  enforce MPD ladder bounds

fallback:
  if model unavailable -> classical controller
  if NaN/Inf score -> classical controller
  if malformed state -> classical controller
  if unsafe low-buffer decision -> optional conservative cap, to be specified later
```

## What this design intentionally avoids

```text
No free bitrate prediction.
No direct controller integration yet.
No online RL.
No direct PPO-first training.
No reward learning.
No VMAF dependency.
No large model.
No reliance on GPU.
```
