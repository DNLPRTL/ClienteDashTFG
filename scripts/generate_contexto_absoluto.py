#!/usr/bin/env python3
from __future__ import annotations

import ast
import csv
import html
import json
import os
import re
import subprocess
import sys
import textwrap
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
TFG_ROOT = REPO_ROOT.parent
DOC_OUTPUT = REPO_ROOT / "docs" / "contexto_para_ia" / "CONTEXTO_ABSOLUTO_DASHCLIENTMODULAR4_20260615.md"
PDF_OUTPUT = REPO_ROOT / "output" / "pdf" / "CONTEXTO_ABSOLUTO_DASHCLIENTMODULAR4_20260615.pdf"

EXCLUDED_DIR_NAMES = {
    ".git",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "venv",
}


@dataclass(frozen=True)
class MarkdownInfo:
    path: Path
    rel: str
    size: int
    first_heading: str
    headings: tuple[str, ...]
    status_lines: tuple[str, ...]


@dataclass(frozen=True)
class PythonInfo:
    path: Path
    rel: str
    size: int
    module_doc: str
    classes: tuple[str, ...]
    functions: tuple[str, ...]
    constants: tuple[str, ...]
    parse_error: str = ""


def main() -> int:
    DOC_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PDF_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    markdown = build_markdown()
    DOC_OUTPUT.write_text(markdown, encoding="utf-8", newline="\n")
    render_pdf(markdown, PDF_OUTPUT)

    print(json.dumps({
        "markdown": str(DOC_OUTPUT),
        "pdf": str(PDF_OUTPUT),
        "markdown_bytes": DOC_OUTPUT.stat().st_size,
        "pdf_bytes": PDF_OUTPUT.stat().st_size,
    }, indent=2, ensure_ascii=False))
    return 0


def build_markdown() -> str:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    git_status = run_git(["status", "--short", "--branch"])
    git_branches = run_git(["branch", "--all", "--verbose", "--no-abbrev"])
    git_log = run_git(["log", "--oneline", "--decorate", "--graph", "-n", "120"])
    git_head = run_git(["rev-parse", "HEAD"]).strip()
    repo_files = list_repo_files()
    md_infos = collect_markdown_infos()
    py_infos = collect_python_infos()
    scripts = sorted(
        (
            p
            for p in (REPO_ROOT / "scripts").rglob("*")
            if p.is_file() and not any(part in EXCLUDED_DIR_NAMES for part in p.parts)
        ),
        key=rel_sort_key,
    )
    tests = sorted((p for p in (REPO_ROOT / "tests").rglob("*.py") if p.is_file()), key=rel_sort_key)
    external_top = collect_external_top_level()
    external_dirs = collect_external_directories()
    phase6_packages = collect_phase6_packages()
    external_key_files = collect_external_key_files()
    controller_registry = parse_controller_registry()
    markdown_by_bucket = bucket_markdown(md_infos)

    lines: list[str] = []
    add_title(lines, now, git_head)
    add_scope_and_sources(lines, md_infos, py_infos, scripts, tests, repo_files, external_dirs)
    add_current_state(lines, git_status, git_branches, git_log, controller_registry)
    add_operating_model(lines)
    add_environment_architecture(lines)
    add_repository_and_external_layout(lines, repo_files, external_top, external_dirs, external_key_files)
    add_phase_history(lines)
    add_ai_controller_history(lines)
    add_phase6_method(lines)
    add_scientific_corpus(lines, markdown_by_bucket)
    add_code_architecture(lines, py_infos, controller_registry)
    add_command_protocols(lines)
    add_phase6_packages(lines, phase6_packages)
    add_catalogs(lines, md_infos, py_infos, scripts, tests, external_dirs)
    add_closing_handoff(lines)

    return "\n".join(lines).rstrip() + "\n"


def add_title(lines: list[str], now: str, git_head: str) -> None:
    lines.extend([
        "# Contexto absoluto tecnico - ClienteDashPrudente",
        "",
        "| Campo | Valor |",
        "|---|---|",
        f"| Proyecto | `ClienteDashPrudente` |",
        f"| Ruta Windows | `{REPO_ROOT}` |",
        f"| Raiz TFG Windows | `{TFG_ROOT}` |",
        f"| Fecha de generacion | `{now}` |",
        f"| Rama activa esperada | `rebuild/phase3-from-phase2` |",
        f"| HEAD observado | `{git_head}` |",
        f"| Entregable IA | `{DOC_OUTPUT}` |",
        f"| Entregable humano | `{PDF_OUTPUT}` |",
        "",
        "## Proposito exacto",
        "",
        "Este documento consolida el estado tecnico y operativo materializado en el repositorio y en las carpetas hermanas visibles de `C:\\Users\\danie\\Documents\\TFG`. Esta pensado para que otra IA pueda continuar el proyecto sin depender de memoria conversacional no versionada.",
        "",
        "El documento contiene hechos, contratos, rutas, fases, reglas, arquitectura, estado actual, catalogos de fuentes y piezas de codigo. No contiene recomendaciones nuevas, ranking, conclusiones subjetivas ni afirmaciones de mejora de QoE no autorizadas.",
        "",
        "## Alcance verificable",
        "",
        "- Incluye documentos y chats que estan materializados como archivos Markdown dentro del repo, especialmente `docs/contexto del orquestador el chat web/CONTEXTO_MAESTRO_WEB_TFG.md`.",
        "- Incluye inventario automatico del codigo, scripts, tests, docs y carpetas externas visibles.",
        "- No afirma haber leido conversaciones que no existan como archivo accesible en el filesystem.",
        "- No copia datasets, modelos, trazas, bundles, zips, PDFs ni media al repositorio.",
        "",
    ])


def add_scope_and_sources(
    lines: list[str],
    md_infos: Sequence[MarkdownInfo],
    py_infos: Sequence[PythonInfo],
    scripts: Sequence[Path],
    tests: Sequence[Path],
    repo_files: Sequence[Path],
    external_dirs: Sequence[Mapping[str, Any]],
) -> None:
    docs_count = len(md_infos)
    py_count = len(py_infos)
    script_count = len(scripts)
    test_count = len(tests)
    repo_count = len(repo_files)
    external_count = len(external_dirs)
    lines.extend([
        "## Fuentes inspeccionadas",
        "",
        "| Fuente | Conteo | Observacion |",
        "|---|---:|---|",
        f"| Archivos versionados detectados por `git ls-files` | {repo_count} | Inventario de repo limpio sin `.git` |",
        f"| Markdown versionados | {docs_count} | Docs, source cards, decisiones, runbooks y corpus convertido |",
        f"| Modulos Python inventariados | {py_count} | `core`, `scripts`, `tests`, entrypoints y utilidades |",
        f"| Scripts/runbooks en `scripts/` | {script_count} | Python y shell versionados |",
        f"| Tests Python | {test_count} | `unittest`/tests estructurales |",
        f"| Directorios externos bajo raiz TFG | {external_count} | Inventario de carpetas hermanas y paquetes generados |",
        "",
        "Documentos obligatorios leidos y usados como autoridad inicial:",
        "",
        "```text",
        "docs/arquitectura y procedimientos estandar tfg dash/arquitectura_y_procedimientos_estandar_tfg_dash.md",
        "docs/arquitectura y procedimientos estandar tfg dash/TFG_PLAN_GENERICO.md",
        "docs/contexto rama nueva/fase_4_5_v1/proceso_desarrollo_ia_abr.md",
        "```",
        "",
        "Contexto secundario usado cuando aplica:",
        "",
        "```text",
        "docs/contexto rama nueva/",
        "docs/contexto rama original/",
        "docs/contexto del orquestador el chat web/",
        "docs/todos los estudios pdf convertidos a md/",
        "```",
        "",
    ])


