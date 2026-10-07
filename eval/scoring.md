# Scoring a policy reviewer

Score policy review as separate signals. A single “review passed” number hides
the failure mode that matters to a team.

## Per-case fields

| Field | Check |
| --- | --- |
| Verdict | Does `APPROVE` or `BLOCK` match the expected decision? |
| Policy | Does the returned policy ID match the expected policy, or `none` for approval? |
| Schema | Did the response parse and include every required field? |
| Evidence | Does the response contain at least one expected code token or an equivalent reviewed manually? |

Do not let a long explanation substitute for a correct verdict. Do not count a
valid JSON object as grounded evidence without checking it against the diff.

## Report both error types

```text
false accept = unsafe change approved
false block  = safe change rejected
```

Teams feel false blocks immediately: a reviewer that produces noisy “critical”
comments is ignored. False accepts are quieter and need adversarial fixtures to
surface. Keep both numbers in the report.

## Keep a holdout set

The fixtures under `examples/` are public and answer-labelled. Use them to
develop a policy, not to claim a production score. Keep several near-miss cases
private, run them before changing a prompt or model, and record the exact policy
version used for the run.
