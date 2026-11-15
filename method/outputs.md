# Output formats

Two formats. The one-page teardown leads; the full report is the appendix that backs it. Deliver the teardown by default for hiring-manager, founder or public use, and both when the user asks for an audit for their own company or a client.

Every output opens with a coverage line: which tools were available, which were not, and which findings are therefore `directional`.

---

## A. One-page pipeline teardown

For a hiring manager, a founder, or a public post. Must fit on one page (about 500 words plus one small table and one short play). Written to be read in two minutes.

```
# {Company}: where pipeline is leaking
{date} · outside-in, public data only · by {author}
Coverage: {tools used; tools unavailable and what that limits}

**The constraint.** One or two sentences: the upstream layer that limits pipeline most, and the evidence.

**What I found** (3 findings, one line each, each with its source)
1. {ICP / audience / messaging / offer finding} [source]
2. ...
3. ...

**Story sync:** {x} of 10 buyer-facing surfaces tell the current story (owned {x} of 5, third-party {x} of 5). Biggest gap: {surface}.

**The play I would run first**
Segment · trigger · personas, then three or four "if this, then that" lines from plays.md, ending in the metric and the kill rule.
Why it should work: one sentence [third-party citation with type label].

**What I would run in the first 90 days**
| # | Play or experiment | Pipeline metric | Review |
| 1 | | | week {n} |
| 2 | | | |
| 3 | | | |

**What I would need to confirm this:** {the 2 to 3 data sources that would turn inferences into facts}

Method: {link to repo or site}
```

Rules for the teardown:
- Respectful and specific. Assume the team knows most of this; show the thing they may not have seen.
- Only `observed` findings and clearly labeled `inferred` ones. No `needs data` items presented as fact.
- No numbers about the company's internal performance; outside-in runs cannot see them.
- For a public post, remove anything that reads as confidential or as criticism of a named person.

---

## B. Full report

For client work and internal planning. Markdown; the user may ask for HTML or PDF.

```
# Pipeline audit: {Company}
{date} · {outside-in | outside-in + supplied data: list} · prepared with newlogo-growth
Coverage: {tools used; tools unavailable; findings labeled directional as a result}

## Summary
3 to 5 sentences. The single biggest constraint on pipeline, in plain words. The top 3 priorities in one line each.

## Profile
Stage: {stage} ({evidence}) · Motion: {motion} ({evidence})
Stated ICP vs observed ICP, one line each.

## Layer scores
| Layer | Score 0–3 | Why (finding IDs) |
| ICP | | |
| Audiences | | |
| Messaging (story sync x of 10; owned x of 5; third-party x of 5) | | |
| Offers | | |
| Motion and channels | | |
| Measurement | | |

## Priorities
For each of the 3 to 5 priorities:
### {n}. {Root cause, stated plainly}
- Findings: {IDs}
- Pipeline effect: {metric} · Impact {1–5} · Effort {S/M/L}
- Play: {play name, below}
- Depends on: {other priority, or none}

## Plays
One play per priority, in the play format from plays.md, each with its third-party evidence.

## Experiments
One table per experiment, using the experiment format in scoring.md. Each names the play it tests.

## Findings
All findings in the finding format, grouped by layer. The story sync table sits under Messaging.

## Parking lot
One line per deferred item.

## What we could not see
Each `needs data` item and the export or access that would resolve it.

## Sources
Company sources: every URL and query used, with dates.
Third-party evidence: every citation used in plays and priorities, with its type label (analyst, consultancy, academic, public data, vendor-own, vendor-commissioned) and the date it was checked.
```
