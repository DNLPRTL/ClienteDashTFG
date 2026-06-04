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

from core.trace_replay.inventory import build_raw_dataset_inventory, write_raw_dataset_inventory

TFG_ROOT = REPO_ROOT.parent
DEFAULT_RAW_ROOT = TFG_ROOT / "dataset en bruto"
DEFAULT_OUTPUT = TFG_ROOT / "auditorias_trazas" / "phase3" / "phase3_raw_dataset_inventory.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 3A read-only raw dataset inventory.")
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--hash-mode", choices=("full", "sample", "none"), default="full")
    args = parser.parse_args(argv)

    inventory = build_raw_dataset_inventory(args.raw_root, hash_mode=args.hash_mode)
    output_path = write_raw_dataset_inventory(inventory, args.output)
    print(
        json.dumps(
            {
                "schema_id": inventory["schema_id"],
                "raw_root": inventory["raw_root"],
                "hash_mode": inventory["hash_mode"],
                "dataset_count": inventory["dataset_count"],
                "file_count": inventory["file_count"],
                "total_bytes": inventory["total_bytes"],
                "output": str(output_path),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
