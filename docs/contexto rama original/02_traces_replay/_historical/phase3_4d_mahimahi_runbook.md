# Phase 3.4D Mahimahi Runbook

This is an Ubuntu-only optional runbook for future environment probing. It does not require Mahimahi to be installed and does not authorize actual Mahimahi execution in Phase 3.4D.

## Scope

Mahimahi can be useful later as a secondary validation tool for shell-based HTTP record/replay and network emulation. It does not replace the custom Python trace-driven pipeline and does not produce benchmark results in Phase 3.4D.

## Probe Commands Only

If an Ubuntu machine is available, the only Phase 3.4D action is to probe whether commands are present:

```bash
command -v mm-link
command -v mm-delay
command -v mm-webrecord
command -v mm-webreplay
```

Optional version/help probes may be recorded only if the command exists:

```bash
mm-link --help
mm-delay --help
mm-webrecord --help
mm-webreplay --help
```

Do not install Mahimahi as part of Phase 3.4D. Do not run a Mahimahi experiment unless a later phase separately authorizes it.

## Artifact Policy

Probe output is local/audit-only and must be written outside the repository. It is not a benchmark artifact, not a dry-run artifact and not final evaluation evidence.

## Future Use Conditions

Future Mahimahi use must define:

- the exact Ubuntu environment;
- how normalized traces map to Mahimahi inputs, if at all;
- whether the test uses `mm-link`, `mm-delay`, `mm-webrecord` or `mm-webreplay`;
- how controller/runtime behavior is connected without changing controllers;
- artifact labels that distinguish Mahimahi validation from Python dry-runs;
- cleanup and reproducibility notes;
- explicit non-equivalence with Python dry-run artifacts unless a later benchmark protocol says otherwise.

## Risks

| risk | implication |
| --- | --- |
| Linux-only operational path | Windows development cannot depend on Mahimahi. |
| Tool availability | Phase 3.5 must not be blocked by missing Mahimahi commands. |
| Privilege/namespace assumptions | System-level behavior may vary by Ubuntu environment. |
| HTTP record-replay mismatch | `mm-webrecord`/`mm-webreplay` do not directly match the current fake dry-run loop. |
| Comparability risk | Mahimahi outputs cannot be treated as equivalent to Python dry-run outputs without a later protocol. |

## Interpretation

Mahimahi can validate whether selected behavior remains plausible under an external shell-based emulation workflow. It is not the primary benchmark path, not required for Phase 3.5 and not a source of controller ranking in Phase 3.4D.
