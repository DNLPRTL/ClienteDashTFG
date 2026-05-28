# Phase 4D Codex/code-run logging protocol

## Purpose

Every code-generation or code-editing pass must be recoverable for the memory and defense.

## Local log path

```text
C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\codex_logs
```

## Required record per Codex run

Create a local file named:

```text
codex_phase4d_run_YYYYMMDD_HHMMSS.md
```

with:

```text
prompt used
files changed
commands run
validation output
known limitations
follow-up tasks
```

This log remains local-only and is not committed unless distilled into repo-ready Markdown.
