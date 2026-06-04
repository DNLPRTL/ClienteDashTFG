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

from core.evaluation.artifacts import QoEArtifactError, compute_qoe_artifacts_from_dry_run


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compute QoE artifacts from one trace dry-run-like directory.")
    parser.add_argument("--dry-run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--expected-segment-count", type=int)
    parser.add_argument("--min-bitrate-kbps", type=float)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    try:
        result = compute_qoe_artifacts_from_dry_run(
            dry_run_dir=args.dry_run_dir,
            output_dir=args.output_dir,
            expected_segment_count=args.expected_segment_count,
            min_bitrate_kbps=args.min_bitrate_kbps,
            overwrite=args.overwrite,
        )
    except QoEArtifactError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2, sort_keys=True))
        return 1

    print(json.dumps({"status": "PASS", **result.__dict__}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
