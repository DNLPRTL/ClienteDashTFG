from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

from core.output_artifacts import LEGACY_OUTPUT_FILENAMES


REQUIRED_DIRS = ("00_protocolo", "01_ejecucion", "02_resultados", "03_graficas", "04_informe")
REQUIRED_RESULT_FILES = (
    "raw_chunks.csv",
    "session_summary.csv",
    "aggregates_by_controller.json",
    "statistics.json",
    "resultados_para_validar.json",
    "resultados_para_validar.md",
)


def verify_phase6_package(
    package_root: str | Path,
    *,
    require_plots: bool = True,
    write_artifacts: bool = True,
) -> Dict[str, Any]:
    root = Path(package_root)
    results_dir = root / "02_resultados"
    plots_dir = root / "03_graficas"
    protocol = _read_json(root / "00_protocolo" / "protocolo_validacion.json")
    session_plan = _read_json(root / "00_protocolo" / "session_plan.json")
    results = _read_json(results_dir / "resultados_para_validar.json")
    summaries = _read_csv_dicts(results_dir / "session_summary.csv")
    raw_chunks = _read_csv_dicts(results_dir / "raw_chunks.csv")
    plot_manifest = _read_json(plots_dir / "plot_manifest.json")

    sessions = session_plan.get("sessions", []) if isinstance(session_plan, Mapping) else []
    sessions = [item for item in sessions if isinstance(item, Mapping)]
    failed_rows = [row for row in summaries if str(row.get("run_status")) not in {"completed", "missing"}]
    missing_rows = [row for row in summaries if str(row.get("run_status")) == "missing"]
    completed_rows = [row for row in summaries if str(row.get("run_status")) == "completed"]
    evaluable_rows = [row for row in summaries if _int(row.get("evaluable"))]
    failed_session_ids = {str(row.get("session_id")) for row in failed_rows}
    raw_failed_rows = [row for row in raw_chunks if str(row.get("session_id")) in failed_session_ids]
    legacy_paths = _legacy_artifact_paths(root)
    plot_checks = _verify_plots(plot_manifest, plots_dir=plots_dir, require_plots=require_plots)

    checks = [
        _check("package_root_exists", root.is_dir(), str(root)),
        _check("required_dirs_present", all((root / name).is_dir() for name in REQUIRED_DIRS), ", ".join(REQUIRED_DIRS)),
        _check(
            "required_result_files_present",
            all((results_dir / name).is_file() for name in REQUIRED_RESULT_FILES),
            ", ".join(REQUIRED_RESULT_FILES),
        ),
        _check("session_plan_present", bool(sessions), "{0} sessions".format(len(sessions))),
        _check("session_summary_matches_plan", len(summaries) == len(sessions), "{0}/{1}".format(len(summaries), len(sessions))),
        _check("no_failed_sessions", not failed_rows and not missing_rows, _failure_summary(failed_rows + missing_rows)),
        _check("completed_sessions_evaluable", len(completed_rows) == len(evaluable_rows), "{0}/{1}".format(len(evaluable_rows), len(completed_rows))),
        _check("failed_sessions_not_in_raw_chunks", not raw_failed_rows, "{0} raw rows".format(len(raw_failed_rows))),
        _check("legacy_artifacts_absent", not legacy_paths, ", ".join(legacy_paths[:10])),
        _check("synthetic_reported_separately", _synthetic_reported(results, summaries), ""),
        _check("audit_text_package_available", (results_dir / "resultados_para_validar.md").is_file() and (results_dir / "resultados_para_validar.json").is_file(), ""),
    ]
    checks.extend(plot_checks)

    package = {
        "schema_version": "phase6_package_verification_v1",
        "package_root": str(root),
        "preset": str(protocol.get("preset", "")),
        "counts": {
            "planned": len(sessions),
            "summarized": len(summaries),
            "completed": len(completed_rows),
            "failed": len(failed_rows),
            "missing": len(missing_rows),
            "evaluable": len(evaluable_rows),
            "raw_chunks": len(raw_chunks),
        },
        "failure_reasons": _failure_reasons(failed_rows + missing_rows),
        "checks": checks,
        "all_checks_passed": all(bool(item["passed"]) for item in checks),
        "artifacts": {
            "verification_json": str(results_dir / "verificacion_paquete.json"),
            "verification_md": str(results_dir / "verificacion_paquete.md"),
        },
    }
    if write_artifacts:
        results_dir.mkdir(parents=True, exist_ok=True)
        (results_dir / "verificacion_paquete.json").write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
        (results_dir / "verificacion_paquete.md").write_text(render_phase6_verification_markdown(package), encoding="utf-8")
        _append_verification_to_validation_markdown(results_dir / "resultados_para_validar.md", package)
    return package


