#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence


RAIZ_REPO = Path(__file__).resolve().parents[1]
if str(RAIZ_REPO) not in sys.path:
    sys.path.insert(0, str(RAIZ_REPO))

from core.fase6.catalogo import NOMBRES_PRESET
from core.fase6.configuracion import cargar_config_fase6
from core.fase6.seleccion import cargar_manifest_trazas, seleccionar_ventanas_trazas
from scripts.ejecutar_fase6 import aplicar_overrides_preset
from scripts.verificar_cliente_y_controllers_clasicos import (
    CLASSIC_CONTROLLERS,
    DEFAULT_MPD_URL,
    audit_run_directory,
    latest_run_dir,
    normalize_controller_list,
)


OUTPUT_FOLDER_NAME = "verificacion_clasica_controlada"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Verificacion clasica bajo trazas controladas.")
    parser.add_argument("--config", default=None)
    parser.add_argument("--preset", choices=NOMBRES_PRESET, default="rapido")
    parser.add_argument("--output-root", default=None)
    parser.add_argument("--mpd-url", default=DEFAULT_MPD_URL)
    parser.add_argument("--controllers", nargs="*", default=list(CLASSIC_CONTROLLERS))
    parser.add_argument("--max-windows", type=int, default=2)
    parser.add_argument("--timeout-seconds", type=float, default=240.0)
    args = parser.parse_args(argv)

    config = aplicar_overrides_preset(cargar_config_fase6(args.config), args.preset)
    if args.output_root:
        config.setdefault("paths", {})["output_root"] = args.output_root
    output_root = Path(str(config["paths"]["output_root"])) / OUTPUT_FOLDER_NAME / time.strftime("%Y%m%d_%H%M%S")
    output_root.mkdir(parents=True, exist_ok=True)

    controllers = normalize_controller_list(args.controllers)
    manifest = cargar_manifest_trazas(config["paths"]["manifest_path"])
    windows = [window for window in seleccionar_ventanas_trazas(manifest, args.preset, config) if not window["synthetic"]]
    windows = windows[: max(1, int(args.max_windows))]
    results = []
    for window in windows:
        for controller in controllers:
            results.append(
                run_controlled_smoke(
                    config=config,
                    output_root=output_root,
                    controller=controller,
                    window=window,
                    mpd_url=args.mpd_url,
                    timeout_seconds=args.timeout_seconds,
                )
            )

    summary = {
        "schema_version": "phase6_classic_controlled_verification_v1",
        "status": "accepted" if all(item["status"] == "accepted" for item in results) else "failed",
        "output_root": str(output_root),
        "preset": args.preset,
        "mpd_url": args.mpd_url,
        "controllers": controllers,
        "windows": windows,
        "results": results,
        "benchmark_performed": False,
        "ranking_performed": False,
    }
    (output_root / "resumen_verificacion_clasica_controlada.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    (output_root / "informe_verificacion_clasica_controlada.md").write_text(render_report(summary), encoding="utf-8")
    print("Verificacion clasica controlada")
    print("Output root: {0}".format(output_root))
    print("Status: {0}".format(summary["status"]))
    return 0 if summary["status"] == "accepted" else 1


def run_controlled_smoke(
    *,
    config: Mapping[str, Any],
    output_root: Path,
    controller: str,
    window: Mapping[str, Any],
    mpd_url: str,
    timeout_seconds: float,
) -> Dict[str, Any]:
    session_id = "{0}_{1}".format(controller, window["trace_window_id"])
    session_root = output_root / "runs" / session_id
    config_dir = output_root / "configs"
    log_dir = output_root / "command_logs"
    session_root.mkdir(parents=True, exist_ok=True)
    config_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    config_path = config_dir / "{0}.yaml".format(session_id)
    command_log_path = log_dir / "{0}.log".format(session_id)
    client_config = construir_config_cliente(config, controller, window, mpd_url, session_root)
    config_path.write_text(json.dumps(client_config, indent=2, sort_keys=True), encoding="utf-8")

    command = [sys.executable, str(RAIZ_REPO / "main.py"), "--config", str(config_path)]
    try:
        completed = subprocess.run(
            command,
            cwd=str(RAIZ_REPO),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=max(1.0, timeout_seconds),
            check=False,
        )
        command_log_path.write_text(completed.stdout or "", encoding="utf-8")
    except subprocess.TimeoutExpired as exc:
        command_log_path.write_text(exc.stdout or "", encoding="utf-8")
        return {
            "status": "failed",
            "controller": controller,
            "trace_window_id": window["trace_window_id"],
            "errors": ["timeout"],
            "config_path": str(config_path),
            "command_log_path": str(command_log_path),
        }

    errors: List[str] = []
    if completed.returncode != 0:
        errors.append("main.py devolvio codigo {0}".format(completed.returncode))
    run_dir = latest_run_dir(session_root)
    if run_dir is None:
        errors.append("no se encontro run completado")
    else:
        audit = audit_run_directory(run_dir, expected_controller=controller)
        errors.extend(audit.errors)
    return {
        "status": "failed" if errors else "accepted",
        "controller": controller,
        "trace_window_id": window["trace_window_id"],
        "dataset_id": window["dataset_id"],
        "difficulty_bucket": window["difficulty_bucket"],
        "run_dir": str(run_dir or ""),
        "config_path": str(config_path),
        "command_log_path": str(command_log_path),
        "errors": errors,
    }


def construir_config_cliente(
    config: Mapping[str, Any],
    controller: str,
    window: Mapping[str, Any],
    mpd_url: str,
    output_root: Path,
) -> Dict[str, Any]:
    playback = _mapping(config.get("playback"))
    network = _mapping(config.get("network_replay"))
    return {
        "mpd_url": mpd_url,
        "media_engine": {
            "name": "fake",
            "min_queue_time": 0.1,
            "decode_video": False,
            "sink_name": None,
        },
        "controller": {"name": controller, "params": {}},
        "playback": {
            "initial_quality": 0,
            "initial_controller_decision": False,
            "headless": True,
            "max_buffer_seconds": float(playback.get("max_buffer_seconds", 60.0) or 60.0),
            "drain_buffer_sleep_seconds": float(playback.get("drain_buffer_sleep_seconds", 0.01) or 0.01),
            "preroll_seconds": 0.0,
            "max_media_segments": playback.get("max_media_segments", 30),
        },
        "downloader": {"max_retries": 3, "verbose": False},
        "network_replay": {
            "enabled": True,
            "trace_csv_path": window["normalized_trace_path"],
            "window_start_s": window["window_start_s"],
            "window_duration_s": window["window_duration_s"],
            "end_policy": str(network.get("end_policy", "fail")),
            "max_loops": int(network.get("max_loops", 0) or 0),
            "sleep": bool(network.get("sleep", True)),
            "compact_timestamps": bool(network.get("compact_timestamps", True)),
        },
        "output": {
            "root_dir": output_root.as_posix(),
            "segment_telemetry_filename": "segment_telemetry.csv",
            "evaluation_segments_filename": "evaluation_segments.csv",
        },
        "logging": {"enabled": True, "level": "INFO"},
        "analysis": {"enabled": False},
    }


def render_report(summary: Mapping[str, Any]) -> str:
    lines = [
        "# Verificacion clasica controlada",
        "",
        "Esta ejecucion es diagnostica. No es benchmark, ranking ni seleccion de ganador.",
        "",
        "- Status: {0}".format(summary["status"]),
        "- Preset: {0}".format(summary["preset"]),
        "- Sesiones: {0}".format(len(summary["results"])),
        "",
        "## Resultados",
        "",
    ]
    for item in summary["results"]:
        lines.append(
            "- {0} / {1}: {2}".format(
                item["controller"],
                item["trace_window_id"],
                item["status"],
            )
        )
    return "\n".join(lines) + "\n"


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


if __name__ == "__main__":
    raise SystemExit(main())
