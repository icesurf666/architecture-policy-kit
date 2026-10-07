# Scoring a policy reviewer

Score policy review as separate signals. A single “review passed” number hides
the failure mode that matters to a team.

## Per-case fields

| Field | Check |
| --- | --- |
| Verdict | Does `APPROVE` or `BLOCK` match the expected decision? |
| Policy | Does the returned policy ID match the expected policy, or `none` for approval? |
| Schema | Does the response validate against [`review-response.schema.json`](review-response.schema.json)? |
| Evidence | Does the response contain at least one expected code token or an equivalent reviewed manually? |

Do not let a long explanation substitute for a correct verdict. Do not count a
valid JSON object as grounded evidence without checking it against the diff.

## Do not fail open on missing context

The review contract has three outcomes in production:

```text
APPROVE       enough context; policy is satisfied
BLOCK         enough context; policy is violated
NEEDS_CONTEXT the reviewer cannot establish either result safely
```

Route `NEEDS_CONTEXT` to a human or request the named file/symbol. Track its
rate separately: it is not a false accept, but a high rate means the policy or
review integration is under-specified. The public fixtures intentionally carry
enough context for a binary result; `NEEDS_CONTEXT` on one is unresolved, not a
correct verdict.

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
