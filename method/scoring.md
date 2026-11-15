# Findings and experiments: format and scoring

## Finding format

Every finding uses this structure:

| Field | Content |
|---|---|
| **ID** | `L{layer}-{n}`, e.g. `L3-2` |
| **Layer** | ICP, Audiences, Messaging, Offers, Motion, Measurement |
| **Finding** | One sentence: what is true, for which audience, on which surface |
| **Evidence** | URL, query, screenshot reference or data source, with date observed |
| **Status** | `observed`, `inferred`, or `needs data` |
| **Severity** | P1 (blocks pipeline now), P2 (limits pipeline), P3 (polish) |
| **Pipeline effect** | Which pipeline number it affects: accounts reached, first meetings, opportunities, win rate, cycle length, deal size |
| **Root cause** | The upstream cause, if this finding is a symptom |

## Prioritization

1. Group findings by root cause. One root cause often explains several findings.
2. Score each root cause on **impact** (expected pipeline effect, 1 to 5) and **effort** (S, M, L, considering people, budget and dependencies).
3. Sequence by dependency before sorting by score. ICP before audience work, messaging before new channels, clean definitions before attribution claims.
4. Keep the top 3 to 5. Everything else goes in a parking lot with one line each.
5. Turn each kept priority into one play (plays.md): segment, personas, trigger, offer and "if this, then that" branches, backed by third-party evidence for its mechanism (evidence.md).

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
| **Expected lift** | Low / mid / high, each with its reasoning. Plan on the low case. |
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
- Compare against a holdout group of matched accounts where possible.
- Call results `directional` unless the volume supports a test.
