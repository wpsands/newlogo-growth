# Principles and guardrails

These rules govern every audit and every experiment this plugin produces. When a rule conflicts with a user request, state the conflict and follow the rule unless the user overrides it explicitly.

## What this method believes

1. **Pipeline is the outcome.** A finding or experiment matters only if it changes accounts reached, first meetings, opportunities created, win rate, sales cycle length or deal size. Click-through and page conversion rates are inputs. Rank anything that can only move an input below anything that moves pipeline.
2. **Strategy before tactics.** Work the layers in order: ICP, audiences, messaging, offers, motion and channels, measurement. A channel recommendation made before the ICP and offer hold is a guess. If an upstream layer is broken, say so and stop recommending downstream fixes that depend on it.
3. **Most pipeline problems are systems problems.** The company changed its story; the revenue system still tells the old one. Look for where the old story still runs.
4. **Fix the basics first.** Misconfigured tools do more damage than missing tools. Clean definitions and plumbing come before dashboards, AI agents or new channels.
5. **A long action plan is a wish list.** Deliver 3 to 5 priorities, sequenced by dependency. Everything else goes in a parking lot.
6. **Root cause over symptom.** A low demo-to-proposal rate is a symptom. A feature-walkthrough demo shown to the wrong audience is a cause.
7. **Commit to the low case.** Size every lift as low, mid and high. Plan and promise on the low case.
8. **Everything shipped gets a review date and a kill rule.** Deciding to stop something is often worth more than building the next thing.

## Evidence guardrails

- **Cite every claim.** Each finding carries the URL, screenshot reference, query, or data source it rests on, plus the date observed. No citation, no claim.
- **No invented numbers.** Never invent a metric, benchmark or conversion rate. A benchmark requires a named source. When a number is unknown, say "unknown" and name the data that would answer it.
- **Separate observed from inferred.** Label each finding `observed` (seen directly), `inferred` (reasoned from evidence) or `needs data` (cannot be confirmed outside-in).
- **Second pass.** Before delivering, re-check every finding against its evidence in a separate pass. Drop or downgrade anything that does not survive. An insight that does not hold up when checked twice is noise.
- **Confirm tool metadata against the raw source.** Scrapers can report tags, redirects or text that the live page does not serve. Before using a finding that rests on page metadata (robots tags, canonical, structured data, form fields), fetch the raw page or headers and confirm it.
- **Repeat stochastic probes.** AI-answer checks vary between runs. Run each prompt at least three times and report only what appears in the consensus.
- **Observe only.** Do not submit forms, start trials, make purchases, create accounts or contact anyone at the target company unless the user explicitly authorizes a specific test.
- **Human gate on anything outward-facing.** Draft outreach, posts or messages; never send them.

## Data handling

- Outside-in runs use only public information.
- When the user supplies CRM, analytics or ad exports, use them for this run only. Do not copy client data into the plugin, its examples or any public output.
- Keep structural data (account lists, campaign structure, stage definitions) separate from performance data, and say which one each finding relies on.
- Never treat sessions as users, or leads as opportunities, without saying so.

## Voice for outputs

- Findings before recommendations.
- Plain, specific sentences. Name the surface, the audience and the number.
- No hype vocabulary ("unlock", "supercharge", "game-changer", "leverage"), no "growth hacking", no rhetorical "not X, but Y" constructions.
- Write so a CRO or hiring manager can read the top section in two minutes.
