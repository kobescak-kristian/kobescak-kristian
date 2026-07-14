# AI systems with inspectable controls

I build AI systems the way regulated operations are run: eval gates committed to git before the code, audit trails on every run, failures published instead of scrubbed.

Before this: Country Manager at Bolt (Malta and Cyprus). P&L ownership, regulatory engagement, Malta fleet scaled from 500 to 3,000 units (plus ~1,800 in Cyprus), 50+ staff.

## The portfolio

One decision pipeline, five public engines, one bounded agent, one multi-agent orchestrator:

| Repo | What it does |
|---|---|
| [ai-reliability-engine](https://github.com/kobescak-kristian/ai-reliability-engine) | **Flagship.** Blocks invalid AI outputs before they trigger business actions. Committed eval run: 51 records in, 7 failures caught, 0 invalid outputs downstream. |
| [ai-decision-engine](https://github.com/kobescak-kristian/ai-decision-engine) | Tracks outcomes and scores decision correctness over time. |
| [ai-impact-scoring-engine](https://github.com/kobescak-kristian/ai-impact-scoring-engine) | Attaches financial impact to decisions so threshold changes are cost decisions, not guesses. |
| [ai-execution-engine](https://github.com/kobescak-kristian/ai-execution-engine) | Runs the workflow: five queues, deterministic checks, inspectable step by step. |
| [ai-context-engine](https://github.com/kobescak-kristian/ai-context-engine) | Grounds decisions in retrieved precedent and cites sources. Its keyed eval run failed the pre-committed gate and shipped with the failure analyzed in the open. |
| [ai-claim-verification-agent](https://github.com/kobescak-kristian/ai-claim-verification-agent) | Bounded agent: tool whitelist, turn cap, cost ceiling, SQLite audit trail. Shipped only after passing a pre-committed eval gate. |
| [ai-compliance-orchestrator](https://github.com/kobescak-kristian/ai-compliance-orchestrator) | Orchestration: bounded checker agents fanning out over a deterministic control plane, contract-enforced handoffs, full audit trail, and a human gate nothing can bypass. Its detection layer failed the pre-committed eval gate — published as-is. |

Also public from day one: [ai-portfolio-sentinel](https://github.com/kobescak-kristian/ai-portfolio-sentinel) — a scheduled monitor over this portfolio, built fully in the open. Every decision and phase gate is in the git history from the first commit; it enters the table above only when its pre-committed eval gate passes.

## How I work

- Eval thresholds are committed before the first line of system code. Results are recorded pass or fail.
- Every repo validates its own documentation with a pre-push hook and carries code-verified architecture decision records.
- A second model re-derives every claim from a fresh public clone before anything is called done. Self-report is never the final word.

## Honest limitation

All eval data is labeled synthetic. These systems demonstrate the governance pattern; no production or uptime claims are made anywhere in this portfolio.

## Start here

Portfolio and case studies: [kobescak-kristian.github.io](https://kobescak-kristian.github.io)
