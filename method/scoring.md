# Findings and experiments: format and scoring

## Finding format

Every finding uses this structure:

| Field | Content |
|---|---|
| **ID** | `L{layer}-{n}`, e.g. `L3-2` |
| **Layer** | ICP, Audiences, Messaging, Offers, Motion, Measurement |
| **Finding** | One sentence: what is true, for which audience, on which surface |
| **Evidence** | URL, query, screenshot reference or data source, with date observed |
| **Status** | One or more of the five labels below |
| **Severity** | P1 (blocks pipeline now), P2 (limits pipeline), P3 (polish) |
| **Pipeline effect** | Which pipeline number it affects: accounts reached, first meetings, opportunities, win rate, cycle length, deal size |
| **Size** | How much of the pipeline the finding touches, with counts: the number of accounts, deals or dollars affected, or the share of a stated total. From supplied data when present; from a public count when one exists (pages, listings, job posts, accounts in a public record); otherwise "not sized" and the data that would size it |
| **Root cause** | The upstream cause, if this finding is a symptom |

## Status labels

Use these five and no others. A finding can carry two (for example `observed, directional`).

| Label | Meaning |
|---|---|
| `observed` | Seen directly in a public source or raw capture this run |
| `inferred` | Reasoned from observed evidence; the reasoning is stated |
| `supplied` | Rests on data the user supplied; carries the analysis window and team scope; never appears in a public output |
| `directional` | Rests on a weak instrument: a substitute tool, one provider, a search snippet, a sample below the minimum, or a rate whose interval overlaps the comparison |
| `needs data` | Cannot be confirmed with the data available; listed under "What we could not see" with the data that would resolve it |

## Rates and counts

- **Counts beside every rate.** Write "34.8% (173 of 497)", never the percentage alone.
- **Minimum sample.** A rate from fewer than 30 decided deals (or 30 of whatever the denominator is) is `directional` and cannot be the basis of a segment choice, a priority or a P1 or P2 finding on its own. `scripts/crm_profile.py` marks these `low n`.
- **Differences need room.** Before saying one segment beats another, check that the gap is larger than the uncertainty in both rates. The profiling script prints a 95% interval for each rate. If the intervals overlap heavily, say the difference is not established.
- **One window, stated.** Every rate from supplied data names its window and team scope (layers.md, "Reading CRM exports").
- **Correlation is labeled.** A difference between groups in historical data is a correlation unless the groups were assigned. Say so where the number appears.

## Prioritization

1. Group findings by root cause. One root cause often explains several findings.
2. Score each root cause on **impact** (1 to 5, anchors below) and **effort** (S, M, L, considering people, budget and dependencies). State the size behind the impact score in one clause.

   | Impact | Test |
   |---|---|
   | 5 | Touches most of the pipeline in scope (roughly half or more of accounts, deals or value), or blocks every play, and the evidence is `observed` or `supplied` with adequate counts |
   | 4 | Touches a large, named part of the pipeline (roughly a fifth to a half), with evidence of the same quality |
   | 3 | Touches a clear but smaller part, or a large part on `inferred` evidence |
   | 2 | Touches a small part, or the evidence is `directional` |
   | 1 | Polish; no pipeline number would visibly move |

   A root cause that rests only on `directional` or `inferred` evidence scores no higher than 3. If nothing can be sized, say "not sized" and score on the evidence quality alone.
3. Sequence by dependency before sorting by score. ICP before audience work, messaging before new channels, clean definitions before attribution claims.
4. Keep the top 3 to 5. Everything else goes in a parking lot with one line each.
5. Turn the top three priorities into full plays (plays.md): segment, personas, trigger, offer and "if this, then that" branches, backed by third-party evidence for the mechanism (evidence.md). Give priorities four and five one line each: segment, first offer, metric, and the evidence ID if one applies.

## Experiment format

Each experiment tests a strategic hypothesis and has a pipeline outcome.

| Field | Content |
|---|---|
| **Name** | Short, specific |
| **Layer** | The layer it tests |
| **Hypothesis** | "If [audience in ICP segment] gets [message or offer] through [motion], then [pipeline metric] will move from [baseline or unknown] to [target] within [window], because [evidence]." |
| **Play** | The play it tests (plays.md), or none |
| **Finding(s) addressed** | IDs |
| **Pipeline metric** | One primary metric: accounts reached, first meetings, opportunities created, win rate, cycle length, deal size |
| **Leading indicator** | What should move within 2 to 3 weeks to show the experiment is on track |
| **Expected lift** | Low / mid / high, each with its reasoning. Plan on the low case. Without a baseline, write qualitative bands (for example, "equal to the holdout with less effort") and say the baseline is unknown. |
| **Supporting evidence** | Third-party, data-based citation for the mechanism, per evidence.md, with its type label. "No third-party evidence found" when none exists. Never used as the expected lift. |
| **Window** | Usually 6 to 12 weeks. Shorter only if the pipeline metric can move that fast. |
| **Owner** | The role that runs it |
| **Prerequisites** | Measurement or data that must exist first |
| **Review date** | When to decide |
| **Kill rule** | The specific result that stops it |
| **Scale rule** | The specific result that justifies more investment |

## What ranks low or is excluded

- Experiments whose only metric is click-through, open rate, page conversion, or form fills.
- A/B tests on page elements, unless the page is a confirmed bottleneck for a pipeline play (for example, a broken demo form).
- Experiments that need measurement the company does not have, unless the measurement fix is scheduled first.
- Plays or experiments whose only support is a third-party benchmark, with no finding about this company behind them.
- More than two experiments on the same audience at the same time; their effects cannot be separated.

## Sample size and confidence

Most B2B pipeline experiments run on small numbers. Do not claim statistical significance on counts of opportunities in the tens. Instead:
- State the baseline and the counts.
- Before the test starts, work out the outcomes expected on the low case in each group (plays.md, Volume). If that is under about 10 per group, the comparison cannot be read; change the design or call it a pilot.
- Compare against a holdout group of matched accounts where possible.
- Call results `directional` unless the volume supports a test.