def render_phase6_verification_markdown(package: Mapping[str, Any]) -> str:
    lines = [
        "# Verificacion de paquete Phase 6",
        "",
        "- Veredicto tecnico: {0}".format("OK" if package.get("all_checks_passed") else "NO OK"),
        "- Preset: {0}".format(package.get("preset", "")),
        "",
        "## Conteos",
        "",
    ]
    counts = _mapping(package.get("counts"))
    for key in ("planned", "summarized", "completed", "failed", "missing", "evaluable", "raw_chunks"):
        lines.append("- {0}: {1}".format(key, counts.get(key, 0)))
    lines.extend(["", "## Checks", ""])
    for check in package.get("checks", []):
        if not isinstance(check, Mapping):
            continue
        lines.append("- {0}: {1} {2}".format(check.get("name", ""), "OK" if check.get("passed") else "FAIL", check.get("detail", "")))
    reasons = package.get("failure_reasons", [])
    if reasons:
        lines.extend(["", "## Motivos de fallo", ""])
        for row in reasons:
            if isinstance(row, Mapping):
                lines.append("- {0} sesiones: {1}".format(row.get("count", 0), row.get("reason", "")))
    return "\n".join(lines) + "\n"


def _verify_plots(plot_manifest: Mapping[str, Any], *, plots_dir: Path, require_plots: bool) -> List[Dict[str, Any]]:
    plots = plot_manifest.get("plots", []) if isinstance(plot_manifest, Mapping) else []
    plots = [dict(item) for item in plots if isinstance(item, Mapping)]
    generated = [item for item in plots if item.get("status") == "generated"]
    bad_generated = [
        item
        for item in generated
        if not _resolved_plot_path(item, plots_dir).is_file() or _resolved_plot_path(item, plots_dir).stat().st_size <= 0
    ]
    errored = [item for item in plots if item.get("status") == "error"]
    checks = [
        _check("plot_manifest_present", bool(plots) or not require_plots, "{0} plots".format(len(plots))),
        _check("plots_without_errors", not errored, _plot_problem_summary(errored)),
        _check("generated_plots_non_empty", not bad_generated, _plot_problem_summary(bad_generated)),
    ]
    if require_plots:
        checks.append(_check("at_least_one_plot_generated", bool(generated), "{0} generated".format(len(generated))))
    return checks


def _resolved_plot_path(item: Mapping[str, Any], plots_dir: Path) -> Path:
    configured = Path(str(item.get("path", "")))
    if configured.is_file():
        return configured
    if configured.name:
        return plots_dir / configured.name
    return configured


def _append_verification_to_validation_markdown(path: Path, package: Mapping[str, Any]) -> None:
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    marker = "\n## Verificacion automatica de paquete\n"
    if marker in text:
        text = text.split(marker, 1)[0].rstrip() + "\n"
    verdict = "OK" if package.get("all_checks_passed") else "NO OK"
    failed = [item for item in package.get("checks", []) if isinstance(item, Mapping) and not item.get("passed")]
    lines = [
        marker.strip(),
        "",
        "- Veredicto tecnico: {0}".format(verdict),
        "- Checks fallidos: {0}".format(len(failed)),
    ]
    for item in failed[:10]:
        lines.append("- {0}: {1}".format(item.get("name", ""), item.get("detail", "")))
    path.write_text(text.rstrip() + "\n\n" + "\n".join(lines) + "\n", encoding="utf-8")


def _check(name: str, passed: bool, detail: str) -> Dict[str, Any]:
    return {"name": name, "passed": bool(passed), "detail": str(detail or "")}


def _failure_reasons(rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    counter = Counter(str(row.get("failure_reason", "") or row.get("non_evaluable_reason", "") or "sin motivo") for row in rows)
    return [{"reason": reason, "count": count} for reason, count in counter.most_common()]


def _failure_summary(rows: Sequence[Mapping[str, Any]]) -> str:
    reasons = _failure_reasons(rows)
    return ", ".join("{0} x {1}".format(row["count"], row["reason"]) for row in reasons[:5])


def _plot_problem_summary(rows: Sequence[Mapping[str, Any]]) -> str:
    return ", ".join(str(row.get("plot_id", "")) for row in rows[:10])


def _synthetic_reported(results: Mapping[str, Any], summaries: Sequence[Mapping[str, Any]]) -> bool:
    gates = _mapping(results.get("gates"))
    gate_items = _mapping(gates.get("gate_items"))
    if "synthetic_reported_separately" in gate_items:
        return _bool(gate_items.get("synthetic_reported_separately"))
    return any(_bool(row.get("synthetic")) for row in summaries)


def _legacy_artifact_paths(root: Path) -> List[str]:
    found = []
    runs_root = root / "01_ejecucion" / "runs"
    if not runs_root.is_dir():
        return found
    legacy = set(LEGACY_OUTPUT_FILENAMES)
    for path in runs_root.rglob("*"):
        if path.is_file() and path.name in legacy:
            found.append(str(path))
    return found


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _read_csv_dicts(path: Path) -> List[Dict[str, str]]:
    if not path.is_file():
        return []
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "on", "si"}


def _int(value: Any, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return int(default)
