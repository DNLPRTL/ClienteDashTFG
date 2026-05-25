# Phase 3.5 Validation Summary

This document records the known Phase 3.5 validation history and the final closure validation set.

## Known Closure Commits

| subphase | commit |
| --- | --- |
| A0 | `0a43675` |
| A1 | `475c2b2` |
| A2 | `8970fd4` |
| A2.1 | `02c0695` |
| B | `b4636ab` |
| C | `50dd3aa` |
| D | `e540ac3` |

## Final Validation Themes

- Around 361 tests were present by the Phase 3.5D closure point, depending on local discovery details.
- `check_client_readiness.py --strict` passed with 78 OK, 0 WARN and 0 FAIL.
- Controlled external smoke used 4 scenarios.
- Smoke output preserved `outputs_are_benchmark_results=false`.
- Smoke output preserved `no_final_ranking=true`.
- The forbidden-file check was empty.
- Generated artifacts were kept outside the repository.

## Windows And Ubuntu Notes

Windows is the primary local validation environment for the current repository. Ubuntu remains relevant for future Mahimahi or `tc/netem` runbooks, but Phase 3.5 closure does not require either tool.

## Validation markers

- PHASE_3_5_VALIDATION_SUMMARY: complete
- A0=0a43675
- A1=475c2b2
- A2=8970fd4
- A2_1=02c0695
- B=b4636ab
- C=50dd3aa
- D=e540ac3
- readiness_strict_pass=true
- forbidden_files=false
- generated_artifacts_in_git=false
