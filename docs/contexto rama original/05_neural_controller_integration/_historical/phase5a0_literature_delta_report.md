# Phase 5A0 literature delta report

## What Phase 5A0 adds beyond Phase 4

Phase 4 answered how to train and export a small NeuralABR-Lite Candidate Scorer. Phase 5A0 adds the runtime integration evidence needed before client code exists:

- the scorer must be guarded by runtime safety logic;
- representation selection must use an action mask;
- invalid MPD representations must never be selectable;
- bundle loading must be local-only and fail closed;
- PyTorch loading must use safe CPU `state_dict` loading;
- diagnostic telemetry must not become benchmark evidence;
- structural smoke tests are not benchmarks.

## Does any source invalidate Phase 4?

No. None of the Phase 5 sources invalidates the Phase 4 decision. The new sources reinforce the existing Candidate Scorer design because variable ladders, production encodings and action masks are common integration problems.

## Does any source change the integration design?

The sources refine the integration design. Phase 5 should not implement a full neural controller. The accepted design is a guarded neural scorer controller:

```text
online feedback -> feature builder -> schema check -> train-only normalization
-> action mask -> CPU scorer -> raw_action -> safety guard -> safe_action/fallback
-> diagnostic-only telemetry
```

## Mandatory safety constraints

- Build an action mask for current valid representations.
- Apply the mask before argmax.
- Reject all-false masks.
- Validate the selected action after inference.
- Run a safety guard after `raw_action`.
- If unsafe, downshift to the highest lower feasible representation.
- If no feasible action exists, use fallback.
- Fail closed on missing bundle, bad schema, load failure, non-finite scores, timeout or runtime exception.

## Mandatory runtime constraints

- Use only features available before the segment request.
- Build throughput history only from completed downloads.
- Use candidate chunk size only if the MPD/client exposes it before the decision.
- Use chunks remaining only if known before the decision.
- Return an existing ladder rate, never an arbitrary bitrate.
- Do not require GStreamer or real playback for fake-engine structural smoke.

## Mandatory model loading constraints

- Bundle is local-only and outside the repository.
- Validate manifest and sha256 hashes before model use.
- Instantiate architecture from trusted local repo code.
- Load weights with `torch.load(path, map_location="cpu", weights_only=True)`.
- Reject full pickle model loading.
- Do not use remote URLs, `torch.hub`, or `weights_only=False` at runtime.
- If safe loading is unavailable, disable neural and use fallback.

## Mandatory telemetry constraints

- Telemetry is diagnostic-only.
- Record raw action, safe action, fallback, safety intervention and inference latency.
- Do not emit benchmark rank, winner, improvement percent, p-value or statistical significance claim in Phase 5.
- Do not treat runtime logs as training labels or benchmark data.

## Conclusion

No source invalidates Phase 4. The literature delta reinforces guarded scorer integration with mandatory fallback, mandatory action mask, local-only CPU inference, strict model loading and no benchmark claims until Phase 6.
