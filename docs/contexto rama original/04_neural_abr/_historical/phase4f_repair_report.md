# Phase 4F-R1 Repair Report

Phase 4F-R1 repairs the cross-platform bundle validation gate.

Ubuntu failed the temporary fixture test because `no_repo_artifacts` was classified as a default hard failure inside pure bundle validation. That made a valid minimal bundle fixture return `PHASE4F_BLOCKED_NEEDS_FIX` when the repository hygiene scan found an environmental issue unrelated to the temporary bundle.

The repair separates gate classes:

- hard correctness gates: required bundle files, manifest hashes, CPU model load, schemas, train-only normalization, action validity, valid action rate, finite scores, and deterministic inference;
- bundle readiness gates: offline p95 inference latency;
- environmental/repo hygiene gates: forbidden repo artifacts, protected-path changes, and git working tree hygiene.

Default Phase 4F bundle validation now marks repo hygiene as `NOT_CHECKED` unless `--check-repo-hygiene` is supplied. This keeps temporary unit fixtures from being blocked by unrelated repository state.

When `--check-repo-hygiene` is supplied, repo artifact and protected-path failures remain blocking and are included in `hard_failures`.

Phase 4F remains export/inference only. No client integration, controller registration, benchmark, ranking, SOTA claim, or real-world validation claim is made.

Phase 4G is allowed only after the repaired Phase 4F tests and readiness checks pass on both Windows and Ubuntu.
