# Phase 3 Rebuild Closure Report

Date: 2026-06-04

## Verdict

Windows closure status: PASS.

Phase 3 Rebuild has a final external trace corpus and a validated final manifest. This is not a benchmark, not IA training, not a ranking and not a QoE claim.

Ubuntu client validation is still required after `git pull` before advancing operationally.

## Final Artifacts

External raw root:

```text
C:\Users\danie\Documents\TFG\dataset en bruto
```

Final external artifacts:

```text
C:\Users\danie\Documents\TFG\auditorias_trazas\phase3\final\phase3_raw_dataset_inventory.json
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_conversion_manifest.json
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_final.json
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_closure_report.json
C:\Users\danie\Documents\TFG\runs_trazas\phase3\final\phase3_trace_replay_smoke_summary.json
```

The final corpus is defined by `phase3_trace_manifest_final.json`, not by walking the normalized directory.

After the quality audit, the recommended usable corpus for training/evaluation preparation is:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
```

This curated manifest keeps bad/intermittent network traces when they have enough signal, and excludes only traces that are too short or all-zero.

## Final Counts

Final accepted traces:

```text
trace_count=5957
excluded_duplicate_count=11
```

Splits:

```text
train=4139
test=904
eval=914
```

Semantics:

```text
available_bandwidth=917
active_fixed_broadband_download_test=4302
active_mobile_speedtest=522
observed_application_traffic=122
real_streaming_delivery_rate=94
```

Puffer policy:

```text
mode=bounded_video_sent_acked_join
max_sessions=100
min_samples_per_session=30
max_acked_rows=1000000
max_sent_rows=2000000
```

Puffer produced 94 valid sessions under the bounded policy.

## Windows Commands Run

```powershell
python -m unittest discover
python scripts\check_client_readiness.py --strict
python scripts\run_phase3_trace_closure.py --artifact-set final --clean-derived
python scripts\validate_phase3_trace_manifest.py --manifest "C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_final.json"
```

Validation result:

```text
status=PASS
ready_for_benchmark=false
benchmark_authorized=false
```

Technical replay smoke:

```text
success_count=5
failure_count=0
```

One trace per semantics was loaded and used to simulate a synthetic segment download. This is a technical smoke only.

## Ubuntu Client Validation

After the branch is pushed:

```bash
cd ~/TFG/DashClientModular4
git checkout rebuild/phase3-from-phase2
git pull --ff-only
python -m unittest discover
python scripts/check_client_readiness.py --strict
python scripts/validate_phase3_trace_manifest.py --manifest "<ubuntu-path-to>/manifests_trazas/phase3/final/phase3_trace_manifest_final.json"
```

If Ubuntu paths differ from Windows paths inside the manifest, regenerate the final artifacts on Ubuntu with:

```bash
python scripts/run_phase3_trace_closure.py --raw-root "<ubuntu-path-to>/dataset en bruto" --artifact-set final --clean-derived
python scripts/validate_phase3_trace_manifest.py --manifest "<ubuntu-path-to>/manifests_trazas/phase3/final/phase3_trace_manifest_final.json"
```

## Guardrails

The manifest keeps:

```text
ready_for_benchmark=false
benchmark_authorized=false
outputs_are_benchmark_results=false
```

Training, QoE, plots, rankings and winner claims remain unauthorized.
