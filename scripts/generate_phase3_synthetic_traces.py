#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
TFG_ROOT = REPO_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.trace_replay.manifest_validation import validate_phase3_trace_manifest_data
from core.trace_replay.synthetic import (
    DEFAULT_SYNTHETIC_COUNT_PER_SCENARIO,
    DEFAULT_SYNTHETIC_SAMPLE_DURATION_S,
    DEFAULT_SYNTHETIC_SEED,
    DEFAULT_SYNTHETIC_TRACE_DURATION_S,
    SYNTHETIC_DATASET_ID,
    generate_synthetic_trace_set,
    merge_synthetic_entries_into_manifest,
)


DEFAULT_MANIFEST_ROOT = TFG_ROOT / "manifests_trazas" / "phase3" / "final"
DEFAULT_NORMALIZED_ROOT = TFG_ROOT / "datasets_normalizados" / "phase3" / "final"
DEFAULT_AUDIT_ROOT = TFG_ROOT / "auditorias_trazas" / "phase3" / "final"
FINAL_MANIFEST = "phase3_trace_manifest_final.json"
FINAL_SNAPSHOT = "phase3_trace_manifest_final_real_only_snapshot.json"
CURATED_MANIFEST = "phase3_trace_manifest_curated.json"
CURATED_SNAPSHOT = "phase3_trace_manifest_curated_real_only_snapshot.json"
GENERATION_REPORT = "phase3_synthetic_trace_generation_report.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate controlled synthetic Phase 3 traces and merge them into final manifests.")
    parser.add_argument("--manifest-root", type=Path, default=DEFAULT_MANIFEST_ROOT)
    parser.add_argument("--normalized-root", type=Path, default=DEFAULT_NORMALIZED_ROOT)
    parser.add_argument("--audit-root", type=Path, default=DEFAULT_AUDIT_ROOT)
    parser.add_argument("--count-per-scenario", type=int, default=DEFAULT_SYNTHETIC_COUNT_PER_SCENARIO)
    parser.add_argument("--duration-s", type=int, default=DEFAULT_SYNTHETIC_TRACE_DURATION_S)
    parser.add_argument("--sample-duration-s", type=float, default=DEFAULT_SYNTHETIC_SAMPLE_DURATION_S)
    parser.add_argument("--seed", default=DEFAULT_SYNTHETIC_SEED)
    parser.add_argument("--train-ratio", type=float, default=0.7)
    parser.add_argument("--test-ratio", type=float, default=0.15)
    args = parser.parse_args(argv)

    manifest_root = args.manifest_root
    final_path = manifest_root / FINAL_MANIFEST
    final_snapshot_path = manifest_root / FINAL_SNAPSHOT
    curated_path = manifest_root / CURATED_MANIFEST
    curated_snapshot_path = manifest_root / CURATED_SNAPSHOT
    _preserve_snapshot(final_path, final_snapshot_path)
    if curated_path.is_file():
        _preserve_snapshot(curated_path, curated_snapshot_path)

    base_manifest = json.loads(final_snapshot_path.read_text(encoding="utf-8"))
    validate_phase3_trace_manifest_data(base_manifest)
    synthetic_entries, generation_report = generate_synthetic_trace_set(
        normalized_root=args.normalized_root,
        metadata_root=manifest_root,
        count_per_scenario=args.count_per_scenario,
        duration_s=args.duration_s,
        sample_duration_s=args.sample_duration_s,
        seed=args.seed,
        train_ratio=args.train_ratio,
        test_ratio=args.test_ratio,
        clean=True,
    )
    merged_manifest = merge_synthetic_entries_into_manifest(base_manifest, synthetic_entries)
    merged_manifest["real_only_snapshot_manifest_path"] = str(final_snapshot_path)
    merged_manifest["synthetic_generation_report_path"] = str(args.audit_root / GENERATION_REPORT)
    validate_phase3_trace_manifest_data(merged_manifest)
    final_path.write_text(json.dumps(merged_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    args.audit_root.mkdir(parents=True, exist_ok=True)
    generation_report.update(
        {
            "final_manifest_path": str(final_path),
            "real_only_snapshot_manifest_path": str(final_snapshot_path),
            "curated_real_only_snapshot_manifest_path": str(curated_snapshot_path) if curated_snapshot_path.is_file() else None,
        }
    )
    report_path = args.audit_root / GENERATION_REPORT
    report_path.write_text(json.dumps(generation_report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "PASS",
                "synthetic_dataset_id": SYNTHETIC_DATASET_ID,
                "synthetic_trace_count": generation_report["trace_count"],
                "synthetic_split_counts": generation_report["split_counts"],
                "final_manifest_path": str(final_path),
                "generation_report_path": str(report_path),
                "ready_for_benchmark": False,
                "benchmark_authorized": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def _preserve_snapshot(source: Path, snapshot: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(source)
    if snapshot.is_file():
        return
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, snapshot)


if __name__ == "__main__":
    raise SystemExit(main())
