#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import csv
import json
import math
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.controller.registry import create_controller
from core.dataset_schema import build_evaluation_segments_header
from core.output_artifacts import (
    ENVIRONMENT_FILENAME,
    EVALUATION_SEGMENTS_FILENAME,
    LEGACY_OUTPUT_FILENAMES,
    RESOLVED_CONFIG_FILENAME,
    RUN_LOG_FILENAME,
    RUN_MANIFEST_FILENAME,
    SEGMENT_TELEMETRY_FILENAME,
)


PUBLIC_PHASE_NAME = "Fase de Verificacion del Cliente y Controllers Clasicos"
OUTPUT_FOLDER_NAME = "fase_verificacion_cliente_y_controllers_clasicos"
REPORT_FILENAME = "informe_verificacion_cliente_y_controllers_clasicos.md"
SUMMARY_FILENAME = "resumen_verificacion_cliente_y_controllers_clasicos.json"
DEFAULT_MPD_URL = (
    "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/"
    "Paseo_Almunecar_1min_30fps_simple_4s.mpd"
)

CLASSIC_CONTROLLERS = (
    "rate_based",
    "bba",
    "bola",
    "mpc",
    "robust_mpc",
)

FORBIDDEN_HEADER_TOKENS = (
    "trace_id",
    "dataset_id",
    "source_id",
    "split",
    "group_id",
    "leakage_group",
    "future",
    "qoe",
    "reward",
    "winner",
    "ranking",
)

CONTROLLER_DESCRIPTIONS: Mapping[str, Mapping[str, str]] = {
    "rate_based": {
        "idea": "Selecciona la mayor representacion por debajo de un throughput medido y protegido por safety factor.",
        "code": "core/controller/rate_based.py",
        "tests": "tests/test_rate_based_controller.py",
        "spec": "docs/contexto rama original/01_baselines/rate_based/implementation_spec.md",
        "human_reason": "El probe comprueba conversion a bytes/s, safety factor y subida conservadora.",
    },
    "bba": {
        "idea": "Usa el buffer como senal principal mediante reservoir y cushion al estilo BBA-0.",
        "code": "core/controller/bba.py",
        "tests": "tests/test_bba_controller.py",
        "spec": "docs/contexto rama original/01_baselines/bba/implementation_spec.md",
        "human_reason": "El probe situa el buffer dentro del cushion y espera una calidad intermedia.",
    },
    "bola": {
        "idea": "Calcula una puntuacion BOLA-basic por representacion usando utilidad, buffer y tamano estimado.",
        "code": "core/controller/bola.py",
        "tests": "tests/test_bola_controller.py",
        "spec": "docs/contexto rama original/01_baselines/bola/implementation_spec.md",
        "human_reason": "El probe comprueba que se elige el nivel con mejor score BOLA-basic.",
    },
    "mpc": {
        "idea": "Enumera secuencias de calidad, simula buffer futuro y devuelve la primera accion de la mejor secuencia.",
        "code": "core/controller/mpc.py",
        "tests": "tests/test_mpc_controller.py",
        "spec": "docs/contexto rama original/01_baselines/mpc/implementation_spec.md",
        "human_reason": "El probe comprueba prediccion armonica, horizonte y objetivo interno no final.",
    },
    "robust_mpc": {
        "idea": "Aplica MPC con una prediccion de throughput conservadora corregida por error reciente.",
        "code": "core/controller/robust_mpc.py",
        "tests": "tests/test_robust_mpc_controller.py",
        "spec": "docs/contexto rama original/01_baselines/robust_mpc/implementation_spec.md",
        "human_reason": "El probe comprueba que la prediccion robusta no supera la prediccion base y que no usa IA/RL.",
    },
}


