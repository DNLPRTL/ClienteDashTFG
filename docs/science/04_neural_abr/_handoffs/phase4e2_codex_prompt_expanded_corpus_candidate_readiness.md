# Codex Prompt â€” Phase 4E.2 Expanded External Corpus + Candidate Readiness Gate

You are working on DashClientModular4, a TFG project about ABR with AI for DASH streaming.

This prompt is intentionally self-contained because it may be executed in a fresh Codex thread.
Read this whole prompt before editing anything.

## 0. Current phase

We are in:

```text
Phase 4E.2 â€” expanded external trace corpus + candidate-readiness gate
```

Already closed:

```text
Phase 4A0 â€” literature intake and triage
Phase 4A1 â€” source_cards + evidence_matrix
Phase 4A2 â€” method_decision
Phase 4B  â€” state/action/reward/training-data contracts
Phase 4C  â€” training environment / simulator contract
Phase 4D  â€” offline NeuralABR-Lite pipeline implementation
Phase 4E  â€” synthetic training smoke
Phase 4E.1 â€” external normalized trace smoke
```

Do **not** move to Phase 4F unless the explicit Phase 4E.2 gate says so.

## 1. Mandatory project context

Project: DashClientModular4 â€” TFG ABR con IA para streaming DASH.
Branch: main.
Latest validated HEAD before this task: `d05167d test(neural-abr): add Phase 4E.1 external trace smoke support`.

Classic controllers already implemented:

```text
min_rate, fixed_rate, max_rate, rate_based, bba, bola, mpc, robust_mpc
```

Phase 3.5 QoE/reward is closed:

```text
qoe_linear_v1          selected QoE/reward basis
reward_n               normalized reward for IA candidate work
qoe_linear_mean         aggregate reporting
qoe_log_v1             sensitivity-only
startup                report-only
VMAF                   deferred
use_for_eval           gate for eval rows
diagnostic_only        diagnostic rows
do_not_use_for_eval    excluded rows
```

There is still:

```text
no formal benchmark
no final ranking
no final IA controller integration
no real-world claim
no SOTA claim
```

## 2. Scientific decision inherited from Phase 4Aâ€“4B

The selected method is:

```text
NeuralABR-Lite Candidate Scorer
```

Method:

```text
small CPU-first neural ABR
behavior cloning / imitation learning
teacher = robust_mpc primary, mpc secondary/comparator, oracle limited diagnostic-only
action = representation_index inside MPD ladder
output = score per valid representation
action mask mandatory
reward basis = qoe_linear_v1 / reward_n
fallback classical policy later
```

Rejected as base:

```text
PPO-first
A3C/Pensieve clone
full meta-RL
full offline RL
AIRL/reward learning
NMoE/MoE/transformer/large model
CUDA/ROCm/DirectML required training
```

Important evidence behind this decision:

```text
Pensieve: state/action/reward reference, not a stack to clone.
Comyco/SABR: imitation/behavior cloning is sample-efficient and TFG-friendly.
ABRL/Facebook: candidate scoring over valid representations is better than fixed softmax.
Oboe/ANT/BETA/Plume/Gelato: network regimes and trace skew matter.
Puffer/Fugu/Into the Wild/CausalSim: simulation and real-world diverge; avoid inflated claims and leakage.
SODA: non-IA ABR can be very strong; do not sell IA as universal improvement.
```

## 3. Phase 4D implementation status

The offline pipeline already exists under:

```text
core/neural_abr/
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
tests/test_neural_abr_*.py
```

Phase 4D passed:

```text
python -m unittest discover -> PASS
python scripts/check_client_readiness.py --strict -> PASS, 78 OK / 0 WARN / 0 FAIL
```

## 4. Phase 4E and Phase 4E.1 status

Phase 4E synthetic smoke:

```text
Decision: PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA
Synthetic model predicted only representation 3.
Not a Phase 4F candidate.
```

Phase 4E.1 external trace smoke:

```text
Decision: PHASE4E1_EXTERNAL_TRACE_SMOKE_PASS_NOT_CANDIDATE
```

Phase 4E.1 implemented external normalized trace ingestion. It did not touch controller/player/runtime/media and did not register a neural controller.

Phase 4E.1 results:

```text
Dataset build: PASS, 15 traces
Samples: train 1367, validation 407, OOD diagnostic 427
Dataset validation: PASS
Offline validation: PASS
Validation valid action rate: 1.0
OOD valid action rate: 1.0
Validation prediction distribution: {"0": 9, "1": 15, "2": 36, "3": 20, "4": 327}
OOD prediction distribution: {"0": 16, "1": 21, "2": 36, "3": 57, "4": 297}
Unit tests: PASS, 385 tests OK
Readiness: PASS, 78 OK / 0 WARN / 0 FAIL
Forbidden generated artifacts in repo: PASS
```

Interpretation:

```text
Phase 4E.1 is a successful external-trace smoke.
It is not a Phase 4F candidate.
The corpus is too small and diagnostic-only.
No CPU latency gate was closed.
No export/inference contract exists.
No benchmark/ranking/real-world claim was made.
```

