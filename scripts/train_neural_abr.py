#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.training import train_model


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a CPU NeuralABR-Lite behavior-cloning training smoke.")
    parser.add_argument("--dataset-dir", required=True, help="Dataset directory outside the repository.")
    parser.add_argument("--output-dir", required=True, help="Run directory outside the repository.")
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--smoke", action="store_true", help="Mark the run as a diagnostic smoke.")
    args = parser.parse_args(argv)

    report = train_model(
        dataset_dir=args.dataset_dir,
        output_dir=args.output_dir,
        epochs=args.epochs,
        batch_size=args.batch_size,
        seed=args.seed,
        device=args.device,
        smoke=args.smoke,
    )
    print("NeuralABR-Lite training smoke summary")
    print("status: PASS")
    print("device: {0}".format(report["device"]))
    print("loss_last: {0}".format(report["loss_last"]))
    print("validation_metrics: {0}".format(json.dumps(report["validation_metrics"], sort_keys=True)))
    print("diagnostic_only: true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