def add_current_state(
    lines: list[str],
    git_status: str,
    git_branches: str,
    git_log: str,
    controller_registry: Sequence[Mapping[str, str]],
) -> None:
    lines.extend([
        "## Estado actual de rama y continuidad",
        "",
        "Estado Git observado al generar este documento:",
        "",
        "```text",
        git_status.strip() or "(sin salida)",
        "```",
        "",
        "Ramas observadas:",
        "",
        "```text",
        git_branches.strip(),
        "```",
        "",
        "Lectura tecnica del estado:",
        "",
        "- La rama activa es `rebuild/phase3-from-phase2`.",
        "- La rama `archive/current-before-phase3-rebuild` existe como referencia historica protegida del estado anterior a la reconstruccion desde Phase 2.",
        "- `main` aparece como referencia historica/otra rama, no como rama activa de trabajo de este hilo.",
        "- El ultimo commit observado en la rama activa es `feat(phase45): add closed-loop spbc spc dataset`.",
        "- La fase activa declarada por `AGENTS.md` es `Phase 6 implementation ready - validacion comparativa formal`.",
        "- Fase 4-5 v1 queda abierta como iteracion nueva e independiente para controllers IA nuevos; no sustituye las Phase 4/5 cerradas.",
        "",
        "Log reciente de la rama activa:",
        "",
        "```text",
        git_log.strip(),
        "```",
        "",
        "Controllers registrados en `core/controller/registry.py`:",
        "",
        "| Key | Label | Factory |",
        "|---|---|---|",
    ])
    for row in controller_registry:
        lines.append(f"| `{row['key']}` | {escape_table(row['label'])} | `{row['factory']}` |")
    lines.extend([
        "",
        "Interpretacion de registry:",
        "",
        "- Sanity/control: `min_rate`, `fixed_rate`, `max_rate`, `fixed_quality`, `scripted_quality`, `max_quality`.",
        "- Baselines academicos clasicos: `rate_based`, `bba`, `bola`, `mpc`, `robust_mpc`.",
        "- IA historica Phase 4/5: `neural_abr_lite_robust_mpc`, `neural_abr_lite_teacher_hibrido`.",
        "- IA experimental SPBC v2: `spbc_abr_v2_dpo_anchor_safe_rank`.",
        "- IA viva Neural-MPC: `phase45_v3_neural_throughput_calibrated_mpc_v1` y `phase45_v3_neural_throughput_calibrated_mpc_v2`.",
        "",
    ])


def add_operating_model(lines: list[str]) -> None:
    lines.extend([
        "## Modelo de trabajo Codex-Daniel",
        "",
        "Contrato operativo permanente:",
        "",
        "```text",
        "Codex prepara, implementa, valida rapido, commitea/pushea cuando cierre cambios.",
        "Daniel ejecuta en Ubuntu cliente o WSL2 los entrenamientos/evaluaciones largos.",
        "Daniel pega resultados, logs o resumenes.",
        "Se discute el resultado y se decide el siguiente paso documentado.",
        "```",
        "",
        "Responsabilidades:",
        "",
        "| Actor/entorno | Responsabilidad | No debe hacer |",
        "|---|---|---|",
        "| Codex en Windows | Desarrollo, scripts, docs, tests, commits, push, runbooks cortos | Pedir bloques largos manuales, improvisar ciencia sin spec |",
        "| Daniel en Ubuntu cliente | `git pull`, lanzar validaciones Phase 6, devolver resultados | Editar codigo manualmente como flujo normal |",
        "| Daniel en WSL2 ROCm | Lanzar entrenamientos IA pesados con scripts versionados | Usar `/mnt/c/...` como raiz principal de entrenamiento |",
        "| Ubuntu servidor | Servir MPD, segmentos e inicializaciones DASH por HTTP | Definir la red experimental o el benchmark |",
        "",
        "Forma de dar comandos a Daniel:",
        "",
        "- Comandos cortos.",
        "- Preferencia por `git pull` y `bash scripts/<script>.sh`.",
        "- Sin heredocs largos, bucles extensos ni listas de flags manuales.",
        "- Si una ejecucion larga se repite, se versiona un script en `scripts/`.",
        "- Windows y Ubuntu cliente se conectan por GitHub, no copiando codigo a mano.",
        "",
        "Cierre normal de un bloque en Windows:",
        "",
        "```powershell",
        "git status --short --branch",
        "git diff --check",
        "python -m unittest discover",
        "python scripts/comprobar_cliente.py --strict",
        "git add <rutas explicitas>",
        "git commit -m \"mensaje claro\"",
        "git push",
        "```",
        "",
        "Sin embargo, artefactos pesados o generados no se commitean: datasets, trazas normalizadas, manifests finales generados, runs, logs, modelos, bundles, zips, PDFs, videos, segmentos DASH y paquetes de evidencia.",
        "",
    ])


def add_environment_architecture(lines: list[str]) -> None:
    lines.extend([
        "## Arquitectura de entornos",
        "",
        "La arquitectura operativa no trata el proyecto como una unica maquina. Hay cuatro entornos con responsabilidades separadas.",
        "",
        "| Entorno | Ruta/estado | Papel |",
        "|---|---|---|",
        "| Windows fisico | `C:\\Users\\danie\\Documents\\TFG\\ClienteDashPrudente` | Desarrollo, tests rapidos, docs, commits, push |",
        "| WSL2 Ubuntu ROCm | `~/TFG/ClienteDashPrudente`, venv `~/venvs/rocm721` | Entrenamiento IA pesado y generacion de artefactos externos |",
        "| Ubuntu cliente | `~/TFG/ClienteDashPrudente` | Validacion real, Phase 6, paquetes de evidencia |",
        "| Ubuntu servidor | `/var/www/html/dash` | Servir MPD/segmentos/inits por HTTP |",
        "",
        "Estado WSL2/ROCm observado y documentado:",
        "",
        "```text",
        "Distribucion: Ubuntu-24.04 en WSL2",
        "Ubuntu observado: Ubuntu 24.04.4 LTS",
        "Venv GPU: ~/venvs/rocm721",
        "Torch observado: 2.9.1+rocm7.2.1",
        "GPU observada: AMD Radeon RX 7800 XT",
        "torch.cuda.is_available(): True",
        "```",
        "",
        "Comprobacion WSL2 recomendada:",
        "",
        "```bash",
        "wsl -d Ubuntu-24.04",
        "cd ~/TFG/ClienteDashPrudente",
        "git pull",
        "source ~/venvs/rocm721/bin/activate",
        "python3 -c \"import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))\"",
        "```",
        "",
        "Regla de rutas WSL2:",
        "",
        "- Datasets, checkpoints, modelos, logs y runs de entrenamiento deben vivir bajo rutas Linux dentro de `~/TFG`.",
        "- `/mnt/c/Users/danie/Documents/TFG/...` puede usarse para consultas puntuales, no como workspace principal de entrenamiento pesado.",
        "",
        "Servidor DASH observado/documentado:",
        "",
        "```text",
        "Base Ubuntu servidor: /var/www/html/dash",
        "URL ejemplo: http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd",
        "Comprobacion aceptada: HTTP/1.1 200 OK",
        "```",
        "",
    ])


def add_repository_and_external_layout(
    lines: list[str],
    repo_files: Sequence[Path],
    external_top: Sequence[Mapping[str, Any]],
    external_dirs: Sequence[Mapping[str, Any]],
    external_key_files: Sequence[Mapping[str, Any]],
) -> None:
    by_top = Counter(path.parts[0] if path.parts else "." for path in repo_files)
    lines.extend([
        "## Estructura del repositorio y carpetas hermanas",
        "",
        "Top-level versionado detectado por `git ls-files`:",
        "",
        "| Carpeta/archivo | Archivos versionados |",
        "|---|---:|",
    ])
    for name, count in sorted(by_top.items()):
        lines.append(f"| `{name}` | {count} |")
    lines.extend([
        "",
        "Carpetas principales del repo:",
        "",
        "| Ruta | Papel tecnico |",
        "|---|---|",
        "| `core/` | Codigo de cliente, controllers, trace replay, QoE, Phase 6 y entrenamiento IA |",
        "| `scripts/` | Runbooks ejecutables, generadores, entrenadores, validadores, empaquetadores |",
        "| `tests/` | Tests unitarios/estructurales/contratos |",
        "| `docs/` | Contexto cientifico, decisiones, source cards, runbooks, cierres y memoria |",
        "| `config/` | Configs ejemplo de cliente y Phase 6 |",
        "| `output/pdf/` | PDFs generados localmente; no se deben commitear |",
        "",
        "Carpetas hermanas externas detectadas bajo la raiz TFG:",
        "",
        "| Nombre | Directorios | Archivos | Ultima modificacion |",
        "|---|---:|---:|---|",
    ])
    for row in external_top:
        lines.append(f"| `{row['name']}` | {row['directories']} | {row['files']} | `{row['mtime']}` |")
    lines.extend([
        "",
        "Rutas externas canonicas activas:",
        "",
        "```text",
        "C:\\Users\\danie\\Documents\\TFG\\dataset en bruto",
        "C:\\Users\\danie\\Documents\\TFG\\datasets_normalizados",
        "C:\\Users\\danie\\Documents\\TFG\\manifests_trazas",
        "C:\\Users\\danie\\Documents\\TFG\\runs_trazas",
        "C:\\Users\\danie\\Documents\\TFG\\auditorias_trazas",
        "C:\\Users\\danie\\Documents\\TFG\\modelos",
        "```",
        "",
        "Artefactos externos relevantes fijados por instrucciones:",
        "",
        "```text",
        "C:\\Users\\danie\\Documents\\TFG\\manifests_trazas\\phase3\\final\\phase3_trace_manifest_curated.json",
        "C:\\Users\\danie\\Documents\\TFG\\runs_trazas\\phase3_5\\smoke",
        "```",
        "",
        "Archivos externos clave encontrados por nombre/patron:",
        "",
        "| Ruta relativa a TFG | Tamano bytes | Ultima modificacion |",
        "|---|---:|---|",
    ])
    for row in external_key_files[:300]:
        lines.append(f"| `{escape_table(row['rel'])}` | {row['size']} | `{row['mtime']}` |")
    if len(external_key_files) > 300:
        lines.append(f"| `(catalogo truncado en PDF/MD principal)` | {len(external_key_files) - 300} | archivos clave adicionales omitidos de esta tabla |")
    lines.extend([
        "",
        "Nota de no contaminacion: el inventario externo documenta existencia y rutas. No mueve ni copia artefactos al repo.",
        "",
    ])


