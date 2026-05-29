# Phase 4E.1 Windows Commands

## Apply package

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$Zip = "$env:USERPROFILE\Downloads\phase4e1_external_trace_intake.zip"
$ExtractTo = "C:\Users\danie\Documents\TFG\_literature\phase4_AI\10_upload_batches\phase4e1_external_trace_intake"

New-Item -ItemType Directory -Path $ExtractTo -Force | Out-Null
Expand-Archive -Path $Zip -DestinationPath $ExtractTo -Force

Set-Location "C:\Users\danie\Documents\TFG\DashClientModular4"
$RepoRoot = git rev-parse --show-toplevel

& "$ExtractTo\apply_phase4e1_external_trace_intake.ps1" -RepoRoot $RepoRoot
& "$ExtractTo\validate_phase4e1_external_trace_intake.ps1" -RepoRoot $RepoRoot

python scripts\check_client_readiness.py --strict
```

## Repair local synthetic smoke wrapper

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E1_external_trace_intake\phase4e_repair_synthetic_smoke_wrapper_windows.ps1"
```

## Stage Phase 3 normalized traces for Phase 4E.1

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E1_external_trace_intake\phase4e1_prepare_phase3_trace_workspace_windows.ps1" `
  -Phase3Root "C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay" `
  -Phase4Root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI"

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E1_external_trace_intake\phase4e1_validate_phase3_trace_workspace_windows.ps1" `
  -Phase4Root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI"
```

## Run Codex

Use:

```text
docs/science/04_neural_abr/phase4e1_codex_prompt_external_trace_dataset.md
```

## Run external trace smoke after Codex

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E1_external_trace_intake\phase4e1_run_external_trace_smoke_after_codex_windows.ps1" `
  -RepoPath "C:\Users\danie\Documents\TFG\DashClientModular4" `
  -Phase4Root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI"
```

## Validate after Codex/smoke

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E1_external_trace_intake\phase4e1_validate_windows.ps1" `
  -RepoPath "C:\Users\danie\Documents\TFG\DashClientModular4"
```

## Commit and push if PASS

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E1_external_trace_intake\phase4e1_commit_push_windows.ps1" `
  -RepoPath "C:\Users\danie\Documents\TFG\DashClientModular4" `
  -CommitAndPush
```
