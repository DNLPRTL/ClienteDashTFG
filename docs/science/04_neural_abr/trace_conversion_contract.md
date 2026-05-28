# Trace conversion contract

## Goal

Convert external trace datasets into the canonical Phase 4 trace format without contaminating the repository.

## Local-only input/output

Trace conversion inputs and generated trace files must live outside the repo:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\raw
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\converted
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\manifests
```

## Conversion manifest

Every converted dataset must have a manifest containing:

```text
dataset_id
source_name
source_url_or_citation
license_or_access_note
download_date
conversion_script_version
input_files
output_files
field_mapping
unit_mapping
missing_value_policy
filtering_policy
number_of_traces
trace_duration_summary
throughput_summary
known_biases
not_for_benchmark_flag
```

## No legacy dry-runs

DashClientModular4 dry-runs, smoke scenarios and previous controller logs are forbidden as training traces in Phase 4 unless a later explicit research decision overrides this gate. This package does not override it.

## Conversion reproducibility

A future conversion command must be reproducible from manifest and script arguments. Hand-edited converted traces are not allowed unless explicitly marked diagnostic-only.

## Repository policy

Converted traces must not be committed. Only manifest summaries and methodology docs may enter `docs/science/04_neural_abr/`.