@dataclass(frozen=True)
class VerificationResult:
    status: str
    controller: str
    errors: List[str]
    data: Dict[str, Any]

    @property
    def accepted(self) -> bool:
        return self.status == "accepted"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verifica cliente DASH y controllers clasicos sin ejecutar benchmark.",
    )
    parser.add_argument("--mpd-url", default=DEFAULT_MPD_URL, help="URL MPD del servidor DASH.")
    parser.add_argument(
        "--output-root",
        default=None,
        help="Directorio externo donde guardar configs, runs e informe.",
    )
    parser.add_argument(
        "--controllers",
        nargs="*",
        default=list(CLASSIC_CONTROLLERS),
        help="Controllers a verificar. Acepta espacios o comas.",
    )
    parser.add_argument(
        "--skip-theory-probes",
        action="store_true",
        help="No ejecutar probes controlados por controller.",
    )
    parser.add_argument(
        "--skip-server-smokes",
        action="store_true",
        help="No ejecutar reproducciones contra el servidor DASH.",
    )
    parser.add_argument(
        "--run-gstreamer-demo",
        action="store_true",
        help="Ejecutar una demo opcional GStreamer con robust_mpc si el entorno lo permite.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=180.0,
        help="Timeout por run de main.py.",
    )
    parser.add_argument(
        "--max-example-rows",
        type=int,
        default=5,
        help="Numero maximo de decisiones por controller en el informe.",
    )
    args = parser.parse_args(argv)

    controllers = normalize_controller_list(args.controllers)
    output_root = Path(args.output_root) if args.output_root else default_output_root()
    output_root.mkdir(parents=True, exist_ok=True)

    started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    theory_results: List[VerificationResult] = []
    smoke_results: List[VerificationResult] = []
    gstreamer_result: Optional[VerificationResult] = None

    if not args.skip_theory_probes:
        theory_results = [run_theory_probe(controller) for controller in controllers]

    if not args.skip_server_smokes:
        smoke_results = [
            run_server_smoke(
                controller=controller,
                mpd_url=args.mpd_url,
                output_root=output_root,
                timeout_seconds=args.timeout_seconds,
                max_example_rows=args.max_example_rows,
                media_engine="fake",
            )
            for controller in controllers
        ]

    if args.run_gstreamer_demo:
        gstreamer_result = run_server_smoke(
            controller="robust_mpc",
            mpd_url=args.mpd_url,
            output_root=output_root,
            timeout_seconds=args.timeout_seconds,
            max_example_rows=args.max_example_rows,
            media_engine="gst",
            demo_label="gstreamer_demo",
        )

    summary = build_summary(
        started_at=started_at,
        mpd_url=args.mpd_url,
        output_root=output_root,
        controllers=controllers,
        theory_results=theory_results,
        smoke_results=smoke_results,
        gstreamer_result=gstreamer_result,
    )
    summary_path = output_root / SUMMARY_FILENAME
    report_path = output_root / REPORT_FILENAME
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    report_path.write_text(render_report(summary), encoding="utf-8")

    print("Fase de Verificacion")
    print("Output root: {0}".format(output_root))
    print("Summary: {0}".format(summary_path))
    print("Report: {0}".format(report_path))
    print("Status: {0}".format(summary["status"]))
    return 0 if summary["status"] != "failed" else 1


def default_output_root() -> Path:
    return REPO_ROOT.parent / "runs_trazas" / OUTPUT_FOLDER_NAME


def normalize_controller_list(raw_items: Iterable[str]) -> List[str]:
    controllers: List[str] = []
    for item in raw_items:
        for part in str(item).split(","):
            controller = part.strip()
            if controller:
                controllers.append(controller)
    if not controllers:
        controllers = list(CLASSIC_CONTROLLERS)

    unknown = [controller for controller in controllers if controller not in CLASSIC_CONTROLLERS]
    if unknown:
        raise SystemExit(
            "Controllers no permitidos en esta verificacion: {0}. Permitidos: {1}".format(
                ", ".join(unknown),
                ", ".join(CLASSIC_CONTROLLERS),
            )
        )
    return controllers


def run_theory_probe(controller: str) -> VerificationResult:
    errors: List[str] = []
    feedback = probe_feedback(controller)
    instance = create_controller(controller)

    try:
        instance.setPlayerFeedback(feedback)
        target_rate = float(instance.calcControlAction())
        chosen_level = int(instance.quantizeRate(target_rate))
        metrics = json_safe(getattr(instance, "last_metrics", {}))
    except Exception as exc:
        return VerificationResult(
            status="failed",
            controller=controller,
            errors=["probe_exception: {0}".format(format_exception(exc))],
            data={},
        )

    rates = list(feedback["rates"])
    if not math.isfinite(target_rate):
        errors.append("target_rate no es finito")
    if chosen_level < 0 or chosen_level >= len(rates):
        errors.append("chosen_level fuera de ladder")
    elif not nearly_equal(target_rate, rates[chosen_level]):
        errors.append("target_rate no corresponde al chosen_level")

    errors.extend(validate_probe_expectation(controller, chosen_level, metrics))

    return VerificationResult(
        status="failed" if errors else "accepted",
        controller=controller,
        errors=errors,
        data={
            "controller": controller,
            "target_rate_Bps": target_rate,
            "chosen_level": chosen_level,
            "rates_Bps": rates,
            "feedback": json_safe(feedback),
            "metrics": metrics,
            "human_reason": CONTROLLER_DESCRIPTIONS[controller]["human_reason"],
        },
    )


