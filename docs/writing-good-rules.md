# Writing a rule worth enforcing

Start from a failure you can describe without saying “clean architecture.”

Bad:

```text
Keep the domain clean.
```

Useful:

```text
packages/domain must not import a database client, validation library, or UI package.
Reason: domain types are used by the CLI, desktop processes, and tests without an adapter runtime.
```

For every policy, write five things:

1. **Scope** — which paths does it apply to?
2. **Boundary** — what is allowed and forbidden?
3. **Reason** — which concrete failure does it prevent?
4. **Counterexample** — what looks similar but should be allowed?
5. **Enforcement** — can lint, a test, or an LLM check it?

If you cannot name a counterexample, the policy is probably too vague for a
reviewer. If you cannot name a failure, it may be preference rather than policy.
