# Deterministic checks first

Use a deterministic check when the policy can be stated as a path, import, AST,
or input/output property. It is cheaper, reproducible, and does not need a
confidence score.

| Policy shape | First choice |
| --- | --- |
| `renderer/**` cannot import `electron` | ESLint import restriction |
| An output stays beneath a root directory | Unit test with traversal and sibling-prefix inputs |
| An MP4 duration matches a story budget | Integration test plus `ffprobe` |
| A change weakens a domain boundary indirectly | LLM review plus human review |

`mixed` rules are common. For example, an integration test can prove that a
recovery manifest survives a controlled crash, while a reviewer can flag a new
save path that bypasses the established writer.

LLM review earns its place where the policy needs context. It should not be
asked to impersonate a linter.
