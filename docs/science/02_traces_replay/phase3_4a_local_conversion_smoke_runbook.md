# Phase 3.4A Local Conversion Smoke Runbook

This runbook explains how to run a small local conversion smoke outside the repository. It does not create benchmark results.

## Storage Rule

Raw datasets, normalized real traces and generated manifests must stay outside git. Use local directories such as:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_raw_candidates
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_manifests
```

Do not copy raw logs, ZIPs, normalized CSVs or generated manifest JSON files into `DashClientModular4`.

## Smoke Command

From the repository root, run one dataset at a time:

```text
python scripts/convert_trace_dataset.py --dataset hsdpa_norway_mmsys2013 --input-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_raw_candidates\hsdpa_norway_mmsys2013 --output-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1\hsdpa_norway_mmsys2013 --manifest-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_manifests\trace_manifest_v1\hsdpa_norway_mmsys2013 --max-traces 5 --overwrite
```

```text
python scripts/convert_trace_dataset.py --dataset ghent_4g_lte_bandwidth_logs --input-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_raw_candidates\ghent_4g_lte_bandwidth_logs --output-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1\ghent_4g_lte_bandwidth_logs --manifest-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_manifests\trace_manifest_v1\ghent_4g_lte_bandwidth_logs --max-traces 5 --overwrite
```

```text
python scripts/convert_trace_dataset.py --dataset lancaster_abr_throughput_traces --input-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_raw_candidates\lancaster_abr_throughput_traces --output-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1\lancaster_abr_throughput_traces --manifest-dir C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_manifests\trace_manifest_v1\lancaster_abr_throughput_traces --max-traces 5 --overwrite
```

The smoke uses `--max-traces 5` to limit blast radius. Remove or increase it only after inspecting outputs and confirming storage paths are outside the repo.

## Expected Output

The CLI prints:

- dataset id;
- input directory;
- output directory;
- manifest directory;
- converted trace count;
- skipped input count;
- errors, if any.

Exit code `0` means at least one normalized CSV was emitted and validated. Exit code non-zero means no traces were converted or a converter error occurred.

## Inspection Checklist

After a smoke run:

1. Confirm normalized CSV files are under the external normalized directory, not the repo.
2. Confirm manifest JSON files are under the external manifest directory, not the repo.
3. Open one CSV and check required columns: `timestamp_s`, `duration_s`, `throughput_kbps`.
4. Open one manifest and check `split_candidate` is `conversion_only_no_final_split`.
5. Run `git status --short` and confirm no raw datasets, ZIPs, logs, generated CSVs or generated manifests appear inside the repository.

## Non-Goals

This runbook does not run replay, Mahimahi, `tc/netem`, benchmarks, QoE/reward calculation, controller ranking, final split assignment or IA/RL training.
