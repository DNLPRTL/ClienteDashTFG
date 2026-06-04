# Phase 4E.2 Windows commands

## Apply package

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$Zip = "$env:USERPROFILE\Downloads\phase4e2_expanded_corpus_candidate_readiness.zip"
$ExtractTo = "C:\Users\danie\Documents\TFG\_literature\phase4_AI\10_upload_batches\phase4e2_expanded_corpus_candidate_readiness"

New-Item -ItemType Directory -Path $ExtractTo -Force | Out-Null
Expand-Archive -Path $Zip -DestinationPath $ExtractTo -Force

Set-Location "C:\Users\danie\Documents\TFG\DashClientModular4"
$RepoRoot = git rev-parse --show-toplevel

& "$ExtractTo\apply_phase4e2_candidate_readiness.ps1" -RepoRoot $RepoRoot
& "$ExtractTo\validate_phase4e2_candidate_readiness.ps1" -RepoRoot $RepoRoot

python scripts\check_client_readiness.py --strict
```

## After Codex implementation

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E2_candidate_readiness\phase4e2_run_after_codex_windows.ps1" `
  -RepoPath "C:\Users\danie\Documents\TFG\DashClientModular4" `
  -Phase3Root "C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay" `
  -Phase4Root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI"
```

## Validate Windows

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E2_candidate_readiness\phase4e2_validate_windows.ps1" `
  -RepoPath "C:\Users\danie\Documents\TFG\DashClientModular4"
```

## Commit + push

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

& "C:\Users\danie\Documents\TFG\_scripts\phase4_AI\phase4E2_candidate_readiness\phase4e2_commit_push_windows.ps1" `
  -RepoPath "C:\Users\danie\Documents\TFG\DashClientModular4" `
  -CommitAndPush
```
