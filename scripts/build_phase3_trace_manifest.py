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

from core.trace_replay.splits import build_phase3_trace_manifest

TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST_ROOT = TFG_ROOT / "manifests_trazas" / "phase3"
DEFAULT_INPUT = DEFAULT_MANIFEST_ROOT / "phase3_trace_conversion_manifest.json"
DEFAULT_OUTPUT = DEFAULT_MANIFEST_ROOT / "phase3_trace_manifest_final.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 3D build final split manifest from normalized traces.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--seed", default="phase3_rebuild_v1")
    parser.add_argument("--train-ratio", type=float, default=0.7)
    parser.add_argument("--test-ratio", type=float, default=0.15)
    args = parser.parse_args(argv)

    conversion_manifest = json.loads(args.input.read_text(encoding="utf-8"))
    manifest = build_phase3_trace_manifest(
        conversion_manifest.get("traces", ()),
        seed=args.seed,
        train_ratio=args.train_ratio,
        test_ratio=args.test_ratio,
    )
    manifest["source_conversion_manifest"] = str(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    print(
        json.dumps(
            {
                "schema_id": manifest["schema_id"],
                "trace_count": manifest["trace_count"],
                "excluded_duplicate_count": manifest["excluded_duplicate_count"],
                "split_counts": manifest["split_counts"],
                "output": str(args.output),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