def probe_feedback(controller: str) -> Dict[str, Any]:
    base = {
        "queued_bytes": 0,
        "queued_time": 20.0,
        "cur_bitrate": 200.0,
        "bwe": 1000.0,
        "level": 0,
        "max_level": 3,
        "cur_rate": 100.0,
        "max_rate": 800.0,
        "min_rate": 100.0,
        "max_bitrate": 800.0,
        "min_bitrate": 100.0,
        "last_fragment_size": 4000.0,
        "last_download_time": 4.0,
        "downloaded_bytes": 0,
        "fragment_duration": 4.0,
        "rates": [100.0, 200.0, 400.0, 800.0],
        "segment_index": 3,
        "start_segment_request": 1.0,
        "stop_segment_request": 2.0,
    }
    if controller == "rate_based":
        base.update({"queued_time": 10.0, "level": 1, "cur_rate": 200.0, "cur_bitrate": 200.0, "bwe": 1000.0})
    elif controller == "bba":
        base.update({"queued_time": 10.0})
    elif controller == "bola":
        base.update({"queued_time": 12.0, "fragment_duration": 4.0})
    elif controller == "mpc":
        base.update({"queued_time": 20.0, "level": 0, "throughput_history_Bps": [1000.0]})
    elif controller == "robust_mpc":
        base.update(
            {
                "queued_time": 20.0,
                "level": 0,
                "throughput_history_Bps": [1000.0],
                "prediction_error_history": [1.0],
            }
        )
    return base


def validate_probe_expectation(controller: str, chosen_level: int, metrics: Mapping[str, Any]) -> List[str]:
    errors: List[str] = []
    reason = str(metrics.get("reason", ""))

    if controller == "rate_based":
        if reason != "throughput_selection":
            errors.append("rate_based no uso throughput_selection")
        if chosen_level != 2:
            errors.append("rate_based no eligio el nivel seguro esperado")
        safe = metrics.get("safe_throughput_Bps")
        decision = metrics.get("decision_throughput_Bps")
        if not (is_number(safe) and is_number(decision) and float(safe) <= float(decision)):
            errors.append("rate_based no registro safety factor coherente")
    elif controller == "bba":
        if reason != "cushion":
            errors.append("bba no entro en la zona cushion esperada")
        if chosen_level != 1:
            errors.append("bba no eligio el nivel intermedio esperado")
    elif controller == "bola":
        if reason != "score_selection":
            errors.append("bola no uso score_selection")
        if metrics.get("raw_best_level") != chosen_level:
            errors.append("bola no eligio el raw_best_level")
        if not metrics.get("scores_by_level"):
            errors.append("bola no registro scores por nivel")
    elif controller == "mpc":
        if reason != "mpc_sequence_selection":
            errors.append("mpc no uso seleccion de secuencia")
        if not metrics.get("internal_objective_only"):
            errors.append("mpc no marco su objetivo como interno")
        if not metrics.get("best_sequence"):
            errors.append("mpc no registro mejor secuencia")
    elif controller == "robust_mpc":
        if reason != "robust_mpc_sequence_selection":
            errors.append("robust_mpc no uso seleccion robusta")
        base_prediction = metrics.get("base_prediction_Bps")
        robust_prediction = metrics.get("robust_prediction_Bps")
        if not (
            is_number(base_prediction)
            and is_number(robust_prediction)
            and float(robust_prediction) <= float(base_prediction)
        ):
            errors.append("robust_mpc no redujo o acoto la prediccion")
        if metrics.get("pensieve_implemented") is not False:
            errors.append("robust_mpc no marco Pensieve como no implementado")
        if metrics.get("rl_or_neural_state_used") is not False:
            errors.append("robust_mpc no marco IA/RL como no usado")
    return errors


