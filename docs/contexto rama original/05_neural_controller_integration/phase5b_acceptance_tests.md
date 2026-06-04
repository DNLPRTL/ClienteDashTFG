# Phase 5B acceptance tests

These tests are to implement later. No test files are created in this documentation block.

## Future structural tests

| Test | Expected behavior |
|---|---|
| Bundle missing | Fallback, no crash, fallback reason recorded |
| Invalid manifest | Fallback, no crash, fallback reason recorded |
| Hash mismatch | Fallback, no crash, fallback reason recorded |
| Feature schema mismatch | Fallback, no crash, fallback reason recorded |
| Missing required feature | Fallback, no crash, fallback reason recorded |
| All-false action mask | Fallback, no crash, fallback reason recorded |
| NaN/Inf score | Fallback, no crash, fallback reason recorded |
| Selected masked action | Fallback, invalid action telemetry recorded |
| Single representation | Select only representation or lowest valid fallback |
| Variable ladder | Never select invalid index |
| Deterministic inference | Same input gives same action |
| Controller returns rate from ladder | Returned rate is exactly one `feedback["rates"]` value |
| Telemetry fields populated | Required diagnostic fields exist |
| No benchmark fields emitted | No rank, winner, improvement percent or p-value |

## Boundary

These are integration acceptance tests, not benchmark tests.
