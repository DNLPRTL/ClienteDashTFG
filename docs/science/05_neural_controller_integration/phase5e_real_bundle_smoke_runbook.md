# Phase 5E real bundle smoke runbook

## Boundary

This runbook exercises a real local Phase 4F NeuralABR-Lite bundle through the DashClientModular4 client path. It is structural smoke only. It is not a benchmark, not a controller comparison, and not Phase 6 validation.

The bundle and run outputs must stay outside the repository.

## Required inputs

The bundle directory must contain:

```text
bundle_manifest.json
model_card.json
feature_schema.json
normalization_stats.json
ladder_schema.json
inference_contract.json
fallback_policy.json
model_state.pt
```

Use a local MPD path or a VM-served MPD URL. Do not add media, segments, run outputs, logs, CSVs, or model files to Git.

## Windows PowerShell fake-engine smoke

Set placeholders:

```powershell
$BundleDir = "D:\outside_repo\neural_abr_lite_bundle"
$RunRoot = "D:\outside_repo\phase5e_runs"
$ConfigPath = "$env:TEMP\phase5e_neural_abr_lite.fake.yaml"
$MpdUrl = "D:\outside_repo\dash_media\tiny.mpd"
```

Write a temporary config outside the repo:

```powershell
@"
mpd_url: '$MpdUrl'
media_engine:
  name: 'fake'
  min_queue_time: 0.001
controller:
  name: 'neural_abr_lite'
  params:
    bundle_dir: '$BundleDir'
    enabled: true
    verify_hashes: true
    fallback_controller: 'robust_mpc'
    diagnostic_telemetry: true
    fail_closed: true
    idle_duration: 0.0
playback:
  initial_quality: 0
  initial_controller_decision: false
  headless: true
  max_buffer_seconds: 60.0
  drain_buffer_sleep_seconds: 0.01
  preroll_seconds: 0.0
downloader:
  max_retries: 3
  verbose: false
output:
  root_dir: '$RunRoot'
  segment_telemetry_filename: 'segment_telemetry.csv'
  evaluation_segments_filename: 'evaluation_segments.csv'
logging:
  enabled: true
  level: 'WARNING'
analysis:
  enabled: false
"@ | Set-Content -Path $ConfigPath -Encoding UTF8
```

Run the client:

```powershell
python main.py --config $ConfigPath
```

Find the latest run directory:

```powershell
$RunDir = Get-ChildItem -Path $RunRoot -Directory |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1
$RunDir.FullName
```

Then use `phase5e_artifact_inspection_checklist.md`.

## Windows no-bundle fallback smoke

This optional smoke uses the same path but omits `bundle_dir`. It should complete without crashing and should record fallback diagnostics such as `missing_bundle_dir`.

```powershell
$RunRoot = "D:\outside_repo\phase5e_no_bundle_runs"
$ConfigPath = "$env:TEMP\phase5e_neural_abr_lite.no_bundle.yaml"
$MpdUrl = "D:\outside_repo\dash_media\tiny.mpd"

@"
mpd_url: '$MpdUrl'
media_engine:
  name: 'fake'
  min_queue_time: 0.001
controller:
  name: 'neural_abr_lite'
  params:
    enabled: true
    fallback_controller: 'robust_mpc'
    diagnostic_telemetry: true
    fail_closed: true
    idle_duration: 0.0
playback:
  initial_quality: 0
  initial_controller_decision: false
  headless: true
  max_buffer_seconds: 60.0
  drain_buffer_sleep_seconds: 0.01
  preroll_seconds: 0.0
downloader:
  max_retries: 3
  verbose: false
output:
  root_dir: '$RunRoot'
  segment_telemetry_filename: 'segment_telemetry.csv'
  evaluation_segments_filename: 'evaluation_segments.csv'
logging:
  enabled: true
  level: 'WARNING'
analysis:
  enabled: false
"@ | Set-Content -Path $ConfigPath -Encoding UTF8

python main.py --config $ConfigPath
```

## Ubuntu fake-engine smoke

Set placeholders:

```bash
export NEURAL_ABR_BUNDLE="/mnt/outside_repo/neural_abr_lite_bundle"
export PHASE5E_RUN_ROOT="/mnt/outside_repo/phase5e_runs"
export PHASE5E_CONFIG="/tmp/phase5e_neural_abr_lite.fake.yaml"
export PHASE5E_MPD_URL="/mnt/outside_repo/dash_media/tiny.mpd"
```

Write the config:

```bash
cat > "$PHASE5E_CONFIG" <<EOF
mpd_url: "$PHASE5E_MPD_URL"
media_engine:
  name: "fake"
  min_queue_time: 0.001
controller:
  name: "neural_abr_lite"
  params:
    bundle_dir: "$NEURAL_ABR_BUNDLE"
    enabled: true
    verify_hashes: true
    fallback_controller: "robust_mpc"
    diagnostic_telemetry: true
    fail_closed: true
    idle_duration: 0.0
playback:
  initial_quality: 0
  initial_controller_decision: false
  headless: true
  max_buffer_seconds: 60.0
  drain_buffer_sleep_seconds: 0.01
  preroll_seconds: 0.0
downloader:
  max_retries: 3
  verbose: false
output:
  root_dir: "$PHASE5E_RUN_ROOT"
  segment_telemetry_filename: "segment_telemetry.csv"
  evaluation_segments_filename: "evaluation_segments.csv"
logging:
  enabled: true
  level: "WARNING"
analysis:
  enabled: false
EOF
```

Run:

```bash
python3 main.py --config "$PHASE5E_CONFIG"
```

Find the latest run directory:

```bash
RUN_DIR="$(find "$PHASE5E_RUN_ROOT" -maxdepth 1 -type d -name 'run_*' -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d' ' -f2-)"
printf '%s\n' "$RUN_DIR"
```

Then use `phase5e_artifact_inspection_checklist.md`.

## Expected structural outcomes

- Exit code is `0`.
- `run_manifest.json` status is `completed`.
- Manifest controller name is `neural_abr_lite`.
- Segment telemetry contains `feedback_neural_*` diagnostic columns.
- Evaluation telemetry contains no neural diagnostic columns.
- Any fallback is represented as diagnostic-only telemetry.
- No output is interpreted as benchmark evidence.