def run_server_smoke(
    controller: str,
    mpd_url: str,
    output_root: Path,
    timeout_seconds: float,
    max_example_rows: int,
    media_engine: str = "fake",
    demo_label: str = "server_smoke",
) -> VerificationResult:
    errors: List[str] = []
    config_dir = output_root / "configs"
    command_log_dir = output_root / "command_logs"
    run_output_root = output_root / "runs" / demo_label / controller
    config_dir.mkdir(parents=True, exist_ok=True)
    command_log_dir.mkdir(parents=True, exist_ok=True)
    run_output_root.mkdir(parents=True, exist_ok=True)

    config_path = config_dir / "{0}_{1}.yaml".format(demo_label, controller)
    command_log_path = command_log_dir / "{0}_{1}.log".format(demo_label, controller)
    config_path.write_text(
        build_client_config_yaml(
            mpd_url=mpd_url,
            controller=controller,
            output_root=run_output_root,
            media_engine=media_engine,
        ),
        encoding="utf-8",
    )

    command = [sys.executable, str(REPO_ROOT / "main.py"), "--config", str(config_path)]
    try:
        completed = subprocess.run(
            command,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=max(1.0, timeout_seconds),
            check=False,
        )
        command_log_path.write_text(completed.stdout or "", encoding="utf-8")
    except subprocess.TimeoutExpired as exc:
        command_log_path.write_text(exc.stdout or "", encoding="utf-8")
        return VerificationResult(
            status="failed",
            controller=controller,
            errors=["timeout tras {0:.1f}s".format(timeout_seconds)],
            data={
                "config_path": str(config_path),
                "command_log_path": str(command_log_path),
                "media_engine": media_engine,
            },
        )

    if completed.returncode != 0:
        errors.append("main.py devolvio codigo {0}".format(completed.returncode))

    run_dir = latest_run_dir(run_output_root)
    if run_dir is None:
        errors.append("no se encontro directorio run_*")
        return VerificationResult(
            status="failed",
            controller=controller,
            errors=errors,
            data={
                "config_path": str(config_path),
                "command_log_path": str(command_log_path),
                "media_engine": media_engine,
            },
        )

    audit = audit_run_directory(
        run_dir=run_dir,
        expected_controller=controller,
        max_example_rows=max_example_rows,
    )
    errors.extend(audit.errors)
    data = {
        "config_path": str(config_path),
        "command_log_path": str(command_log_path),
        "media_engine": media_engine,
        "run_dir": str(run_dir),
    }
    data.update(audit.data)
    return VerificationResult(
        status="failed" if errors else "accepted",
        controller=controller,
        errors=errors,
        data=data,
    )


def build_client_config_yaml(mpd_url: str, controller: str, output_root: Path, media_engine: str) -> str:
    sink_name = "null"
    decode_video = "false"
    min_queue_time = "0.1" if media_engine == "fake" else "1.0"
    return "\n".join(
        [
            'mpd_url: "{0}"'.format(escape_yaml_scalar(mpd_url)),
            "",
            "media_engine:",
            '  name: "{0}"'.format(media_engine),
            "  min_queue_time: {0}".format(min_queue_time),
            "  decode_video: {0}".format(decode_video),
            "  sink_name: {0}".format(sink_name),
            "",
            "controller:",
            '  name: "{0}"'.format(controller),
            "  params: {}",
            "",
            "playback:",
            "  initial_quality: 0",
            "  initial_controller_decision: false",
            "  headless: true",
            "  max_buffer_seconds: 60.0",
            "  drain_buffer_sleep_seconds: 0.01",
            "  preroll_seconds: 0.0",
            "",
            "downloader:",
            "  max_retries: 3",
            "  verbose: false",
            "",
            "output:",
            '  root_dir: "{0}"'.format(escape_yaml_scalar(output_root.as_posix())),
            '  segment_telemetry_filename: "{0}"'.format(SEGMENT_TELEMETRY_FILENAME),
            '  evaluation_segments_filename: "{0}"'.format(EVALUATION_SEGMENTS_FILENAME),
            "",
            "logging:",
            "  enabled: true",
            '  level: "INFO"',
            "",
            "analysis:",
            "  enabled: false",
            "",
        ]
    )