def add_phase_history(lines: list[str]) -> None:
    lines.extend([
        "## Historia formal por fases",
        "",
        "### Phase 1 - Client hardening",
        "",
        "Estado: cerrada.",
        "",
        "Objetivo: convertir el cliente DASH en una base tecnica estable, modular, reproducible y ABR-neutral.",
        "",
        "Resultados cerrados:",
        "",
        "- Config YAML y runner controlado.",
        "- Layout reproducible de runs.",
        "- Outputs canonicos: `run_manifest.json`, `config.resolved.json`, `environment.json`, `run.log`, `segment_telemetry.csv`, `evaluation_segments.csv`.",
        "- Eliminacion de outputs legacy `dataset.csv` y `dataset_training.csv` como artefactos canonicos.",
        "- Fake media engine como camino controlado.",
        "- GStreamer como integracion/demo, no evidencia equivalente de benchmark.",
        "- Controller contract y feedback runtime.",
        "- Benchmark neutrality contract.",
        "- Readiness gate con `scripts/comprobar_cliente.py --strict`.",
        "",
        "No significa: benchmark, ranking, QoE final, baselines academicos o IA.",
        "",
        "### Phase 2 - Baselines ABR clasicos",
        "",
        "Estado: cerrada.",
        "",
        "Controllers implementados:",
        "",
        "```text",
        "min_rate",
        "fixed_rate",
        "max_rate",
        "rate_based",
        "bba",
        "bola",
        "mpc",
        "robust_mpc",
        "```",
        "",
        "Proceso usado:",
        "",
        "```text",
        "paper/source -> paper_card/source_evidence -> implementation_spec -> controller_api_mapping -> acceptance_tests -> codigo -> tests -> docs",
        "```",
        "",
        "Papel de cada baseline:",
        "",
        "- `rate_based`: seleccion por throughput medido y factor de seguridad.",
        "- `bba`: decision por ocupacion de buffer con reservoir/cushion.",
        "- `bola`: utilidad/buffer, BOLA-basic, sin DYNAMIC ni FAST SWITCHING.",
        "- `mpc`: enumeracion de secuencias con prediccion de throughput y reward interno.",
        "- `robust_mpc`: MPC conservador con error historico y fallback seguro.",
        "",
        "No significa: comparacion formal, ganador ni QoE final.",
        "",
        "### Phase 3 Rebuild - Trazas y replay",
        "",
        "Estado: cerrada en Windows con corpus externo, auditoria de calidad, replay tecnico y manifest curado recomendado.",
        "",
        "Unidad canonica:",
        "",
        "```text",
        "throughput_kbps",
        "```",
        "",
        "Schema normalizado:",
        "",
        "```csv",
        "timestamp_s,duration_s,throughput_kbps",
        "```",
        "",
        "Separacion obligatoria:",
        "",
        "- Las muestras que ve el replay no contienen `trace_id`, `dataset_id`, `source_id`, `split`, `group_id`, `leakage_group`, etiqueta OOD ni futuro throughput como input del controller.",
        "- Los splits `train`, `test` y `eval` se hacen por `leakage_group`/grupo semantico, no por filas.",
        "- FCC, Puffer y GAViST quedan marcados por semantica para no tratarlos sin control como trazas directas de ancho de banda disponible.",
        "",
        "Manifest curado activo:",
        "",
        "```text",
        "C:\\Users\\danie\\Documents\\TFG\\manifests_trazas\\phase3\\final\\phase3_trace_manifest_curated.json",
        "```",
        "",
        "### Addendum sintetico Phase 3",
        "",
        "Contrato sintetico:",
        "",
        "```text",
        "dataset_id=synthetic_controlled_network",
        "semantics=synthetic_available_bandwidth",
        "generator_id=phase3_synthetic_controlled_network_v1",
        "trace_count=6768",
        "synthetic_trace_count=1024",
        "synthetic_split_counts=train:720,test:152,eval:152",
        "```",
        "",
        "Regla: resultados sinteticos futuros se reportan separados de trazas reales y no autorizan generalizacion real-world.",
        "",
        "### Phase 3.5 Rebuild - QoE, reward y gates",
        "",
        "Estado: cerrada en Windows con contrato `qoe_linear_v1`, calculadora QoE pura, postprocesador QoE, gates y smokes sinteticos controlados.",
        "",
        "Formula cerrada:",
        "",
        "```text",
        "qoe_formula_version=qoe_linear_v1",
        "reward_n = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps",
        "primary_session_metric=qoe_linear_mean",
        "```",
        "",
        "Detalles:",
        "",
        "- `qoe_log_v1` es metrica secundaria de sensibilidad.",
        "- `startup_delay_s` es report-only.",
        "- VMAF queda deferred/artifact-dependent.",
        "- Gates validos: `use_for_eval`, `diagnostic_only`, `do_not_use_for_eval`.",
        "- Smokes QoE son sinteticos y no consumen trazas reales.",
        "",
        "Flags requeridos para smokes QoE:",
        "",
        "```text",
        "outputs_are_benchmark_results=false",
        "benchmark_performed=false",
        "ranking_performed=false",
        "no_final_ranking=true",
        "ia_training_performed=false",
        "```",
        "",
        "### Phase 4 Rebuild - NeuralABR-Lite offline",
        "",
        "Estado: cerrada en Ubuntu con dos bundles offline `NeuralABR-Lite`: uno entrenado con `robust_mpc` real y otro con `teacher_hibrido`.",
        "",
        "Metodo:",
        "",
        "- Candidate scorer pequeno, CPU-first.",
        "- Entrenamiento por imitation learning/behavior cloning.",
        "- Salida como score por representacion candidata.",
        "- Action mask, normalization train-only y contrato de bundle.",
        "- Artefactos pesados fuera de Git.",
        "",
        "No hay benchmark, ranking, ganador ni afirmacion autorizada de mejora QoE.",
        "",
        "### Phase 5 - Integracion de IA historica",
        "",
        "Estado: cerrada en Ubuntu con dos controllers IA integrados.",
        "",
        "Controllers:",
        "",
        "```text",
        "neural_abr_lite_robust_mpc",
        "neural_abr_lite_teacher_hibrido",
        "```",
        "",
        "Contrato de runtime:",
        "",
        "- Carga de bundle local-only fuera del repo.",
        "- Inferencia CPU.",
        "- Verificacion de hashes cuando esta configurada.",
        "- Action mask.",
        "- Safety guard.",
        "- Fallback a `robust_mpc`.",
        "- Telemetria neural diagnostica en `segment_telemetry.csv`.",
        "- `evaluation_segments.csv` queda limpio de columnas IA.",
        "",
        "No significa que la IA gane, ni benchmark, ni ranking, ni mejora QoE.",
        "",
        "### Fase de Verificacion del Cliente y Controllers Clasicos",
        "",
        "Estado: cerrada en Ubuntu con informe externo aceptado.",
        "",
        "Evidencia reportada:",
        "",
        "```text",
        "python scripts/comprobar_cliente.py --strict -> 88 OK / 0 WARN / 0 FAIL",
        "curl -I http://192.168.1.132/dash/.../Paseo_Almunecar_1min_30fps_simple_4s.mpd -> HTTP/1.1 200 OK",
        "python scripts/verificar_cliente_y_controllers_clasicos.py --mpd-url ... -> Status: accepted",
        "```",
        "",
        "Demuestra funcionamiento estructural contra servidor DASH y ausencia de contaminacion en runs clasicos. No demuestra ranking ni mejora de ningun controller.",
        "",
        "### Phase 6 - Validacion comparativa formal",
        "",
        "Estado: pipeline reproducible implementado para ejecucion en Ubuntu cliente. La fase formal solo autoriza comparacion si pasan gates del paquete.",
        "",
        "Objetivo:",
        "",
        "- Congelar protocolo, controllers, MPDs/media profiles, trazas, QoE, seeds, gates y estadistica.",
        "- Ejecutar sesiones trace-driven en Ubuntu cliente con engine `fake` para reproducibilidad.",
        "- Generar paquete de evidencia externo con protocolo, ejecucion, resultados, graficas e informe.",
        "",
        "Presets relevantes:",
        "",
        "- `diagnostico`: 6 segmentos por sesion, verifica maquinaria completa, no ranking.",
        "- `rapido`: amplia cobertura, sigue sin ser benchmark final ni ranking.",
        "- `equilibrado`/`extendido`: solo autorizan ranking si pasan todos los gates y verificacion automatica.",
        "",
    ])


