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

## Inputs

Collect, asking only for what is missing:

1. **Company** name and primary URL. Required.
2. **Scope**: the whole company, or one motion or business line (for example a self-serve store or an enterprise product).
3. **Output**: teardown, full report, or both. Default to both.
4. **Supplied data** (optional): CRM, analytics or ad exports, a sales deck, outbound samples, an earlier audit, or a connected `~~CRM` / `~~analytics` tool. Use only what the user provides in this run, and label it `supplied`.
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
Convert observations into findings using the format in scoring.md. Label each `observed`, `inferred`, `needs data` or `supplied`. Identify root causes.

### 4. Score layers
Score each layer with the anchors in layers.md, citing finding IDs. Score each layer on its own findings. Upstream gating sets the order of priorities, not the scores.

### 5. Prioritize
Group by root cause, score impact and effort, sequence by dependency, keep 3 to 5, park the rest. If measurement scores 0 or 1, the measurement fix is priority 1.

### 6. Design plays
Turn each priority into one play in the plays.md format: a list-able segment, a trigger, at least two personas (the one who feels the problem and the one who signs), and "if this, then that" steps that match the offer to each persona's readiness, with an owner and a pipeline stage on every branch.

### 7. Back plays with evidence
Run `evidence-researcher` on the drafted plays, or follow evidence.md directly. Each play gets at least one verified, data-based third-party citation for its mechanism, with its type label, or "no third-party evidence found". Never turn a benchmark into the company's expected lift.

### 8. Draft experiments
For each play, draft one experiment in the scoring.md format. For a fuller backlog, hand off to `pipeline-experiments`.

### 9. Verify
Second pass over every finding, play and citation:
- Re-open the source for each finding where possible. Drop or downgrade anything that does not hold.
- Recheck metadata findings (tags, form settings, link targets) against the raw file.
- Re-open each third-party citation and confirm the quote and year.
- Recompute every total and percentage.
- Check that no number is invented, and that the report still stands if `supplied` findings are removed.

### 10. Deliver
Write the outputs from outputs.md. Save to the user's working directory as `{company-slug}-pipeline-teardown-{YYYY-MM-DD}.md` and `{company-slug}-pipeline-audit-{YYYY-MM-DD}.md` unless the user names another location. In chat, give the constraint, the top priorities and the first play, then the file paths.

## Rules

- Strategy before tactics. Never lead with channels.
- No A/B tests or page tweaks as priorities unless a page blocks a pipeline play.
- Observe only: no form submissions, trials, purchases, account creation or contact with the company without explicit authorization.
- Supplied client data stays in this run's output. Never write it into the plugin directory or a public file.
