# Phase 3.5C QoE Artifact Computation Spec

Status: implemented_phase3_5c_isolated_post_processor.

PHASE_3_5C_COMPUTATION: isolated_post_processor

## Scope

Phase 3.5C adds an isolated post-processor that reads one dry-run artifact directory and writes QoE artifacts to an explicit output directory.

It does not modify the dry-run runner, execute a dry-run, aggregate controllers or produce benchmark evidence.

## Inputs

Required source files:

- `trace_dry_run_segments.csv`
- `trace_dry_run_summary.json`
- `trace_dry_run_manifest.json`

The segment CSV supplies bitrate and rebuffering inputs. The JSON files provide provenance and expected segment count when present.

## Outputs

Generated QoE files:

- `qoe_segment_rewards.csv`
- `qoe_run_summary.json`
- `qoe_artifact_manifest.json`

All outputs keep:

- `outputs_are_benchmark_results=false`
- `no_final_ranking=true`
- `eval_phase=phase3_5c_qoe_artifact_computation`

## API

The public implementation surface is in `core.evaluation.artifacts`:

- `QoEArtifactError`
- `QoEArtifactComputationResult`
- `load_segment_qoe_inputs_from_csv`
- `compute_qoe_summary_from_segments_csv`
- `compute_qoe_artifacts_from_dry_run`

## CLI

The CLI is:

```powershell
python scripts\compute_qoe_from_dry_run.py --dry-run-dir <dir> --output-dir <dir>
```

Optional arguments:

- `--expected-segment-count`
- `--min-bitrate-kbps`
- `--overwrite`

The CLI processes exactly one dry-run directory per invocation.

## Boundaries

- No runner integration.
- No dry-run execution.
- No benchmark.
- No ranking.
- No IA/training.
- No pandas or numpy.
- No dataset discovery.
