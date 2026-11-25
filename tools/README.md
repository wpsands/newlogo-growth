# Optional tools

Two scripts for the New Logo Growth plugin. They sit outside the plugin folder, so installing the plugin does not install them. The plugin works without them and asks where they are before using them; see [`plugins/newlogo-growth/method/tools.md`](../plugins/newlogo-growth/method/tools.md).

Both use the Python standard library only. To use them, keep a copy of this repository and tell Claude where it is when asked.

## ai_probe.py

Asks Claude, ChatGPT, Perplexity and Gemini buyer questions with web search on, several runs per question, and records whether the company is named, its rank among named vendors, the sentence that describes it and the sources cited. A company counts as present for a question only when it appears in a majority of runs.

It calls the providers' APIs on your own accounts, so each run is billed to them. Set a key for each provider you want to query, or one OpenRouter key for all four. The variable names and model defaults are in the header of [`ai_probe.py`](ai_probe.py). Providers without a key are skipped and listed in the output. Keys are never printed.

```
python3 tools/ai_probe.py --brand Outreach --aliases outreach.ai,outreach.io \
  --competitors Gong,Salesloft,Apollo --questions-file questions.txt \
  --runs 3 --out probe.json
```

## crm_profile.py

Profiles CRM opportunity exports: what each file holds, whether the files agree, where the closed definition changed, and win rates by team, segment, source and partner inside one consistent window, with counts and intervals. Its output holds your data, so keep it out of the repository.

```
python3 tools/crm_profile.py --closed closed.csv --open open.csv \
  --history stage_history.csv --roles contact_roles.csv --json profile.json
```

Tests for it are in [`tests/`](../tests/).
