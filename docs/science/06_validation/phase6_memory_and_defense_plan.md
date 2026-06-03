# Phase 6 Memory And Defense Plan

Status: final Phase 6A2 protocol decision for thesis/defense integration.

## Chapter 6 Evaluation

Phase 6 feeds Chapter 6 with:

- the final evaluation protocol;
- controller classification;
- trace selection and eligibility policy;
- media profile decision;
- metrics schema;
- statistical comparison plan;
- evidence package and reproducibility checklist;
- threats to validity.

Chapter 6 must make clear that results are valid only for eligible traces, frozen media profile and documented gates.

## Chapter 7 Conclusions And Future Work

Chapter 7 should use Phase 6 to separate:

- what the TFG validated under a controlled protocol;
- what remains future work, including broader OOD datasets, VMAF/perceptual artifacts, live deployment, ABR-Arena-like testing and richer causal evaluation.

## Figures/Tables Register

The figures/tables register should include the planned figures and tables from `results_tables_plan.md`, especially:

- Phase 6 pipeline diagram;
- trace eligibility/gating flow;
- controller matrix;
- primary result table;
- per-dataset result table;
- gates/exclusions table;
- reproducibility/evidence manifest table.

## Reproducibility Appendix

The appendix should summarize:

- exact commit;
- commands;
- environment;
- trace manifest audit;
- artifact manifest;
- controller matrix;
- media profile;
- exclusions and gates.

This maps directly to `ubuntu_evidence_package_spec.md` and `reproducibility_checklist.md`.

## Defense Slides

Defense slides should emphasize:

- the ABR controller families being compared;
- why trace leakage was blocked;
- why session/trace is the statistical unit;
- what `qoe_linear_mean` means and what it does not mean;
- why no MOS/VMAF claim exists without artifacts;
- neural safety/fallback behavior as a separate diagnostic summary;
- limitations and future work without overclaiming.
