# Codex adapter

Use the [generic prompt](generic.md) as the review contract. Add this instruction
when Codex has repository access:

```text
Inspect the changed path and only the minimal adjacent code needed to resolve
the policy. Do not edit files. Return the JSON contract without Markdown.
If a deterministic check exists for this policy, name it in evidence but do not
claim the check passed unless you ran it.
Return NEEDS_CONTEXT rather than APPROVE when the available context cannot
establish compliance.
```

Treat the response as a second review signal. The repository's lint, tests, and
path validation remain the enforcement layer.