## 5. Goal of this Codex task

Implement Phase 4E.2:

```text
expanded external trace corpus + candidate-readiness gate
```

This task must:

1. Prepare or support a larger balanced trace corpus from Phase 3 external trace material.
2. Keep all raw/converted datasets and runs outside the repo.
3. Add a formal candidate-readiness auditor.
4. Run or enable an extended external-trace diagnostic training.
5. Generate docs for memory and defense.
6. Decide one of exactly:

```text
PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F
PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE
PHASE4E2_BLOCKED_NEEDS_FIX
```

## 6. Absolute prohibitions

Do not do any of this:

```text
Do not touch controllers/.
Do not touch player.
Do not touch runtime.
Do not touch media engines.
Do not register a neural controller.
Do not integrate inference into DashClientModular4.
Do not create Phase 4F export bundle.
Do not run formal benchmark.
Do not produce ranking.
Do not use dry-runs legacy as training data.
Do not train on test/future benchmark data.
Do not commit PDFs, zips, CSV datasets, logs, .pt/.pth/.onnx, numpy files, pickles, checkpoints, TensorBoard or generated artifacts.
Do not claim SOTA.
Do not claim real-world validation.
```

## 7. Files you may modify or add

Allowed code:

```text
core/neural_abr/constants.py
core/neural_abr/content_ladder.py
core/neural_abr/trace_source.py
core/neural_abr/dataset_builder.py
core/neural_abr/validation.py
core/neural_abr/training.py
core/neural_abr/artifacts.py
core/neural_abr/candidate_readiness.py      # new allowed
core/neural_abr/trace_corpus.py             # new allowed
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
scripts/prepare_neural_abr_trace_corpus.py  # new required if needed
scripts/assess_neural_abr_candidate.py      # new required
tests/test_neural_abr_external_trace.py
tests/test_neural_abr_trace_corpus.py       # new required
tests/test_neural_abr_candidate_readiness.py # new required
```

Allowed docs:

```text
docs/science/04_neural_abr/phase4e2_*.md
```

Do not edit anything else unless strictly necessary. If you think another file is needed, stop and explain why.

## 8. Dataset and artifact locations

Local-only roots on Windows:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI
C:\Users\danie\Documents\TFG\_runs\phase4_AI
C:\Users\danie\Documents\TFG\_models\phase4_AI
```

Expected Phase 3 local root:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay
```

Relevant Phase 3 material:

```text
_normalized/schema_v1/phase3_4a_smoke
_manifests/phase3_4a_conversion_smoke
_expanded_phase3_4a
```

Never copy:

```text
_runs
phase3 dry-run outputs
controller runtime logs
benchmark outputs
smoke QoE outputs
```

## 9. Required implementation

### 9.1 Trace corpus preparation

Implement a robust corpus preparation path that can use:

```text
existing normalized CSV traces with manifests;
expanded raw Phase 3 trace candidates when safely parseable;
a deterministic sample cap and balancing policy.
```

CLI requirement:

```powershell
python scripts/prepare_neural_abr_trace_corpus.py `
  --phase3-root "C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay" `
  --output-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase4e2_expanded" `
  --max-total-traces 300 `
  --max-traces-per-dataset 120 `
  --seed 123 `
  --overwrite
```

Output layout:

```text
<output-root>/normalized/**/*.csv
<output-root>/manifests/**/*.json
<output-root>/phase4e2_trace_inventory.json
<output-root>/phase4e2_trace_corpus_summary.json
```

Required normalized CSV schema:

```text
timestamp_s,duration_s,throughput_kbps
```

Required manifest fields, at least:

```text
trace_id
dataset_id
leakage_group
sample_count
source_kind
converter
mean_throughput_kbps
min_throughput_kbps
max_throughput_kbps
coefficient_of_variation
regime_bucket
checksum_or_source_fingerprint
```

If an expanded raw format cannot be parsed safely, do not guess silently. Record it as skipped with reason in the inventory.

### 9.2 Regime-balanced split

Implement or verify a deterministic split policy:

```text
phase4e2_regime_balanced_trace_v1
```

Requirements:

```text
split by trace_id / leakage_group, never by random segment;
no leakage_group overlap between train/validation/OOD;
try to preserve dataset_id and regime_bucket diversity;
OOD diagnostic must be held out and diagnostic-only;
normalization stats fit on train only;
```

### 9.3 Candidate-readiness auditor

Implement:

```text
scripts/assess_neural_abr_candidate.py
core/neural_abr/candidate_readiness.py
```

It must read dataset/run/validation artifacts and emit:

```text
phase4e2_candidate_readiness_report.json
phase4e2_candidate_readiness_report.md
```

The auditor must classify:

```text
PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F
PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE
PHASE4E2_BLOCKED_NEEDS_FIX
```

### 9.4 Candidate-readiness gates

The model can be `CANDIDATE_READY_FOR_PHASE4F` only if all hard gates pass:

