# Output formats

Two formats. The user chooses; default to the full report.

---

## A. Full report

For client work and internal planning. Markdown; the user may ask for HTML or PDF.

```
# Pipeline audit: {Company}
{date} · {outside-in | outside-in + supplied data: list} · prepared with newlogo-growth

## Summary
3 to 5 sentences. The single biggest constraint on pipeline, in plain words. The top 3 priorities in one line each.

## Profile
Stage: {stage} ({evidence}) · Motion: {motion} ({evidence})
Stated ICP vs observed ICP, one line each.

## Layer scores
| Layer | Score 0–3 | Why (finding IDs) |
| ICP | | |
| Audiences | | |
| Messaging (story sync rate: x of y surfaces current) | | |
| Offers | | |
| Motion and channels | | |
| Measurement | | |

## Priorities
For each of the 3 to 5 priorities:
### {n}. {Root cause, stated plainly}
- Findings: {IDs}
- Pipeline effect: {metric} · Impact {1–5} · Effort {S/M/L}
- What to do first
- Depends on: {other priority, or none}

## Experiments
One table per experiment, using the experiment format in scoring.md.

## Findings
All findings in the finding format, grouped by layer.

## Parking lot
One line per deferred item.

## What we could not see
Each `needs data` item and the export or access that would resolve it.

## Sources
Every URL and query used, with dates.
```

---

## B. One-page pipeline teardown

For a hiring manager, a founder, or a public post. Must fit on one page (about 450 words plus one small table). Written to be read in two minutes.

```
# {Company}: where pipeline is leaking
{date} · outside-in, public data only · by {author}

**The constraint.** One or two sentences: the upstream layer that limits pipeline most, and the evidence.

**What I found** (3 findings, one line each, each with its source)
1. {ICP / audience / messaging / offer finding} [source]
2. ...
3. ...

**Story sync:** {x} of {y} buyer-facing surfaces tell the current story. Biggest gap: {surface}.

**What I would run in the first 90 days**
| # | Experiment | Pipeline metric | Review |
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
