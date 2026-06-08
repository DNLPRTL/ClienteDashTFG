#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.evaluation.qoe import LINEAR_QOE_VERSION
from core.phase6 import PHASE6_SCHEMA_VERSION
from core.phase6.analysis import analyze_phase6_run
from core.phase6.catalog import controller_params, discover_comparable_controllers, media_profiles_for_preset, preset_spec
from core.phase6.config import load_phase6_config, write_phase6_example_config
from core.phase6.selection import load_trace_manifest, select_trace_windows


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Ejecuta Phase 6 validacion comparativa formal.")
    parser.add_argument("--config", default=None, help="Config local Phase 6. Por defecto usa config/phase6.local.yaml si existe.")
    parser.add_argument("--preset", choices=["rapido", "equilibrado", "extendido"], default=None)
    parser.add_argument("--output-root", default=None, help="Directorio externo de paquetes Phase 6.")
    parser.add_argument("--package-root", default=None, help="Carpeta Phase 6 existente para reanudar o analizar.")
    parser.add_argument("--dry-run", action="store_true", help="Genera protocolo y configs sin ejecutar sesiones.")
    parser.add_argument("--only-plan", action="store_true", help="Solo genera protocolo y plan.")
    parser.add_argument("--skip-analysis", action="store_true", help="No recalcula resultados al final.")
    parser.add_argument("--resume", dest="resume", action="store_true", default=None)
    parser.add_argument("--no-resume", dest="resume", action="store_false")
    parser.add_argument("--max-sessions", type=int, default=None, help="Limite tecnico para pruebas del runner.")
    parser.add_argument("--write-example-config", action="store_true", help="Regenera config/phase6.example.yaml y termina.")
    args = parser.parse_args(argv)

    if args.write_example_config:
        path = write_phase6_example_config()
        print("Config ejemplo escrita: {0}".format(path))
        return 0

    config = load_phase6_config(args.config)
    if args.preset:
        config.setdefault("experiment", {})["preset"] = args.preset
    if args.output_root:
        config.setdefault("paths", {})["output_root"] = args.output_root
    if args.package_root:
        config.setdefault("execution", {})["package_root"] = args.package_root
    if args.resume is not None:
        config.setdefault("execution", {})["resume"] = bool(args.resume)
    if args.max_sessions is not None:
        config.setdefault("execution", {})["max_sessions"] = int(args.max_sessions)

    package = run_phase6(
        config,
        dry_run=bool(args.dry_run),
        only_plan=bool(args.only_plan),
        skip_analysis=bool(args.skip_analysis),
    )
    print("Phase 6 package: {0}".format(package["package_root"]))
    print("Sessions planned: {0}".format(package["session_count"]))
    print("Sessions executed: {0}".format(package["executed_count"]))
    if package.get("analysis_path"):
        print("Resultados para validar: {0}".format(package["analysis_path"]))
    return 0 if package["failed_count"] == 0 else 1


def run_phase6(
    config: Mapping[str, Any],
    *,
    dry_run: bool = False,
    only_plan: bool = False,
    skip_analysis: bool = False,
) -> Dict[str, Any]:
    preset = str(_mapping(config.get("experiment")).get("preset", "rapido"))
    package_root = resolve_package_root(config, preset)
    existing = load_existing_protocol_package(package_root)
    if existing is None:
        protocol, sessions = build_phase6_protocol_and_plan(config, preset, package_root)
        write_protocol_package(package_root, protocol, sessions)
    else:
        protocol, sessions = existing

    executed_count = 0
    failed_count = 0
    if not dry_run and not only_plan and _bool(_mapping(config.get("execution")).get("run_sessions", True)):
        for session in sessions:
            result = run_session(config, session)
            executed_count += int(result["executed"])
            failed_count += int(result["failed"])

    analysis_path = ""
    if not dry_run and not only_plan and not skip_analysis and _bool(_mapping(config.get("execution")).get("run_analysis", True)):
        result_package = analyze_phase6_run(package_root)
        analysis_path = result_package["artifacts"]["resultados_para_validar_md"]

    return {
        "package_root": str(package_root),
        "session_count": len(sessions),
        "executed_count": executed_count,
        "failed_count": failed_count,
        "analysis_path": analysis_path,
    }


