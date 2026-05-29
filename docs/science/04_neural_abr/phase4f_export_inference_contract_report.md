# Phase 4F — export/inference contract report

Status: scaffold for Phase 4F.

Phase 4F is opened only because Phase 4E.2 produced an offline candidate and the cross-platform candidate-readiness gates passed after repair.

Phase 4F purpose:

- convert the Phase 4E.2 offline candidate into a versioned, validated inference bundle;
- define the inference API without integrating it into the DASH client;
- prove that loading the bundle, building features, applying action masks and producing a valid representation score/action is deterministic and CPU-first;
- document everything needed for memory and defense;
- keep benchmark/ranking/client integration blocked.

Phase 4F is not Phase 5. It must not touch controllers, player, runtime or media.