def add_ai_controller_history(lines: list[str]) -> None:
    lines.extend([
        "## Desarrollo IA ABR actual",
        "",
        "### Fase 4-5 v1 como iteracion nueva",
        "",
        "Fase 4-5 v1 queda abierta como iteracion nueva e independiente. No sustituye a Phase 4 ni Phase 5 cerradas y no hereda automaticamente decisiones de `NeuralABR-Lite`.",
        "",
        "Corpus canonico:",
        "",
        "```text",
        "docs/contexto rama nueva/fase_4_5_v1/abr ia md/",
        "```",
        "",
        "Proceso obligatorio:",
        "",
        "```text",
        "decision documentada",
        "-> dataset pilot",
        "-> auditoria dataset pilot",
        "-> entrenamiento pilot 1 seed",
        "-> resumen y analisis de errores",
        "-> pilot multi-seed",
        "-> diagnostico closed-loop offline",
        "-> bundle experimental externo",
        "-> smoke/runtime load",
        "-> Phase 6 diagnostico en Ubuntu cliente",
        "-> Phase 6 rapido si procede",
        "-> iteracion controlada",
        "-> full dataset/full training solo si la evidencia lo justifica",
        "```",
        "",
        "Criterios permanentes de no avance:",
        "",
        "- No avanzar si `best_epoch=0` por fallback.",
        "- No avanzar si pasa copiando referencia sin aprendizaje real.",
        "- No avanzar si rompe gates anti-colapso.",
        "- No avanzar si produce acciones invalidas.",
        "- No avanzar si requiere relajar gates.",
        "- No avanzar si usa artefactos fuera de rutas Linux en WSL.",
        "- No avanzar si necesita comandos manuales largos no versionados.",
        "",
        "### Decision inicial Fase 4-5 v1",
        "",
        "Candidatos definidos el 2026-06-09:",
        "",
        "| Candidato | Tipo | Estado |",
        "|---|---|---|",
        "| `spc_abr_v1` | Predictor neural de throughput/capacidad + planner ABR determinista risk-aware | Prioridad inicial |",
        "| `spbc_abr_v1` | Policy neural con predictor auxiliar, behavior cloning desde `oracle_qoe_beam_v1` | Segundo candidato |",
        "| `spbc_ppo_abr_v1` | Fine-tuning RL de `spbc_abr_v1` | Condicionado a gates |",
        "",
        "Opciones descartadas como primer controller: DQN puro, A3C/Pensieve clonado, meta-RL completo, Mamba/SSM como dependencia inicial, energia, edge, multiusuario, live playback speed, short-video MARL y VMAF.",
        "",
        "### SPBC historico y SPBC v2",
        "",
        "Hecho documentado: el SPBC historico fracaso como controller runtime por desalineacion entre dinamica offline y dinamica del cliente final.",
        "",
        "Sintomas de colapso reportados para SPBC v2 en Phase 6 rapido:",
        "",
        "```text",
        "controller=propio_spbc_v2_anchor",
        "status=FAIL",
        "collapse_detected=True",
        "high_capacity_action0_rate=0.6623376623376623",
        "max_consecutive_action0_after_startup=26",
        "fallback_row_count=5",
        "fallback_reasons={\"inference_timeout\": 5}",
        "qoe_delta_vs_baseline_mean=-1.7679512342365435",
        "mean_measured_throughput_kbps=100153.01954068724",
        "median_selected_bitrate_kbps=300.0",
        "```",
        "",
        "Diagnostico factual asociado: entrenamiento antiguo con `max_buffer_s=20.0` frente a cliente/Phase 6 con `max_buffer_s=60.0`.",
        "",
        "### Phase45 v3 Q_H scorer bloqueado",
        "",
        "Linea: `phase45_v3_qh_scorer`.",
        "",
        "Objetivo: scorer neural que recibe estado ABR visible por controller y candidatos de bitrate, y ordena acciones segun targets `Q_H(s,a)` generados en entorno cerrado.",
        "",
        "Mejor intento documentado:",
        "",
        "```text",
        "run=qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1",
        "status=REVIEW",
        "top1_accuracy=0.788844",
        "mean_regret_q_h=0.395739",
        "gate_mean_regret_q_h<=0.35 FAIL",
        "high_capacity_predicted_action0_rate=0.002946 PASS",
        "```",
        "",
        "Intentos que no avanzaron el gate principal:",
        "",
        "```text",
        "pilot_adv_regret_v1 mean_regret_q_h=0.395739",
        "pilot_adv_regret_gru_v1 mean_regret_q_h=0.442516",
        "hardneg_v1 mean_regret_q_h=0.401737",
        "hardneg_v2 mean_regret_q_h=0.417399",
        "```",
        "",
        "Lectura aceptada: no era solo un problema de loss. El target `Q_H(s,a)` usa futuro como target-only; estados visibles similares pueden tener targets distintos por futuro inmediato no observable. El scorer queda como experimento negativo, diagnostico y posible ablation, no como via principal.",
        "",
        "### Linea viva - Neural Throughput-Calibrated MPC",
        "",
        "Controller candidato:",
        "",
        "```text",
        "phase45_v3_neural_throughput_calibrated_mpc_v1",
        "predictor neuronal de cuantiles de throughput futuro",
        "+ planner MPC explicito sobre qoe_linear_v1",
        "```",
        "",
        "Contrato tecnico:",
        "",
        "- La red no elige bitrate directamente.",
        "- La red predice log-ratios de throughput futuro respecto a una base robusta.",
        "- El planner MPC auditable elige accion.",
        "- `future throughput` se usa solo como target de entrenamiento, nunca como input.",
        "- `eval` queda excluido de entrenamiento.",
        "",
        "Targets:",
        "",
        "```text",
        "base_tp = harmonic_mean(throughput_history_bps)",
        "target_log_ratio_h = log((future_tp_h + eps) / (base_tp + eps))",
        "horizon=5",
        "quantiles=0.10,0.25,0.50,0.75",
        "```",
        "",
        "Loss:",
        "",
        "```text",
        "loss = pinball + crossing_penalty + temporal_smoothness_penalty",
        "```",
        "",
        "Regla de cuantiles por buffer:",
        "",
        "```text",
        "buffer < 4s         -> q10",
        "4s <= buffer < 12s  -> q25",
        "12s <= buffer <20s  -> blend(q25,q50)",
        "buffer >=20s        -> q50",
        "```",
        "",
        "Reward usado por MPC:",
        "",
        "```text",
        "reward = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps",
        "```",
        "",
        "Gates diagnosticos:",
        "",
        "- `high_capacity_action0_rate <= 0.05`.",
        "- `high_capacity_mean_bitrate_ratio_vs_robust_mpc >= 0.70`.",
        "- `fallback_rate == 0`.",
        "- `invalid_action_count == 0`.",
        "- Rebuffer en bucket `2_5_mbps` no debe explotar frente a `robust_mpc`.",
        "- QoE media no debe ser catastroficamente peor que `robust_mpc`.",
        "",
        "Piloto inicial: tras calibracion de planner paso de `bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean=+1.3203728087318694 s` a `+0.08001783155587106 s`, con `status=PASS` en 32 sesiones/8 ventanas.",
        "",
        "Diagnostico ampliado: 3 seeds x 32 ventanas, todas `PASS`, sin fallback, sin acciones invalidas y sin colapso high-capacity a accion 0.",
        "",
        "Bundle v1:",
        "",
        "```text",
        "~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1",
        "schema_id=phase45_v3_neural_mpc_experimental_bundle_v1",
        "runtime_controller_integrated=false al definir bundle",
        "phase6_formal_evaluation_performed=false",
        "```",
        "",
        "Runtime v1: integrado como controller guarded con bundle externo, fallback `robust_mpc`, `weights_only=True` en runtime, telemetria neural diagnostica y hash validation.",
        "",
        "### Neural-MPC v2 full",
        "",
        "Motivo de v2: `20260615_112752_rapido` mostro integracion runtime limpia pero una debilidad localizada en ventana real media-variable con rebuffer alto frente a Robust MPC.",
        "",
        "Perfil v2:",
        "",
        "```text",
        "dataset_dir=~/TFG/datasets_normalizados/phase45_v3/throughput_quantile_full_v1_neural_mpc_v2",
        "model_root=~/TFG/modelos/phase45_v3/throughput_quantile_predictor/full_v1_neural_mpc_v2",
        "run_root=~/TFG/runs_phase45_v3/neural_mpc_full_v1_v2",
        "seeds=452001,452002,452003",
        "train_window_count=4096",
        "validation_window_count=1024",
        "qh_horizon_segments=5",
        "qh_beam_width=24",
        "max_windows_per_trace=4",
        "```",
        "",
        "Lectura de full training v2:",
        "",
        "- Tres seeds con training `PASS` y evaluacion closed-loop offline `PASS`.",
        "- `fallback=0`, acciones invalidas `0`, sin accion 0 en alta capacidad.",
        "- Seed `452001` activa warning `paired_rebuffer_spike_vs_robust_mpc` con peor delta `+5.409446542610964 s`.",
        "- Seeds `452002` y `452003` no activan warnings.",
        "- Seed canonica aprobada para bundle v2: `452003`.",
        "- Controller key v2: `phase45_v3_neural_throughput_calibrated_mpc_v2`.",
        "",
        "Flags siguen siendo diagnosticos:",
        "",
        "```text",
        "benchmark_performed=false",
        "ranking_performed=false",
        "no_final_ranking=true",
        "qoe_claims_authorized=false",
        "```",
        "",
        "Secuencia correcta definida para v2:",
        "",
        "```text",
        "exportar bundle v2 en WSL",
        "-> empaquetar y mover a Ubuntu cliente",
        "-> validar bundle v2",
        "-> smoke runtime controller v2",
        "-> Phase 6 diagnostico con v1 y v2",
        "-> Phase 6 rapido con v1 y v2 si pasa",
        "-> solo despues decidir si equilibrado tiene sentido",
        "```",
        "",
        "### Nueva linea paralela - Closed-loop SPBC/SPC v1",
        "",
        "Decision: abrir `phase45_v3_closedloop_spbc_spc_v1` como linea paralela sin tocar Neural-MPC.",
        "",
        "Filosofia:",
        "",
        "```text",
        "SPBC-v3 = policy neural candidata",
        "SPC-v3  = critic predictivo por accion",
        "hybrid  = SPBC propone + SPC audita/veta/reordena localmente",
        "```",
        "",
        "Primer paso autorizado:",
        "",
        "```text",
        "disenar e implementar generador de dataset pilot closedloop_spbc_spc_v1",
        "```",
        "",
        "Ruta dataset propuesta:",
        "",
        "```text",
        "~/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_pilot_v1",
        "```",
        "",
        "No autorizado todavia: entrenamiento, bundle, controller runtime, Phase 6, ranking ni claim de QoE.",
        "",
    ])