def audit_run_directory(run_dir: Path, expected_controller: str, max_example_rows: int = 5) -> VerificationResult:
    errors: List[str] = []
    required_files = (
        RUN_MANIFEST_FILENAME,
        RESOLVED_CONFIG_FILENAME,
        ENVIRONMENT_FILENAME,
        RUN_LOG_FILENAME,
        SEGMENT_TELEMETRY_FILENAME,
        EVALUATION_SEGMENTS_FILENAME,
    )
    for filename in required_files:
        if not (run_dir / filename).is_file():
            errors.append("falta artifact canonico: {0}".format(filename))
    for legacy_name in LEGACY_OUTPUT_FILENAMES:
        if (run_dir / legacy_name).exists():
            errors.append("artifact legacy no permitido: {0}".format(legacy_name))

    manifest = read_json_if_exists(run_dir / RUN_MANIFEST_FILENAME)
    if manifest:
        if manifest.get("status") != "completed":
            errors.append("run_manifest status no es completed")
        controller_name = (manifest.get("controller") or {}).get("name")
        if controller_name != expected_controller:
            errors.append("run_manifest controller inesperado: {0}".format(controller_name))
        neutrality = manifest.get("benchmark_neutrality") or {}
        if neutrality.get("outputs_are_benchmark_results") is not False:
            errors.append("manifest no marca outputs_are_benchmark_results=false")
        if neutrality.get("final_qoe_reward_defined") is not False:
            errors.append("manifest no marca final_qoe_reward_defined=false")
        if neutrality.get("final_training_dataset_defined") is not False:
            errors.append("manifest no marca final_training_dataset_defined=false")
    elif (run_dir / RUN_MANIFEST_FILENAME).exists():
        errors.append("run_manifest.json no se pudo leer")

    segment_path = run_dir / SEGMENT_TELEMETRY_FILENAME
    eval_path = run_dir / EVALUATION_SEGMENTS_FILENAME
    segment_header, segment_rows = read_csv_dicts(segment_path)
    eval_header, eval_rows = read_csv_dicts(eval_path)

    if segment_path.exists() and not segment_header:
        errors.append("segment_telemetry.csv sin cabecera")
    if eval_path.exists() and not eval_header:
        errors.append("evaluation_segments.csv sin cabecera")

    if eval_header and eval_header != build_evaluation_segments_header():
        errors.append("evaluation_segments.csv no mantiene el schema limpio esperado")

    bad_segment_columns = forbidden_columns(segment_header)
    if bad_segment_columns:
        errors.append("segment_telemetry contiene columnas prohibidas: {0}".format(", ".join(bad_segment_columns)))
    bad_eval_columns = forbidden_columns(eval_header)
    if bad_eval_columns:
        errors.append("evaluation_segments contiene columnas prohibidas: {0}".format(", ".join(bad_eval_columns)))

    eval_internal_columns = [
        column for column in eval_header if column.startswith("feedback_") or column.startswith("policy_")
    ]
    if eval_internal_columns:
        errors.append(
            "evaluation_segments contiene columnas internas no permitidas: {0}".format(
                ", ".join(eval_internal_columns)
            )
        )

    neural_cols = [column for column in segment_header + eval_header if column.startswith("feedback_neural_")]
    if neural_cols:
        errors.append("run clasico contiene columnas IA: {0}".format(", ".join(sorted(set(neural_cols)))))

    decision_errors, decision_summary, examples = validate_policy_decisions(segment_rows, max_example_rows)
    errors.extend(decision_errors)

    data = {
        "run_dir": str(run_dir),
        "required_artifacts_present": all((run_dir / name).is_file() for name in required_files),
        "legacy_artifacts_absent": not any((run_dir / name).exists() for name in LEGACY_OUTPUT_FILENAMES),
        "segment_telemetry_rows": len(segment_rows),
        "evaluation_segments_rows": len(eval_rows),
        "segment_telemetry_columns": len(segment_header),
        "evaluation_segments_columns": len(eval_header),
        "evaluation_segments_clean": bool(eval_header == build_evaluation_segments_header()),
        "neural_columns_present": sorted(set(neural_cols)),
        "decision_summary": decision_summary,
        "example_decisions": examples,
        "manifest": json_safe(manifest),
    }
    return VerificationResult(
        status="failed" if errors else "accepted",
        controller=expected_controller,
        errors=errors,
        data=data,
    )


