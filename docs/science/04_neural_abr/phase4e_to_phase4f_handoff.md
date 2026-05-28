# Phase 4E to Phase 4F handoff

Phase 4F can open only if Phase 4E closes as:

```text
PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F
```

Required handoff artifacts:

- model checkpoint outside repo;
- dataset manifest outside repo;
- training report in docs;
- offline validation report in docs;
- model card draft in docs;
- latency/valid-action/collapse checks;
- explicit limitations.

If Phase 4E closes only with synthetic smoke, Phase 4F remains blocked.
