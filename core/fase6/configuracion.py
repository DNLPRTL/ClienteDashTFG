from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping, Optional


RAIZ_REPO = Path(__file__).resolve().parents[2]
RUTA_CONFIG_EJEMPLO_FASE6 = RAIZ_REPO / "config" / "fase6.example.yaml"
RUTA_CONFIG_LOCAL_FASE6 = RAIZ_REPO / "config" / "fase6.local.yaml"
# Compatibilidad: nombre anterior de la config local (maquinas ya configuradas).
RUTA_CONFIG_LOCAL_ANTERIOR = RAIZ_REPO / "config" / "phase6.local.yaml"

CONFIG_FASE6_POR_DEFECTO: Dict[str, Any] = {
    "schema_version": "phase6_config_v1",
    "paths": {
        "manifest_path": "/home/daniel/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json",
        "output_root": "/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa",
        "repo_root": "/home/daniel/TFG/ClienteDashPrudente",
        "python": "python",
        "trace_path_rewrites": [],
    },
    "experiment": {
        "preset": "rapido",
        "seed": 606,
        "engine": "fake",
        "controllers": [],
        "media_profile_ids": [],
        "include_synthetic_diagnostic": True,
        "repetitions": 1,
    },
    "network_replay": {
        "window_duration_s": 300.0,
        "decision_interval_s": 4.0,
        "end_policy": "fail",
        "max_loops": 0,
        "compact_timestamps": True,
        "min_mean_throughput_kbps_for_formal": 450.0,
        "min_max_throughput_kbps_for_formal": 300.0,
        "sleep": True,
    },
    "playback": {
        "max_media_segments": 30,
        "initial_quality": 0,
        "initial_controller_decision": False,
        "max_buffer_seconds": 60.0,
        "drain_buffer_sleep_seconds": 0.01,
        "preroll_seconds": 0.0,
    },
    "execution": {
        "timeout_seconds": 900.0,
        "resume": True,
        "run_sessions": True,
        "run_analysis": True,
        "max_sessions": None,
    },
    "controller_params": {
        "neural_abr_lite_robust_mpc": {
            "bundle_dir": "/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite",
            "fallback_controller": "robust_mpc",
            "verify_hashes": True,
            "max_inference_latency_ms": 50.0,
            "diagnostic_only": False,
        },
        "neural_abr_lite_teacher_hibrido": {
            "bundle_dir": "/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite",
            "fallback_controller": "robust_mpc",
            "verify_hashes": True,
            "max_inference_latency_ms": 50.0,
            "diagnostic_only": False,
        },
        "spbc_abr_v2_dpo_anchor_safe_rank": {
            "bundle_dir": "/home/daniel/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1_bundle",
            "fallback_controller": "robust_mpc",
            "verify_hashes": True,
            "max_inference_latency_ms": 50.0,
            "diagnostic_only": False,
        },
        "phase45_v3_neural_throughput_calibrated_mpc_v1": {
            "bundle_dir": "/home/daniel/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1",
            "fallback_controller": "robust_mpc",
            "verify_hashes": True,
            "max_inference_latency_ms": 50.0,
            "diagnostic_only": False,
        },
        "phase45_v3_neural_throughput_calibrated_mpc_v2": {
            "bundle_dir": "/home/daniel/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v2",
            "fallback_controller": "robust_mpc",
            "verify_hashes": True,
            "max_inference_latency_ms": 50.0,
            "diagnostic_only": False,
        },
    },
}


def cargar_config_fase6(path: Optional[str | Path] = None) -> Dict[str, Any]:
    selected = _elegir_ruta(path)
    config = deepcopy(CONFIG_FASE6_POR_DEFECTO)
    if RUTA_CONFIG_EJEMPLO_FASE6.exists():
        config = _fusion_profunda(config, _cargar_fichero_mapping(RUTA_CONFIG_EJEMPLO_FASE6))
    if selected is not None:
        if not selected.exists():
            raise FileNotFoundError("Config de Phase 6 no encontrada: {0}".format(selected))
        config = _fusion_profunda(config, _cargar_fichero_mapping(selected))
    return config


def escribir_config_ejemplo_fase6(path: Optional[str | Path] = None) -> Path:
    target = Path(path) if path is not None else RUTA_CONFIG_EJEMPLO_FASE6
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(CONFIG_FASE6_POR_DEFECTO, indent=2, sort_keys=True), encoding="utf-8")
    return target


def _elegir_ruta(path: Optional[str | Path]) -> Optional[Path]:
    if path is not None:
        return Path(path)
    if RUTA_CONFIG_LOCAL_FASE6.exists():
        return RUTA_CONFIG_LOCAL_FASE6
    if RUTA_CONFIG_LOCAL_ANTERIOR.exists():
        return RUTA_CONFIG_LOCAL_ANTERIOR
    return None


def _cargar_fichero_mapping(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig")
    stripped = text.lstrip()
    if not stripped:
        return {}
    if stripped.startswith("{"):
        loaded = json.loads(text)
    else:
        try:
            import yaml  # type: ignore
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "La config YAML de Phase 6 requiere PyYAML salvo que el fichero sea JSON."
            ) from exc
        loaded = yaml.safe_load(text) or {}
    if not isinstance(loaded, dict):
        raise ValueError("La raiz de la config de Phase 6 debe ser un mapping: {0}".format(path))
    return loaded


def _fusion_profunda(base: Mapping[str, Any], override: Mapping[str, Any]) -> Dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(merged.get(key), Mapping):
            merged[key] = _fusion_profunda(merged[key], value)
        else:
            merged[key] = value
    return merged
