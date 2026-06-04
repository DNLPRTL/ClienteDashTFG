# Phase 3.5B QoE Calculator Acceptance Tests

Status: implemented_phase3_5b_synthetic_tests.

PHASE_3_5B_ACCEPTANCE_TESTS: synthetic_unittest_only

## Test Scope

The tests in `tests/test_qoe_metrics.py` use synthetic in-memory segment inputs only. They do not create files, generate CSVs, execute dry-runs or call benchmark tooling.

## Synthetic Cases

| case | input | expected evidence |
| --- | --- | --- |
| linear no rebuffer | 1000, 2000, 1000 kbps | quality utility `4.0`, smoothness `2.0`, QoE sum `2.0`, mean `2/3`, two switches |
| linear with rebuffer | same bitrates, `1.0s` rebuffer on segment 2 | rebuffer penalty `4.3`, total rebuffer `1.0`, one stall event, QoE sum `-2.3` |
| single segment | one bitrate, no rebuffer | zero smoothness, zero switches, QoE equals quality utility |
| invalid empty input | no segments | `ValueError` |
| invalid bitrate | zero or negative bitrate | `ValueError` |
| invalid rebuffer | negative rebuffer | `ValueError` |
| invalid non-finite values | NaN or infinity in bitrate, rebuffer or weights | `ValueError` |
| log sensitivity | 1000 and 2000 kbps, `min_bitrate_kbps=1000` | quality utility `log(2)`, smoothness `log(2)`, QoE sum `0.0` |
| invalid log minimum | `min_bitrate_kbps <= 0` or non-finite | `ValueError` |
| immutable rewards | any valid run | `segment_rewards` is a tuple |

## Commands

```powershell
python -m py_compile core\evaluation\__init__.py core\evaluation\qoe.py tests\test_qoe_metrics.py
python -m unittest tests.test_qoe_metrics
python -m unittest discover
```

## Limits

- No real artifacts are read or written.
- No dry-run is executed.
- No formal benchmark is produced.
- No controller ranking is produced.
- No IA/training is opened.
