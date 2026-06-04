#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.trace_replay.manifest_validation import validate_phase3_trace_manifest_data
from core.trace_replay.quality import TraceQualityPolicy, build_quality_audit

TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_final.json"
DEFAULT_AUDIT = TFG_ROOT / "auditorias_trazas" / "phase3" / "final" / "phase3_trace_quality_audit.json"
DEFAULT_CURATED = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit Phase 3 trace quality and build a curated manifest.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--output-curated-manifest", type=Path, default=DEFAULT_CURATED)
    parser.add_argument("--min-samples", type=int, default=30)
    parser.add_argument("--min-duration-s", type=float, default=30.0)
    parser.add_argument("--mostly-zero-threshold", type=float, default=0.5)
    parser.add_argument("--extreme-throughput-kbps", type=float, default=1_000_000.0)
    args = parser.parse_args(argv)

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    validate_phase3_trace_manifest_data(manifest)
    policy = TraceQualityPolicy(
        min_samples=args.min_samples,
        min_duration_s=args.min_duration_s,
        mostly_zero_threshold=args.mostly_zero_threshold,
        extreme_throughput_kbps=args.extreme_throughput_kbps,
    )
    audit, curated_manifest = build_quality_audit(manifest, policy=policy)
    validate_phase3_trace_manifest_data(curated_manifest)

    audit["source_manifest_path"] = str(args.manifest)
    audit["curated_manifest_path"] = str(args.output_curated_manifest)
    args.output_audit.parent.mkdir(parents=True, exist_ok=True)
    args.output_curated_manifest.parent.mkdir(parents=True, exist_ok=True)
    args.output_audit.write_text(json.dumps(audit, indent=2, sort_keys=True), encoding="utf-8")
    args.output_curated_manifest.write_text(json.dumps(curated_manifest, indent=2, sort_keys=True), encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "PASS",
                "source_manifest_trace_count": audit["source_manifest_trace_count"],
                "kept_trace_count": audit["kept_trace_count"],
                "excluded_trace_count": audit["excluded_trace_count"],
                "quality_exclusion_counts": audit["quality_exclusion_counts"],
                "quality_flag_counts": audit["quality_flag_counts"],
                "audit_path": str(args.output_audit),
                "curated_manifest_path": str(args.output_curated_manifest),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