```text
Unit tests PASS.
Readiness PASS.
Forbidden artifact check PASS.
Dataset validation PASS.
Offline validation PASS.
No NaN/Inf.
No invalid labels.
Validation valid action rate == 1.0.
OOD diagnostic valid action rate == 1.0.
Split is trace-level and leakage_group-clean.
Normalizer was fit on train only.
No dry-run legacy data was used.
No controller/player/runtime/media files changed.
No neural controller was registered.
CPU-only execution.
At least 30 traces after corpus preparation.
At least 2 dataset_id families.
At least 3 regime buckets across all splits, or explicit PASS_NOT_CANDIDATE if not enough diversity.
CPU inference latency measured and p95 <= 10 ms per ABR decision on the user's CPU.
Model card exists.
Limitations doc exists.
```

Soft/diagnostic gates:

```text
Validation teacher agreement should be reported.
OOD teacher agreement should be reported if available.
Prediction distribution must be compared against teacher label distribution.
Do not reject a high-bitrate-heavy distribution just because representation 4 dominates; compare it against teacher distribution.
Flag pathological collapse if predicted distribution is much sharper than teacher distribution, e.g. total variation distance > 0.25 or entropy ratio < 0.60, unless documented.
Report validation and OOD action distributions.
Report per-dataset and per-regime summaries if possible.
```

If hard technical gates pass but corpus diversity is insufficient, return:

```text
PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE
```

not failure.

If leakage, invalid actions, artifacts in repo, tests fail, readiness fails, or controller/player/runtime/media are touched, return:

```text
PHASE4E2_BLOCKED_NEEDS_FIX
```

### 9.5 Training command that must work after implementation

After implementing, the following end-to-end style should work through the provided local script or equivalent commands:

```powershell
python scripts/prepare_neural_abr_trace_corpus.py --phase3-root "C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay" --output-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase4e2_expanded" --max-total-traces 300 --max-traces-per-dataset 120 --seed 123 --overwrite

python scripts/build_neural_abr_dataset.py --trace-csv-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase4e2_expanded\normalized" --trace-manifest-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase4e2_expanded\manifests" --output-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate" --split-policy phase4e2_regime_balanced_trace_v1 --representation-kbps 300,750,1200,1850,2850 --segment-duration-s 4.0 --teacher robust_mpc --seed 123 --diagnostic-only --overwrite

python scripts/validate_neural_abr_dataset.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate"

python scripts/train_neural_abr.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate" --output-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E2\expanded_candidate" --epochs 20 --batch-size 32 --seed 123 --device cpu

python scripts/validate_neural_abr_offline.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate" --run-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E2\expanded_candidate" --output-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E2\validation_expanded_candidate"

python scripts/assess_neural_abr_candidate.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate" --run-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E2\expanded_candidate" --validation-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E2\validation_expanded_candidate" --output-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E2\candidate_assessment" --phase phase4e2
```

You may adjust exact argument names if existing scripts require it, but then update docs and local commands accordingly.

## 10. Required documentation for memory and defense

Create/update:

```text
docs/science/04_neural_abr/phase4e2_expanded_corpus_report.md
docs/science/04_neural_abr/_historical/phase4e2_candidate_readiness_report.md
docs/science/04_neural_abr/phase4e2_model_card.md
docs/science/04_neural_abr/_historical/phase4e2_validation_report.md
docs/science/04_neural_abr/phase4e2_defense_talking_points.md
docs/science/04_neural_abr/_historical/phase4e2_open_limitations.md
docs/science/04_neural_abr/_historical/phase4e2_closure_report.md
```

Docs must clearly explain:

```text
what was implemented;
which traces were used;
which traces were skipped and why;
how trace-level split avoids leakage;
how normalization train-only is enforced;
how candidate scoring works;
how robust_mpc teacher labels are used;
why this is still not a benchmark;
why no real-world/SOTA claim is made;
whether the result is ready for Phase 4F or not;
what a future defense slide/table should say.
```

## 11. Required tests

Add tests for:

```text
trace corpus inventory generation;
manifest fields;
trace-level split no leakage_group overlap;
candidate readiness classification;
pathological collapse detection;
prediction-vs-teacher distribution comparison;
latency gate result parsing;
forbidden artifact protection if relevant.
```

All tests must pass with:

```powershell
python -m unittest discover
```

## 12. Acceptance commands

Run these before final response:

```powershell
python -m unittest discover
python scripts\check_client_readiness.py --strict
git diff --check
git status --short --branch
```

Also run the Phase 4E.2 end-to-end commands or the local wrapper script created by this package.

## 13. Final response format required from Codex

Return:

```text
Phase 4E.2 Decision: <one of the three exact decision strings>

Files changed:
...

Commands executed:
...

Corpus summary:
...

Dataset summary:
...

Training summary:
...

Validation summary:
...

Candidate-readiness gates:
...

Artifacts outside repo:
...

Memory/defense docs created:
...

Limitations:
...

Next step:
...
```

Never say the model is integrated into the client. Never claim benchmark/ranking/SOTA/real-world.

