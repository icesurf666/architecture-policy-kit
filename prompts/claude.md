# Claude adapter

Use the [generic prompt](generic.md) as the review contract. Add this instruction
when Claude has repository access:

```text
Read only files needed to resolve the policy scope and the symbols in the diff.
Do not expand the task into a full refactor or comment on unrelated style.
Before answering, verify that the policy scope matches the changed path.
```

Validate the returned JSON before consuming it in CI or an automation. A model
may reach the right verdict and still produce an unusable structured response.
