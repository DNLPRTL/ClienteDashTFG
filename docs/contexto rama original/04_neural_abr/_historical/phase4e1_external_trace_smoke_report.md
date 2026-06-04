# Phase 4E.1 external trace smoke report

## Status

Decision:

```text
PHASE4E1_EXTERNAL_TRACE_SMOKE_PASS_NOT_CANDIDATE
```

This is a diagnostic external-trace smoke. It is not Phase 4F, not export readiness, not client integration, and not a benchmark/ranking.

## Inputs

Normalized trace CSV root:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase3_4a_smoke\normalized
```

Trace manifest root:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase3_4a_smoke\manifests
```

The smoke consumed 15 Phase 3 normalized external trace CSVs:

- 5 from `ghent_4g_lte_bandwidth_logs`;
- 5 from `hsdpa_norway_mmsys2013`;
- 5 from `lancaster_abr_throughput_traces`.

Dry-runs, QoE smokes, player logs and benchmark outputs were not used.

## Commands executed

```powershell
python scripts\build_neural_abr_dataset.py --trace-csv-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase3_4a_smoke\normalized" --trace-manifest-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase3_4a_smoke\manifests" --output-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST" --split-policy phase4e1_trace_level_regime_v1 --representation-kbps 300,750,1200,1850,2850 --segment-duration-s 4.0 --teacher robust_mpc --seed 123 --diagnostic-only --overwrite
python scripts\validate_neural_abr_dataset.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST"
python scripts\train_neural_abr.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST" --output-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\external_trace_smoke_TEST" --epochs 5 --batch-size 16 --seed 123 --device cpu --smoke
python scripts\validate_neural_abr_offline.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST" --run-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\external_trace_smoke_TEST" --output-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\validation_TEST"
python -m unittest discover
python scripts\check_client_readiness.py --strict
```

## Dataset build result

Dataset output:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST
```

Sample counts:

```json
{"train": 1367, "validation": 407, "ood_diagnostic": 427}
```

The fixed ladder was:

```text
300,750,1200,1850,2850 kbps
```

Segment duration was 4.0 seconds. Segment count is derived per trace as floor(trace duration / 4.0).

## Training result

Training run output:

```text
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\external_trace_smoke_TEST
```

Training parameters:

- epochs: 5
- batch size: 16
- seed: 123
- device: CPU
- final loss: 0.6211519241333008
- mean loss: 0.5170281020772838

Validation metrics from the training report:

```json
{
  "sample_count": 407,
  "valid_action_rate": 1.0,
  "teacher_agreement": 0.941031941031941,
  "prediction_distribution": {"0": 9, "1": 15, "2": 36, "3": 20, "4": 327}
}
```

## Verification

- `python -m unittest discover`: PASS, 385 tests OK.
- `python scripts\check_client_readiness.py --strict`: PASS, 78 OK, 0 WARN, 0 FAIL.
- Forbidden generated artifact check: PASS.

## Interpretation

The external trace smoke validates ingestion, trace-level splitting, action-mask label validity, CPU training and offline validation on the Phase 3 normalized external smoke subset.

It is still not a model candidate for Phase 4F because the run is small, diagnostic-only, has no export/inference contract, and has no formal latency or broader external-trace validation gate.
