# State representation contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This document defines the observable state for `NeuralABR-Lite Candidate Scorer` before any dataset or model code is written.

The state must satisfy four requirements:

```text
observable online
small enough for CPU-first training
compatible with DashClientModular4 telemetry/controller contracts
free of future-information leakage
```

## Primary temporal horizon

The default temporal window is:

```text
K_CONTEXT = 5
```

Rationale:

- `k = 5` is small, CPU-friendly and aligned with compact meta-RL designs found in the literature.
- `k = 8` remains a documented sensitivity option because several generalization papers use longer windows, but it is not the default.
- Any change from `K_CONTEXT = 5` must be versioned in the dataset manifest and model config.

## Context features

The context vector is built from data known before choosing the next segment representation.

### Historical throughput

```text
throughput_history_bps[K_CONTEXT]
```

Definition:

```text
bytes_downloaded_for_previous_segment * 8 / download_time_s
```

Rules:

- Only previous completed downloads may be used.
- Missing early entries are left-padded with zero plus an availability mask if implemented.
- Throughput measured during future or current undecided downloads is forbidden.

### Historical download time

```text
download_time_history_s[K_CONTEXT]
```

Rules:

- Previous completed segment downloads only.
- Must not include the download time of the segment being selected.

### Buffer

```text
buffer_s
```

Rules:

- Buffer level immediately before selecting the next representation.
- May be clipped/normalized, but raw seconds should remain recoverable in generated artifacts.

### Last representation and bitrate

```text
last_representation_index
last_bitrate_bps
```

Rules:

- `last_representation_index` is the index actually requested for the previous media segment.
- `last_bitrate_bps` comes from the MPD ladder / representation metadata.
- If there is no previous segment, use a documented sentinel and availability flag.

### Recent rebuffer signal

```text
recent_rebuffer_s
```

Rules:

- Rebuffering observed before the current decision may be used.
- Future stall or stall caused by the current undecided action is forbidden.

### Recent switching signal

```text
recent_switch_abs
```

Definition:

```text
abs(last_representation_index - previous_representation_index)
```

Rules:

- Used to make smoothness visible to the model.
- Must be based only on previous actions.

### Chunks remaining

```text
chunks_remaining_norm
has_chunks_remaining
```

Rules:

- Allowed for VoD if known from the manifest or deterministic media index.
- Must be disabled or marked unavailable for live/unknown-length streams.
- Must not encode hidden test/dataset identity.

## Candidate representation features

For each valid representation candidate `r`, the model receives candidate-specific features.

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

Rules:

- Candidate features are evaluated independently for each representation.
- `candidate_chunk_size_bytes` is allowed only if the same information would be available before the request in the real client path.
- If chunk size is not available online, use `candidate_chunk_size_available = 0` and a neutral numeric value.

## Explicitly forbidden features

The following features are forbidden in model inputs:

```text
future throughput
future download time
future stall
future reward
future QoE
teacher action
teacher score
final run QoE
trace split label
trace id as numeric feature
controller name as feature
benchmark rank
anything generated after the current decision
```

## State shape policy

The preferred implementation shape is candidate-scoring, not fixed softmax:

```text
context_features: one vector per decision
candidate_features: one vector per valid representation
score(context, candidate) -> scalar
```

This allows different MPD ladders without changing the output layer.

## Phase 4B decision

State is closed as:

```text
small online-observable temporal context
+ per-candidate representation features
+ action mask
+ train-only normalization
```

No large sequence model, transformer, MoE, latent VAE, or meta-RL context encoder is selected for the base implementation.
