# Phase 4E.2 to Phase 4F gate

Phase 4F can open only if Phase 4E.2 writes:

```text
PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F
```

If Phase 4E.2 writes:

```text
PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE
```

then do not export yet. The next step is either:

```text
expand corpus further;
adjust teacher/data contract;
document negative result;
repeat diagnostic training;
```

If Phase 4E.2 writes:

```text
PHASE4E2_BLOCKED_NEEDS_FIX
```

then fix the blocking issue before proceeding.