def validate_policy_decisions(
    rows: Sequence[Mapping[str, str]],
    max_example_rows: int,
) -> Tuple[List[str], Dict[str, Any], List[Dict[str, Any]]]:
    errors: List[str] = []
    checked = 0
    invalid = 0
    levels = set()
    rates_seen = set()
    examples: List[Dict[str, Any]] = []

    for row in rows:
        raw_level = str(row.get("policy_chosen_level", "")).strip()
        raw_target = str(row.get("policy_target_rate", "")).strip()
        if not raw_level or not raw_target:
            continue
        checked += 1
        level = parse_int(raw_level)
        target = parse_float(raw_target)
        rates = parse_rates(row.get("feedback_rates", ""))
        if level is None or target is None or not rates:
            invalid += 1
            continue
        if level < 0 or level >= len(rates):
            invalid += 1
            continue
        if not nearly_equal(target, rates[level]):
            invalid += 1
            continue
        levels.add(level)
        rates_seen.add(rates[level])
        if len(examples) < max(0, max_example_rows):
            examples.append(
                {
                    "segment_index": row.get("segment_index", ""),
                    "buffer_s": row.get("feedback_queued_time", ""),
                    "measured_rate_Bps": row.get("feedback_bwe", ""),
                    "chosen_level": level,
                    "target_rate_Bps": target,
                    "policy_decision_ms": row.get("policy_decision_ms", ""),
                    "eval_phase": row.get("eval_phase", ""),
                    "use_for_eval": row.get("use_for_eval", ""),
                }
            )

    if checked == 0:
        errors.append("no hay decisiones policy_* auditables")
    if invalid:
        errors.append("{0} decisiones policy_* no son validas contra la ladder".format(invalid))

    return errors, {
        "checked_policy_decisions": checked,
        "invalid_policy_decisions": invalid,
        "levels_seen": sorted(levels),
        "rates_seen_Bps": sorted(rates_seen),
    }, examples


def build_summary(
    started_at: str,
    mpd_url: str,
    output_root: Path,
    controllers: Sequence[str],
    theory_results: Sequence[VerificationResult],
    smoke_results: Sequence[VerificationResult],
    gstreamer_result: Optional[VerificationResult],
) -> Dict[str, Any]:
    result_groups: List[Sequence[VerificationResult]] = [theory_results, smoke_results]
    if gstreamer_result is not None:
        result_groups.append([gstreamer_result])
    all_results = [result for group in result_groups for result in group]
    all_accepted = all(result.accepted for result in all_results) if all_results else True
    closure_ready = bool(theory_results) and bool(smoke_results) and all_accepted
    if closure_ready:
        status = "accepted"
    elif all_accepted:
        status = "accepted_local_only"
    else:
        status = "failed"
    return {
        "phase_name": PUBLIC_PHASE_NAME,
        "status": status,
        "started_at": started_at,
        "mpd_url": mpd_url,
        "output_root": str(output_root),
        "controllers": list(controllers),
        "theory_probes_executed": bool(theory_results),
        "server_smokes_executed": bool(smoke_results),
        "closure_ready": closure_ready,
        "benchmark_performed": False,
        "ranking_performed": False,
        "winner_declared": False,
        "qoe_improvement_claimed": False,
        "network_performance_claimed": False,
        "theory_probes": [result_to_dict(result) for result in theory_results],
        "server_smokes": [result_to_dict(result) for result in smoke_results],
        "gstreamer_demo": result_to_dict(gstreamer_result) if gstreamer_result else None,
    }


