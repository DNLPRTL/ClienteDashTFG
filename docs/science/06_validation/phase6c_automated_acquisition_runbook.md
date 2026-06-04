# Phase 6C Automated Acquisition Runbook

Status: Phase 6C automation contract. No benchmark authorization.

Phase 6C is automated. The user should not manually create source configuration JSON files, local manifests, candidate manifests or final manifests. The repository provides the source registry plus acquisition, extraction, normalization, manifest building, validation, audit and freeze scripts.

## Safe First Real Command

The first real materialization should focus on primary OOD sources only: Raca 4G LTE and Raca 5G. This is the recommended Windows command after the Phase 6C-H1 robustness hotfix:

Windows:

```powershell
python -u scripts\run_phase6c_trace_materialization.py ^
  --external-root C:\Users\danie\Documents\TFG\_datasets\phase6_validation ^
  --phase4-dataset-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate_20260529_080755\dataset_manifest.json ^
  --sources primary ^
  --download ^
  --extract ^
  --normalize ^
  --build-reference ^
  --build-candidate ^
  --validate ^
  --audit ^
  --freeze ^
  --strict ^
  --resume ^
  --skip-existing ^
  --clean-derived ^
  --progress-every 10
```

Ubuntu:

```bash
python -u scripts/run_phase6c_trace_materialization.py \
  --external-root /path/to/TFG/_datasets/phase6_validation \
  --phase4-dataset-manifest /path/to/TFG/_datasets/phase4_AI/neural_abr_lite/phase4E2_expanded_candidate_20260529_080755/dataset_manifest.json \
  --sources primary \
  --download \
  --extract \
  --normalize \
  --build-reference \
  --build-candidate \
  --validate \
  --audit \
  --freeze \
  --strict \
  --resume \
  --skip-existing \
  --clean-derived \
  --progress-every 10
```

If no action flags are supplied, the orchestrator runs the same full materialization sequence by default. If `--sources` is omitted, the source selection is `primary`.

## Source Selection

- `--sources primary` means `raca_4g_lte,raca_5g`.
- `--sources all` includes Lumos5G plus Ghent/HSDPA diagnostics, but Lancaster remains excluded.
- `--include-lumos` adds Lumos5G to the selected source set.
- `--include-diagnostic` adds Ghent and HSDPA diagnostic sources.
- A comma list such as `--sources raca_4g_lte,raca_5g` is also accepted.

Lumos5G is optional and may be blocked by Google Drive. Ghent and HSDPA are same-family diagnostic unless explicitly included. Lancaster is not downloaded, normalized or frozen as `use_for_eval`.

## External Layout

The orchestrator creates:

```text
<external_root>/
  raw/
  archives/
  extracted/
  normalized/
  manifests/
  reports/
  audit/
  receipts/
  logs/
  _local_inventory/
```

Real datasets, downloaded archives, extracted files, normalized CSVs, receipts, local manifests, reports and audit outputs live outside the repository. They must not be committed.

## Pipeline

1. Create the external directory layout.
2. Download configured public sources into `archives/`.
3. Extract zip archives safely into `extracted/`.
4. Normalize traces into `normalized_trace_schema_v1` CSVs.
5. Build `phase4_training_reference_manifest.json`.
6. Build `phase6_candidate_trace_manifest.json`.
7. Validate the candidate manifest with strict final schema checks.
8. Audit the candidate against the Phase 4 reference by `trace_id`, `leakage_group`, `checksum_sha256` and `canonical_content_fingerprint`.
9. Freeze `phase6_trace_manifest_final.json` only if validation and audit pass.
10. Write materialization summaries and command transcripts.

Download and extraction can pass while normalization still has a large input surface to inspect. Phase 6C-H1 hardens normalization with source filters, bounded sniffing, progress output, per-step logs and timeouts so an interrupted run can be resumed.

If normalization is interrupted, rerun the safe first command with:

```text
--resume --skip-existing --clean-derived
```

`--clean-derived` removes selected-source normalized outputs and per-trace metadata plus current-run candidate, validation, audit and freeze reports. It does not delete downloaded archives by default.

## Boundary

Phase 6C does not run dry-runs, controllers, QoE computation, statistical comparison, plots, rankings or benchmarks.

The external `phase6_trace_manifest_final.json` freezes trace IDs only after acquisition, normalization, validation, eligibility audit and freeze. It still records:

```json
{
  "ready_for_benchmark": false,
  "benchmark_authorized": false
}
```

`ready_for_phase6c` is not `ready_for_benchmark`.
