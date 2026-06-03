# Phase 5E Ubuntu GStreamer structural smoke runbook

## Boundary

This smoke is optional and Ubuntu-only. It checks structural compatibility between `neural_abr_lite`, the config runner, and the GStreamer media engine path.

It is not benchmark-grade, not a controller comparison, not a network experiment, and not Phase 6 validation. GStreamer timing, VM bridge behavior, fakesink behavior, and local network serving are demo/integration context only.

## Environment checks

Run from the repository root on Ubuntu:

```bash
python3 scripts/check_environment.py --profile dev --strict
python3 scripts/check_environment.py --profile gst --strict
```

If the GStreamer profile fails, stop and record the environment issue. Do not interpret it as a neural controller result.

## Inputs outside the repo

Use a Phase 4F bundle outside the repository:

```bash
export NEURAL_ABR_BUNDLE="/mnt/outside_repo/neural_abr_lite_bundle"
```

Use a run root outside the repository:

```bash
export PHASE5E_RUN_ROOT="/mnt/outside_repo/phase5e_gst_runs"
export PHASE5E_CONFIG="/tmp/phase5e_neural_abr_lite.gst.yaml"
```

Use a local MPD path or a VM-served MPD URL:

```bash
export PHASE5E_MPD_URL="http://192.168.56.10:8000/tiny.mpd"
```

If serving media from a VM, start the server outside the Git repo, for example:

```bash
python3 -m http.server 8000 --directory "$PHASE5E_MEDIA_ROOT"
```

The bridge/network path is structural demo plumbing only. It is not benchmark evidence and must not be compared against fake-engine runs.

## Headless/fakesink config

The current config supports `media_engine.name: "gst"`, `decode_video: false`, and `sink_name: null`. That headless mode should select fakesink behavior where supported.

Write a temporary config:

```bash
cat > "$PHASE5E_CONFIG" <<EOF
mpd_url: "$PHASE5E_MPD_URL"
media_engine:
  name: "gst"
  min_queue_time: 1.0
  decode_video: false
  sink_name: null
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
  drain_buffer_sleep_seconds: 0.5
  preroll_seconds: 10.0
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

## Inspect

Find the latest run:

```bash
RUN_DIR="$(find "$PHASE5E_RUN_ROOT" -maxdepth 1 -type d -name 'run_*' -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d' ' -f2-)"
printf '%s\n' "$RUN_DIR"
```

Then run the Ubuntu commands in `../phase5e_artifact_inspection_checklist.md`.

Expected structural signals:

- `run_manifest.json` status is `completed`.
- `media_engine.name` is `gst`.
- `controller.name` is `neural_abr_lite`.
- `segment_telemetry.csv` contains neural diagnostic columns.
- `evaluation_segments.csv` contains no neural diagnostic columns.
- No legacy dataset artifacts are produced.

## Interpretation

Passing this smoke means the GStreamer run path can host the guarded controller structurally. It does not validate playback quality, controller superiority, QoE, startup quality, stall behavior, or network realism.
