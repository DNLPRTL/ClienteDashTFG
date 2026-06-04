# Phase 4D implementation report

Status: PASS for offline pipeline implementation smoke.

## What was implemented

Phase 4D adds an offline-only `core/neural_abr/` package plus four scripts:

```text
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
```

The package implements the NeuralABR-Lite Candidate Scorer pipeline:

```text
normalized_trace_schema_v1 traces
  -> deterministic segment replay
  -> pre-decision context and candidate features
  -> robust_mpc teacher labels
  -> JSONL supervised dataset
  -> train-only normalization
  -> small shared MLP candidate scorer
  -> offline sanity validation report
```

No neural controller was registered. No player, runtime, downloader, parser, media engine, or classical controller file was edited.

## Method fit

The code follows the Phase 4A2/4B decision: a small CPU-first behavior-cloning model scores each valid MPD representation candidate. This keeps the design close to Pensieve-style state/action/reward framing, Comyco/SABR-style imitation, ABRL-style candidate scoring, and Puffer/CausalSim caution about trace replay claims. It does not implement PPO, full offline RL, meta-RL, AIRL, MoE, transformers, VMAF, or a learned reward.

## Trace to sample flow

Trace loading reuses:

```text
core.trace_replay.loader
core.trace_replay.schema
core.trace_replay.validation
core.trace_replay.network_model
```

The builder consumes only `normalized_trace_schema_v1` traces. For each trace and segment, the replay environment builds features before the next action is selected, then advances with:

```text
download_time_s = trace network model download duration
rebuffer_s = max(download_time_s - buffer_s, 0)
buffer_s = max(buffer_s - download_time_s, 0) + segment_duration_s
buffer_s = min(buffer_s, max_buffer_s)
```

Each JSONL row contains context features, per-candidate features, an action mask, label metadata, and non-input provenance metadata.

## Teacher labels

The primary teacher is an offline `robust_mpc` labeler. It uses previous throughput history only, applies a conservative safety factor, enumerates a small horizon, and scores candidate sequences with the documented `qoe_linear_v1 / reward_n` basis. `mpc` remains implemented as a secondary policy constructor. The bounded oracle is represented only as a diagnostic-only boundary name, not as a training source.

Teacher action and reward fields are labels/metadata only. They are never placed in `context` or `candidates`.

## Leakage prevention

The feature builder rejects forbidden model input keys such as:

```text
future_throughput
future_download_time
teacher_action
teacher_reward_n
split
trace_id
source_dataset
regime_label
benchmark_result
```

Trace-level split disjointness is checked in the dataset builder and validator. Dataset provenance stays in `metadata`, not in model feature payloads. The generated `leakage_audit.json` records the gates and marks the synthetic smoke as diagnostic-only.

## Action masking

All labels and model decisions use `representation_index`. Masks have one boolean per representation. Validation enforces:

```text
0 <= representation_index < representation_count
action_mask[representation_index] == true
```

The model scores all padded candidates but invalid candidates are masked to a very negative score before cross entropy or argmax.

## Train-only normalization

`FeatureNormalizer.fit_train()` accepts only samples whose split is `train`. Passing validation or OOD samples to fit raises an error. The training script writes `normalization_stats.json` fitted on train samples only and applies those stats to validation/OOD diagnostics.

## CPU-first reproducibility

Training defaults to `--device cpu` and rejects non-CPU devices in Phase 4D. The training smoke sets Python and PyTorch seeds and enables deterministic PyTorch algorithms. The model is a small shared MLP with hidden sizes `(32, 16)`.

## Artifact policy

Dataset, run, checkpoint, normalization, and validation outputs are blocked inside the repository. The scripts require external output directories, matching the Phase 4 artifact hygiene contract.

## Not a benchmark

The synthetic smoke is diagnostic-only. The reports include teacher agreement and valid-action sanity metrics, but they are not a controller ranking, not a final QoE comparison, and not a real-world validation claim.

## Client integration remains blocked

Phase 4D produces offline artifacts only. A neural ABR controller is not registered and Phase 5 integration is still blocked until later Phase 4 acceptance/export/inference gates explicitly allow it.