def add_phase6_method(lines: list[str]) -> None:
    lines.extend([
        "## Phase 6 - Protocolo, metricas y paquete de evidencia",
        "",
        "Phase 6 se ejecuta con `scripts/ejecutar_fase6.py`.",
        "",
        "Config base:",
        "",
        "```text",
        "schema_version=phase6_config_v1",
        "manifest_path=/home/daniel/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json",
        "output_root=/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa",
        "repo_root=/home/daniel/TFG/ClienteDashPrudente",
        "engine=fake",
        "seed=606",
        "decision_interval_s=4.0",
        "window_duration_s=300.0",
        "compact_timestamps=true",
        "max_media_segments=30",
        "max_buffer_seconds=60.0",
        "initial_quality=0",
        "initial_controller_decision=false",
        "```",
        "",
        "Seleccion de trazas:",
        "",
        "- Solo `split=eval`.",
        "- `usable_for_eval` no debe ser `false`.",
        "- Duracion >= ventana requerida.",
        "- Sinteticas identificadas por `dataset_id=synthetic_controlled_network` o `semantics=synthetic_available_bandwidth`.",
        "- Trazas reales formales deben superar suelo de throughput medio y maximo configurado.",
        "- Seleccion balanceada por `dataset_id`, `semantics`, `network_condition` y `difficulty_bucket`.",
        "",
        "Buckets de dificultad:",
        "",
        "```text",
        "mean < 1500 kbps -> baja_capacidad",
        "1500 <= mean < 5000 -> media_capacidad o media_capacidad_variable",
        "5000 <= mean < 20000 -> alta_capacidad o alta_capacidad_variable",
        "mean >= 20000 -> muy_alta_capacidad",
        "variabilidad = (max-min)/mean; variable si >= 1.5",
        "```",
        "",
        "Package structure:",
        "",
        "```text",
        "<package_root>/",
        "  00_protocolo/",
        "    protocolo_validacion.json",
        "    session_plan.json",
        "    session_plan.csv",
        "    trace_windows.csv",
        "    controllers.csv",
        "    media_profiles.csv",
        "    client_configs/",
        "  01_ejecucion/",
        "    runs/",
        "    command_logs/",
        "  02_resultados/",
        "    raw_chunks.csv",
        "    session_summary.csv",
        "    aggregates_by_controller.json",
        "    statistics.json",
        "    resultados_para_validar.json",
        "    resultados_para_validar.md",
        "  03_graficas/",
        "    plot_manifest.json",
        "  04_informe/",
        "    informe_comparativo.md",
        "    conclusiones_tecnicas.md",
        "    manifest_paquete_evidencia.json",
        "```",
        "",
        "Metricas agregadas por controller:",
        "",
        "- `qoe_linear_mean` y `qoe_linear_sum`.",
        "- `avg_quality_mbps`.",
        "- `total_rebuffer_s_mean`.",
        "- `rebuffer_ratio_mean`.",
        "- `smoothness_penalty_mean`.",
        "- `decision_latency_ms_mean`.",
        "- Percentiles y conteos segun analisis.",
        "- Auditoria neural en controllers propios: inference rows, fallback rows, diagnostic rows, hash ok, feature ok y latency.",
        "",
        "Estadistica:",
        "",
        "- Deltas emparejados por controller.",
        "- Intervalos `ci95_low/high`.",
        "- `sign_test_p_value`.",
        "- Ranking solo si `benchmark_authorized` y `ranking_authorized` pasan gates.",
        "",
        "Gates de paquete:",
        "",
        "- Artefactos requeridos presentes.",
        "- Sessions completadas y evaluables.",
        "- Sin artefactos legacy.",
        "- Controllers propios con auditoria neural correcta cuando son evaluables.",
        "- Preset con capacidad de benchmark/ranking solo en condiciones permitidas.",
        "",
        "Config local para comparar Neural-MPC v1/v2:",
        "",
        "```text",
        "config/phase6.neural_mpc_v1_v2.local.example.json",
        "controllers=[rate_based, bola, robust_mpc, phase45_v3_neural_throughput_calibrated_mpc_v1, phase45_v3_neural_throughput_calibrated_mpc_v2]",
        "output_root=/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa_neural_mpc_v1_v2",
        "preset=diagnostico por defecto en el ejemplo",
        "```",
        "",
    ])


def add_scientific_corpus(lines: list[str], markdown_by_bucket: Mapping[str, Sequence[MarkdownInfo]]) -> None:
    phase45_corpus = markdown_by_bucket.get("phase45_corpus", [])
    converted_studies = markdown_by_bucket.get("converted_studies", [])
    source_cards = markdown_by_bucket.get("source_cards", [])
    lines.extend([
        "## Corpus cientifico y documental",
        "",
        "Regla metodologica permanente: no implementar directamente desde PDFs brutos si existen source cards, specs, decisiones canonicas o documentos operativos.",
        "",
        "Flujo PDF/fuente -> Codex:",
        "",
        "```text",
        "PDF/fuente",
        "-> paper_card.md o source_card.md",
        "-> decision_matrix.md",
        "-> implementation_spec.md",
        "-> controller_api_mapping.md",
        "-> acceptance_tests.md",
        "-> prompt autosuficiente para Codex",
        "-> implementacion",
        "-> tests",
        "-> validacion",
        "-> cierre documental",
        "```",
        "",
        "### Corpus operativo Fase 4-5 v1 - ABR IA",
        "",
        f"Documentos detectados en `docs/contexto rama nueva/fase_4_5_v1/abr ia md/`: {len(phase45_corpus)}.",
        "",
        "| # | Documento | Primer heading |",
        "|---:|---|---|",
    ])
    for index, info in enumerate(sorted(phase45_corpus, key=lambda item: item.rel), start=1):
        lines.append(f"| {index} | `{escape_table(info.rel)}` | {escape_table(info.first_heading)} |")
    lines.extend([
        "",
        "Sintesis de decisiones extraidas de `decision_tecnica_modelos_v1.md`:",
        "",
        "- Comyco y SABR aportan imitation learning, experto offline, DAgger/rollouts y BC antes de PPO.",
        "- Puffer/Fugu, BPA y MamBRA apoyan predictor de throughput + decision ABR segura.",
        "- A2BR, ANT, BETA, Oboe, Gelato/Plume, MERINA, MetaABR y EAStream apoyan balance por regimen, evaluacion por buckets y posible especializacion posterior.",
        "- SODA, Oboe, Puffer/Fugu y CausalSim actuan como guardrails de deployability, consistencia y sesgo de simulacion.",
        "- Energia, edge, multiusuario, live playback speed, short video MARL y VMAF quedan fuera del contrato Phase 6 actual.",
        "",
        "### Estudios PDF convertidos a Markdown",
        "",
        f"Documentos detectados en `docs/todos los estudios pdf convertidos a md/`: {len(converted_studies)}.",
        "",
        "| Documento | Primer heading |",
        "|---|---|",
    ])
    for info in sorted(converted_studies, key=lambda item: item.rel):
        lines.append(f"| `{escape_table(info.rel)}` | {escape_table(info.first_heading)} |")
    lines.extend([
        "",
        "### Source cards y paper cards versionadas",
        "",
        f"Tarjetas detectadas por nombre (`source_cards`, `paper_cards`, `paper_card`, `source_evidence`): {len(source_cards)}.",
        "",
        "| Documento | Primer heading |",
        "|---|---|",
    ])
    for info in sorted(source_cards, key=lambda item: item.rel)[:220]:
        lines.append(f"| `{escape_table(info.rel)}` | {escape_table(info.first_heading)} |")
    if len(source_cards) > 220:
        lines.append(f"| `(resto en catalogo exhaustivo)` | {len(source_cards) - 220} tarjetas adicionales |")
    lines.extend([
        "",
    ])


