# New Logo Growth

A Claude Code plugin for new-logo pipeline in B2B SaaS. It audits a company's pipeline system from public data, scores ICP, audiences, messaging, offers, motion and measurement, and turns each priority into a play backed by verified third-party research, with experiments ranked by their effect on pipeline.

Site: [newlogogrowth.ai](https://newlogogrowth.ai)

## Install

In Claude Code:

```
/plugin marketplace add wpsands/newlogo-growth
/plugin install newlogo-growth@newlogo-growth
```

## What is in this repository

| Folder | Contents |
|---|---|
| [`plugins/newlogo-growth/`](plugins/newlogo-growth/) | The plugin: skills, agents and the method. Its [README](plugins/newlogo-growth/README.md) describes what it does and how to use it. |
| [`tools/`](tools/) | Two optional Python scripts, an AI-answer probe and a CRM export profiler. They are not installed with the plugin; see [`tools/README.md`](tools/README.md). |
| [`tests/`](tests/) | Tests for `crm_profile.py` and a test case for the `verifier` agent, with made-up data. See [`tests/README.md`](tests/README.md). |
| [`examples/`](examples/) | A sample full audit and one-page teardown of Outreach, from public data. |

## Author

Built by [Page Sands](https://sandsdx.com), SandsDX.

## License

MIT
