# QoE artifact computation spec

Status: implemented_phase3_5_rebuild.

El postprocesador QoE procesa exactamente un directorio dry-run-like por invocacion.

Entrada:

```text
trace_dry_run_segments.csv
trace_dry_run_summary.json
trace_dry_run_manifest.json
```

Columnas requeridas en `trace_dry_run_segments.csv`:

```text
representation_bitrate_kbps
rebuffer_s
```

Salida:

```text
qoe_segment_rewards.csv
qoe_run_summary.json
qoe_artifact_manifest.json
```

CLI:

```powershell
python scripts\compute_qoe_from_dry_run.py --dry-run-dir <dir> --output-dir <dir> --overwrite
```

La salida siempre conserva:

```text
outputs_are_benchmark_results=false
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
ia_training_performed=false
```

No ejecuta controllers, no genera dry-runs, no agrega resultados y no compara algoritmos.