def add_code_architecture(
    lines: list[str],
    py_infos: Sequence[PythonInfo],
    controller_registry: Sequence[Mapping[str, str]],
) -> None:
    by_dir = defaultdict(list)
    for info in py_infos:
        parts = Path(info.rel).parts
        key = "/".join(parts[:2]) if len(parts) > 1 else parts[0]
        by_dir[key].append(info)
    lines.extend([
        "## Arquitectura de codigo",
        "",
        "Separacion tecnica obligatoria mantenida por el proyecto:",
        "",
        "- parser MPD;",
        "- descarga de segmentos;",
        "- buffer;",
        "- motor de reproduccion;",
        "- control ABR;",
        "- logging;",
        "- evaluacion;",
        "- trace replay;",
        "- normalizacion de datasets;",
        "- documentacion cientifica;",
        "- workspaces externos.",
        "",
        "Mapa funcional:",
        "",
        "| Area | Archivos | Papel |",
        "|---|---:|---|",
        f"| `core/parser` | {len(by_dir.get('core/parser', []))} | Parser MPD y contratos de representaciones |",
        f"| `core/downloader.py` | {1 if any(i.rel == 'core/downloader.py' for i in py_infos) else 0} | Descarga HTTP/fragmentos |",
        f"| `core/media_engine` | {len(by_dir.get('core/media_engine', []))} | Engine fake/GStreamer |",
        f"| `core/controller` | {len(by_dir.get('core/controller', []))} | Controllers clasicos, IA, registry y safety |",
        f"| `core/trace_replay` | {sum(len(v) for k, v in by_dir.items() if k.startswith('core/trace_replay'))} | Schema, manifest, converters, network model |",
        f"| `core/evaluation` | {len(by_dir.get('core/evaluation', []))} | QoE y artefactos de evaluacion |",
        f"| `core/neural_abr` | {len(by_dir.get('core/neural_abr', []))} | NeuralABR-Lite training/inference/bundles |",
        f"| `core/phase45_v1` | {len(by_dir.get('core/phase45_v1', []))} | SPBC/SPC v1/v2 dataset/training/offline validation |",
        f"| `core/phase45_v3` | {len(by_dir.get('core/phase45_v3', []))} | Entorno cerrado, QH scorer, Neural-MPC, bundle, validation |",
        f"| `core/phase6` | {len(by_dir.get('core/phase6', []))} | Config, catalog, seleccion, analisis, verificacion Phase 6 |",
        "",
        "Entrypoints principales:",
        "",
        "| Archivo | Papel |",
        "|---|---|",
        "| `main.py` | Runner principal cliente DASH con config |",
        "| `player.py` | Loop de reproduccion/runtime; tocar solo con contrato y tests |",
        "| `analysis_metrics.py` | Utilidades historicas/metricas de analisis |",
        "| `progress_bar.py` | Presentacion/progreso, no autoridad experimental |",
        "",
        "Controllers actuales:",
        "",
        "| Key | Factory | Papel |",
        "|---|---|---|",
    ])
    for row in controller_registry:
        role = controller_role(row["key"])
        lines.append(f"| `{row['key']}` | `{row['factory']}` | {role} |")
    lines.extend([
        "",
        "Inventario AST resumido de modulos Python por area:",
        "",
    ])
    for area in sorted(by_dir):
        if not area.startswith("core"):
            continue
        lines.append(f"### `{area}`")
        lines.append("")
        lines.append("| Archivo | Clases | Funciones | Constantes top-level |")
        lines.append("|---|---|---|---|")
        for info in sorted(by_dir[area], key=lambda item: item.rel):
            lines.append(
                f"| `{escape_table(info.rel)}` | {short_join(info.classes, 8)} | {short_join(info.functions, 10)} | {short_join(info.constants, 8)} |"
            )
        lines.append("")


def add_command_protocols(lines: list[str]) -> None:
    lines.extend([
        "## Comandos y runbooks operativos",
        "",
        "Validacion minima Windows segun aplique:",
        "",
        "```powershell",
        "git status --short --branch",
        "git diff --check",
        "python -m unittest discover",
        "python scripts/comprobar_cliente.py --strict",
        "```",
        "",
        "Sincronizacion Ubuntu cliente:",
        "",
        "```bash",
        "cd ~/TFG/ClienteDashPrudente",
        "git pull",
        "```",
        "",
        "Sincronizacion WSL2/ROCm:",
        "",
        "```bash",
        "wsl -d Ubuntu-24.04",
        "cd ~/TFG/ClienteDashPrudente",
        "git pull",
        "source ~/venvs/rocm721/bin/activate",
        "python3 -c \"import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))\"",
        "```",
        "",
        "Phase 6 comparativa:",
        "",
        "```bash",
        "cd ~/TFG/ClienteDashPrudente",
        "git pull",
        "python scripts/ejecutar_fase6.py --preset diagnostico",
        "python scripts/verificar_paquete_fase6.py --package-root <paquete>",
        "```",
        "",
        "Phase45 Neural-MPC v1/v2 config local recomendada:",
        "",
        "```bash",
        "cp config/phase6.neural_mpc_v1_v2.local.example.json config/phase6.local.yaml",
        "python scripts/ejecutar_fase6.py --config config/phase6.local.yaml --preset diagnostico",
        "```",
        "",
        "Runbooks WSL/Ubuntu relevantes detectados por nombre:",
        "",
        "```text",
        "scripts/run_phase45_v3_neural_mpc_pilot_wsl.sh",
        "scripts/run_phase45_v3_neural_mpc_expanded_diagnostic_wsl.sh",
        "scripts/generate_phase45_v3_neural_mpc_full_dataset_v2_wsl.sh",
        "scripts/run_phase45_v3_neural_mpc_full_training_v2_wsl.sh",
        "scripts/export_phase45_v3_neural_mpc_experimental_bundle_wsl.sh",
        "scripts/export_phase45_v3_neural_mpc_experimental_bundle_v2_wsl.sh",
        "scripts/package_phase45_v3_neural_mpc_experimental_bundle_transfer_wsl.sh",
        "scripts/package_phase45_v3_neural_mpc_experimental_bundle_v2_transfer_wsl.sh",
        "scripts/validate_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh",
        "scripts/smoke_phase45_v3_neural_mpc_runtime_controller_ubuntu_cliente.sh",
        "scripts/smoke_phase45_v3_neural_mpc_runtime_controller_v2_ubuntu_cliente.sh",
        "```",
        "",
    ])


def add_phase6_packages(lines: list[str], packages: Sequence[Mapping[str, Any]]) -> None:
    lines.extend([
        "## Paquetes Phase 6 externos detectados",
        "",
        "Estos paquetes estan fuera del repo bajo la raiz TFG. Se documentan como evidencia de ejecuciones existentes, no como benchmark automaticamente autorizado.",
        "",
        "| Paquete | Preset | Sesiones | Controllers | Benchmark autorizado | Ranking autorizado | Resultado MD |",
        "|---|---|---:|---:|---|---|---|",
    ])
    for package in packages:
        lines.append(
            f"| `{escape_table(package['rel'])}` | `{package.get('preset', '')}` | {package.get('session_count', '')} | {package.get('controller_count', '')} | `{package.get('benchmark_authorized', '')}` | `{package.get('ranking_authorized', '')}` | `{escape_table(package.get('result_md', ''))}` |"
        )
    lines.extend([
        "",
    ])


