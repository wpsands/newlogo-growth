---
name: pipeline-audit
description: Audits a B2B SaaS company's pipeline system from public data, from seed to enterprise. Works top-down through ICP, audiences, messaging, offers, motion and measurement, scores each layer, ranks 3 to 5 priorities by pipeline effect, and turns each into a multi-step play (segment, personas, trigger, offer, if-then branches) backed by verified third-party research. Produces a one-page pipeline teardown and a full report. Use when the user says "audit {company or URL}", "pipeline audit", "where is {company} leaking pipeline", "teardown of {company}", "GTM audit", "why isn't {company} generating pipeline", or wants a one-pager to send a hiring manager or founder.
---

# Pipeline audit

Audit a B2B SaaS company's ability to create new-logo pipeline. Work strategy first: ICP, audiences, messaging and offers before motion and channels. Every finding cites evidence; every priority names its pipeline effect and ends in a play; every play cites third-party evidence for its mechanism.

Assume the user has only a company URL. The audit must stand on public evidence.

## Load the method

Read these before starting and follow them throughout:

- `${CLAUDE_PLUGIN_ROOT}/method/principles.md` (beliefs, evidence guardrails, voice)
- `${CLAUDE_PLUGIN_ROOT}/method/profiles.md` (stage × motion profile)
- `${CLAUDE_PLUGIN_ROOT}/method/layers.md` (the six layers, the ten story sync surfaces, public signals, layer scores)
- `${CLAUDE_PLUGIN_ROOT}/method/scoring.md` (finding format, prioritization, experiment format)
- `${CLAUDE_PLUGIN_ROOT}/method/plays.md` (play format and rules)
- `${CLAUDE_PLUGIN_ROOT}/method/evidence.md` (third-party evidence standard and starter library)
- `${CLAUDE_PLUGIN_ROOT}/method/outputs.md` (teardown and full report templates)
- `${CLAUDE_PLUGIN_ROOT}/method/crm-reports.md` (which CRM reports to ask for; read only when the user offers or asks about CRM data)
- `${CLAUDE_PLUGIN_ROOT}/method/tools.md` (optional scripts kept outside the plugin, and the fallback for each)

## Inputs

Collect, asking only for what is missing:

1. **Company** name and primary URL. Required.
2. **Scope**: the whole company, or one motion or business line (for example a self-serve store or an enterprise product).
3. **Output**: teardown, full report, or both. Default to both.
4. **Supplied data** (optional): CRM, analytics or ad exports, a sales deck, outbound samples, an earlier audit, or a connected `~~CRM` / `~~analytics` tool. Use only what the user provides in this run, and label it `supplied`. If the user offers CRM data or asks what to pull, give them the report list in crm-reports.md (four required reports, three optional, the rules for every report and the five questions for sales operations) before they export anything.
5. **Context** (optional): the stated ICP, known competitors, what the user already suspects.

Do not ask more than one round of questions. If the user gives only a URL, proceed with public data, whole company, both outputs.

## Workflow

### 0. Check coverage
Test each `~~` connector this run will use (CONNECTORS.md). Record which work and the exact error for any that fail. Write the coverage line for the top of the output now, so missing tools are stated up front and the affected findings are labeled `directional`.

### 1. Profile
Place the company on stage and motion (profiles.md) from the site, pricing, careers, funding news and `~~enrichment`. State the profile with evidence. If below seed, say so and limit the output as profiles.md directs.

### 2. Collect evidence
Run the three researchers in parallel when the environment supports subagents, each with its own notes file:
- `icp-offers-researcher` for layers 1, 2 and 4, plus the named-customer list and public signals
- `story-sync-researcher` for layer 3, the ten surfaces and competitors
- `motion-measurement-researcher` for layers 5 and 6

Without subagents, work the same checks in layer order. Either way, record raw observations with source and date before interpreting them, and look for a public signal (layers.md) before marking anything `needs data`.

### 3. Write findings
Convert observations into findings using the format in scoring.md. Label each `observed`, `inferred`, `needs data` or `supplied`. Identify root causes. Give every finding a size with counts, or "not sized" (scoring.md). Put counts beside every rate and treat rates under the minimum sample as `directional`. If CRM exports are supplied, profile them first (the optional `crm_profile.py` tool in tools.md if the user has it) and work through the checks in layers.md ("Reading CRM exports") before computing any rate; state the analysis window and team scope on every `supplied` finding. Record what changed in the last 12 months (layers.md).

### 4. Score layers
Score each layer with the anchors in layers.md, citing finding IDs. Score each layer on its own findings. Upstream gating sets the order of priorities, not the scores.

### 5. Prioritize
Group by root cause, score impact against the anchors in scoring.md with the size stated, score effort, sequence by dependency, keep 3 to 5, park the rest. If measurement scores 0 or 1, the measurement fix is priority 1; it blocks the plays only when no usable baseline exists. Before naming the constraint, say what evidence would have pointed to a different one (principles.md, "Earn the diagnosis").

### 6. Design plays
Turn each of the top three priorities into a full play in the plays.md format (priorities four and five get one line each; internal fixes use the fix format): a list-able segment, a trigger, at least two personas (the one who feels the problem and the one who signs), and "if this, then that" steps that match the offer to each persona's readiness, with an owner and a pipeline stage on every branch. Pick each play's shape from the findings (plays.md, Shapes), check the company is not already running it, and add the baseline, volume and capacity lines. Then write the play assets for the first play: the list filter, a first-touch draft, the offer outline, and a worked sample for up to three accounts when public data allows.

### 7. Back plays with evidence
Run `evidence-researcher` on the drafted plays, or follow evidence.md directly. Each play gets at least one verified, data-based third-party citation for its mechanism, with its type label, or "no third-party evidence found". Never turn a benchmark into the company's expected lift.

### 8. Add the test
Give each full play its test block (plays.md). In the audit, the test block is the experiment; there is no separate experiments section. For a fuller backlog with complete experiment tables and a 90-day calendar, hand off to `pipeline-experiments`.

### 9. Verify
Run the `verifier` agent on the draft. Give it the draft, the raw captures folder and the paths of any supplied data files. Do not give it the researchers' notes or your analysis scripts. Fix everything it lists under Must fix, and fix or label everything under Should fix. Without subagents, do the same checks yourself in a separate pass, writing new checks instead of rereading the old ones. The check covers:
- Re-open the source for each finding where possible. Drop or downgrade anything that does not hold.
- Recheck metadata findings (tags, form settings, link targets) against the raw file.
- Re-open each third-party citation and confirm the quote and year.
- Recompute every total and percentage.
- For `supplied` CRM findings, confirm that every rate uses the stated window and team scope, that no comparison mixes exports whose totals differ, and that each claimed field or record problem survives the report's own filters.
- For each play, confirm the shape was chosen from the findings, the volume line shows a readable test or says pilot, the capacity line is present, and no timing or number was copied from plays.md.
- Confirm the constraint is earned by this company's evidence.
- Check that no number is invented, and that the report still stands if `supplied` findings are removed.

### 10. Deliver
Write the outputs from outputs.md. Save to the user's working directory as `{company-slug}-pipeline-teardown-{YYYY-MM-DD}.md` and `{company-slug}-pipeline-audit-{YYYY-MM-DD}.md` unless the user names another location. In chat, give the constraint, the top priorities and the first play, then the file paths.

## Rules

- Strategy before tactics. Never lead with channels.
- No A/B tests or page tweaks as priorities unless a page blocks a pipeline play.
- Observe only: no form submissions, trials, purchases, account creation or contact with the company without explicit authorization.
- Supplied client data stays in this run's output. Never write it into the plugin directory or a public file.
