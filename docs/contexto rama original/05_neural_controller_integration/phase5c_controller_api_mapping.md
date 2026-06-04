# Phase 5C controller API mapping

## Future controller identity

- Controller registry key: `neural_abr_lite`.
- Future class: `NeuralAbrLiteController`.
- API status: compatible with the current dict-based `BaseController` API.

## Constructor params

| Param | Required default | Purpose |
|---|---|---|
| `bundle_dir` | optional string/path | Local bundle directory outside the repo. |
| `enabled` | `false` unless `bundle_dir` is valid | Allows disabled example config and fail-closed startup. |
| `fallback_controller` | `robust_mpc` | Preferred classical fallback. |
| `fallback_params` | empty mapping | Params passed to fallback controller factory. |
| `safety_buffer_margin_s` | conservative positive value | Buffer margin for safety guard. |
| `inference_timeout_ms` | optional diagnostic threshold | Timeout/fallback threshold, diagnostic-only. |
| `diagnostic_telemetry` | `true` | Emit diagnostic-only fields. |
| `fail_closed` | `true` | Disable neural/fallback on any unsafe condition. |

## Required methods

`NeuralAbrLiteController` must support:

- `setPlayerFeedback(feedback)`;
- `calcControlAction()`;
- `quantizeRate(rate)`;
- `getControlAction()`;
- `augment_feedback(feedback, context=None)`;
- optional `get_last_decision_telemetry()` if the telemetry hook is approved.

## Return contract

`calcControlAction()` must return a selected rate in bytes per second from the current `feedback["rates"]` ladder:

```text
selected_rate_Bps = feedback["rates"][safe_action_index]
```

The controller must call `setControlAction(selected_rate_Bps)` and set idle duration consistently with existing controllers.

## Never allowed

The future controller must never use:

- arbitrary bitrates outside the ladder;
- future throughput or future download time;
- future rebuffer/QoE/reward;
- teacher labels as runtime inputs;
- benchmark data as runtime inputs;
- controller identity as model input;
- model artifacts from Git;
- unsafe model loading.

Phase 5D remains diagnostic-only and not benchmark work.
