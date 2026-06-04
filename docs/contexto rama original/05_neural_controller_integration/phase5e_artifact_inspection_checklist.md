# Phase 5E artifact inspection checklist

## Boundary

These checks inspect structural artifacts only. They do not create a benchmark, rank controllers, compare baselines, or claim neural improvement.

## Required artifacts

For the selected `run_*` directory, verify:

- `run_manifest.json` exists.
- `config.resolved.json` exists.
- `environment.json` exists.
- `run.log` exists.
- `segment_telemetry.csv` exists.
- `evaluation_segments.csv` exists.
- `dataset.csv` does not exist.
- `dataset_training.csv` does not exist.

## Required neural diagnostic fields

`segment_telemetry.csv` should contain these diagnostic columns when `neural_abr_lite` is selected:

```text
feedback_neural_enabled
feedback_neural_bundle_configured
feedback_neural_bundle_loaded
feedback_neural_bundle_schema_ok
feedback_neural_bundle_hash_ok
feedback_neural_feature_schema_ok
feedback_neural_feature_vector_ok
feedback_neural_missing_features
feedback_neural_action_mask_valid_count
feedback_neural_raw_action
feedback_neural_raw_rate_Bps
feedback_neural_safe_action
feedback_neural_safe_rate_Bps
feedback_neural_safety_intervened
feedback_neural_fallback_used
feedback_neural_fallback_reason
feedback_neural_inference_ms
feedback_neural_nan_inf_detected
feedback_neural_invalid_action_detected
feedback_neural_diagnostic_only
```

`evaluation_segments.csv` must not contain neural diagnostic columns.

## Windows PowerShell checks

Set the latest run directory:

```powershell
$RunRoot = "D:\outside_repo\phase5e_runs"
$RunDir = Get-ChildItem -Path $RunRoot -Directory |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1
$RunPath = $RunDir.FullName
```

Check required files:

```powershell
$Required = @(
  "run_manifest.json",
  "config.resolved.json",
  "environment.json",
  "run.log",
  "segment_telemetry.csv",
  "evaluation_segments.csv"
)
$Required | ForEach-Object {
  [PSCustomObject]@{
    File = $_
    Exists = Test-Path (Join-Path $RunPath $_)
  }
}
```

Check legacy files are absent:

```powershell
@("dataset.csv", "dataset_training.csv") | ForEach-Object {
  [PSCustomObject]@{
    File = $_
    Exists = Test-Path (Join-Path $RunPath $_)
  }
}
```

Check manifest status and controller:

```powershell
$Manifest = Get-Content (Join-Path $RunPath "run_manifest.json") -Raw | ConvertFrom-Json
$Manifest.status
$Manifest.controller.name
$Manifest.benchmark_neutrality.outputs_are_benchmark_results
```

Check CSV headers:

```powershell
$SegmentRows = Import-Csv (Join-Path $RunPath "segment_telemetry.csv")
$EvalRows = Import-Csv (Join-Path $RunPath "evaluation_segments.csv")
$SegmentHeader = $SegmentRows[0].PSObject.Properties.Name
$EvalHeader = $EvalRows[0].PSObject.Properties.Name

$ExpectedNeural = @(
  "feedback_neural_enabled",
  "feedback_neural_bundle_configured",
  "feedback_neural_bundle_loaded",
  "feedback_neural_bundle_schema_ok",
  "feedback_neural_bundle_hash_ok",
  "feedback_neural_feature_schema_ok",
  "feedback_neural_feature_vector_ok",
  "feedback_neural_missing_features",
  "feedback_neural_action_mask_valid_count",
  "feedback_neural_raw_action",
  "feedback_neural_raw_rate_Bps",
  "feedback_neural_safe_action",
  "feedback_neural_safe_rate_Bps",
  "feedback_neural_safety_intervened",
  "feedback_neural_fallback_used",
  "feedback_neural_fallback_reason",
  "feedback_neural_inference_ms",
  "feedback_neural_nan_inf_detected",
  "feedback_neural_invalid_action_detected",
  "feedback_neural_diagnostic_only"
)

$ExpectedNeural | Where-Object { $_ -notin $SegmentHeader }
$EvalHeader | Where-Object { $_ -like "*neural*" }
```

Check diagnostic-only marker:

```powershell
$SegmentRows |
  Select-Object -ExpandProperty feedback_neural_diagnostic_only -Unique
```

Expected values are empty for rows before a decision or `1` for diagnostic rows. There should be no value implying benchmark use.

Check no benchmark/ranking/improvement fields:

```powershell
$Forbidden = @("rank", "winner", "improvement", "p_value", "p-value")
($SegmentHeader + $EvalHeader) | Where-Object {
  $Column = $_.ToLowerInvariant()
  $Forbidden | Where-Object { $Column.Contains($_) }
}
```

Check selected policy rates are from the feedback ladder:

```powershell
@'
import ast
import csv
import sys

path = sys.argv[1]
bad = []
with open(path, newline="", encoding="utf-8") as handle:
    for row_number, row in enumerate(csv.DictReader(handle), start=2):
        target = row.get("policy_target_rate", "")
        if target in ("", None):
            continue
        try:
            target_value = float(target)
            rates = [float(value) for value in ast.literal_eval(row["feedback_rates"])]
        except Exception as exc:
            bad.append((row_number, "parse_error", str(exc)))
            continue
        if not any(abs(target_value - rate) <= 1e-9 for rate in rates):
            bad.append((row_number, target_value, rates))
if bad:
    raise SystemExit("policy_target_rate outside feedback_rates ladder: {0}".format(bad))
print("policy_target_rate values are from the feedback_rates ladder")
'@ | python - (Join-Path $RunPath "segment_telemetry.csv")
```

## Ubuntu bash checks

Set the latest run directory:

```bash
export PHASE5E_RUN_ROOT="/mnt/outside_repo/phase5e_runs"
RUN_DIR="$(find "$PHASE5E_RUN_ROOT" -maxdepth 1 -type d -name 'run_*' -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d' ' -f2-)"
printf '%s\n' "$RUN_DIR"
```

Check required files and legacy absence:

```bash
for file in run_manifest.json config.resolved.json environment.json run.log segment_telemetry.csv evaluation_segments.csv; do
  test -f "$RUN_DIR/$file" && printf 'OK %s\n' "$file" || printf 'MISSING %s\n' "$file"
done

for file in dataset.csv dataset_training.csv; do
  test ! -e "$RUN_DIR/$file" && printf 'ABSENT %s\n' "$file" || printf 'UNEXPECTED %s\n' "$file"
done
```

Check manifest and headers:

```bash
python3 - "$RUN_DIR" <<'PY'
import csv
import json
import sys
from pathlib import Path

run_dir = Path(sys.argv[1])
manifest = json.loads((run_dir / "run_manifest.json").read_text(encoding="utf-8"))
print("status:", manifest["status"])
print("controller:", manifest["controller"]["name"])
print("outputs_are_benchmark_results:", manifest["benchmark_neutrality"]["outputs_are_benchmark_results"])

with (run_dir / "segment_telemetry.csv").open(newline="", encoding="utf-8") as handle:
    segment_header = next(csv.reader(handle))
with (run_dir / "evaluation_segments.csv").open(newline="", encoding="utf-8") as handle:
    eval_header = next(csv.reader(handle))

expected = {
    "feedback_neural_enabled",
    "feedback_neural_bundle_configured",
    "feedback_neural_bundle_loaded",
    "feedback_neural_bundle_schema_ok",
    "feedback_neural_bundle_hash_ok",
    "feedback_neural_feature_schema_ok",
    "feedback_neural_feature_vector_ok",
    "feedback_neural_missing_features",
    "feedback_neural_action_mask_valid_count",
    "feedback_neural_raw_action",
    "feedback_neural_raw_rate_Bps",
    "feedback_neural_safe_action",
    "feedback_neural_safe_rate_Bps",
    "feedback_neural_safety_intervened",
    "feedback_neural_fallback_used",
    "feedback_neural_fallback_reason",
    "feedback_neural_inference_ms",
    "feedback_neural_nan_inf_detected",
    "feedback_neural_invalid_action_detected",
    "feedback_neural_diagnostic_only",
}
missing = sorted(expected - set(segment_header))
contaminated = [column for column in eval_header if "neural_" in column]
forbidden_terms = ("rank", "winner", "improvement", "p_value", "p-value")
forbidden = [
    column for column in segment_header + eval_header
    if any(term in column.lower() for term in forbidden_terms)
]
print("missing_neural_segment_columns:", missing)
print("evaluation_neural_columns:", contaminated)
print("forbidden_claim_columns:", forbidden)
if missing or contaminated or forbidden:
    raise SystemExit(1)
PY
```

Check diagnostic-only marker and selected rates:

```bash
python3 - "$RUN_DIR/segment_telemetry.csv" <<'PY'
import ast
import csv
import sys

path = sys.argv[1]
diagnostic_values = set()
bad_rates = []
with open(path, newline="", encoding="utf-8") as handle:
    for row_number, row in enumerate(csv.DictReader(handle), start=2):
        diagnostic_values.add(row.get("feedback_neural_diagnostic_only", ""))
        target = row.get("policy_target_rate", "")
        if target in ("", None):
            continue
        try:
            target_value = float(target)
            rates = [float(value) for value in ast.literal_eval(row["feedback_rates"])]
        except Exception as exc:
            bad_rates.append((row_number, "parse_error", str(exc)))
            continue
        if not any(abs(target_value - rate) <= 1e-9 for rate in rates):
            bad_rates.append((row_number, target_value, rates))
print("neural_diagnostic_only values:", sorted(diagnostic_values))
if bad_rates:
    raise SystemExit("policy_target_rate outside feedback_rates ladder: {0}".format(bad_rates))
PY
```

## Acceptance notes

- Empty neural diagnostic cells can appear on rows before a controller decision.
- `feedback_neural_fallback_used=1` is not a failure by itself; inspect `feedback_neural_fallback_reason`.
- `evaluation_segments.csv` must remain compact and free of `neural_` fields.
- These checks are diagnostic-only and must not be converted into ranking evidence.
