---
name: pipeline-experiments
description: Builds a short, ranked backlog of B2B SaaS pipeline experiments, each testing an ICP, audience, messaging, offer or motion hypothesis with a named pipeline metric, review date and kill rule. Use after a pipeline audit, or with the user's own findings, CRM export or goals. Triggers include "what experiments should we run", "pipeline experiment backlog", "plan next quarter's growth experiments", "90-day plan for {company}", "turn these findings into experiments", or "what would you run in your first 90 days".
---

# Pipeline experiments

Turn findings into 3 to 5 experiments that each test a strategic hypothesis and move a pipeline number. A short list the team will run beats a long list it will not.

## Load the method

- `${CLAUDE_PLUGIN_ROOT}/method/principles.md`
- `${CLAUDE_PLUGIN_ROOT}/method/profiles.md`
- `${CLAUDE_PLUGIN_ROOT}/method/scoring.md` (experiment format, what ranks low, sample size)
- `${CLAUDE_PLUGIN_ROOT}/method/plays.md` (play format: segment, personas, trigger, offer, if-then branches)
- `${CLAUDE_PLUGIN_ROOT}/method/evidence.md` (third-party evidence standard and starter library)
- `${CLAUDE_PLUGIN_ROOT}/method/layers.md` (for layer context)
- `${CLAUDE_PLUGIN_ROOT}/method/tools.md` (optional scripts kept outside the plugin, and the fallback for each; read when CRM data is supplied)

## Inputs

Use whichever exist, in this order of preference:
1. A pipeline audit from this conversation or a file produced by `pipeline-audit`.
2. Findings, goals or a CRM or analytics export the user supplies. Profile the export first (layers.md, "Reading CRM exports", with the optional `crm_profile.py` tool in tools.md if the user has it) before using any rate from an export as a baseline. If the user asks what to pull, give them the list in crm-reports.md.
3. A company URL alone: run a reduced profile and story-sync check first, or offer to run `pipeline-audit`.

Also ask, if not known: the pipeline goal for the period, the team available to run experiments (roles, not names), and any constraint (budget, no outbound, regulated industry).

## Workflow

1. **Restate the constraint.** Name the lowest-scoring upstream layer and the root causes from the findings. If ICP or measurement scores 0 or 1, the first experiment addresses it.
2. **Generate candidates.** For each top root cause, generate 2 to 3 candidate experiments across layers, starting with the highest upstream layer that is broken. Draw from the favored patterns in layers.md, adapted to the profile in profiles.md.
3. **Filter.** Remove candidates that only move inputs (clicks, opens, form fills), that need measurement that does not exist, or that overlap on the same audience in the same window.
4. **Build the play.** For each surviving candidate, write or reuse the play it tests (plays.md): segment, trigger, at least two personas, and "if this, then that" steps with an owner and stage on every branch.
5. **Back it with evidence.** Run the `evidence-researcher` agent, or follow evidence.md, to cite at least one verified, data-based third-party source for each play's mechanism, with its type label. Say "no third-party evidence found" when none exists.
6. **Write each survivor** in the experiment format from scoring.md. The hypothesis must name the audience, the message or offer, the motion, the pipeline metric, the window and the evidence.
7. **Rank and sequence.** Order by dependency, then impact over effort. Keep 3 to 5. Place the rest in a parking lot.
8. **Build the calendar.** A simple week-by-week view: start, leading-indicator check (week 2 to 3), review date, decision.
9. **Verify.** Run the `verifier` agent on the draft, or do its checks in a separate pass. Check every play has baseline, volume and capacity lines and a shape chosen from the findings, every hypothesis cites a finding, every play has two personas and a silent branch, every third-party citation was opened in this run or is a current library entry, every expected lift has low/mid/high reasoning from the company's own baseline, every experiment has a kill rule, and no number is invented.

## Output

Markdown, saved as `{company-slug}-pipeline-experiments-{YYYY-MM-DD}.md` unless the user names another location:

```
# Pipeline experiments: {Company}
{date} · based on {audit file or inputs}

## Constraint
## Plays
## Experiments (ranked)
## 90-day calendar
## Parking lot
## Prerequisites and data needed
## Sources and third-party evidence
```

For a hiring-manager or public context, also offer the three-row "first 90 days" table from the one-page teardown in outputs.md.

## Rules

- Each experiment has exactly one primary pipeline metric.
- Plan on the low case.
- Call results directional unless volumes support a statistical test.
- Draft any outreach copy for review; never send it.
