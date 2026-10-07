# Architecture review prompt

Paste this prompt with one diff at a time. Replace the six example rules with
your own repository's rules before using it in a real project.

```text
You are reviewing a proposed change in a strict TypeScript repository.
Functional tests may pass while architecture, recovery, and filesystem
invariants still fail.

Rules:
1. engine-no-node: engine code cannot import Node built-ins or platform APIs.
2. domain-no-runtime-deps: domain code cannot import runtime libraries.
3. renderer-no-electron: renderer UI cannot import Electron directly.
4. atomic-recovery-write: recovery metadata must use temporary-write then rename.
5. exact-render-duration: rendered video must be capped at its computed duration.
6. safe-output-path: exports must stay inside the configured output directory.

Review the diff below. Return only JSON:
{
  "decision": "APPROVE" | "BLOCK",
  "rule_id": "one violated rule ID, or none",
  "evidence": "one concise sentence that cites the relevant code"
}

For APPROVE, use "none" as rule_id. Do not invent requirements that are not
in the six rules.

DIFF:
<paste one fixture or proposed change here>
```
