# Phase 4E — Plain-language training runbook

## What “training the model” means here

Think of the model as a small decision assistant.

It does not watch a real video yet. It does not control the DASH player yet. It learns offline from examples.

Each example says:

```text
Given this buffer, these recent download speeds, and these available video qualities,
which representation would the teacher choose?
```

The teacher is not a human. It is a classical ABR method such as robust MPC or MPC replayed offline.

## What happens with traces

A trace is just a recorded or synthetic description of how the network behaves over time.

We do not train from old player dry-runs, because those logs were produced by previous controllers and can be biased.

The safe flow is:

```text
external network trace
  -> normalized trace
  -> offline replay
  -> teacher chooses actions
  -> JSONL training samples
  -> small neural model trains by imitation
```

## What Codex does

Codex implements code, fixes small issues, runs short smokes, and writes reports.

Codex should not be treated as the long-running trainer. For a long real training run, you launch the command in PowerShell and leave the terminal open. When it finishes, you paste the log and reports here.

## When the “terminal left open” part happens

That starts in Phase 4E, but only after we have a dataset worth training on.

There are three levels:

1. Synthetic smoke: short, seconds/minutes. Codex or you can run it.
2. External trace smoke: still short, maybe minutes. You run it with the exact command.
3. Candidate training: longer, maybe tens of minutes or hours on CPU. You run it in PowerShell and leave the terminal open.

## What counts as success

Training loss going down is not enough.

We need:

- valid actions only;
- no NaN or Inf;
- no future leakage;
- train-only normalization;
- no collapse to always min, always max, or always same bitrate;
- validation and OOD diagnostic reports;
- CPU reproducibility;
- all artifacts outside the repo;
- honest limitations.

## What does not count as success

- A nice-looking training curve on synthetic data.
- Good train reward with bad validation behavior.
- Using test/OOD to tune the model.
- Using old dry-runs as training data.
- Claiming it beats all classical controllers before Phase 6.
