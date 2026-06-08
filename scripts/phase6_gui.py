#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase6.catalog import discover_comparable_controllers
from core.phase6.config import DEFAULT_PHASE6_LOCAL_CONFIG, load_phase6_config


RUNNER_SCRIPT = REPO_ROOT / "scripts" / "run_phase6_validacion_comparativa.py"
ANALYSIS_SCRIPT = REPO_ROOT / "scripts" / "analyze_phase6_results.py"
CLASSIC_SCRIPT = REPO_ROOT / "scripts" / "run_phase6_verificacion_clasica_controlada.py"


def build_phase6_command(
    *,
    config_path: Optional[str] = None,
    preset: str = "rapido",
    output_root: Optional[str] = None,
    package_root: Optional[str] = None,
    dry_run: bool = False,
    only_plan: bool = False,
    skip_analysis: bool = False,
    resume: bool = True,
    max_sessions: Optional[int] = None,
) -> List[str]:
    command = [sys.executable, str(RUNNER_SCRIPT), "--preset", str(preset)]
    if config_path:
        command.extend(["--config", str(config_path)])
    if output_root:
        command.extend(["--output-root", str(output_root)])
    if package_root:
        command.extend(["--package-root", str(package_root)])
    command.append("--resume" if resume else "--no-resume")
    if dry_run:
        command.append("--dry-run")
    if only_plan:
        command.append("--only-plan")
    if skip_analysis:
        command.append("--skip-analysis")
    if max_sessions is not None:
        command.extend(["--max-sessions", str(int(max_sessions))])
    return command


def build_analysis_command(package_root: str, *, no_plots: bool = False) -> List[str]:
    command = [sys.executable, str(ANALYSIS_SCRIPT), str(package_root)]
    if no_plots:
        command.append("--no-plots")
    return command


def build_classic_controlled_command(
    *,
    config_path: Optional[str] = None,
    preset: str = "rapido",
    output_root: Optional[str] = None,
    max_windows: int = 2,
) -> List[str]:
    command = [sys.executable, str(CLASSIC_SCRIPT), "--preset", str(preset), "--max-windows", str(int(max_windows))]
    if config_path:
        command.extend(["--config", str(config_path)])
    if output_root:
        command.extend(["--output-root", str(output_root)])
    return command


def write_gui_override_config(
    *,
    base_config_path: Optional[str],
    preset: str,
    engine: str,
    output_root: str,
    controllers: Sequence[str],
) -> Path:
    config = load_phase6_config(base_config_path)
    config.setdefault("experiment", {})["preset"] = preset
    config.setdefault("experiment", {})["engine"] = engine
    config.setdefault("experiment", {})["controllers"] = list(controllers)
    if output_root:
        config.setdefault("paths", {})["output_root"] = output_root
    generated_dir = Path(str(config["paths"]["output_root"])) / "_gui_configs"
    generated_dir.mkdir(parents=True, exist_ok=True)
    target = generated_dir / "phase6_gui_{0}.yaml".format(time.strftime("%Y%m%d_%H%M%S"))
    target.write_text(json.dumps(config, indent=2, sort_keys=True), encoding="utf-8")
    return target


