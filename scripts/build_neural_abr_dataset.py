#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.dataset_builder import build_synthetic_smoke_dataset


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an offline NeuralABR-Lite dataset.")
    parser.add_argument("--synthetic-smoke", action="store_true", help="Build the diagnostic synthetic smoke dataset.")
    parser.add_argument("--output-dir", required=True, help="Output directory outside the repository.")
    parser.add_argument("--overwrite", action="store_true", help="Replace the output directory if it exists.")
    args = parser.parse_args(argv)

    if not args.synthetic_smoke:
        parser.error("Phase 4D currently supports --synthetic-smoke only")

    result = build_synthetic_smoke_dataset(args.output_dir, overwrite=args.overwrite)
    print("NeuralABR-Lite dataset build summary")
    print("dataset_dir: {0}".format(result["dataset_dir"]))
    print("sample_counts: {0}".format(json.dumps(result["sample_counts"], sort_keys=True)))
    print("diagnostic_only: true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
