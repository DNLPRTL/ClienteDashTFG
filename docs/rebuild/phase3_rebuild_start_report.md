# Phase 3 rebuild start report

Date: 2026-06-04

## Purpose

Prepare a safe restart point for rebuilding the project from Phase 3, using the
real Phase 2 closure commit as the base, without destroying the current
Phase 3/3.5/4/5/6 history.

This report does not start the Phase 3 rebuild.

## Initial repository state

- Initial branch inspected: `main`
- Initial `git status --short --branch`: `## main...origin/main [ahead 1]`
- Uncommitted changes at inspection time: none
- Existing tags observed: `phase1-client-readiness`

## Current work protected

- Protected commit: `133f24ca4f34b9c3f546c3bb16c10884dcc7f623`
- Protected commit short name: `133f24c`
- Protected commit subject: `feat(validation): add Phase 6 MPD media profile freeze`
- Archive reference created: branch `archive/current-before-phase3-rebuild`
- Archive reference target: `133f24ca4f34b9c3f546c3bb16c10884dcc7f623`

This preserves the current local state of `main` as a normal Git branch before
the rebuild branch was created.

## Phase 2 closure commit selected

- Selected commit: `28f9741847e548f590c7be6730e37878af55e11c`
- Selected commit short name: `28f9741`
- Commit subject: `docs(science): formally close Phase 2 baseline work`
- Commit date: `2026-05-20T09:15:55+02:00`
- Parent commit: `db5f8c88cb173c8a4f2d9ac5bf01772f44df7dd5`
- Parent subject: `docs(science): close Phase 2.3 baseline implementation audit`

## Evidence for selecting `28f9741`

The commit was selected after searching the Git history for Phase 2 and baseline
terms including `phase2`, `fase2`, `baseline`, `closure`, and `cierre`.

Relevant matching commits around the selected point:

```text
28f9741 docs(science): formally close Phase 2 baseline work
db5f8c8 docs(science): close Phase 2.3 baseline implementation audit
504f48f feat(controller): add RobustMPC ABR baseline
a36be16 feat(controller): add MPC ABR baseline
1819aa3 feat(controller): add BOLA ABR baseline
2120c5f feat(controller): add BBA ABR baseline
cf5e583 feat(controller): add rate based ABR baseline
7a2dac7 docs(science): add Phase 2 ABR baseline operational specs
c12ba5a docs(science): scaffold Phase 2 ABR baseline literature docs
```

The first commits after `28f9741` start Phase 3 trace replay work:

```text
1df5389 docs(science): scaffold Phase 3 trace replay methodology
1c50d8c docs(science): add Phase 3 trace replay source cards
5a8cc4c docs(science): define Phase 3 common trace schema
6016fb6 docs(science): record Phase 3 local dataset acquisition
e908119 feat(trace): add synthetic trace schema validation
```

The selected commit also adds or updates explicit Phase 2 closure documents,
including:

```text
docs/architecture/phase2_baseline_closure.md
docs/science/01_baselines/phase2_baseline_closure.md
docs/science/01_baselines/phase2_academic_validity_statement.md
docs/science/01_baselines/phase2_open_limitations_and_deferred_work.md
docs/science/01_baselines/phase2_test_validation_summary.md
docs/science/01_baselines/phase2_transition_to_phase3.md
```

Conclusion: `28f9741` is the correct restart base because it formally closes
Phase 2, follows the Phase 2.3 baseline implementation audit, and immediately
precedes the Phase 3 trace replay sequence.

## Rebuild branch created

- New branch: `rebuild/phase3-from-phase2`
- Branch base before this report commit: `28f9741847e548f590c7be6730e37878af55e11c`
- `main` was not reset, rewritten, force-pushed, or moved.

## Final repository status

After committing this report on `rebuild/phase3-from-phase2`, the intended final
status is:

```text
## rebuild/phase3-from-phase2
```

No Phase 3 rebuild implementation has been started.

## External workspace warning

Git references protect only versioned repository content. External folders such
as `C:\Users\danie\Documents\TFG\_datasets`,
`C:\Users\danie\Documents\TFG\_models`,
`C:\Users\danie\Documents\TFG\_runs`,
`C:\Users\danie\Documents\TFG\_scripts`,
`C:\Users\danie\Documents\TFG\_literature`,
`C:\Users\danie\Documents\TFG\_audits`, and
`C:\Users\danie\Documents\TFG\_archive` may contain unversioned artifacts and
must be reviewed or backed up separately before relying on them during the
rebuild.