def build_phase6_protocol_and_plan(
    config: Mapping[str, Any],
    preset: str,
    package_root: Path,
) -> tuple[Dict[str, Any], List[Dict[str, Any]]]:
    paths = _mapping(config.get("paths"))
    experiment = _mapping(config.get("experiment"))
    execution = _mapping(config.get("execution"))
    manifest = load_trace_manifest(str(paths.get("manifest_path")))
    spec = preset_spec(preset)
    engine = str(experiment.get("engine", "fake")).lower()
    media_profiles = media_profiles_for_preset(preset, config)
    controllers = discover_comparable_controllers(config)
    trace_windows = select_trace_windows(manifest, preset, config)
    repetitions = int(experiment.get("repetitions", 1) or 1)
    max_sessions = execution.get("max_sessions")

    benchmark_capable = bool(spec["benchmark_capable"] and engine == "fake")
    ranking_capable = bool(spec["ranking_capable"] and engine == "fake")
    protocol = {
        "schema_version": PHASE6_SCHEMA_VERSION,
        "created_at_local": datetime.now().astimezone().isoformat(),
        "preset": preset,
        "engine": engine,
        "qoe_formula_version": LINEAR_QOE_VERSION,
        "benchmark_capable": benchmark_capable,
        "ranking_capable": ranking_capable,
        "benchmark_authorized": False,
        "ranking_authorized": False,
        "controller_visibility_guardrail": (
            "controllers receive only runtime feedback, ladder, buffer and measured download time"
        ),
        "synthetic_policy": "synthetic windows are diagnostic and reported separately",
        "media_profiles": media_profiles,
        "controllers": controllers,
        "trace_windows": trace_windows,
    }

    sessions: List[Dict[str, Any]] = []
    index = 0
    for repetition in range(1, repetitions + 1):
        for trace_window in trace_windows:
            for media_profile in media_profiles:
                for controller in controllers:
                    index += 1
                    session = build_session(
                        index=index,
                        package_root=package_root,
                        preset=preset,
                        engine=engine,
                        controller=controller,
                        media_profile=media_profile,
                        trace_window=trace_window,
                        repetition=repetition,
                    )
                    sessions.append(session)
                    if max_sessions is not None and len(sessions) >= int(max_sessions):
                        return protocol, sessions
    return protocol, sessions


def build_session(
    *,
    index: int,
    package_root: Path,
    preset: str,
    engine: str,
    controller: Mapping[str, Any],
    media_profile: Mapping[str, Any],
    trace_window: Mapping[str, Any],
    repetition: int,
) -> Dict[str, Any]:
    session_id = "s{0:05d}_{1}_{2}_{3}_r{4}".format(
        index,
        controller["alias"],
        media_profile["media_profile_id"],
        trace_window["trace_window_id"],
        repetition,
    )
    session_id = _safe_path_token(session_id)
    run_output_root = package_root / "01_ejecucion" / "runs" / session_id
    config_path = package_root / "00_protocolo" / "client_configs" / "{0}.yaml".format(session_id)
    command_log_path = package_root / "01_ejecucion" / "command_logs" / "{0}.log".format(session_id)
    return {
        "session_id": session_id,
        "preset": preset,
        "engine": engine,
        "controller_key": controller["controller_key"],
        "controller_alias": controller["alias"],
        "controller_display_name": controller["display_name"],
        "media_profile_id": media_profile["media_profile_id"],
        "media_display_name": media_profile.get("display_name", media_profile["media_profile_id"]),
        "mpd_url": media_profile["mpd_url"],
        "segment_duration_s": float(media_profile.get("segment_duration_s", 0.0) or 0.0),
        "media_diagnostic_only": bool(media_profile.get("diagnostic_only", False)),
        "trace_window_id": trace_window["trace_window_id"],
        "trace_id": trace_window["trace_id"],
        "dataset_id": trace_window["dataset_id"],
        "semantics": trace_window["semantics"],
        "network_condition": trace_window["network_condition"],
        "difficulty_bucket": trace_window["difficulty_bucket"],
        "synthetic": bool(trace_window["synthetic"]),
        "source_split": trace_window["source_split"],
        "normalized_trace_path": trace_window["normalized_trace_path"],
        "window_start_s": float(trace_window["window_start_s"]),
        "window_duration_s": float(trace_window["window_duration_s"]),
        "repetition": int(repetition),
        "run_output_root": str(run_output_root),
        "client_config_path": str(config_path),
        "command_log_path": str(command_log_path),
    }


