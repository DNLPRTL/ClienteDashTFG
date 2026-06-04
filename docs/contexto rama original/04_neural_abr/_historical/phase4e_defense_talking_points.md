# Phase 4E defense talking points

- Phase 4E Tier 0 trained offline only. No neural controller was registered.
- Codex did not choose a new method. It executed the already selected NeuralABR-Lite Candidate Scorer method from Phase 4A2/4B/4D.
- The smoke used synthetic diagnostic traces only. This is enough to test the pipeline, but not enough to claim a real candidate.
- Traces become supervised samples through deterministic replay: pre-decision context, candidate features, valid action mask, robust-MPC teacher label, then transition update.
- Teacher labels are produced by an offline `robust_mpc` labeler using `qoe_linear_v1 / reward_n`. The bounded oracle remains diagnostic-only.
- Future leakage is blocked by feature validation: future throughput, future download time, teacher action, teacher reward, split, trace ID, source dataset and benchmark results are forbidden as model inputs.
- Normalization is fitted on train samples only and then applied to validation/OOD samples.
- Action masks prevent impossible bitrates because the model action is always `representation_index` and invalid candidates are masked before loss/argmax.
- The smoke passed action validity: validation and OOD diagnostic valid action rate were both 1.0.
- The smoke model collapsed to representation `3` on the tiny synthetic set. This is documented as a limitation and blocks any Phase 4F-ready interpretation.
- Phase 4E is not a benchmark or ranking. It does not compare against BBA, BOLA, MPC or robustMPC as final results.
- The next step is external trace preparation and a trace-level train/validation/OOD smoke, still offline and still outside the repository.
