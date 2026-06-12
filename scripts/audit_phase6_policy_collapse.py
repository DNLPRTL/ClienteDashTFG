from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase45_v3.policy_collapse_audit import (
    PolicyCollapseAuditConfig,
    PolicyCollapseAuditError,
    audit_phase6_policy_collapse,
    write_audit_json,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audita colapso conservador de un controller propio en un paquete Phase 6."
    )
    parser.add_argument("--phase6-results-dir", required=True, help="Raiz del paquete Phase 6 o carpeta 02_resultados.")
    parser.add_argument("--controller-alias", default="propio_spbc_v2_anchor")
    parser.add_argument("--baseline-alias", default="base_robust_mpc")
    parser.add_argument("--output-json")
    parser.add_argument("--fail-on-collapse", action="store_true")
    parser.add_argument("--allow-fallback", action="store_true")
    parser.add_argument("--max-high-capacity-action0-rate", type=float, default=0.05)
    parser.add_argument("--max-consecutive-action0-after-startup", type=int, default=2)
    parser.add_argument("--reach-bitrate-kbps", type=float, default=2850.0)
    args = parser.parse_args(argv)

    config = PolicyCollapseAuditConfig(
        controller_alias=args.controller_alias,
        baseline_alias=args.baseline_alias,
        max_high_capacity_action0_rate=args.max_high_capacity_action0_rate,
        max_consecutive_action0_after_startup=args.max_consecutive_action0_after_startup,
        reach_bitrate_kbps=args.reach_bitrate_kbps,
        require_no_fallback=not bool(args.allow_fallback),
    )
    try:
        report = audit_phase6_policy_collapse(args.phase6_results_dir, config)
    except PolicyCollapseAuditError as exc:
        print("POLICY_COLLAPSE_AUDIT_ERROR {0}".format(exc), file=sys.stderr)
        return 2

    if args.output_json:
        write_audit_json(report, args.output_json)
    print(
        "policy_collapse_audit status={0} collapse_detected={1} controller={2} "
        "high_capacity_action0_rate={3:.6f} max_consecutive_action0={4} "
        "fallback_rows={5} qoe_delta_vs_baseline={6:.6f}".format(
            report["status"],
            report["collapse_detected"],
            args.controller_alias,
            float(report["metrics"]["high_capacity_safe_action0_rate"]),  # type: ignore[index]
            int(report["metrics"]["max_consecutive_action0_after_startup"]),  # type: ignore[index]
            int(report["metrics"]["fallback_row_count"]),  # type: ignore[index]
            float(report["metrics"]["qoe_delta_vs_baseline_mean"]),  # type: ignore[index]
        )
    )
    if args.output_json:
        print("audit_json={0}".format(args.output_json))
    else:
        print(json.dumps(report, indent=2, sort_keys=True))
    if args.fail_on_collapse and report["status"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
