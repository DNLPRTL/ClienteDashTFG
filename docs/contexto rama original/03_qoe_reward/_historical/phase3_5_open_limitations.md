# Phase 3.5 Open Limitations

Phase 3.5 closes the QoE/reward and artifact-methodology foundation. It does not close experimental evaluation.

## Limitations

- No formal benchmark exists yet.
- No controller ranking exists yet.
- Controlled smoke scenarios are synthetic and only validate artifact flow.
- Legacy dry-runs must be regenerated under the final contract if they are ever used for evaluation.
- VMAF is not calculated because reproducible perceptual artifacts are not available.
- Startup remains report-only because homogeneous measurement is still pending.
- No sim-to-real validation has been performed.
- Mahimahi and `tc/netem` are not gates for Phase 3.5 closure.
- No IA/RL model has been trained.
- The documented reward is a future candidate, not a training dataset.
- Trace splits and formal evaluation protocol remain pending for a later phase.

## Interpretation Boundary

Phase 3.5 can be cited as a methodology and tooling closure. It cannot be cited as evidence that one controller outperforms another.

## Validation markers

- PHASE_3_5_LIMITATIONS_DECLARED: true
- no formal benchmark yet
- no controller ranking yet
- no IA training yet
- VMAF deferred
- startup report-only
- smoke not benchmark