def add_catalogs(
    lines: list[str],
    md_infos: Sequence[MarkdownInfo],
    py_infos: Sequence[PythonInfo],
    scripts: Sequence[Path],
    tests: Sequence[Path],
    external_dirs: Sequence[Mapping[str, Any]],
) -> None:
    lines.extend([
        "## Catalogos exhaustivos",
        "",
        "### Catalogo Markdown versionado",
        "",
        "| # | Ruta | Bytes | Primer heading | Status/flags detectados |",
        "|---:|---|---:|---|---|",
    ])
    for index, info in enumerate(sorted(md_infos, key=lambda item: item.rel), start=1):
        status = "; ".join(info.status_lines[:3])
        lines.append(
            f"| {index} | `{escape_table(info.rel)}` | {info.size} | {escape_table(info.first_heading)} | {escape_table(status)} |"
        )
    lines.extend([
        "",
        "### Catalogo Python versionado",
        "",
        "| # | Ruta | Bytes | Clases | Funciones | Parse error |",
        "|---:|---|---:|---|---|---|",
    ])
    for index, info in enumerate(sorted(py_infos, key=lambda item: item.rel), start=1):
        lines.append(
            f"| {index} | `{escape_table(info.rel)}` | {info.size} | {short_join(info.classes, 10)} | {short_join(info.functions, 12)} | {escape_table(info.parse_error)} |"
        )
    lines.extend([
        "",
        "### Catalogo scripts",
        "",
        "| # | Ruta | Tipo | Bytes |",
        "|---:|---|---|---:|",
    ])
    for index, path in enumerate(sorted(scripts, key=rel_sort_key), start=1):
        lines.append(f"| {index} | `{escape_table(rel(path))}` | `{path.suffix or '(sin extension)'}` | {path.stat().st_size} |")
    lines.extend([
        "",
        "### Catalogo tests",
        "",
        "| # | Ruta | Bytes |",
        "|---:|---|---:|",
    ])
    for index, path in enumerate(sorted(tests, key=rel_sort_key), start=1):
        lines.append(f"| {index} | `{escape_table(rel(path))}` | {path.stat().st_size} |")
    lines.extend([
        "",
        "### Catalogo de directorios externos bajo raiz TFG",
        "",
        "| # | Profundidad | Ruta relativa | Directorios hijos | Archivos hijos |",
        "|---:|---:|---|---:|---:|",
    ])
    for index, row in enumerate(external_dirs, start=1):
        lines.append(
            f"| {index} | {row['depth']} | `{escape_table(row['rel'])}` | {row['child_dirs']} | {row['child_files']} |"
        )
    lines.extend([
        "",
    ])


def add_closing_handoff(lines: list[str]) -> None:
    lines.extend([
        "## Punto exacto de continuacion",
        "",
        "Estado operativo al generar este documento:",
        "",
        "- Rama: `rebuild/phase3-from-phase2`.",
        "- Fase activa global: Phase 6 implementation ready - validacion comparativa formal.",
        "- Fase IA nueva activa: Fase 4-5 v1/v3, con Neural-MPC v1/v2 y linea paralela closed-loop SPBC/SPC v1.",
        "- No hay autorizacion general para benchmark/ranking/ganador fuera de Phase 6 con gates superados.",
        "- Cualquier modelo IA nuevo debe seguir el embudo documentado en `proceso_desarrollo_ia_abr.md`.",
        "- `phase45_v3_neural_throughput_calibrated_mpc_v1` no debe tocarse por abrir lineas paralelas.",
        "- `phase45_v3_closedloop_spbc_spc_v1` acaba de autorizar dataset pilot/generador, no entrenamiento ni runtime.",
        "",
        "Checklist que debe aplicar una IA externa antes de actuar:",
        "",
        "1. Leer `AGENTS.md`.",
        "2. Leer los tres documentos obligatorios.",
        "3. Verificar `git status --short --branch`.",
        "4. Identificar si la tarea afecta a runtime/player/controller/evaluacion.",
        "5. No tocar `player.py`, runtime, media engine, controllers ni evaluacion sin contrato explicito y tests.",
        "6. No usar PDFs brutos si existe `.md` operativo.",
        "7. No llamar benchmark a smoke, dry-run, entrenamiento offline ni diagnostico.",
        "8. Mantener datasets/modelos/runs fuera de Git.",
        "9. Dar a Daniel comandos cortos versionados.",
        "10. Si una linea se bloquea mas de dos ejecuciones sin avance de paso, generar informe objetivo autosuficiente de bloqueo.",
        "",
        "Formula final que rige comparacion formal:",
        "",
        "```text",
        "reward_n = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps",
        "primary_session_metric = qoe_linear_mean",
        "```",
        "",
        "Frase metodologica valida:",
        "",
        "> El proyecto busca un controller IA ABR propio defendible, integrado como controller normal del cliente, evaluado solo mediante protocolo Phase 6 reproducible con trazas, media profile, QoE y gates congelados.",
        "",
    ])


def list_repo_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [Path(line.strip()) for line in result.stdout.splitlines() if line.strip()]


def collect_markdown_infos() -> list[MarkdownInfo]:
    infos: list[MarkdownInfo] = []
    for path in sorted((REPO_ROOT / "docs").rglob("*.md"), key=rel_sort_key):
        if path.resolve() == DOC_OUTPUT.resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
        headings = tuple(line.strip().lstrip("#").strip() for line in text.splitlines() if line.lstrip().startswith("#"))
        first_heading = headings[0] if headings else path.stem
        status_lines = extract_status_lines(text)
        infos.append(
            MarkdownInfo(
                path=path,
                rel=rel(path),
                size=path.stat().st_size,
                first_heading=first_heading[:180],
                headings=headings[:40],
                status_lines=status_lines,
            )
        )
    return infos


def extract_status_lines(text: str) -> tuple[str, ...]:
    patterns = (
        r"^\s*Status\s*:\s*(.+)$",
        r"^\s*Estado\s*:\s*(.+)$",
        r"^\s*status\s*=\s*(.+)$",
        r"^\s*benchmark_performed\s*=\s*(.+)$",
        r"^\s*ranking_performed\s*=\s*(.+)$",
        r"^\s*qoe_claims_authorized\s*=\s*(.+)$",
    )
    found: list[str] = []
    for line in text.splitlines():
        for pattern in patterns:
            match = re.match(pattern, line, flags=re.IGNORECASE)
            if match:
                found.append(line.strip()[:160])
                break
        if len(found) >= 8:
            break
    return tuple(found)


def collect_python_infos() -> list[PythonInfo]:
    paths = []
    for base in (REPO_ROOT / "core", REPO_ROOT / "scripts", REPO_ROOT / "tests"):
        if base.exists():
            paths.extend(path for path in base.rglob("*.py") if not any(part in EXCLUDED_DIR_NAMES for part in path.parts))
    for path in (REPO_ROOT / "main.py", REPO_ROOT / "player.py", REPO_ROOT / "analysis_metrics.py", REPO_ROOT / "progress_bar.py"):
        if path.exists():
            paths.append(path)
    infos: list[PythonInfo] = []
    for path in sorted(set(paths), key=rel_sort_key):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(text)
            module_doc = ast.get_docstring(tree) or ""
            classes = []
            functions = []
            constants = []
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    classes.append(node.name)
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    functions.append(node.name)
                elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target in targets:
                        if isinstance(target, ast.Name) and target.id.isupper():
                            constants.append(target.id)
            infos.append(
                PythonInfo(
                    path=path,
                    rel=rel(path),
                    size=path.stat().st_size,
                    module_doc=one_line(module_doc),
                    classes=tuple(classes),
                    functions=tuple(functions),
                    constants=tuple(constants),
                )
            )
        except Exception as exc:
            infos.append(
                PythonInfo(
                    path=path,
                    rel=rel(path),
                    size=path.stat().st_size if path.exists() else 0,
                    module_doc="",
                    classes=(),
                    functions=(),
                    constants=(),
                    parse_error=str(exc)[:180],
                )
            )
    return infos


def collect_external_top_level() -> list[Mapping[str, Any]]:
    rows = []
    for path in sorted((p for p in TFG_ROOT.iterdir() if p.is_dir()), key=lambda p: p.name.lower()):
        dirs = 0
        files = 0
        for root, dirnames, filenames in os.walk(path):
            dirnames[:] = [name for name in dirnames if name not in EXCLUDED_DIR_NAMES]
            dirs += len(dirnames)
            files += len(filenames)
        rows.append({
            "name": path.name,
            "directories": dirs,
            "files": files,
            "mtime": format_mtime(path),
        })
    return rows


def collect_external_directories() -> list[Mapping[str, Any]]:
    rows = []
    for root, dirnames, filenames in os.walk(TFG_ROOT):
        dirnames[:] = [name for name in dirnames if name not in EXCLUDED_DIR_NAMES]
        path = Path(root)
        if any(part in EXCLUDED_DIR_NAMES for part in path.parts):
            continue
        try:
            relative = path.relative_to(TFG_ROOT)
        except ValueError:
            relative = path
        rel_text = "." if str(relative) == "." else str(relative)
        depth = 0 if rel_text == "." else len(relative.parts)
        rows.append({
            "rel": rel_text,
            "depth": depth,
            "child_dirs": len(dirnames),
            "child_files": len(filenames),
        })
    return sorted(rows, key=lambda row: (int(row["depth"]), str(row["rel"]).lower()))