class Phase6Gui:
    def __init__(self) -> None:
        import tkinter as tk
        from tkinter import filedialog, messagebox, ttk

        self.tk = tk
        self.ttk = ttk
        self.filedialog = filedialog
        self.messagebox = messagebox
        self.root = tk.Tk()
        self.root.title("Phase 6 - Validacion comparativa")
        self.root.geometry("980x700")
        self.process: Optional[subprocess.Popen[str]] = None

        self.config_path = tk.StringVar(value=str(DEFAULT_PHASE6_LOCAL_CONFIG) if DEFAULT_PHASE6_LOCAL_CONFIG.exists() else "")
        config = self._safe_load_config()
        self.output_root = tk.StringVar(value=str(_mapping(config.get("paths")).get("output_root", "")))
        self.preset = tk.StringVar(value=str(_mapping(config.get("experiment")).get("preset", "rapido")))
        self.engine = tk.StringVar(value=str(_mapping(config.get("experiment")).get("engine", "fake")))
        self.resume = tk.BooleanVar(value=True)
        self.dry_run = tk.BooleanVar(value=False)
        self.only_plan = tk.BooleanVar(value=False)
        self.skip_analysis = tk.BooleanVar(value=False)
        self.max_sessions = tk.StringVar(value="")
        self.package_to_analyze = tk.StringVar(value="")
        self.progress_percent = tk.DoubleVar(value=0.0)
        self.progress_text = tk.StringVar(value="Progreso: esperando ejecucion")
        self.controller_vars: Dict[str, Any] = {}

        self._build_layout()
        self._load_controllers()
        self._refresh_command_preview()

    def run(self) -> None:
        self.root.mainloop()

    def _build_layout(self) -> None:
        ttk = self.ttk
        tk = self.tk
        main = ttk.Frame(self.root, padding=12)
        main.pack(fill="both", expand=True)

        top = ttk.Frame(main)
        top.pack(fill="x")
        ttk.Label(top, text="Config").grid(row=0, column=0, sticky="w")
        ttk.Entry(top, textvariable=self.config_path).grid(row=0, column=1, sticky="ew", padx=6)
        ttk.Button(top, text="Buscar", command=self._browse_config).grid(row=0, column=2)
        ttk.Label(top, text="Salida").grid(row=1, column=0, sticky="w", pady=(8, 0))
        ttk.Entry(top, textvariable=self.output_root).grid(row=1, column=1, sticky="ew", padx=6, pady=(8, 0))
        ttk.Button(top, text="Carpeta", command=self._browse_output).grid(row=1, column=2, pady=(8, 0))
        top.columnconfigure(1, weight=1)

        options = ttk.Frame(main)
        options.pack(fill="x", pady=10)
        ttk.Label(options, text="Preset").grid(row=0, column=0, sticky="w")
        preset_box = ttk.Combobox(options, textvariable=self.preset, values=["rapido", "equilibrado", "extendido"], state="readonly", width=16)
        preset_box.grid(row=0, column=1, padx=6)
        ttk.Label(options, text="Motor").grid(row=0, column=2, sticky="w")
        engine_box = ttk.Combobox(options, textvariable=self.engine, values=["fake", "gst"], state="readonly", width=12)
        engine_box.grid(row=0, column=3, padx=6)
        ttk.Checkbutton(options, text="Reanudar", variable=self.resume, command=self._refresh_command_preview).grid(row=0, column=4, padx=8)
        ttk.Checkbutton(options, text="Dry run", variable=self.dry_run, command=self._refresh_command_preview).grid(row=0, column=5, padx=8)
        ttk.Checkbutton(options, text="Solo plan", variable=self.only_plan, command=self._refresh_command_preview).grid(row=0, column=6, padx=8)
        ttk.Checkbutton(options, text="Sin analisis", variable=self.skip_analysis, command=self._refresh_command_preview).grid(row=0, column=7, padx=8)
        ttk.Label(options, text="Limite").grid(row=0, column=8)
        ttk.Entry(options, textvariable=self.max_sessions, width=8).grid(row=0, column=9, padx=4)

        controllers_frame = ttk.LabelFrame(main, text="Controllers comparables")
        controllers_frame.pack(fill="x", pady=8)
        self.controllers_inner = ttk.Frame(controllers_frame)
        self.controllers_inner.pack(fill="x", padx=8, pady=8)

        buttons = ttk.Frame(main)
        buttons.pack(fill="x", pady=8)
        ttk.Button(buttons, text="Ejecutar / reanudar", command=self._run_phase6).pack(side="left", padx=4)
        ttk.Button(buttons, text="Generar plan", command=self._plan_only).pack(side="left", padx=4)
        ttk.Button(buttons, text="Analizar carpeta", command=self._run_analysis).pack(side="left", padx=4)
        ttk.Button(buttons, text="Verificacion clasica controlada", command=self._run_classic).pack(side="left", padx=4)
        ttk.Button(buttons, text="Detener", command=self._stop_process).pack(side="right", padx=4)

        progress_row = ttk.Frame(main)
        progress_row.pack(fill="x", pady=4)
        ttk.Progressbar(progress_row, variable=self.progress_percent, maximum=100.0).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 8),
        )
        ttk.Label(progress_row, textvariable=self.progress_text, width=42).pack(side="right")

        analysis_row = ttk.Frame(main)
        analysis_row.pack(fill="x", pady=4)
        ttk.Label(analysis_row, text="Paquete existente").pack(side="left")
        ttk.Entry(analysis_row, textvariable=self.package_to_analyze).pack(side="left", fill="x", expand=True, padx=6)
        ttk.Button(analysis_row, text="Buscar", command=self._browse_package).pack(side="left")

        preview_frame = ttk.LabelFrame(main, text="Comando")
        preview_frame.pack(fill="x", pady=8)
        self.command_preview = tk.Text(preview_frame, height=3, wrap="word")
        self.command_preview.pack(fill="x", padx=8, pady=8)

        log_frame = ttk.LabelFrame(main, text="Salida")
        log_frame.pack(fill="both", expand=True, pady=8)
        self.log_text = tk.Text(log_frame, wrap="word")
        self.log_text.pack(fill="both", expand=True, padx=8, pady=8)

        for variable in (self.config_path, self.output_root, self.preset, self.engine, self.max_sessions):
            variable.trace_add("write", lambda *_: self._refresh_command_preview())

    def _load_controllers(self) -> None:
        for child in self.controllers_inner.winfo_children():
            child.destroy()
        config = self._safe_load_config()
        configured = set(_mapping(config.get("experiment")).get("controllers") or [])
        controllers = discover_comparable_controllers(config)
        for index, controller in enumerate(controllers):
            key = str(controller["controller_key"])
            selected = True if not configured else key in configured
            var = self.tk.BooleanVar(value=selected)
            self.controller_vars[key] = var
            self.ttk.Checkbutton(
                self.controllers_inner,
                text=str(controller["display_name"]),
                variable=var,
                command=self._refresh_command_preview,
            ).grid(row=index // 4, column=index % 4, sticky="w", padx=8, pady=4)

    def _safe_load_config(self) -> Dict[str, Any]:
        path = self.config_path.get().strip() if hasattr(self, "config_path") else ""
        try:
            return load_phase6_config(path or None)
        except Exception:
            return load_phase6_config(None)

    def _selected_controllers(self) -> List[str]:
        return [key for key, var in self.controller_vars.items() if bool(var.get())]

    def _generated_config(self) -> Path:
        return write_gui_override_config(
            base_config_path=self.config_path.get().strip() or None,
            preset=self.preset.get(),
            engine=self.engine.get(),
            output_root=self.output_root.get(),
            controllers=self._selected_controllers(),
        )

    def _phase6_command(self, *, only_plan: Optional[bool] = None) -> List[str]:
        generated = self._generated_config()
        max_sessions = _optional_int(self.max_sessions.get())
        return build_phase6_command(
            config_path=str(generated),
            preset=self.preset.get(),
            output_root=self.output_root.get(),
            package_root=self.package_to_analyze.get().strip() or None,
            dry_run=bool(self.dry_run.get()),
            only_plan=bool(self.only_plan.get()) if only_plan is None else bool(only_plan),
            skip_analysis=bool(self.skip_analysis.get()),
            resume=bool(self.resume.get()),
            max_sessions=max_sessions,
        )

    def _refresh_command_preview(self) -> None:
        if not hasattr(self, "command_preview"):
            return
        try:
            command = build_phase6_command(
                config_path=self.config_path.get().strip() or None,
                preset=self.preset.get(),
                output_root=self.output_root.get(),
                package_root=self.package_to_analyze.get().strip() or None,
                dry_run=bool(self.dry_run.get()),
                only_plan=bool(self.only_plan.get()),
                skip_analysis=bool(self.skip_analysis.get()),
                resume=bool(self.resume.get()),
                max_sessions=_optional_int(self.max_sessions.get()),
            )
            text = " ".join(command)
        except Exception as exc:
            text = str(exc)
        self.command_preview.delete("1.0", "end")
        self.command_preview.insert("1.0", text)

    def _run_phase6(self) -> None:
        self._run_command(self._phase6_command())

    def _plan_only(self) -> None:
        self._run_command(self._phase6_command(only_plan=True))

    def _run_analysis(self) -> None:
        package = self.package_to_analyze.get().strip()
        if not package:
            self.messagebox.showerror("Falta carpeta", "Selecciona una carpeta Phase 6.")
            return
        self._run_command(build_analysis_command(package))

    def _run_classic(self) -> None:
        generated = self._generated_config()
        self._run_command(
            build_classic_controlled_command(
                config_path=str(generated),
                preset=self.preset.get(),
                output_root=self.output_root.get(),
            )
        )

    def _run_command(self, command: Sequence[str]) -> None:
        if self.process is not None and self.process.poll() is None:
            self.messagebox.showwarning("Proceso activo", "Ya hay un proceso en marcha.")
            return
        self.progress_percent.set(0.0)
        self.progress_text.set("Progreso: iniciando")
        self.log_text.insert("end", "\n$ {0}\n".format(" ".join(command)))
        thread = threading.Thread(target=self._worker, args=(list(command),), daemon=True)
        thread.start()

    def _worker(self, command: List[str]) -> None:
        self.process = subprocess.Popen(
            command,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert self.process.stdout is not None
        for line in self.process.stdout:
            if line.startswith("PHASE6_PROGRESS "):
                progress = parse_phase6_progress_line(line)
                if progress:
                    self.root.after(0, self._update_progress, progress)
            self.root.after(0, self.log_text.insert, "end", line)
            self.root.after(0, self.log_text.see, "end")
        code = self.process.wait()
        self.root.after(0, self.log_text.insert, "end", "\nProceso terminado con codigo {0}\n".format(code))
        if code == 0:
            self.root.after(0, self.progress_text.set, "Progreso: terminado correctamente")
        else:
            self.root.after(0, self.progress_text.set, "Progreso: terminado con incidencias")

    def _update_progress(self, progress: Mapping[str, Any]) -> None:
        percent = float(progress.get("percent", 0.0) or 0.0)
        processed = int(progress.get("processed", 0) or 0)
        total = int(progress.get("total", 0) or 0)
        failed = int(progress.get("failed", 0) or 0)
        skipped = int(progress.get("skipped", 0) or 0)
        self.progress_percent.set(max(0.0, min(100.0, percent)))
        self.progress_text.set(
            "Progreso: {0:.1f}% ({1}/{2}) | fallidas {3} | reanudadas {4}".format(
                percent,
                processed,
                total,
                failed,
                skipped,
            )
        )

    def _stop_process(self) -> None:
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()

    def _browse_config(self) -> None:
        path = self.filedialog.askopenfilename(filetypes=[("YAML/JSON", "*.yaml *.yml *.json"), ("Todos", "*.*")])
        if path:
            self.config_path.set(path)
            self._load_controllers()

    def _browse_output(self) -> None:
        path = self.filedialog.askdirectory()
        if path:
            self.output_root.set(path)

    def _browse_package(self) -> None:
        path = self.filedialog.askdirectory()
        if path:
            self.package_to_analyze.set(path)


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _optional_int(value: Any) -> Optional[int]:
    text = str(value or "").strip()
    if not text:
        return None
    return int(text)


def parse_phase6_progress_line(line: str) -> Dict[str, Any]:
    text = str(line or "").strip()
    if not text.startswith("PHASE6_PROGRESS "):
        return {}
    result: Dict[str, Any] = {}
    for token in text.split()[1:]:
        key, sep, value = token.partition("=")
        if not sep:
            continue
        if key in {"processed", "total", "executed", "failed", "skipped"}:
            try:
                result[key] = int(float(value))
            except ValueError:
                result[key] = 0
        elif key == "percent":
            try:
                result[key] = float(value)
            except ValueError:
                result[key] = 0.0
        else:
            result[key] = value
    return result


def main() -> int:
    gui = Phase6Gui()
    gui.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
