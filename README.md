# Operations practitioner turning business workflows into controlled AI-assisted systems

I build AI-assisted systems the way operations are run: the workflow logic stays deterministic, the model is given a narrow bounded role, and results are published as measured rather than as hoped.

Before this: Country Manager at Bolt (Malta and Cyprus). P&L ownership, regulatory engagement, Malta fleet scaled from 500 to 3,000 units (plus ~1,800 in Cyprus), 50+ staff.

## Featured systems

Independent repositories. They share a way of working, not a shared runtime.

| Repo | What it does |
|---|---|
| [ai-compliance-orchestrator](https://github.com/kobescak-kristian/ai-compliance-orchestrator) | **Portfolio flagship.** Multi-jurisdiction iGaming compliance surveillance: one bounded checker agent per jurisdiction over a deterministic control plane, contract-enforced handoffs, an append-only adjudication ledger, and a human gate nothing in the system can bypass. Latest official evaluation: passed gate v2.1 on a private test set, with 29 of 30 synthetic scenarios passed in all 3 runs and 52 of 52 deterministic checks passed. |
| [ai-portfolio-sentinel](https://github.com/kobescak-kristian/ai-portfolio-sentinel) | Scheduled monitor over my own public repositories: inventory derived live from the GitHub API, deterministic checks, a persistent finding ledger with dedup, and two judgment check classes handled by a caged single-tool agent. Read-only on everything it monitors, holding no credentials for them. Status: **in development toward production-ready**; scheduled runs are paused during qualification for unattended operation. |
| [ai-claim-verification-agent](https://github.com/kobescak-kristian/ai-claim-verification-agent) | Bounded agent that checks a page's factual claims against source pages. Four read-only tools and nothing else, a 20-turn cap, a per-run cost ceiling, and a SQLite audit trail written before each tool result reaches the model. On a synthetic evaluation of 12 cases / 35 claims, run with neutral case names, it scored precision 1.00 / recall 1.00 (35/35), as did its [LangGraph port](https://github.com/kobescak-kristian/ai-claim-verification-langgraph). |
| [ai-context-engine](https://github.com/kobescak-kristian/ai-context-engine) | Retrieval-grounded decision support: retrieved precedent, a validated decision with risk flags, and the full chain persisted for audit. Its keyed eval run scored 58/75 against a 69/75 threshold fixed before the run, with the miss pattern analyzed in its evaluation record. |
| [ai-execution-engine](https://github.com/kobescak-kristian/ai-execution-engine) | Deterministic CRM lead workflow: normalization across three source types, score-based routing into five named queues, full stage history per lead, and a bounded agent that reads the resulting metrics and proposes changes without modifying any workflow state. |
| [ai-impact-scoring-engine](https://github.com/kobescak-kristian/ai-impact-scoring-engine) | Attaches financial impact to lead-routing decisions, so threshold changes become cost decisions instead of guesses. Its figures come from a simulated 75-lead dataset built to produce both positive and negative outcomes. |

Also public: [ai-reliability-engine](https://github.com/kobescak-kristian/ai-reliability-engine) and [ai-decision-engine](https://github.com/kobescak-kristian/ai-decision-engine).

## Workflow automations (n8n)

Business workflows built in n8n. Each repository holds the workflow files, the visible test cases and a results record. Tests use made-up data on a local n8n, not live traffic.

| Repo | What it does |
|---|---|
| [n8n-ai-lead-qualifier](https://github.com/kobescak-kristian/n8n-ai-lead-qualifier) | Scores every new lead with Claude, sends clear good fits to HubSpot, and asks a person in Slack before anything uncertain reaches the CRM or a prospect's inbox. Final test: 88 of 89 AI-scored leads routed as expected in all 3 runs, and no reply sent without a person's approval. |
| [n8n-ai-output-guard](https://github.com/kobescak-kristian/n8n-ai-output-guard) | Reusable sub-workflow that checks every AI answer before the workflow uses it: schema check, one retry, a fallback, and a person in Slack for anything still invalid. On a broken claims workflow it took crashes from 26 to 0 and bad rows saved from 42 to 0 in each of 3 gated runs. It checks format, not truth. |
| [n8n-ai-support-bot](https://github.com/kobescak-kristian/n8n-ai-support-bot) | Answers customers only from the business's own help articles, checks every price, number, e-mail and link in code before sending, and hands off to a person in Slack. 3 runs of 235 made-up conversations: 0 critical failures, 131 of 133 normal questions right in all 3 runs. |
| [n8n-data-sync](https://github.com/kobescak-kristian/n8n-data-sync) | WooCommerce orders into HubSpot with no AI step: every field checked before any write, no duplicate contacts or deals, and orders it cannot sync sent to a person in Slack with a replay step (the exceptions are listed in its README). 110 of 110 test cases right in each of 3 runs. |

## How I work

- **Deterministic control plane, bounded model.** In the Python systems, ingestion, scoring, routing and dedup are plain code, and a model gets a narrow read-only role with caps on tools, turns and cost, and proposes rather than acts. In the n8n workflows that use AI the model does more, so code checks its output and anything uncertain goes to a person.
- **Threshold first, result either way.** Where a system has an eval gate, the threshold is committed before the run, and the outcome is published as recorded, with the results record attached.
- **Claims traced back to source.** A claim about a system is re-derived from the repository it describes rather than from memory, and failed runs and limitations stay in the record instead of being edited out.

## Limitations

- Evaluation datasets in these repositories are labeled synthetic. The exception is the portfolio sentinel, whose scheduled runs use real public repository and CI evidence while its eval gate runs on synthetic fixtures.
- No production or uptime claims. Most of these systems are demonstrated in human-initiated test runs; the one built for unattended operation is still in development toward production-ready.
- Controls differ per repository. These are independent projects, not one governed platform, so what any given system actually enforces is what its own README and evaluation record show.

## Start here

Portfolio and case studies: [kobescak-kristian.github.io](https://kobescak-kristian.github.io)
