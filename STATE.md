# STATE — kobescak-kristian

**Classification:** PROJECT · T0 (public GitHub profile repository — `AGENTS.md` states this explicitly: "a public signal surface, not an application or executable system"; `domains/github-ops/CONVENTIONS.md` PROJECT/SYSTEM/EXPERIMENT taxonomy).

**RECONSTRUCTED** (GOVERNANCE.md Build-repo STATE rule, clause 7): derived from git history at scaffold time (2026-09-19, Q-72(f)), not written contemporaneously. Reconstructed entries are retrospective evidence, not contemporaneous record — the commit that adds this file begins the contemporaneous record going forward.

## Current state

`README.md` (the rendered GitHub profile page) currently lists the five public engines, `ai-claim-verification-agent`, and `ai-compliance-orchestrator` in "The portfolio" table, with `ai-portfolio-sentinel` named as public-from-day-one but not yet table-listed (pending its own eval gate). No decision record exists — this repo has no `adr/` or `decisions/` directory; its content is profile prose, not an executable system requiring architectural decisions.

## Build history (from `git log --reverse`, oldest → newest — almost entirely README revisions)

- **2026-04-05** (`fec1449` + 3 same-day README updates) — Initial profile commit and early wording passes.
- **2026-04-22** (`a4572ed` + 3 same-day updates) — Reliability engine and P5 added to "What I build."
- **2026-04-24** (`97eb07d`, `4cda2f2`) — README revised to reflect current AI-systems focus; stack section clarified.
- **2026-06-15** (`01aa5e9`, `ac24a48`) — Upwork link updated; clarity bullet points added.
- **2026-06-16** (`1ddd91a`) — Featured links repointed to canonical repo names.
- **2026-06-18** (`e8a059d`, `3b1033a`, `7dc0ca2`, `cacdc7e`) — Engine names standardized; profile reframed around the five-engine system; Upwork link removed.
- **2026-07-06** (`4370e9e`) — Portfolio link fixed to point at ai-reliability-engine (flagship).
- **2026-07-13** (`0b0da3e`) — README aligned with governance positioning; agent card added.
- **2026-07-14** (`1496267`, `17e2a31`) — ai-compliance-orchestrator added to the portfolio table; ai-portfolio-sentinel build-in-the-open line added.
- **2026-07-24** (`b3e0139`) — Canonical pre-commit local-path guard added (Q-48 wave 1).
- **2026-08-03** (`f6c137d`) — Publish-gate coverage canary added.
- **2026-08-04** (`3f8cc5f`, `c649a59`) — Apache-2.0 license added; Q-35 pre-push hook installed with the validator call left disabled ("no validator yet" — accurate at the time, no local validator file existed until the next entry).
- **2026-09-16** (`623ff54`) — Canonical AGENTS.md router adopted (Q-93); this is also when `.githooks/validate_artifacts.py` was first added to this repo — the pre-push comment from `c649a59` was not revisited at that point.
- **2026-09-19** (this commit) — Q-72(f): STATE.md added (this file); validator gains a STATE.md-existence check; the pre-push validator call, dormant since before the validator file existed, is enabled (see the validator-convergence commit for verification detail).

## Open loops

None specific to this repository beyond the hook-wiring completion recorded above.
