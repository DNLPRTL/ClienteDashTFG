from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PHASE6_EXAMPLE_CONFIG = REPO_ROOT / "config" / "phase6.example.yaml"
DEFAULT_PHASE6_LOCAL_CONFIG = REPO_ROOT / "config" / "phase6.local.yaml"

DEFAULT_PHASE6_CONFIG: Dict[str, Any] = {
    "schema_version": "phase6_config_v1",
    "paths": {
        "manifest_path": "/home/daniel/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json",
        "output_root": "/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa",
        "repo_root": "/home/daniel/TFG/DashClientModular4",
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
    },
}


def load_phase6_config(path: Optional[str | Path] = None) -> Dict[str, Any]:
    selected = _select_path(path)
    config = deepcopy(DEFAULT_PHASE6_CONFIG)
    if DEFAULT_PHASE6_EXAMPLE_CONFIG.exists():
        config = _deep_merge(config, _load_mapping_file(DEFAULT_PHASE6_EXAMPLE_CONFIG))
    if selected is not None:
        if not selected.exists():
            raise FileNotFoundError("Phase 6 config not found: {0}".format(selected))
        config = _deep_merge(config, _load_mapping_file(selected))
    return config


def write_phase6_example_config(path: Optional[str | Path] = None) -> Path:
    target = Path(path) if path is not None else DEFAULT_PHASE6_EXAMPLE_CONFIG
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(DEFAULT_PHASE6_CONFIG, indent=2, sort_keys=True), encoding="utf-8")
    return target


def _select_path(path: Optional[str | Path]) -> Optional[Path]:
    if path is not None:
        return Path(path)
    if DEFAULT_PHASE6_LOCAL_CONFIG.exists():
        return DEFAULT_PHASE6_LOCAL_CONFIG
    return None


def _load_mapping_file(path: Path) -> Dict[str, Any]:
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
                "Phase 6 YAML config requires PyYAML unless the file is JSON-formatted."
            ) from exc
        loaded = yaml.safe_load(text) or {}
    if not isinstance(loaded, dict):
        raise ValueError("Phase 6 config root must be a mapping: {0}".format(path))
    return loaded


def _deep_merge(base: Mapping[str, Any], override: Mapping[str, Any]) -> Dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(merged.get(key), Mapping):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged
