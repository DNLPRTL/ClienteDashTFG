# Historical Document Policy

The science tree intentionally keeps many Markdown files from closed phases. They preserve traceability, but not every file is canonical for current work.

## Categories

| category | meaning | expected use |
| --- | --- | --- |
| canonical | Current authoritative source for a phase, contract, or decision. | Read first and cite for current project state. |
| historical | Preserved intermediate note, draft, or earlier decision context. | Use for provenance only; do not treat as current if a later closure supersedes it. |
| handoff | Prompt, transition note, or next-phase instruction from a closed block. | Use to understand intent, not as a standing implementation order. |
| closure | Final acceptance, limitation, or non-claim record for a phase/subphase. | Prefer over intermediate notes when stating project status. |
| template | Reusable structure for cards, specs, tests, or memory notes. | Copy only when opening a new explicitly approved block. |
| memory-feed | Material intended for thesis chapters, defense, figures, or tables. | Use for writing the TFG memory; validate against canonical docs before making claims. |
| local-only reference | External workspace note, script, bundle marker, manifest, or audit artifact outside Git. | Reference by path when useful; do not commit the artifact itself. |

## Current Canonical Route

Use these entry points before opening deep historical paths:

- `docs/INDEX.md`
- `docs/science/PHASE_INDEX.md`
- `docs/science/CANONICAL_DOCUMENTS.md`
- phase-specific `README.md` files
- latest closure reports for closed phases

## Phase 6P2 Layout

Phase 6P2 groups non-canonical closed-phase working material inside the phase where it belongs:

- `_historical/`: intermediate reports, notes, local runbooks, superseded plans, and closure trail fragments.
- `_handoffs/`: prompts, handoffs, transition notes, and next-step records.
- `_templates/`: reusable templates.

Canonical and support documents remain in the phase directory root. Do not treat `_historical/` or `_handoffs/` files as current instructions unless a current index explicitly points to them for provenance.

## Supersession Rules

- A closure report supersedes implementation prompts from the same block.
- A no-benchmark or non-claim policy remains active until a later explicit validation phase replaces it.
- Local-only artifacts such as bundles, datasets, run logs, PDFs, and audit JSON files are never canonical Git content.
- Phase 4 teacher agreement and OOD diagnostics remain historical/diagnostic for generalization claims after the checksum leakage finding.

## Preservation Rule

Do not delete historical Markdown during maintenance hygiene unless a later task explicitly scopes archival or removal. Documentation hygiene should index, classify, and clarify first.
