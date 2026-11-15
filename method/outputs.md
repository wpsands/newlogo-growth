# Output formats

Two formats. The one-page teardown leads; the full report is the appendix that backs it. Deliver both by default. Deliver the teardown alone when the user asks for a one-pager.

Every output opens with a coverage line: which tools worked, which failed (with the error), which worked only partly or through a substitute, and which findings are therefore `directional`.

When the output will be public, both documents are public. Leave out anything from supplied data, and keep page-source details to what any visitor could see.

---

## A. One-page pipeline teardown

For a hiring manager, a founder, or a public post. Must fit on one page (about 650 words including the coverage line, one small table and one short play). Written to be read in two minutes.

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

Aim for 3,500 to 4,000 words of prose; table syntax and URLs do not count. Rough budget: coverage, summary, profile and scores 600; priorities 250; plays 1,100 (three full plays at about 350 words, plus one-liners); findings 1,250; parking lot, gaps and verify pass 350; sources as long as they need to be. If the report runs long, cut repetition between plays and findings first, then secondary branches in plays. Never cut a fact a finding or play depends on.

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
Full plays, in the plays.md format with the test block, for the top three priorities. Each carries its third-party evidence. Priorities four and five, if any, get one line each: segment, first offer, metric. Internal fixes use the fix format from plays.md.

## Findings
P1 and P2 findings in the finding format, grouped by layer. Keep the finding to one sentence and the evidence to source and date. P3 findings go in a short list at the end of the section, one line each. Observed strengths are cited in the layer scores table, not listed as findings. The story sync table sits under Messaging.

## Parking lot
One line per deferred item.

Week 0: internal fixes that plays depend on but that are not priorities, one line each with owner and done criterion.

## What we could not see
Each `needs data` item and the export or access that would resolve it. `needs data` findings live here, not in the findings tables.

## Verify pass
Outcomes only: what was dropped, downgraded or corrected, and what was re-confirmed against raw sources.

## Sources
Company sources: every URL and query used, with dates.
Third-party evidence: every citation used in plays and priorities, with its type label, year and URL (the quote appears where the citation is used) (analyst, consultancy, academic, public data, vendor-own, vendor-commissioned) and the date it was checked.
```
