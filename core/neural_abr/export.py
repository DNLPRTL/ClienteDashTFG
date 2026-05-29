"""Phase 4F export support for local-only NeuralABR-Lite bundles."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, MutableMapping

import torch

from core.neural_abr.artifacts import ensure_existing_dir, read_json, write_json
from core.neural_abr.bundle import (
    BUNDLE_ACTION_SPACE,
    BUNDLE_MODEL_FAMILY,
    BUNDLE_PHASE,
    BUNDLE_REWARD_CONTEXT,
    BUNDLE_SCHEMA_VERSION,
    BUNDLE_SOURCE_PHASE,
    BUNDLE_TEACHER,
    BUNDLE_TRAINING_METHOD,
    prepare_bundle_output_dir,
    validate_bundle_dir,
    write_bundle_manifest,
    write_json_file,
)
from core.neural_abr.constants import (
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_VECTOR_NAMES,
    FEATURE_SCHEMA_VERSION,
    NORMALIZATION_SCHEMA_VERSION,
    PHASE4E2_DECISION_CANDIDATE_READY,
    PRIMARY_TEACHER,
    REWARD_VERSION,
    TRAIN_SPLIT,
)


class ExportError(ValueError):
    """Raised when the Phase 4F export cannot be built safely."""


@dataclass(frozen=True)
class ExportResult:
    bundle_dir: Path
    manifest: Mapping[str, object]
    export_report: Mapping[str, object]

    def to_json(self) -> Mapping[str, object]:
        return {
            "bundle_dir": str(self.bundle_dir),
            "manifest": dict(self.manifest),
            "export_report": dict(self.export_report),
        }


def export_neural_abr_bundle(
    dataset_dir: object,
    run_dir: object,
    validation_dir: object,
    assessment_dir: object,
    output_dir: object,
    phase: str = BUNDLE_PHASE,
    overwrite: bool = False,
    docs_dir: object | None = None,
) -> ExportResult:
    if phase != BUNDLE_PHASE:
        raise ExportError("unsupported phase: {0}".format(phase))

    dataset_path = ensure_existing_dir(dataset_dir, purpose="Phase 4E.2 dataset")
    run_path = ensure_existing_dir(run_dir, purpose="Phase 4E.2 training run")
    validation_path = ensure_existing_dir(validation_dir, purpose="Phase 4E.2 validation")
    assessment_path = ensure_existing_dir(assessment_dir, purpose="Phase 4E.2 assessment")
    bundle_path = prepare_bundle_output_dir(output_dir, overwrite=overwrite)

    source_files = _source_files(dataset_path, run_path, validation_path, assessment_path)
    _assert_source_files(source_files)
    checkpoint = _load_checkpoint_cpu(source_files["checkpoint"])
    model_config = _model_config_from_checkpoint(checkpoint, read_json(source_files["model_config"]))
    normalization_stats = read_json(source_files["normalization_stats"])
    _validate_normalization_stats(normalization_stats)
    dataset_manifest = read_json(source_files["dataset_manifest"])
    training_report = read_json(source_files["training_report"])
    validation_report = read_json(source_files["offline_validation_report"])
    assessment_report = read_json(source_files["candidate_readiness_report"])
    _validate_assessment(assessment_report)

    shutil.copy2(source_files["checkpoint"], bundle_path / "model_state.pt")
    shutil.copy2(source_files["normalization_stats"], bundle_path / "normalization_stats.json")
    write_json_file(bundle_path / "feature_schema.json", _feature_schema(source_files["feature_schema"], dataset_manifest))
    write_json_file(bundle_path / "ladder_schema.json", _ladder_schema(dataset_manifest))
    write_json_file(bundle_path / "inference_contract.json", build_inference_contract())
    write_json_file(bundle_path / "fallback_policy.json", build_fallback_policy())
    model_card = build_model_card_json(
        dataset_manifest=dataset_manifest,
        training_report=training_report,
        validation_report=validation_report,
        assessment_report=assessment_report,
        model_config=model_config,
        source_paths={
            "dataset_dir": str(dataset_path),
            "run_dir": str(run_path),
            "validation_dir": str(validation_path),
            "assessment_dir": str(assessment_path),
        },
    )
    write_json_file(bundle_path / "model_card.json", model_card)

    created_at_utc = _utc_now()
    manifest_metadata = {
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "phase": BUNDLE_PHASE,
        "source_phase": BUNDLE_SOURCE_PHASE,
        "model_family": BUNDLE_MODEL_FAMILY,
        "training_method": BUNDLE_TRAINING_METHOD,
        "teacher": BUNDLE_TEACHER,
        "action_space": BUNDLE_ACTION_SPACE,
        "reward_context": BUNDLE_REWARD_CONTEXT,
        "model_file": "model_state.pt",
        "feature_schema_file": "feature_schema.json",
        "normalization_stats_file": "normalization_stats.json",
        "fallback_policy_file": "fallback_policy.json",
        "created_at_utc": created_at_utc,
        "source_run_dir": str(run_path),
        "source_dataset_dir": str(dataset_path),
        "source_validation_dir": str(validation_path),
        "source_assessment_dir": str(assessment_path),
        "model_config": model_config,
        "source_decision": assessment_report.get("decision"),
        "controller_registered": False,
        "client_integration": False,
        "diagnostic_only": True,
        "not_benchmark": True,
        "no_ranking": True,
        "no_sota_claim": True,
        "no_real_world_claim": True,
    }
    manifest = write_bundle_manifest(bundle_path, manifest_metadata)
    validate_bundle_dir(bundle_path)

    export_report = build_export_report(
        bundle_dir=bundle_path,
        manifest=manifest,
        model_card=model_card,
        training_report=training_report,
        validation_report=validation_report,
        assessment_report=assessment_report,
        created_at_utc=created_at_utc,
    )
    write_json(bundle_path / "export_log.json", export_report)
    if docs_dir is not None:
        write_phase4f_export_docs(export_report, model_card, docs_dir)

    return ExportResult(bundle_dir=bundle_path, manifest=manifest, export_report=export_report)


def build_inference_contract() -> Mapping[str, object]:
    return {
        "schema_version": "neural_abr_lite_inference_contract_v1",
        "phase": BUNDLE_PHASE,
        "offline_only": True,
        "cpu_first": True,
        "deterministic_eval_required": True,
        "input": {
            "context": list(CONTEXT_VECTOR_NAMES),
            "candidates": list(CANDIDATE_VECTOR_NAMES),
            "action_mask": "boolean mask over representation_index",
            "normalization": "train-only normalization_stats.json",
        },
        "output": {
            "scores": "one finite score per candidate representation after masking",
            "selected_representation_index": "integer representation_index with action_mask[index] == true",
        },
        "hard_rules": [
            "no future information",
            "no bitrate outside the MPD ladder",
            "no client runtime integration in Phase 4F",
            "no benchmark or ranking claim",
            "no SOTA or real-world validation claim",
        ],
    }


def build_fallback_policy() -> Mapping[str, object]:
    return {
        "schema_version": "neural_abr_lite_fallback_policy_v1",
        "phase": BUNDLE_PHASE,
        "future_integration_only": True,
        "fallback_controller_family": "classical_safe_controller",
        "fallback_required_when": [
            "bundle_missing_or_invalid",
            "schema_mismatch",
            "normalization_invalid",
            "model_load_failure",
            "nan_or_inf_score",
            "invalid_or_masked_action",
            "latency_safety_gate_failure",
        ],
        "phase4f_behavior": "document and validate offline only; no DashClientModular4 controller registration",
    }


def build_model_card_json(
    dataset_manifest: Mapping[str, object],
    training_report: Mapping[str, object],
    validation_report: Mapping[str, object],
    assessment_report: Mapping[str, object],
    model_config: Mapping[str, object],
    source_paths: Mapping[str, object],
) -> Mapping[str, object]:
    return {
        "schema_version": "neural_abr_lite_phase4f_model_card_v1",
        "phase": BUNDLE_PHASE,
        "model_family": BUNDLE_MODEL_FAMILY,
        "training_method": BUNDLE_TRAINING_METHOD,
        "teacher": PRIMARY_TEACHER,
        "action_space": BUNDLE_ACTION_SPACE,
        "reward_context": BUNDLE_REWARD_CONTEXT,
        "device": "cpu",
        "model_config": dict(model_config),
        "dataset_summary": dict(assessment_report.get("dataset_summary", {})),
        "training_summary": {
            "epochs": training_report.get("epochs"),
            "batch_size": training_report.get("batch_size"),
            "seed": training_report.get("seed"),
            "loss_last": training_report.get("loss_last"),
            "loss_mean": training_report.get("loss_mean"),
            "validation_metrics": training_report.get("validation_metrics"),
        },
        "validation_summary": {
            "status": validation_report.get("status"),
            "validation_metrics": validation_report.get("validation_metrics"),
            "ood_diagnostic_metrics": validation_report.get("ood_diagnostic_metrics"),
        },
        "source_decision": assessment_report.get("decision"),
        "dataset_ladder": dataset_manifest.get("content_ladder"),
        "source_paths": dict(source_paths),
        "boundaries": {
            "offline_export_inference_only": True,
            "client_integration": False,
            "controller_registered": False,
            "benchmark_or_ranking": False,
            "sota_claim": False,
            "real_world_validation_claim": False,
            "bundle_artifacts_local_only_outside_repo": True,
        },
    }


def build_export_report(
    bundle_dir: Path,
    manifest: Mapping[str, object],
    model_card: Mapping[str, object],
    training_report: Mapping[str, object],
    validation_report: Mapping[str, object],
    assessment_report: Mapping[str, object],
    created_at_utc: str,
) -> Mapping[str, object]:
    return {
        "schema_version": "neural_abr_lite_phase4f_export_report_v1",
        "phase": BUNDLE_PHASE,
        "status": "PASS",
        "decision": "EXPORT_COMPLETE_VALIDATION_REQUIRED",
        "created_at_utc": created_at_utc,
        "bundle_dir": str(bundle_dir),
        "source_decision": assessment_report.get("decision"),
        "required_files": manifest.get("required_files"),
        "hash_policy": manifest.get("hash_policy"),
        "model_family": model_card.get("model_family"),
        "training_method": model_card.get("training_method"),
        "teacher": model_card.get("teacher"),
        "validation_metrics": validation_report.get("validation_metrics"),
        "ood_diagnostic_metrics": validation_report.get("ood_diagnostic_metrics"),
        "training_validation_metrics": training_report.get("validation_metrics"),
        "boundaries": model_card.get("boundaries"),
    }


def write_phase4f_export_docs(
    export_report: Mapping[str, object],
    model_card: Mapping[str, object],
    docs_dir: object,
) -> None:
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)
    documents = {
        "phase4f_export_report.md": render_export_report_markdown(export_report),
        "phase4f_model_card.md": render_model_card_markdown(model_card),
        "phase4f_defense_talking_points.md": render_defense_talking_points_markdown(export_report),
        "phase4f_open_limitations.md": render_open_limitations_markdown(),
        "phase4f_closure_report.md": render_closure_report_markdown(
            decision="PHASE4F_EXPORT_PASS_NOT_READY_FOR_PHASE4G",
            reason="Export completed, bundle validation and inference smoke still need to run.",
            bundle_dir=str(export_report.get("bundle_dir")),
        ),
        "phase4f_to_phase4g_handoff.md": render_handoff_markdown(
            decision="PHASE4F_EXPORT_PASS_NOT_READY_FOR_PHASE4G",
            phase4g_allowed=False,
        ),
    }
    for filename, text in documents.items():
        (docs_path / filename).write_text(text, encoding="utf-8")


def render_export_report_markdown(report: Mapping[str, object]) -> str:
    validation = _mapping(report.get("validation_metrics"))
    ood = _mapping(report.get("ood_diagnostic_metrics"))
    return "\n".join(
        [
            "# Phase 4F Export Report",
            "",
            "Phase 4F is export/inference only. No DashClientModular4 controller is registered and there is no client integration.",
            "",
            "- Export status: `{0}`".format(report.get("status")),
            "- Bundle dir: `{0}`".format(report.get("bundle_dir")),
            "- Source decision: `{0}`".format(report.get("source_decision")),
            "- Validation valid action rate: `{0}`".format(validation.get("valid_action_rate")),
            "- OOD diagnostic valid action rate: `{0}`".format(ood.get("valid_action_rate")),
            "- Hash policy: `{0}`".format(report.get("hash_policy")),
            "",
            "The bundle artifacts are local-only and outside the repository. This report is not a benchmark, ranking, SOTA claim, or real-world validation.",
            "",
        ]
    )


def render_model_card_markdown(model_card: Mapping[str, object]) -> str:
    dataset = _mapping(model_card.get("dataset_summary"))
    training = _mapping(model_card.get("training_summary"))
    validation = _mapping(model_card.get("validation_summary"))
    validation_metrics = _mapping(validation.get("validation_metrics"))
    ood_metrics = _mapping(validation.get("ood_diagnostic_metrics"))
    return "\n".join(
        [
            "# Phase 4F Model Card",
            "",
            "Model: NeuralABR-Lite Candidate Scorer.",
            "",
            "This is a local-only export/inference bundle for Phase 4F. It is not integrated into the DASH client and no neural controller is registered.",
            "",
            "- Training method: `behavior_cloning` / `imitation_learning`",
            "- Teacher: `{0}`".format(model_card.get("teacher")),
            "- Action: `{0}`".format(model_card.get("action_space")),
            "- Reward context: `{0}`".format(model_card.get("reward_context")),
            "- Device: `{0}`".format(model_card.get("device")),
            "- Trace count: `{0}`".format(dataset.get("trace_count")),
            "- Validation valid action rate: `{0}`".format(validation_metrics.get("valid_action_rate")),
            "- OOD diagnostic valid action rate: `{0}`".format(ood_metrics.get("valid_action_rate")),
            "- Epochs: `{0}`".format(training.get("epochs")),
            "- Batch size: `{0}`".format(training.get("batch_size")),
            "",
            "No benchmark/ranking, SOTA, or real-world validation claim is made. Phase 4G will decide whether Phase 5 integration is allowed.",
            "",
        ]
    )


def render_defense_talking_points_markdown(report: Mapping[str, object]) -> str:
    return "\n".join(
        [
            "# Phase 4F Defense Talking Points",
            "",
            "- Phase 4F deliberately separates model export/inference from client integration.",
            "- The bundle contains the model state, feature schema, train-only normalization, ladder schema, inference contract, fallback policy, model card, and manifest hashes.",
            "- Action masking is enforced at inference so invalid MPD representation indices cannot be selected.",
            "- CPU-only loading keeps the candidate compatible with the validated hardware boundary.",
            "- The fallback policy is documented for future Phase 5 integration, but Phase 4F does not execute a client fallback path.",
            "- The latency report is a safety feasibility check only, not a benchmark against ABR controllers.",
            "- No benchmark/ranking, SOTA, or real-world validation claim is made.",
            "- Phase 4G remains the gate that decides whether Phase 5 integration is allowed.",
            "- Phase 4F-R1 separates correctness gates from environmental/repo hygiene gates.",
            "- Pure temporary bundle fixtures report repo hygiene as not checked unless `--check-repo-hygiene` is supplied.",
            "- Explicit repo hygiene validation remains blocking when requested.",
            "- Phase 4G is allowed only after Windows and Ubuntu both pass the repaired Phase 4F validation commands.",
            "",
            "Bundle dir: `{0}`".format(report.get("bundle_dir")),
            "",
        ]
    )


def render_open_limitations_markdown() -> str:
    return "\n".join(
        [
            "# Phase 4F Open Limitations",
            "",
            "- Phase 4F is export/inference only.",
            "- NeuralABR-Lite is not registered as a controller and is not integrated into DashClientModular4 runtime.",
            "- No benchmark, ranking, SOTA claim, or real-world validation claim is made.",
            "- Bundle artifacts are local-only and must stay outside the repository.",
            "- OOD diagnostics remain diagnostic-only and must not be tuned on.",
            "- Future Phase 4G must decide whether Phase 5 integration is allowed.",
            "- Future integration must retain a classical safe fallback for invalid, slow, missing, or non-finite neural inference.",
            "- Default pure bundle validation does not scan repository hygiene. Run `scripts/validate_neural_abr_bundle.py --check-repo-hygiene` or external validation/commit checks when repo artifact hygiene must be blocking.",
            "- Phase 4G is allowed only after the repaired Phase 4F validation passes on both Windows and Ubuntu.",
            "",
        ]
    )


def render_closure_report_markdown(decision: str, reason: str, bundle_dir: str | None = None) -> str:
    return "\n".join(
        [
            "# Phase 4F Closure Report",
            "",
            "Decision: `{0}`".format(decision),
            "",
            reason,
            "",
            "- Phase 4F scope: export/inference only.",
            "- Client integration: `false`.",
            "- Controller registered: `false`.",
            "- Benchmark/ranking: `false`.",
            "- SOTA or real-world claim: `false`.",
            "- Bundle artifacts local-only outside repo: `true`.",
            "- Bundle dir: `{0}`".format(bundle_dir or ""),
            "",
            "Phase 4G is allowed only after Windows and Ubuntu both pass the repaired Phase 4F validation commands. Phase 4G will decide whether Phase 5 integration is allowed.",
            "",
        ]
    )


def render_handoff_markdown(decision: str, phase4g_allowed: bool) -> str:
    return "\n".join(
        [
            "# Phase 4F to Phase 4G Handoff",
            "",
            "- Decision: `{0}`".format(decision),
            "- Phase 4G allowed: `{0}`".format(str(bool(phase4g_allowed)).lower()),
            "",
            "Phase 4G may review the local-only bundle, validation report, inference smoke report, latency report, and limitations before deciding whether Phase 5 client integration is allowed.",
            "",
            "This handoff does not register a neural controller and does not change controllers, player, runtime, media, or `main.py`.",
            "",
        ]
    )


def _source_files(dataset_path: Path, run_path: Path, validation_path: Path, assessment_path: Path) -> Mapping[str, Path]:
    return {
        "dataset_manifest": dataset_path / "dataset_manifest.json",
        "feature_schema": dataset_path / "feature_schema.json",
        "checkpoint": run_path / "checkpoint.pt",
        "model_config": run_path / "model_config.json",
        "normalization_stats": run_path / "normalization_stats.json",
        "training_report": run_path / "training_report.json",
        "offline_validation_report": validation_path / "offline_validation_report.json",
        "candidate_readiness_report": assessment_path / "candidate_readiness_report.json",
    }


def _assert_source_files(source_files: Mapping[str, Path]) -> None:
    missing = [name for name, path in source_files.items() if not path.is_file()]
    if missing:
        details = ", ".join("{0}={1}".format(name, source_files[name]) for name in missing)
        raise ExportError("missing source artifact(s): {0}".format(details))


def _load_checkpoint_cpu(path: Path) -> Mapping[str, object]:
    try:
        checkpoint = _torch_load_cpu(path)
    except Exception as exc:  # noqa: BLE001 - preserve clear export failure.
        raise ExportError("failed to load checkpoint on CPU: {0}".format(path)) from exc
    if not isinstance(checkpoint, Mapping):
        raise ExportError("checkpoint must contain a mapping: {0}".format(path))
    if "model_state_dict" not in checkpoint:
        raise ExportError("checkpoint missing model_state_dict: {0}".format(path))
    return checkpoint


def _torch_load_cpu(path: Path) -> object:
    try:
        return torch.load(path, map_location="cpu", weights_only=True)
    except TypeError:
        return torch.load(path, map_location="cpu")
    except Exception:
        return torch.load(path, map_location="cpu", weights_only=False)


def _model_config_from_checkpoint(checkpoint: Mapping[str, object], file_config: Mapping[str, object]) -> Mapping[str, object]:
    raw_config = checkpoint.get("model_config")
    config = dict(raw_config if isinstance(raw_config, Mapping) else file_config)
    if config.get("device_default", "cpu") != "cpu":
        raise ExportError("model_config device_default must be cpu")
    if config.get("controller_registered") is not False:
        raise ExportError("model_config must keep controller_registered=false")
    return config


def _validate_normalization_stats(stats: Mapping[str, object]) -> None:
    if stats.get("schema_version") != NORMALIZATION_SCHEMA_VERSION:
        raise ExportError("normalization_stats schema_version is invalid")
    if stats.get("fitted_on_split") != TRAIN_SPLIT:
        raise ExportError("normalization_stats must be fitted on train")


def _validate_assessment(report: Mapping[str, object]) -> None:
    if report.get("decision") != PHASE4E2_DECISION_CANDIDATE_READY:
        raise ExportError("Phase 4E.2 assessment is not candidate-ready")
    if report.get("correctness_failures"):
        raise ExportError("Phase 4E.2 assessment has correctness failures")
    if report.get("candidate_failures"):
        raise ExportError("Phase 4E.2 assessment has candidate failures")


def _feature_schema(feature_schema_path: Path, dataset_manifest: Mapping[str, object]) -> Mapping[str, object]:
    schema: MutableMapping[str, object] = dict(read_json(feature_schema_path))
    if schema.get("schema_version") != FEATURE_SCHEMA_VERSION:
        raise ExportError("feature_schema schema_version is invalid")
    schema["phase4f_export"] = {
        "source_phase": BUNDLE_SOURCE_PHASE,
        "dataset_split_policy": dataset_manifest.get("split_policy"),
        "context_vector_names": list(CONTEXT_VECTOR_NAMES),
        "candidate_vector_names": list(CANDIDATE_VECTOR_NAMES),
        "no_future_information": True,
        "teacher_labels_are_not_inputs": True,
    }
    return dict(schema)


def _ladder_schema(dataset_manifest: Mapping[str, object]) -> Mapping[str, object]:
    ladder = dataset_manifest.get("content_ladder")
    if not isinstance(ladder, Mapping):
        raise ExportError("dataset_manifest missing content_ladder")
    return {
        "schema_version": "neural_abr_lite_ladder_schema_v1",
        "phase": BUNDLE_PHASE,
        "source": "dataset_manifest.content_ladder",
        "action_space": BUNDLE_ACTION_SPACE,
        "reward_version": REWARD_VERSION,
        "representation_index_policy": "contiguous_zero_based_indices",
        "content_ladder": dict(ladder),
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}
