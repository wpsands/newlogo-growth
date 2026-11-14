---
name: pipeline-audit
description: Audits a B2B SaaS company's pipeline system from the outside in, from seed to enterprise. Works top-down through ICP, audiences, messaging, offers, motion and measurement, scores each layer, and ranks 3 to 5 priorities by pipeline effect. Produces a full report or a one-page pipeline teardown. Use when the user says "audit {company or URL}", "pipeline audit", "where is {company} leaking pipeline", "teardown of {company}", "GTM audit", "why isn't {company} generating pipeline", or wants a one-pager to send a hiring manager or founder.
---

# Pipeline audit

Audit a B2B SaaS company's ability to create new-logo pipeline. Work strategy first: ICP, audiences, messaging and offers before motion and channels. Every finding must cite evidence; every priority must name its pipeline effect.

## Load the method

Read these before starting and follow them throughout:

- `${CLAUDE_PLUGIN_ROOT}/method/principles.md` (beliefs, evidence guardrails, voice)
- `${CLAUDE_PLUGIN_ROOT}/method/profiles.md` (stage × motion profile)
- `${CLAUDE_PLUGIN_ROOT}/method/layers.md` (the six layers and their checks)
- `${CLAUDE_PLUGIN_ROOT}/method/scoring.md` (finding format, prioritization)
- `${CLAUDE_PLUGIN_ROOT}/method/outputs.md` (report and teardown templates)

## Inputs

Collect, asking only for what is missing:

1. **Company** name and primary URL. Required.
2. **Output**: full report (default) or one-page teardown.
3. **Supplied data** (optional): CRM export, analytics export, ad account export, sales deck, outbound samples, or a connected `~~CRM` / `~~analytics` tool. Without these, run outside-in and mark inside-out checks `needs data`.
4. **Context** (optional): the stated ICP or positioning, known competitors, and what the user already suspects.

Do not ask more than one round of questions. If the user gives only a URL, proceed outside-in with full-report output.

## Workflow

### 1. Profile
Gather enough public evidence to place the company on stage and motion (profiles.md). Sources: site, pricing, careers page, funding news, `~~enrichment` firmographics. State the profile with evidence. If below seed, say so and limit the output as profiles.md directs.

### 2. Collect evidence by layer
Work layers 1 to 6 in order, using the checks in layers.md. For each check, record raw observations with source and date before interpreting them.

Tools, by placeholder (see CONNECTORS.md):
- `~~web scraper` for site pages, pricing, careers, case studies, review sites
- `~~SEO tool` for organic keywords, paid search ads, competitors
- `~~enrichment` for customer and target firmographics
- `~~AI visibility`, or direct prompts, for what AI assistants say; 3+ runs per prompt, consensus only
- `~~CRM`, `~~analytics` only when connected or supplied as files

When a tool is unavailable, use web search and fetch, and note the reduced coverage in "What we could not see".

Large audits: run independent evidence collection for layers 1 to 3 and the competitor scan in parallel subagents when the environment supports it. Keep synthesis in the main thread.

### 3. Write findings
Convert observations into findings using the finding format in scoring.md. Label each `observed`, `inferred` or `needs data`. Identify root causes.

### 4. Score layers
Score each layer 0 to 3 with cited finding IDs. If an upstream layer scores 0 or 1, make fixing it the first priority and do not recommend downstream channel work that depends on it.

### 5. Prioritize
Group by root cause, score impact and effort, sequence by dependency, keep 3 to 5 priorities, park the rest.

### 6. Draft experiments
For each priority, draft one experiment in the experiment format from scoring.md. For a fuller backlog, hand off to the `pipeline-experiments` skill.

### 7. Verify
Run a second pass over every finding against its evidence. Re-open the source where possible. Drop or downgrade anything that does not hold. Check that no number is invented and every benchmark has a named source.

### 8. Deliver
Write the chosen output format from outputs.md. Save to the user's working directory as `{company-slug}-pipeline-audit-{YYYY-MM-DD}.md` (or `-teardown-` for the one-pager) unless the user names another location. Present the summary and top priorities in chat, then the file path.

## Rules

- Strategy before tactics. Never lead with channels.
- No A/B tests or page tweaks as priorities unless a page blocks a pipeline play.
- Observe only: no form submissions, trials, purchases, account creation or contact with the company without explicit authorization.
- Client data supplied by the user stays in this run's output. Never write it into the plugin directory.
