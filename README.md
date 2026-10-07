# Architecture Review Kit

Small, copyable fixtures for reviewing TypeScript changes that may work while
violating repository boundaries.

The kit is useful when a project has rules such as “the UI never imports
Electron” or “recovery records are written atomically”, but those rules live in
someone's head instead of a repeatable review process.

It includes six rules, a good and bad diff for each rule, and a structured
prompt for an AI reviewer. The examples come from the architecture of
[ProgressCut](https://github.com/icesurf666/progress-cut), but contain no
screenshots, user sessions, or application code.

## Start here

1. Read [rules.md](rules.md).
2. Paste [audit-prompt.md](audit-prompt.md) and one diff into your preferred
   review agent.
3. Compare the result with the expected verdict in the fixture header.
4. Replace the example rules with the actual boundaries in your repository.

```text
good/  → changes a reviewer should approve
bad/   → changes a reviewer should block
```

The examples are paired deliberately. A renderer calling a typed bridge is
allowed; importing Electron directly is not. A `resolve()` check with a path
separator is allowed; a prefix-only check is not.

## Rules covered

| Rule | Good fixture | Bad fixture |
| --- | --- | --- |
| Pure engine | `good/01-pure-engine-function.diff` | `bad/01-engine-node-import.diff` |
| Runtime-free domain | `good/02-domain-branded-id.diff` | `bad/02-domain-runtime-import.diff` |
| Renderer boundary | `good/03-renderer-bridge.diff` | `bad/03-renderer-electron-import.diff` |
| Atomic recovery | `good/04-atomic-manifest.diff` | `bad/04-non-atomic-manifest.diff` |
| Exact render duration | `good/05-duration-cap.diff` | `bad/05-uncapped-render.diff` |
| Safe export path | `good/06-safe-output-path.diff` | `bad/06-output-prefix-confusion.diff` |

## What this is not

This is not a universal benchmark or a replacement for tests and code review.
It is a compact starting point for making architecture policy explicit. The
fixtures are synthetic, single-file, and intentionally readable in under a
minute.

For the public model comparison built from these fixtures, see the
[Kaggle benchmark](https://www.kaggle.com/benchmarks/pavelkazantsev7776/architecture-aware-typescript-code-review/versions/1).

## Keep the discussion going

I publish small engineering experiments about local-first tools, reliability,
and AI-assisted development at [pkazantsev.com/writing](https://www.pkazantsev.com/writing).

## License

[MIT](LICENSE)
