# Memory and defense traceability for Phase 4D

Every Codex/code implementation run in Phase 4D must leave thesis-ready documentation.

## Required implementation docs after Codex

Codex must create or update:

```text
docs/science/04_neural_abr/_historical/phase4d_implementation_report.md
docs/science/04_neural_abr/phase4d_code_traceability_matrix.md
docs/science/04_neural_abr/_historical/phase4d_test_report.md
docs/science/04_neural_abr/_historical/phase4d_defense_talking_points.md
docs/science/04_neural_abr/_historical/phase4d_open_limitations.md
```

## Traceability matrix columns

```text
implemented_file
implemented_symbol
contract_source
paper_decision_source
purpose
leakage_gate
test_file
memory_section
```

## Defense requirements

The implementation must be explainable as student-built:

- no opaque giant model;
- no external black-box ABR framework;
- no hidden dataset;
- no uncontrolled GPU dependency;
- no benchmark claim;
- clear mapping from papers to design;
- clear mapping from design to code;
- clear limitations.

