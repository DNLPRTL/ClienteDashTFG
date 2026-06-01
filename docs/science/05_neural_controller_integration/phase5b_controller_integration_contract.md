# Phase 5B controller integration contract

## Purpose

This contract defines how a future NeuralABR-Lite controller may integrate with the existing DashClientModular4 controller API. It is documentation-only and creates no runtime code.

## API compatibility

The future controller must be compatible with the current dict-based controller API:

- read player feedback through `setPlayerFeedback`;
- compute the next action through `calcControlAction`;
- return or select an existing ladder rate;
- never return an arbitrary bitrate outside `feedback["rates"]`;
- map `representation_index` to `feedback["rates"][index]`;
- preserve player/runtime contracts except through the documented controller interface.

## Runtime constraints

- The controller must not require GStreamer.
- The controller must work in fake engine smoke before any real playback use.
- The controller must not mutate MPD, media engine or player state directly.
- The controller must not register itself until the future implementation block explicitly allows registry changes.

## Output rule

The neural scorer outputs a candidate `representation_index`. The controller output must be the corresponding existing rate:

```text
selected_rate_Bps = feedback["rates"][safe_action_index]
```

If this mapping cannot be performed safely, the controller must fallback.

## Benchmark boundary

This contract supports future structural smokes only. It is diagnostic-only and not benchmark evidence.
