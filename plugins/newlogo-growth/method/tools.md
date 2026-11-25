# Optional tools

Two Python scripts make parts of the audit faster and more exact. They are not part of the plugin and are not installed with it. They live in the `tools/` folder of the repository, https://github.com/wpsands/newlogo-growth, and run only from a copy of that folder the user keeps on their own machine.

Every check works without them. Use a tool when the user has it, and the fallback otherwise.

## Finding the tools

If a tool would help and the user has not said where it is, ask once whether they have a copy of the repository and where it is. Do not search the user's machine for it. If they do not have one, use the fallback and say in the coverage line that the tool was not used. Do not ask again in the same run.

## ai_probe.py: what AI assistants say

Asks Claude, ChatGPT, Perplexity and Gemini the buyer questions with web search on, several runs each, and reports per assistant whether the company is named in a majority of runs, its rank among named vendors, the sentence that describes it and the sources cited. Its setup, including which accounts it uses, is in `tools/README.md` in the repository.

```
python3 {tools folder}/ai_probe.py --brand "{company}" --aliases "{domains,other names}" \
  --competitors "{3 to 5 competitors}" --questions-file {path} --runs 3 --out {notes dir}/ai-probe.json
```

Write the five questions to the file one per line. Run one question once first as a smoke test. Report which assistants ran, by which route, and which were skipped, and run only the assistants the user chose for this run.

**Fallback.** Use a connected `~~AI visibility` tool (CONNECTORS.md). If there is none, use search-engine results for the same questions and label those findings `directional`. Never answer a buyer question from your own training knowledge as a stand-in for an assistant. If nothing can be queried, score the surface `needs data`.

## crm_profile.py: reading CRM exports

Profiles CRM opportunity exports: what each file holds, whether the files agree, where the closed definition changed, and win rates by team, segment, source and partner inside one consistent window, with counts and intervals.

```
python3 {tools folder}/crm_profile.py --closed closed.csv --open open.csv \
  --history stage_history.csv --roles contact_roles.csv \
  --json {notes dir}/crm-profile.json > {notes dir}/crm-profile.md
```

Its output holds client data. Keep it in the run's working directory, never in the plugin or a public file.

Run `python3 {tools folder}/crm_profile.py --help` for every option, including `--exclude-team` and `--window-start`.

**Fallback.** Work through the checks in layers.md ("Reading CRM exports") on the files yourself, writing whatever analysis code the environment allows, and produce the same tables: the inventory, the reconciliation between files, outcomes by quarter, the definition break and analysis window, the standard cuts with counts and intervals, the loss mix, buyer-role and stage tables, and open pipeline. Keep the code and its output with the run's notes.
