#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.validation import validate_offline_run


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run offline NeuralABR-Lite sanity validation.")
    parser.add_argument("--dataset-dir", required=True, help="Dataset directory outside the repository.")
    parser.add_argument("--run-dir", required=True, help="Training run directory outside the repository.")
    parser.add_argument("--output-dir", required=True, help="Validation output directory outside the repository.")
    args = parser.parse_args(argv)

    report = validate_offline_run(args.dataset_dir, args.run_dir, args.output_dir)
    print("NeuralABR-Lite offline validation summary")
    print("status: {0}".format(report["status"]))
    print("validation_metrics: {0}".format(json.dumps(report["validation_metrics"], sort_keys=True)))
    print("ood_diagnostic_metrics: {0}".format(json.dumps(report["ood_diagnostic_metrics"], sort_keys=True)))
    print("diagnostic_only: true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
