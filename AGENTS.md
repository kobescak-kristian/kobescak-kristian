# AGENTS.md — kobescak-kristian

Tool-neutral context router for coding agents working in this repository.
It points to where repository truth lives. It is not profile copy, not
evidence for any claim the profile makes, and not a record of any claim's
current value: cite the source it routes to, never this file.

## Repository purpose

`kobescak-kristian` is Kristian Kobescak's public GitHub profile
repository. Its `README.md` is rendered on the GitHub profile page and is
the public product of this repository: a public signal surface, not an
application or executable system. Its purpose is profile publication
rather than application execution.

The README summarizes the current portfolio positioning, links to the
public repositories, selected evidence-backed technical claims about
those repositories, operating and career background, the stated
limitations of the portfolio, and the recommended starting point for
deeper review.

Everything mutable about the profile lives in `README.md` or in the
public repositories it cites, and is deliberately not restated here:
which repositories are listed, which one is flagship, metrics and
evaluation figures, role and work-history wording, staff and fleet
figures, dates, the status of any monitored repository, and the current
positioning language.

## Authority and conflict handling

| Question | Canonical source |
|---|---|
| What the profile publicly says: positioning, portfolio links, displayed technical claims, work-history and profile claims, limitation language, the "start here" link | `README.md` |
| The technical fact behind a repository or system claim displayed in the README | the linked public source repository |
| Deeper portfolio and case-study presentation, where the README links there | the public portfolio site linked from `README.md`; it does not override the technical source repositories |
| Licence terms | `LICENSE` |
| Machine-local absolute path guard at write time | `.githooks/pre-commit` |
| Push freshness guard | `.githooks/pre-push` |
| Artifact validation | `.githooks/validate_artifacts.py` |

When sources disagree:

- `README.md` owns what this profile publicly says.
- The linked public source repository owns the technical facts claimed
  about that system.
- The portfolio site may carry a richer narrative but never supersedes
  source-repository evidence.
- If the README disagrees with technical source evidence, the README is
  stale or incorrect. Never alter source evidence to rescue profile prose.
- Work-history and profile claims are a separate evidence class from
  repository-backed technical claims; do not treat one as proof of the
  other.
- Surface a material disagreement rather than silently reconciling it.
  If the requested work depends on unresolved evidence, stop for owner
  review.

## Task routing

These are starting points, not exhaustive reading lists.

| Task class | Start here |
|---|---|
| Profile positioning, visible GitHub profile content | `README.md` |
| Portfolio repository list, displayed technical claims | `README.md` together with the linked public source repositories |
| Evidence for a technical repository claim | the relevant linked public repository |
| Deeper portfolio or case-study presentation | the public portfolio-site link in `README.md` |
| Career or operating-background wording | `README.md` |
| Portfolio limitations | `README.md` |
| Licence | `LICENSE` |
| Machine-local path protection | `.githooks/pre-commit` |
| Push freshness | `.githooks/pre-push` |
| Artifact validation | `.githooks/validate_artifacts.py` |

## Always-on constraints

- The README is the public product of this repository. `AGENTS.md` and
  `CLAUDE.md` are working guidance, never profile copy or evidence.
- Technical claims require public source evidence. Any statement about
  what a portfolio repository or system does or achieved must remain
  supportable from the relevant public source repository. Do not invent,
  approximate, inflate or round a claim because it improves positioning.
- README and source repositories have different authority. The README
  owns what the profile says; the linked source repository owns the
  underlying technical fact. When they disagree, the profile claim is
  stale or wrong. Do not modify source evidence to rescue README wording.
- Claim-changing edits require re-verification. Before changing a
  factual system or repository claim in the README, re-derive it from the
  current authoritative public source, not from memory and not from an
  earlier profile value.
- Career claims are a different evidence class. Do not present operating
  or work-history prose as repository-verified technical evidence, and
  keep that distinction explicit when reviewing or editing profile
  content.
- Limitations are never silently removed. Do not sanitize a recorded
  limitation or failed evaluation to make the profile stronger. A claim
  becomes stronger only when new evidence supports it.
- No unrelated profile refresh. A narrow task does not authorize
  refreshing repository lists, metrics, role wording, links, positioning
  or other README copy. Stale content found incidentally is a finding to
  report, not permission to edit.
- Full publication gate before every push. This is a public signal
  repository: every push runs the full repository publish gate against
  the final staged diff. If an in-window fix changes the staged
  publication diff, rerun the gate. A scoped scan is not a substitute.
- No private material. Do not newly publish credentials, private
  operational material, private internal documentation or decision
  material, machine-local absolute paths or non-public repository
  details. A publication allowlist is an explicit exception surface, not
  a bypass: do not create or broaden one merely to make a new leak pass.
  Revise the public text instead unless an explicit owner ruling
  authorizes an exact exception.
- Public links must remain publicly resolvable. When a task changes a
  public link or repository reference, verify it unauthenticated before
  publication.
- Never rewrite pushed history. Public evidence and links may depend on
  stable hashes. No amend, rebase or force-push of already-pushed
  commits.
- This is a profile repository, not an engine repository. Do not impose
  engine-specific README sections, evaluation structure, architecture
  documents, tests or build tooling to make it resemble one.
- Documentation-standard gaps are not self-authorizing. If artifact
  policy and this repository's current structure disagree, surface the
  mismatch. Do not create unrelated artifacts to make a validator pass
  unless the owning task authorizes them; decision-record requirements
  and broader fleet convergence are not solved by a narrow task here.
- `AGENTS.md` is guidance, not enforcement. The git guards, the
  publication-gate tooling, source verification and public-state checks
  remain the enforcement.

## Verification

Verification must use repository surfaces that actually exist for the
task; never fabricate a test, build or CI result.

Routine, safe, bounded checks:

```bash
python .githooks/validate_artifacts.py .
git diff --check
```

For publication-affecting work, additionally:

- the full repository publish gate against the final staged diff, rerun
  after any in-window fix;
- post-push public verification appropriate to the changed surface: the
  pushed files are publicly readable, changed links resolve
  unauthenticated, and the GitHub profile page still renders. When the
  README is unchanged, confirm profile health only; do not claim a
  profile-content update that did not happen.
