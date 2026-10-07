# Architecture Policy Kit for AI Code Review

An AI reviewer is useful only if it follows the architecture rules your team
actually cares about. This kit turns repository invariants into explicit
policies, near-miss fixtures, and a small evaluation set.

It does **not** make LLM code review reliable. The goal is fewer false accepts,
fewer false blocks, and deterministic CI for rules that do not need an LLM.

```text
repository invariants
        ↓
scoped policy pack
        ↓
approve/block near-miss fixtures
        ↓
reviewer evaluation
        ↓
false accepts / false blocks / needs-context / schema failures
        ↓
deterministic CI where possible; LLM review where context matters
```

The included ProgressCut pack is a working example, not a set of Electron rules
you are supposed to copy unchanged.

## Repository map

```text
policy/schema.json                     JSON Schema for a policy pack
templates/policy.yaml                  minimal policy-pack template
examples/progresscut/policy.yaml       six policy examples
examples/progresscut/fixtures/         approve/block scope and boundary cases
prompts/                               generic, Claude, and Codex contracts
eval/cases.jsonl                       answer key for the public example set
eval/review-response.schema.json       JSON Schema for reviewer output
eval/scoring.md                        how to measure reviewer failures
docs/                                  rule-writing and adoption guides
```

## Start with your repository

1. Copy [`templates/policy.yaml`](templates/policy.yaml) into your repository.
2. Write five to fifteen policies from incidents, postmortems, and repeated PR
   comments — not from generic architecture slogans.
3. Give every policy a path scope, a failure it prevents, and one near-miss that
   should still be approved.
4. Classify it:
   - `deterministic` — lint, AST checks, or tests can enforce it;
   - `semantic` — context is needed, so an LLM or human must review it;
   - `mixed` — a deterministic test protects the invariant while a reviewer
     catches new ways to bypass the established path.
5. Run the policy prompt on the fixtures. Record verdict, policy ID, schema
   compliance, evidence, and `NEEDS_CONTEXT` separately.
6. Move deterministic rules into CI. Keep models as a review signal for the
   remainder.

Read [`docs/adopting-in-a-real-repo.md`](docs/adopting-in-a-real-repo.md) before
using a model result as a merge requirement.

### Validate the kit

The repository has no runtime dependency. Run the same validation locally that
GitHub Actions runs on every change:

```bash
python3 scripts/validate_assets.py
```

It verifies schemas, case IDs, fixture references, fixture answer headers,
referenced policy IDs, and local Markdown links. It does not claim to evaluate
a model or to validate arbitrary YAML against the policy schema.

## ProgressCut example

[`examples/progresscut/policy.yaml`](examples/progresscut/policy.yaml) contains
six policies from a local-first Electron application:

| Policy | Classification | Primary enforcement |
| --- | --- | --- |
| Engine has no Node/platform I/O | deterministic | ESLint path restriction |
| Domain has no runtime adapter dependency | mixed | ESLint plus review |
| Renderer has no direct Electron import | deterministic | ESLint path restriction |
| Recovery writes replace-by-rename | mixed | crash/restart integration test |
| Rendered MP4 matches story duration | mixed | `ffprobe` integration test |
| Export path stays under session root | mixed | traversal unit tests |

The fixtures are intentionally close. The renderer may call a typed preload
bridge, but it may not import Electron; Electron use in the main process is
outside that renderer-only policy. A safe export check must reject parent
traversal and sibling prefixes, not merely call `resolve()`.

## Evaluate a reviewer honestly

The public fixtures are answer-labelled teaching material. Do not send
`examples/.../approve` or `examples/.../block` directly to a model and call its
answer a benchmark; the directory and header leak the result.

For a real evaluation:

- keep a private holdout set;
- remove labels before prompting;
- pin the policy, prompt, model, and integration version;
- report false accepts and false blocks separately;
- validate structured output with the response schema before counting a verdict;
- check evidence against the diff rather than accepting a long explanation.

In a real PR integration, route `NEEDS_CONTEXT` to a human. Missing context is
not evidence that a change is safe.

[`eval/scoring.md`](eval/scoring.md) defines the reporting contract. The public
[Kaggle benchmark](https://www.kaggle.com/benchmarks/pavelkazantsev7776/architecture-aware-typescript-code-review/versions/1)
is the first, intentionally small demonstration of the method.

## What this kit does not include

There is no hosted reviewer, GitHub App, CI runner, model vendor lock-in, or
claim that every architecture rule belongs in a prompt. Those are integration
decisions after you know which policies matter and how the reviewer behaves on
your fixtures.

## Read next

- [Writing good rules](docs/writing-good-rules.md)
- [Deterministic checks first](docs/deterministic-vs-llm.md)
- [Adopting a policy pack](docs/adopting-in-a-real-repo.md)
- [ProgressCut: the source project](https://github.com/icesurf666/progress-cut)

## License

[MIT](LICENSE)
