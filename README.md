# New Logo Growth

A Claude Code plugin for new-logo pipeline in B2B SaaS. It audits a company's pipeline system and ranks the few experiments most likely to grow it. It covers companies from seed to enterprise.

It works top-down. ICP, audiences, messaging and offers come first; channels are chosen last, as a consequence. Every finding cites its evidence. Every priority becomes a play: a segment, a trigger, two or more personas, and "if this, then that" steps that match the offer to each persona's readiness. Every play cites verified third-party research (analyst, consultancy, academic or public data) for why its mechanism works, and every experiment names the pipeline number it should move, a review date and a kill rule. A/B tests and landing-page tweaks rank low unless a page is blocking a pipeline play.

It is built to run from a company URL alone. Public signals such as job posts, page source, review-site profiles and category records stand in for private data, and anything you supply is labeled as such.

## Skills

| Skill | Ask it | You get |
|---|---|---|
| `pipeline-audit` | "Audit outreach.io" or "One-page teardown of outreach.io" | A one-page teardown and a full report: layer scores, cited findings, 3 to 5 priorities, one play per priority with third-party evidence, draft experiments. |
| `pipeline-experiments` | "What should Acme run next quarter?" | Plays and a ranked backlog of 3 to 5 pipeline experiments, with evidence and a 90-day calendar. |

Both follow the method in [`method/`](method/):

- [`principles.md`](method/principles.md): beliefs, evidence guardrails, voice
- [`profiles.md`](method/profiles.md): stage × motion profiles
- [`layers.md`](method/layers.md): the six layers and their checks
- [`scoring.md`](method/scoring.md): finding and experiment formats, prioritization
- [`plays.md`](method/plays.md): the play format, combining segments, personas, triggers and offers
- [`evidence.md`](method/evidence.md): the third-party evidence standard and a starter library of verified sources
- [`outputs.md`](method/outputs.md): report and teardown templates
- [`crm-reports.md`](method/crm-reports.md): which CRM reports to pull, with fields and filters, if you want to add your own data

## Agents

The audit runs four research agents, in parallel where the environment allows: `icp-offers-researcher`, `story-sync-researcher`, `motion-measurement-researcher` and `evidence-researcher`. A fifth, `verifier`, checks the draft independently before delivery: it works from the raw evidence without the analysis notes and tests the method behind each number. They live in [`agents/`](agents/).

## Scripts

- [`scripts/ai_probe.py`](scripts/ai_probe.py) asks AI assistants buyer questions and records whether the company appears.
- [`scripts/crm_profile.py`](scripts/crm_profile.py) profiles CRM opportunity exports: what each file holds, whether the files agree, where the closed definition changed, and win rates by team, segment, source and partner inside one consistent window, with counts and intervals.

Both use the Python standard library only.

## Install

In Claude Code:

```
/plugin marketplace add wpsands/newlogo-growth
/plugin install newlogo-growth@newlogo-growth
```

Or clone the repo and load it locally:

```bash
git clone https://github.com/wpsands/newlogo-growth
claude --plugin-dir ./newlogo-growth
```

## Data

Only a company URL is required. Connect SEO, enrichment, AI-visibility, CRM or analytics tools for better coverage; see [CONNECTORS.md](CONNECTORS.md). To add CRM data, pull the reports listed in [`method/crm-reports.md`](method/crm-reports.md). Supplied data is used for that run only and never appears in a public output. Outside-in runs use public information only and never submit forms, start trials or contact the company.

## Author

Built by [Page Sands](https://sandsdx.com), SandsDX. Site: [newlogogrowth.ai](https://newlogogrowth.ai).

## License

MIT
