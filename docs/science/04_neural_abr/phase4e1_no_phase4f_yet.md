# Phase 4E.1 No Phase 4F Yet

Phase 4F export/inference contract is blocked until an external-trace offline candidate exists.

## Reason

The current Phase 4E result is synthetic Tier 0. It validates mechanics, not a usable model candidate.

The smoke model predicted only representation 3 across validation/OOD. That is acceptable as a diagnostic smoke but not acceptable as a model to export for client integration.

## Required before Phase 4F

Before Phase 4F:

- external-trace dataset exists;
- trace-level splits exist;
- CPU training run exists;
- offline validation exists;
- model card exists;
- no-collapse checks pass or the limitation is documented as non-candidate;
- acceptance gate explicitly says ready for export.

## Marker

PHASE4F_ALLOWED=false
