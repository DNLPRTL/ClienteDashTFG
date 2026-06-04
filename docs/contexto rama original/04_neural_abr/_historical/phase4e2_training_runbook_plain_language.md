# Phase 4E.2 training runbook, plain language

This phase is not about integrating the model into the player.

It does four things:

1. Collect a larger set of external traces.
2. Convert them into the simple normalized format used by NeuralABR-Lite.
3. Train a small CPU model to imitate robust_mpc decisions.
4. Decide whether the result is mature enough to prepare an export/inference contract.

The training is launched from PowerShell. Codex prepares and fixes code; the user runs the commands. If a training command takes time, leave the terminal open until it finishes.

Artifacts stay outside the repository:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI
C:\Users\danie\Documents\TFG\_runs\phase4_AI
C:\Users\danie\Documents\TFG\_models\phase4_AI
```

The repo only receives code, tests and Markdown documentation.
