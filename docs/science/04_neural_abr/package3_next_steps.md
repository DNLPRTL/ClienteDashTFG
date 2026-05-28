# Package 3 next steps

## Immediate action

Apply the Package 3 ZIP, validate, and inspect the diff.

## Expected repository changes

Only files under:

```text
docs/science/04_neural_abr/
docs/science/04_neural_abr/source_cards/
```

## Expected post-apply commands

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$Zip = "$env:USERPROFILE\Downloads\phase4a1_package3_source_cards.zip"
$ExtractTo = "C:\Users\danie\Documents\TFG\_literature\phase4_AI\10_upload_batches\phase4a1_package3"

New-Item -ItemType Directory -Path $ExtractTo -Force | Out-Null
Expand-Archive -Path $Zip -DestinationPath $ExtractTo -Force

Set-Location "C:\Users\danie\Documents\TFG\DashClientModular4"

$RepoRoot = git rev-parse --show-toplevel

& "$ExtractTo\apply_phase4a1_package3.ps1" -RepoRoot $RepoRoot
& "$ExtractTo\validate_phase4a1_package3.ps1" -RepoRoot $RepoRoot

git status --short
git diff -- docs/science/04_neural_abr
python scripts/check_client_readiness.py --strict
```

## After validation

Paste:

- output of `validate_phase4a1_package3.ps1`;
- `git status --short`;
- final PASS/FAIL line from `check_client_readiness.py --strict`.

Then proceed to:

```text
Phase 4A2 — method_decision
```
