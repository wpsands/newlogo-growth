# Tests

Two kinds of test. Both use made-up data only. No client data belongs in this repository.

## 1. Script tests

These check `scripts/crm_profile.py` against exports whose right answers are known by construction. They run in under a second and need only Python 3.

```bash
python3 tests/test_crm_profile.py
```

```bash
python3 tests/test_score.py
```

`tests/fixtures.py` builds the exports from fixed counts. Half of all closes are "Closed Cancelled" through 2026Q1 and none are after, so the correct analysis window is 2026Q2 to 2026Q4. The tests fail if the script blends quarters across that change, counts a partner contact as a buyer role, drops a low-sample warning, or misses an export with no opportunity ID.

Run both before every release.

## 2. Verifier test

This checks the `verifier` agent. `tests/verifier/case-01/draft.md` is an audit of a fictional company with eleven planted mistakes and four correct findings. The verifier passes when it reports every planted mistake against the right finding or play ID and does not list a correct finding under Must fix. The answer key is `tests/verifier/case-01/expected.json`.

The test uses a model, so it costs a run and can vary from run to run. Run it when `agents/verifier.md` or anything in `method/` changes.

1. Lay the case out in a scratch folder outside the repository, so the verifier cannot see the answer key. This also prints the brief.

```bash
python3 tests/verifier/prepare.py tests/verifier/case-01 /tmp/verifier-case-01
```

2. In Claude Code, start a fresh agent and give it the printed brief (also saved as `brief.txt` in the scratch folder). Save the text it returns as `/tmp/verifier-case-01/report.md`.

3. Score the report.

```bash
python3 tests/verifier/score.py tests/verifier/case-01 /tmp/verifier-case-01/report.md
```

The scorer prints each planted mistake as caught or missed and ends with PASS or FAIL.

### The planted mistakes

| ID | Mistake |
|---|---|
| L6-1 | A win rate that blends all eight quarters while the stated window is three |
| L1-1 | A rate with no counts |
| L1-2 | A segment decision resting on six deals |
| L2-1 | A buyer-role claim extended to direct deals, where the data cannot show it |
| L3-1 | A finding with no status label |
| L4-1 | An observed finding the page capture contradicts |
| L5-1 | An arithmetic error |
| L5-2 | A comparison between a report with no opportunity ID and the window rate |
| Play 1 | No volume line and no capacity line |
| Play 2 | A third-party benchmark used as the expected lift |
| E-1 | A citation whose quote, year and type do not match the source |

### Adding a case

Copy `case-01`, change the draft and captures, and write a new `expected.json`. Give each planted mistake its own finding or play ID, since the scorer matches on the ID. Add at least two correct findings as controls. If a case needs different data, add a builder to `tests/fixtures.py`.
