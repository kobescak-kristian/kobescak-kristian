#!/usr/bin/env python3
"""Validate the staged profile-compatible ARTIFACT_STANDARD v2.7 checks.

This variant requires the repository surfaces appropriate to the profile
retrofit without importing unrelated fleet-convergence requirements. It
is not the canonical fleet validator; broader convergence is separate
work.

Exit 1 = violations printed. Exit 0 = "Tier 0: PASS".
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

# Legacy eight-name list, unexpanded on purpose: expanding it is fleet
# convergence work, not part of this staged variant.
BANNED_WITHOUT_TRIGGER = ["SYSTEM_WALKTHROUGH.md", "CHANGELOG.md", "RUNBOOK.md",
                          "PRODUCTION_READINESS.md", "THREAT_MODEL.md", "MONITORING.md",
                          "INCIDENT_RESPONSE.md", "TEST_MATRIX.md"]
errors = []

# README: required to exist. Engine section headings are not required and
# profile content is not inspected: the README is mutable public profile
# copy, and artifact validation must not become a profile rewrite.
readme = ROOT / "README.md"
if not readme.exists():
    errors.append("README.md missing")

# AGENTS.md (ARTIFACT_STANDARD v2.7, Tier 0): root file + required H2
# headings. Match is case-insensitive; "&" is accepted for "and". The
# optional "## Repository landmarks" section is not checked.
AGENTS_REQUIRED_HEADINGS = ["Repository purpose", "Authority and conflict handling",
                            "Task routing", "Always-on constraints", "Verification"]
agents = ROOT / "AGENTS.md"
if not agents.exists():
    errors.append("AGENTS.md missing (ARTIFACT_STANDARD v2.7 Tier 0)")
else:
    agents_text = agents.read_text(encoding="utf-8")
    for heading in AGENTS_REQUIRED_HEADINGS:
        words = [r"(?:and|&)" if w == "and" else re.escape(w) for w in heading.split()]
        pattern = r"^##\s+" + r"\s+".join(words) + r"\s*$"
        if not re.search(pattern, agents_text, re.I | re.M):
            errors.append(f"AGENTS.md missing section: ## {heading}")

# Decision-record folder existence is deliberately not enforced by this
# staged profile-compatible variant. The folders are located only so that
# the trigger-gated artifact check below can validate a citation if one
# exists.
decision_dirs = [d for d in (ROOT / "adr", ROOT / "decisions") if d.is_dir()]
decision_records = [f for d in decision_dirs for f in d.glob("*.md")
                    if "template" not in f.name.lower()]

# Trigger-gated artifacts: none is required, and none may appear silently.
# If one exists, a decision-record folder must exist and at least one
# non-template record must cite the file name as its trigger.
for banned in BANNED_WITHOUT_TRIGGER:
    if not (ROOT / banned).exists():
        continue
    if not decision_dirs:
        errors.append(f"{banned} exists but no adr/ (or decisions/) folder records its trigger")
        continue
    justified = any(re.search(re.escape(banned), f.read_text(encoding="utf-8"))
                    for f in decision_records)
    if not justified:
        errors.append(f"{banned} exists without a non-template decision record citing its trigger")

if errors:
    print("ARTIFACT_STANDARD violations:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("Tier 0: PASS")
