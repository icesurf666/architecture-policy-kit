#!/usr/bin/env python3
"""Validate public policy-kit assets without third-party dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "eval/cases.jsonl"
POLICY_PATH = ROOT / "examples/progresscut/policy.yaml"
FIXTURE_HEADER = re.compile(r"^# Expected: (APPROVE|BLOCK) / ([a-z0-9-]+|none)$")
POLICY_ID = re.compile(r"^  - id: ([a-z][a-z0-9-]*)$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")


def load_cases() -> list[dict[str, object]]:
    cases = [
        json.loads(line)
        for line in CASES_PATH.read_text().splitlines()
        if line.strip()
    ]
    assert cases, "evaluation set is empty"
    assert len({case["id"] for case in cases}) == len(cases), "duplicate case id"
    return cases


def policy_ids() -> set[str]:
    ids = set(POLICY_ID.findall(POLICY_PATH.read_text()))
    assert ids, "sample policy has no policy IDs"
    return ids


def validate_case(case: dict[str, object], known_policy_ids: set[str]) -> None:
    case_id = str(case["id"])
    decision = case.get("decision")
    policy_id = case.get("policy_id")
    fixture_path = ROOT / str(case.get("fixture"))

    assert decision in {"APPROVE", "BLOCK"}, f"{case_id}: invalid decision"
    assert isinstance(policy_id, str) and policy_id, f"{case_id}: missing policy ID"
    assert case.get("evidence_any_of"), f"{case_id}: missing evidence token"
    assert fixture_path.is_file(), f"{case_id}: fixture does not exist"
    assert policy_id == "none" or policy_id in known_policy_ids, (
        f"{case_id}: unknown policy ID {policy_id}"
    )

    header = fixture_path.read_text().splitlines()[0]
    match = FIXTURE_HEADER.fullmatch(header)
    assert match, f"{case_id}: malformed fixture header"
    assert match.group(1) == decision, f"{case_id}: fixture decision disagrees"
    assert match.group(2) == policy_id, f"{case_id}: fixture policy disagrees"


def validate_markdown_links() -> None:
    for markdown in ROOT.rglob("*.md"):
        for target in MARKDOWN_LINK.findall(markdown.read_text()):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            assert (markdown.parent / target).resolve().exists(), (
                f"{markdown.relative_to(ROOT)}: missing {target}"
            )


def main() -> None:
    for schema_path in (
        ROOT / "policy/schema.json",
        ROOT / "eval/review-response.schema.json",
    ):
        json.loads(schema_path.read_text())

    known_policy_ids = policy_ids()
    cases = load_cases()
    for case in cases:
        validate_case(case, known_policy_ids)
    validate_markdown_links()

    print(
        f"validated {len(cases)} cases, {len(known_policy_ids)} policies, "
        "2 JSON schemas, and local Markdown links"
    )


if __name__ == "__main__":
    main()
