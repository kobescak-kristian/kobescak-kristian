# Operations practitioner turning business workflows into controlled AI-assisted systems

I build AI-assisted systems the way operations are run: the workflow logic stays deterministic, the model is given a narrow bounded role, and results are published as measured rather than as hoped.

Before this: Country Manager at Bolt (Malta and Cyprus). P&L ownership, regulatory engagement, Malta fleet scaled from 500 to 3,000 units (plus ~1,800 in Cyprus), 50+ staff.

## Featured systems

Independent repositories. They share a way of working, not a shared runtime.

| Repo | What it does |
|---|---|
| [ai-portfolio-sentinel](https://github.com/kobescak-kristian/ai-portfolio-sentinel) | **Portfolio flagship.** Scheduled monitor over my own public repositories: inventory derived live from the GitHub API, deterministic checks, a persistent finding ledger with dedup, and two judgment check classes handled by a caged single-tool agent. Read-only on everything it monitors, holding no credentials for them. Status: **in development toward production-ready** — the standing daily task still launches in stub mode and makes no model calls. |
| [ai-compliance-orchestrator](https://github.com/kobescak-kristian/ai-compliance-orchestrator) | Multi-jurisdiction iGaming compliance surveillance: one bounded checker agent per jurisdiction over a deterministic control plane, contract-enforced handoffs, an append-only adjudication ledger, and a human gate nothing in the system can bypass. The orchestration invariants passed in full; the detection layer failed its pre-committed precision gate (0.844 against a 0.95 threshold) and was published as-is. |
| [ai-claim-verification-agent](https://github.com/kobescak-kristian/ai-claim-verification-agent) | Bounded agent that checks a page's factual claims against source pages. Four read-only tools and nothing else, a 20-turn cap, a per-run cost ceiling, and a SQLite audit trail written before each tool result reaches the model. A synthetic evaluation over 12 cases / 35 claims is published, but the case-directory names exposed the expected outcome to the model, so its scores are not treated as blind accuracy evidence. |
| [ai-context-engine](https://github.com/kobescak-kristian/ai-context-engine) | Retrieval-grounded decision support: retrieved precedent, a validated decision with risk flags, and the full chain persisted for audit. Its keyed eval run scored 58/75 against a 69/75 threshold fixed before the run — reported as measured, with the miss pattern analyzed in the open. |
| [ai-execution-engine](https://github.com/kobescak-kristian/ai-execution-engine) | Deterministic CRM lead workflow: normalization across three source types, score-based routing into five named queues, full stage history per lead, and a bounded agent that reads the resulting metrics and proposes changes without modifying any workflow state. |
| [ai-impact-scoring-engine](https://github.com/kobescak-kristian/ai-impact-scoring-engine) | Attaches financial impact to lead-routing decisions, so threshold changes become cost decisions instead of guesses. Its figures come from a simulated 75-lead dataset built to produce both positive and negative outcomes. |

Also public: [ai-reliability-engine](https://github.com/kobescak-kristian/ai-reliability-engine) and [ai-decision-engine](https://github.com/kobescak-kristian/ai-decision-engine).

## How I work

- **Deterministic control plane, bounded model.** Ingestion, scoring, routing and dedup are plain code. Where a model is used, it gets a narrow read-only role with caps on tools, turns and cost, and it proposes rather than acts.
- **Threshold first, result either way.** Where a system has an eval gate, the threshold is committed before the run, and the outcome is published as recorded. Two systems here shipped with a failing gate and the analysis attached.
- **Claims traced back to source.** A claim about a system is re-derived from the repository it describes rather than from memory, and failed runs and limitations stay in the record instead of being edited out.

## Limitations

- Evaluation datasets in these repositories are labeled synthetic. The exception is the portfolio sentinel, whose scheduled runs read real public repository and CI evidence while its eval gate still runs on synthetic fixtures.
- No production or uptime claims. Most of these systems are demonstrated in single, human-initiated runs; the one built for unattended operation is still in development toward production-ready.
- Controls differ per repository. These are independent projects, not one governed platform, so what any given system actually enforces is what its own README and evaluation record show.

## Start here

Portfolio and case studies: [kobescak-kristian.github.io](https://kobescak-kristian.github.io)
