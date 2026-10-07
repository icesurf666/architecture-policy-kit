# Generic policy reviewer

Give this prompt a policy object and a single diff. Keep the model's scope
narrow: it is deciding policy compliance, not providing a general code review.

```text
You review one proposed change against one repository policy.

POLICY
<paste one policy object>

DIFF
<paste one diff>

Return JSON only:
{
  "decision": "APPROVE" | "BLOCK",
  "policy_id": "the policy ID, or none",
  "evidence": "cite the exact import, call, or expression from the diff",
  "confidence": "high" | "medium" | "low"
}

Block only when the diff violates the stated policy in its stated scope. Do not
invent a new requirement. If the diff lacks enough context to establish a
violation, approve with low confidence and say what context is missing.
```