def collect_external_key_files() -> list[Mapping[str, Any]]:
    patterns = (
        ".md",
        ".json",
        ".yaml",
        ".yml",
        ".csv",
    )
    key_tokens = (
        "manifest",
        "informe",
        "resultados",
        "resumen",
        "auditoria",
        "protocolo",
        "bundle",
        "readiness",
        "report",
        "summary",
    )
    rows = []
    for root, dirnames, filenames in os.walk(TFG_ROOT):
        dirnames[:] = [name for name in dirnames if name not in EXCLUDED_DIR_NAMES]
        root_path = Path(root)
        for name in filenames:
            path = root_path / name
            lower = name.lower()
            if not lower.endswith(patterns) and not any(token in lower for token in key_tokens):
                continue
            if path.is_file():
                rows.append({
                    "rel": str(path.relative_to(TFG_ROOT)),
                    "size": path.stat().st_size,
                    "mtime": format_mtime(path),
                })
    return sorted(rows, key=lambda row: str(row["rel"]).lower())


def collect_phase6_packages() -> list[Mapping[str, Any]]:
    rows = []
    candidates = []
    for child in TFG_ROOT.iterdir():
        if child.is_dir() and re.match(r"^20\d{6}_\d{6}_(diagnostico|rapido|equilibrado|extendido)", child.name):
            candidates.append(child)
    phase6_root = TFG_ROOT / "runs_trazas" / "phase6"
    if phase6_root.exists():
        candidates.extend(path for path in phase6_root.rglob("*") if path.is_dir() and (path / "00_protocolo").exists())
    for package in sorted(set(candidates), key=lambda p: str(p).lower()):
        protocol = read_json(package / "00_protocolo" / "protocolo_validacion.json")
        result = read_json(package / "02_resultados" / "resultados_para_validar.json")
        artifacts = result.get("artifacts", {}) if isinstance(result, Mapping) else {}
        result_md = str(artifacts.get("resultados_para_validar_md", ""))
        rows.append({
            "rel": str(package.relative_to(TFG_ROOT)),
            "preset": protocol.get("preset", ""),
            "session_count": protocol.get("session_count", ""),
            "controller_count": len(protocol.get("controllers", [])) if isinstance(protocol.get("controllers"), list) else "",
            "benchmark_authorized": (result.get("gates", {}) or {}).get("benchmark_authorized", protocol.get("benchmark_authorized", "")) if isinstance(result, Mapping) else protocol.get("benchmark_authorized", ""),
            "ranking_authorized": (result.get("gates", {}) or {}).get("ranking_authorized", protocol.get("ranking_authorized", "")) if isinstance(result, Mapping) else protocol.get("ranking_authorized", ""),
            "result_md": result_md,
        })
    return rows


def parse_controller_registry() -> list[Mapping[str, str]]:
    path = REPO_ROOT / "core" / "controller" / "registry.py"
    text = path.read_text(encoding="utf-8", errors="replace")
    rows = []
    pattern = re.compile(
        r'"(?P<dictkey>[^"]+)"\s*:\s*ControllerSpec\(\s*key="(?P<key>[^"]+)",\s*label="(?P<label>[^"]+)",\s*factory=(?P<factory>[A-Za-z_][A-Za-z0-9_]*)',
        re.MULTILINE,
    )
    for match in pattern.finditer(text):
        rows.append({
            "key": match.group("key"),
            "label": match.group("label"),
            "factory": match.group("factory"),
        })
    return rows


def bucket_markdown(md_infos: Sequence[MarkdownInfo]) -> Mapping[str, list[MarkdownInfo]]:
    buckets: dict[str, list[MarkdownInfo]] = defaultdict(list)
    for info in md_infos:
        path = info.rel.replace("\\", "/")
        if "fase_4_5_v1/abr ia md/" in path:
            buckets["phase45_corpus"].append(info)
        if "todos los estudios pdf convertidos a md/" in path:
            buckets["converted_studies"].append(info)
        lowered = path.lower()
        if "source_cards" in lowered or "paper_cards" in lowered or "paper_card" in lowered or "source_evidence" in lowered:
            buckets["source_cards"].append(info)
    return buckets


def read_json(path: Path) -> Mapping[str, Any]:
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
        return data if isinstance(data, Mapping) else {}
    except Exception:
        return {}


def run_git(args: Sequence[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.stdout


def render_pdf(markdown: str, output_path: Path) -> None:
    try:
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import cm
        from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer
    except ModuleNotFoundError as exc:
        raise SystemExit("reportlab is required to render the PDF") from exc

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="DocTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        spaceAfter=14,
    ))
    styles.add(ParagraphStyle(
        name="H1Custom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        spaceBefore=12,
        spaceAfter=8,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="H2Custom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="BodyCustom",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.7,
        leading=11.2,
        alignment=TA_LEFT,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name="MonoCustom",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=6.7,
        leading=8.2,
        leftIndent=0.2 * cm,
        rightIndent=0.2 * cm,
        spaceBefore=3,
        spaceAfter=4,
        wordWrap="CJK",
    ))
    styles.add(ParagraphStyle(
        name="SmallCustom",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.6,
        leading=9.2,
        spaceAfter=2,
    ))

    story: list[Any] = []
    in_code = False
    code_buffer: list[str] = []

    def flush_code() -> None:
        nonlocal code_buffer
        if not code_buffer:
            return
        wrapped = []
        for raw in code_buffer:
            text = normalize_for_pdf(raw)
            if len(text) <= 118:
                wrapped.append(text)
            else:
                wrapped.extend(textwrap.wrap(text, width=118, replace_whitespace=False, drop_whitespace=False) or [""])
        story.append(Paragraph("<br/>".join(html.escape(line) for line in wrapped), styles["MonoCustom"]))
        code_buffer = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
                code_buffer = []
            continue
        if in_code:
            code_buffer.append(line)
            continue
        if not line.strip():
            story.append(Spacer(1, 3))
            continue
        if line.startswith("# "):
            story.append(Paragraph(escape_pdf(line[2:]), styles["DocTitle"]))
            continue
        if line.startswith("## "):
            story.append(Paragraph(escape_pdf(line[3:]), styles["H1Custom"]))
            continue
        if line.startswith("### "):
            story.append(Paragraph(escape_pdf(line[4:]), styles["H2Custom"]))
            continue
        if line.startswith("|"):
            story.append(Paragraph(escape_pdf(line), styles["MonoCustom"]))
            continue
        if line.startswith("- ") or re.match(r"^\d+\. ", line):
            story.append(Paragraph(escape_pdf(line), styles["BodyCustom"]))
            continue
        if line == "\\pagebreak":
            story.append(PageBreak())
            continue
        story.append(Paragraph(escape_pdf(line), styles["BodyCustom"]))
    if in_code:
        flush_code()

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=1.35 * cm,
        leftMargin=1.35 * cm,
        topMargin=1.25 * cm,
        bottomMargin=1.25 * cm,
        title="Contexto absoluto tecnico - ClienteDashPrudente",
        author="Codex",
    )
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)


def page_footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.drawString(1.35 * 28.3465, 0.65 * 28.3465, "ClienteDashPrudente - contexto tecnico")
    canvas.drawRightString(19.65 * 28.3465, 0.65 * 28.3465, f"Pagina {doc.page}")
    canvas.restoreState()


def escape_pdf(text: str) -> str:
    text = normalize_for_pdf(text)
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    return text


def normalize_for_pdf(text: str) -> str:
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2011": "-",
        "\u2192": "->",
        "\u2248": "~",
        "\u2264": "<=",
        "\u2265": ">=",
        "\u00a0": " ",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def escape_table(text: Any) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")[:320]


def short_join(values: Sequence[str], limit: int) -> str:
    if not values:
        return ""
    shown = list(values[:limit])
    suffix = f" (+{len(values) - limit})" if len(values) > limit else ""
    return "`" + "`, `".join(escape_table(item) for item in shown) + "`" + suffix


def controller_role(key: str) -> str:
    if key in {"min_rate", "fixed_rate", "max_rate", "fixed_quality", "scripted_quality", "max_quality"}:
        return "control tecnico/debug"
    if key in {"rate_based", "bba", "bola", "mpc", "robust_mpc"}:
        return "baseline ABR clasico"
    if key.startswith("neural_abr_lite"):
        return "IA historica Phase 4/5"
    if key.startswith("spbc"):
        return "IA experimental SPBC"
    if key.startswith("phase45_v3_neural"):
        return "IA Neural-MPC Phase45 v3"
    return "controller registrado"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def rel_sort_key(path: Path) -> str:
    return rel(path).lower()


def one_line(text: str) -> str:
    return " ".join(text.split())[:240]


def format_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds")


if __name__ == "__main__":
    raise SystemExit(main())