def render_report(summary: Mapping[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# Informe de Verificacion del Cliente y Controllers Clasicos")
    lines.append("")
    lines.append("Status: `{0}`".format(summary.get("status")))
    lines.append("")
    lines.append("Este informe demuestra funcionamiento y coherencia tecnica. No es un benchmark, no hace ranking, no declara ganador y no afirma mejora de QoE.")
    lines.append("")
    lines.append("## Datos de ejecucion")
    lines.append("")
    lines.append("- Fase: `{0}`".format(summary.get("phase_name")))
    lines.append("- MPD usado: `{0}`".format(summary.get("mpd_url")))
    lines.append("- Carpeta externa: `{0}`".format(summary.get("output_root")))
    lines.append("- Controllers: `{0}`".format(", ".join(summary.get("controllers", []))))
    lines.append("")
    lines.append("## Que se verifica")
    lines.append("")
    lines.append("- El cliente carga un MPD, descarga inicializaciones y segmentos, mantiene buffer y llama al controller por la API comun.")
    lines.append("- Cada controller devuelve un rate de la ladder y el player lo convierte a un nivel valido.")
    lines.append("- Los artifacts canonicos se escriben con nombres actuales y los nombres legacy no aparecen.")
    lines.append("- `evaluation_segments.csv` queda compacto y sin telemetria interna de controllers ni columnas IA.")
    lines.append("- Los datos futuros, splits, identificadores de traza y QoE futura no aparecen como entradas de controller.")
    lines.append("")
    lines.append("## Frontera metodologica")
    lines.append("")
    lines.append("| Campo | Valor |")
    lines.append("| --- | --- |")
    lines.append("| benchmark_performed | `{0}` |".format(summary.get("benchmark_performed")))
    lines.append("| ranking_performed | `{0}` |".format(summary.get("ranking_performed")))
    lines.append("| winner_declared | `{0}` |".format(summary.get("winner_declared")))
    lines.append("| qoe_improvement_claimed | `{0}` |".format(summary.get("qoe_improvement_claimed")))
    lines.append("| network_performance_claimed | `{0}` |".format(summary.get("network_performance_claimed")))
    lines.append("")
    lines.append("## Probes controlados")
    lines.append("")
    lines.append("| Controller | Status | Idea comprobada | Nivel elegido | Rate B/s | Errores |")
    lines.append("| --- | --- | --- | ---: | ---: | --- |")
    for result in summary.get("theory_probes", []):
        controller = result.get("controller", "")
        data = result.get("data", {})
        description = CONTROLLER_DESCRIPTIONS.get(controller, {})
        lines.append(
            "| `{0}` | `{1}` | {2} | `{3}` | `{4}` | {5} |".format(
                controller,
                result.get("status", ""),
                description.get("human_reason", ""),
                data.get("chosen_level", ""),
                data.get("target_rate_Bps", ""),
                format_errors(result.get("errors", [])),
            )
        )
    lines.append("")
    lines.append("## Reproducciones contra servidor")
    lines.append("")
    lines.append("| Controller | Status | Run dir | Filas telemetry | Decisiones validas | Niveles vistos | Errores |")
    lines.append("| --- | --- | --- | ---: | ---: | --- | --- |")
    for result in summary.get("server_smokes", []):
        data = result.get("data", {})
        decision_summary = data.get("decision_summary", {})
        lines.append(
            "| `{0}` | `{1}` | `{2}` | `{3}` | `{4}` | `{5}` | {6} |".format(
                result.get("controller", ""),
                result.get("status", ""),
                data.get("run_dir", ""),
                data.get("segment_telemetry_rows", ""),
                decision_summary.get("checked_policy_decisions", ""),
                decision_summary.get("levels_seen", []),
                format_errors(result.get("errors", [])),
            )
        )
    lines.append("")
    lines.append("## Detalle por controller")
    lines.append("")
    for controller in summary.get("controllers", []):
        description = CONTROLLER_DESCRIPTIONS[controller]
        lines.append("### `{0}`".format(controller))
        lines.append("")
        lines.append("- Idea teorica: {0}".format(description["idea"]))
        lines.append("- Codigo: `{0}`".format(description["code"]))
        lines.append("- Tests: `{0}`".format(description["tests"]))
        lines.append("- Spec local: `{0}`".format(description["spec"]))
        smoke = find_result(summary.get("server_smokes", []), controller)
        if smoke:
            data = smoke.get("data", {})
            lines.append("- Run real: `{0}`".format(data.get("run_dir", "")))
            lines.append("- Artifacts canonicos presentes: `{0}`".format(data.get("required_artifacts_present")))
            lines.append("- Artifacts legacy ausentes: `{0}`".format(data.get("legacy_artifacts_absent")))
            lines.append("- `evaluation_segments.csv` limpio: `{0}`".format(data.get("evaluation_segments_clean")))
            examples = data.get("example_decisions", [])
            if examples:
                lines.append("")
                lines.append("| Segmento | Buffer s | Throughput observado B/s | Nivel | Rate B/s | Fase | use_for_eval |")
                lines.append("| ---: | ---: | ---: | ---: | ---: | --- | --- |")
                for example in examples:
                    lines.append(
                        "| `{0}` | `{1}` | `{2}` | `{3}` | `{4}` | `{5}` | `{6}` |".format(
                            example.get("segment_index", ""),
                            example.get("buffer_s", ""),
                            example.get("measured_rate_Bps", ""),
                            example.get("chosen_level", ""),
                            example.get("target_rate_Bps", ""),
                            example.get("eval_phase", ""),
                            example.get("use_for_eval", ""),
                        )
                    )
        lines.append("")
    lines.append("## Cierre")
    lines.append("")
    if summary.get("status") == "accepted":
        lines.append("Decision: `ACCEPTED_AS_CLIENT_AND_CLASSIC_CONTROLLER_VERIFICATION`.")
        lines.append("")
        lines.append("La fase verifica que el cliente y los controllers clasicos son coherentes para preparar la evaluacion formal posterior. La comparacion de QoE queda fuera de este informe.")
    elif summary.get("status") == "accepted_local_only":
        lines.append("Decision: `ACCEPTED_LOCAL_ONLY_PENDING_SERVER_SMOKES`.")
        lines.append("")
        lines.append("Los probes locales son coherentes, pero falta ejecutar la reproduccion contra el servidor DASH para cerrar la verificacion completa.")
    else:
        lines.append("Decision: `PENDING_FIXES_BEFORE_ACCEPTANCE`.")
        lines.append("")
        lines.append("Hay errores que deben corregirse antes de usar esta evidencia como cierre de verificacion.")
    lines.append("")
    return "\n".join(lines)


def result_to_dict(result: Optional[VerificationResult]) -> Optional[Dict[str, Any]]:
    if result is None:
        return None
    return {
        "status": result.status,
        "controller": result.controller,
        "errors": list(result.errors),
        "data": json_safe(result.data),
    }


def read_json_if_exists(path: Path) -> Optional[Dict[str, Any]]:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def read_csv_dicts(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    if not path.is_file():
        return [], []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        header = list(reader.fieldnames or [])
        return header, list(reader)


def forbidden_columns(header: Sequence[str]) -> List[str]:
    bad: List[str] = []
    for column in header:
        lowered = column.lower()
        if any(token in lowered for token in FORBIDDEN_HEADER_TOKENS):
            bad.append(column)
    return bad


def latest_run_dir(root: Path) -> Optional[Path]:
    if not root.is_dir():
        return None
    candidates = sorted(path for path in root.iterdir() if path.is_dir() and path.name.startswith("run_"))
    return candidates[-1] if candidates else None


def parse_rates(raw: Any) -> List[float]:
    try:
        value = ast.literal_eval(str(raw))
    except Exception:
        return []
    if not isinstance(value, (list, tuple)):
        return []
    rates: List[float] = []
    for item in value:
        parsed = parse_float(item)
        if parsed is None or parsed <= 0:
            return []
        rates.append(parsed)
    return rates


def parse_float(raw: Any) -> Optional[float]:
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(value):
        return None
    return value


def parse_int(raw: Any) -> Optional[int]:
    try:
        return int(float(raw))
    except (TypeError, ValueError):
        return None


def nearly_equal(left: float, right: float, tolerance: float = 1e-6) -> bool:
    return abs(float(left) - float(right)) <= max(tolerance, abs(float(right)) * tolerance)


def is_number(value: Any) -> bool:
    return parse_float(value) is not None


def json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else str(value)
    try:
        return float(value)
    except (TypeError, ValueError):
        return str(value)


def escape_yaml_scalar(value: str) -> str:
    return str(value).replace("\\", "\\\\").replace('"', '\\"')


def format_exception(exc: BaseException) -> str:
    message = str(exc)
    if message:
        return "{0}: {1}".format(exc.__class__.__name__, message)
    return exc.__class__.__name__


def format_errors(errors: Sequence[str]) -> str:
    if not errors:
        return "`none`"
    return "<br>".join("`{0}`".format(error) for error in errors)


def find_result(results: Sequence[Mapping[str, Any]], controller: str) -> Optional[Mapping[str, Any]]:
    for result in results:
        if result.get("controller") == controller:
            return result
    return None


if __name__ == "__main__":
    raise SystemExit(main())