def write_protocol_package(package_root: Path, protocol: Mapping[str, Any], sessions: Sequence[Mapping[str, Any]]) -> None:
    protocol_dir = package_root / "00_protocolo"
    protocol_dir.mkdir(parents=True, exist_ok=True)
    (package_root / "01_ejecucion" / "command_logs").mkdir(parents=True, exist_ok=True)
    (package_root / "02_resultados").mkdir(parents=True, exist_ok=True)
    (package_root / "03_graficas").mkdir(parents=True, exist_ok=True)
    (package_root / "04_informe").mkdir(parents=True, exist_ok=True)
    (protocol_dir / "client_configs").mkdir(parents=True, exist_ok=True)

    (protocol_dir / "protocolo_validacion.json").write_text(
        json.dumps(protocol, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    (protocol_dir / "session_plan.json").write_text(
        json.dumps({"schema_version": "phase6_session_plan_v1", "sessions": list(sessions)}, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    _write_csv(protocol_dir / "session_plan.csv", sessions)
    _write_csv(protocol_dir / "trace_windows.csv", protocol.get("trace_windows", []))
    _write_csv(protocol_dir / "controllers.csv", protocol.get("controllers", []))
    _write_csv(protocol_dir / "media_profiles.csv", protocol.get("media_profiles", []))


def run_session(config: Mapping[str, Any], session: Mapping[str, Any]) -> Dict[str, int]:
    execution = _mapping(config.get("execution"))
    paths = _mapping(config.get("paths"))
    if _bool(execution.get("resume", True)) and _session_completed(session):
        return {"executed": 0, "failed": 0}

    client_config_path = Path(str(session["client_config_path"]))
    client_config_path.parent.mkdir(parents=True, exist_ok=True)
    client_config_path.write_text(
        json.dumps(build_client_config(config, session), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    command_log_path = Path(str(session["command_log_path"]))
    command_log_path.parent.mkdir(parents=True, exist_ok=True)
    Path(str(session["run_output_root"])).mkdir(parents=True, exist_ok=True)

    python_exe = str(paths.get("python", "python"))
    repo_root = Path(str(paths.get("repo_root", REPO_ROOT)))
    command = [python_exe, str(repo_root / "main.py"), "--config", str(client_config_path)]
    started = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    timeout_seconds = float(execution.get("timeout_seconds", 900.0) or 900.0)
    try:
        completed = subprocess.run(
            command,
            cwd=str(repo_root),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        command_log_path.write_text(
            "started_at={0}\ncommand={1}\nreturncode={2}\n\n{3}".format(
                started,
                " ".join(command),
                completed.returncode,
                completed.stdout or "",
            ),
            encoding="utf-8",
        )
        return {"executed": 1, "failed": 1 if completed.returncode != 0 else 0}
    except subprocess.TimeoutExpired as exc:
        command_log_path.write_text(
            "started_at={0}\ncommand={1}\ntimeout_seconds={2}\n\n{3}".format(
                started,
                " ".join(command),
                timeout_seconds,
                exc.stdout or "",
            ),
            encoding="utf-8",
        )
        return {"executed": 1, "failed": 1}


def build_client_config(config: Mapping[str, Any], session: Mapping[str, Any]) -> Dict[str, Any]:
    playback = _mapping(config.get("playback"))
    network = _mapping(config.get("network_replay"))
    downloader = _mapping(config.get("downloader"))
    return {
        "mpd_url": session["mpd_url"],
        "media_engine": {
            "name": str(session.get("engine", "fake")),
            "min_queue_time": 0.1 if session.get("engine") == "fake" else 1.0,
            "decode_video": False,
            "sink_name": None,
        },
        "controller": {
            "name": session["controller_key"],
            "params": controller_params(config, str(session["controller_key"])),
        },
        "playback": {
            "initial_quality": int(playback.get("initial_quality", 0) or 0),
            "initial_controller_decision": _bool(playback.get("initial_controller_decision", False)),
            "headless": True,
            "max_buffer_seconds": float(playback.get("max_buffer_seconds", 60.0) or 60.0),
            "drain_buffer_sleep_seconds": float(playback.get("drain_buffer_sleep_seconds", 0.01) or 0.01),
            "preroll_seconds": float(playback.get("preroll_seconds", 0.0) or 0.0),
            "max_media_segments": playback.get("max_media_segments", 30),
        },
        "downloader": {
            "max_retries": int(downloader.get("max_retries", 3) or 3),
            "verbose": _bool(downloader.get("verbose", False)),
        },
        "network_replay": {
            "enabled": True,
            "trace_csv_path": session["normalized_trace_path"],
            "window_start_s": session["window_start_s"],
            "window_duration_s": session["window_duration_s"],
            "end_policy": str(network.get("end_policy", "fail")),
            "max_loops": int(network.get("max_loops", 0) or 0),
            "sleep": _bool(network.get("sleep", True)),
        },
        "output": {
            "root_dir": session["run_output_root"],
            "segment_telemetry_filename": "segment_telemetry.csv",
            "evaluation_segments_filename": "evaluation_segments.csv",
        },
        "logging": {
            "enabled": True,
            "level": "INFO",
        },
        "analysis": {
            "enabled": False,
        },
    }


def create_package_root(config: Mapping[str, Any], preset: str) -> Path:
    output_root = Path(str(_mapping(config.get("paths")).get("output_root")))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = "{0}_{1}".format(timestamp, preset)
    for index in range(1000):
        package_root = output_root / (base_name if index == 0 else "{0}_{1:03d}".format(base_name, index))
        try:
            package_root.mkdir(parents=True, exist_ok=False)
            return package_root
        except FileExistsError:
            continue
    raise RuntimeError("Could not create Phase 6 package root under {0}".format(output_root))


def resolve_package_root(config: Mapping[str, Any], preset: str) -> Path:
    execution = _mapping(config.get("execution"))
    explicit = str(execution.get("package_root", "") or "").strip()
    if explicit:
        package_root = Path(explicit)
        package_root.mkdir(parents=True, exist_ok=True)
        return package_root
    return create_package_root(config, preset)


def load_existing_protocol_package(package_root: Path) -> Optional[tuple[Dict[str, Any], List[Dict[str, Any]]]]:
    protocol_path = package_root / "00_protocolo" / "protocolo_validacion.json"
    plan_path = package_root / "00_protocolo" / "session_plan.json"
    if not protocol_path.is_file() or not plan_path.is_file():
        return None
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    sessions = plan.get("sessions", [])
    if not isinstance(protocol, dict) or not isinstance(sessions, list):
        raise RuntimeError("Invalid existing Phase 6 protocol package: {0}".format(package_root))
    return protocol, [dict(session) for session in sessions]


def _session_completed(session: Mapping[str, Any]) -> bool:
    run_root = Path(str(session.get("run_output_root", "")))
    if not run_root.is_dir():
        return False
    run_dirs = sorted(path for path in run_root.iterdir() if path.is_dir() and path.name.startswith("run_"))
    if not run_dirs:
        return False
    manifest_path = run_dirs[-1] / "run_manifest.json"
    if not manifest_path.is_file():
        return False
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        return False
    return manifest.get("status") == "completed"


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def _safe_path_token(value: str) -> str:
    chars = []
    for char in value:
        chars.append(char if char.isalnum() or char in {"_", "-"} else "_")
    return "".join(chars)


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "on", "si"}


if __name__ == "__main__":
    raise SystemExit(main())
