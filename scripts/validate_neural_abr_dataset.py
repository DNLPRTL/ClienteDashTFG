#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.validation import validate_dataset_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an offline NeuralABR-Lite dataset.")
    parser.add_argument("--dataset-dir", required=True, help="Dataset directory outside the repository.")
    args = parser.parse_args(argv)

    report = validate_dataset_dir(args.dataset_dir, write_report=True)
    print("NeuralABR-Lite dataset validation summary")
    print("dataset_dir: {0}".format(report["dataset_dir"]))
    print("status: {0}".format(report["status"]))
    print("splits: {0}".format(json.dumps(report["splits"], sort_keys=True)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
