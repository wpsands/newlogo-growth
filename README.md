# New Logo Growth

A Claude Code plugin for new-logo pipeline in B2B SaaS. It audits a company's pipeline system and ranks the few experiments most likely to grow it. It covers companies from seed to enterprise.

It works top-down. ICP, audiences, messaging and offers come first; channels are chosen last, as a consequence. Every finding cites its evidence, and every experiment names the pipeline number it should move, a review date and a kill rule. A/B tests and landing-page tweaks rank low unless a page is blocking a pipeline play.

## Skills

| Skill | Ask it | You get |
|---|---|---|
| `pipeline-audit` | "Audit acme.com" or "One-page teardown of acme.com" | Layer scores, cited findings, 3 to 5 priorities, draft experiments. Full report or a one-page teardown. |
| `pipeline-experiments` | "What should Acme run next quarter?" | A ranked backlog of 3 to 5 pipeline experiments and a 90-day calendar. |

Both follow the method in [`method/`](method/):

- [`principles.md`](method/principles.md): beliefs, evidence guardrails, voice
- [`profiles.md`](method/profiles.md): stage × motion profiles
- [`layers.md`](method/layers.md): the six layers and their checks
- [`scoring.md`](method/scoring.md): finding and experiment formats, prioritization
- [`outputs.md`](method/outputs.md): report and teardown templates

## Install

In Claude Code:

```
/plugin install newlogo-growth --marketplace wpsands/newlogo-growth
```

Or clone the repo and load it locally:

```bash
git clone https://github.com/wpsands/newlogo-growth
claude --plugin-dir ./newlogo-growth
```

## Data

Only a company URL is required. Connect SEO, enrichment, AI-visibility, CRM or analytics tools for better coverage; see [CONNECTORS.md](CONNECTORS.md). Outside-in runs use public information only and never submit forms, start trials or contact the company.

## Author

Built by [Page Sands](https://sandsdx.com), SandsDX. Site: [newlogogrowth.ai](https://newlogogrowth.ai).

## License

MIT
