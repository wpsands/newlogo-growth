# Plays

A priority says what is wrong. A play says what to do about it, for whom, in what order, and what happens when the buyer responds or does not. Every priority in an audit ends in one play. Experiments then test whether the play moves pipeline.

## What a play is

A play is a short sequence of "if this, then that" steps that combines four things from the upstream layers:

1. **Segment**, from the ICP layer. A group of accounts specific enough to build a list from.
2. **Persona**, from the audiences layer. The role the step speaks to.
3. **Trigger**, the event or signal that makes the account ready now (a regulation date, a funding round, a new executive, a tool being sunset, a spike in hiring, a public signal such as an expiring contract or certificate).
4. **Offer**, from the offers layer. What the persona is asked to do, matched to their readiness.

Each step branches on the buyer's response. Each branch names what happens next, who owns it, and the pipeline stage the account moves to. A play ends when the account books a meeting, becomes an opportunity, or is disqualified for a stated reason.

## Rules

- **Two personas at least.** Cover the person who feels the problem and the person who signs. Show how the offer changes between them. Enterprise plays add the blocker (security, procurement, legal) where the evidence shows one.
- **Offer matched to readiness.** The first step never asks an unaware or problem-aware persona for a demo. Use the offer ladder in layers.md: a useful diagnostic or benchmark first, a conversation second, a scoped pilot third.
- **Every branch has an owner and a stage.** Use roles (SDR, AE, marketing operations, solutions engineer), never names. Use the company's stage names when known; otherwise use first meeting, opportunity, closed. Name only roles the evidence shows the company has (job posts, team pages, CRM owner roles); if a play needs a role that is not visible, say so in Prerequisites.
- **A silent branch.** Say what happens when nobody responds, and when the play stops contacting the account.
- **Evidence for the mechanism.** Each play carries at least one third-party, data-based citation for why its mechanism works (for example how buyers research, how response speed affects qualification, how many people sign off), following evidence.md. The citation supports the mechanism. It never stands in for the company's own baseline, and it never becomes a promised lift.
- **Grounded in the findings.** Every play cites the finding IDs it acts on. A play with no finding behind it goes in the parking lot.
- **Shaped by the findings, not by a template.** Choose the shape (see Shapes) that the evidence points to, and say in one clause why. Three plays in one audit should not share a shape unless the findings give no alternative. Derive every timing, touch limit and review week from this company's sales cycle, deal volume and team size, and state the basis ("median cycle is 80 days, so review at week 12"). Never copy a number from this file.
- **Not already running.** Before proposing a play, check for evidence that the company already runs it: campaign names in supplied data, ads, webinars, sequences, landing pages. If something similar exists, the play says how it differs or it is dropped.
- **Volume.** State how many accounts or opportunities enter the play and the holdout, the baseline rate if one is known, and the number of outcomes expected on the low case. If the low case is fewer than about 10 outcomes per group in the window, the test cannot separate the play from chance: enlarge the segment, lengthen the window, move the metric one step earlier in the funnel, or call the play a pilot with no kill-by-comparison rule.
- **Capacity.** State the work the play needs from each owner in hours or units per week, and what it displaces. A play the team cannot staff goes in the parking lot with the reason.
- **Measurable.** Each play names one pipeline metric, a review date and a kill rule, so it can become an experiment. With supplied data, compute the baseline now from the analysis window; do not defer it to a later fix when the data is already there.
- **Observe-only still applies.** Plays describe what the company would do. Drafted messages are for review; the plugin never sends them.

## Internal fixes

Some priorities are repairs inside the company, such as a measurement or routing fix, with no buyer to reach. Write these as a fix, not a play: the owner, the steps in order, the done criterion, the date, and what it unblocks. A fix needs no personas, trigger or evidence citation.

A fix blocks a play only when the play's metric cannot be read without it. When a usable baseline already exists (for example a clean analysis window in supplied data), the fix runs in parallel and the play says which baseline it uses.

## Play format

```
### Play {n}. {Name}
Acts on: {finding IDs} · Priority: {n} · Shape: {shape, and why this one}
Segment: {ICP segment, list-able} · Trigger: {event or signal and where it is visible}
Personas: {persona A, who feels the problem} · {persona B, who signs} · {blocker, if any}

Step 1. {Persona A} gets {offer} through {channel}. Owner {role}.
  If they {engage, e.g. open the diagnostic and reply}, then {next step}, owner {role}, stage {stage}.
  If no response in {n} days, then {fallback offer or channel}, owner {role}.
  If {persona B} engages first, then {step that switches to the signer's offer}.
Step 2. {Persona B} gets {offer suited to the signer} ...
  If ..., then ...
Step 3. ...
Exit. {Meeting booked, opportunity created, or disqualified because ...}
Stops when. {Contact limit, time limit, or signal that ends the play}

Why it should work: {one or two sentences on the mechanism} [{evidence ID or citation}]
Hypothesis: If {segment} gets {offer}, then {metric} moves within {window}, because {finding}.
Metric: {one pipeline metric} · Baseline: {rate and counts from the window, or unknown and what would give it} · Leading indicator: {what moves early}
Volume: {n} in the play, {n} held out · low case {n} outcomes per group in {window} · {readable | pilot only, and why}
Capacity: {role}: {hours or units per week}; {role}: {..} · displaces {what}
Expected lift: low {..} / mid {..} / high {..}, or qualitative bands if no baseline · Prerequisites: {fixes or data needed first}
Owner: {role} · Review: week {n} ({basis}) · Kill rule: {result that stops it} · Scale rule: {result that earns more investment}
```

Keep a full play to about 400 words including the test block. Two or three steps are usually enough; add a step only when the buyer's readiness changes.

## Play assets

A play is ready when the team could start it the following Monday. For the first play, and for others when the user asks, add a short assets block after the plays:

- **The list.** The exact filter or query that builds the segment, and where it runs (CRM report, enrichment tool, public record search). Include the expected count.
- **The first touch.** A draft of the first message for persona A, under 90 words, for review. It leads with something true about the account, not with the product.
- **The offer.** An outline of the diagnostic, benchmark or other first offer: its sections, the data each needs and where that data comes from.
- **A worked sample.** When the offer can be built from public data alone, build it for up to three real accounts in the segment and attach it. A sample that cannot be built from public data is a finding about the offer's cost.

Assets are drafts. Nothing is sent, and nothing in them uses supplied data in a public output.

## Shapes

These are the common shapes. They are starting points for the structure, not content to copy. Each lists when the findings point to it, how it opens, what it branches on and the usual metric. None gives timings; those come from the company's own cycle and volume.

| Shape | The findings point to it when | Opens with | Branches on | Usual metric |
|---|---|---|---|---|
| **Diagnostic to a named list** | The ICP can be listed from a public or CRM signal, and there is no offer short of a demo | A finding about the account's own situation, sent to the person who feels the problem | Reply, forward to the signer, or silence | First meetings per 100 accounts worked |
| **Inbound response and routing** | Buyers raise a hand and wait: form callbacks, no calendar, slow or untracked first response | The form, chat or trial event itself | Account fit and stated need at submission; time to first human response | Share of in-ICP inbound reaching a meeting within a set time |
| **Multi-threading an open deal** | Deals run on one contact; losses are mostly no-decision | The existing contact, asked to bring in the person who runs the work or signs | Whether a second buyer role joins, and which one | Share of treated opportunities advancing a stage; no-decision share |
| **Partner co-sell lane** | Partners appear on a large share of wins; registered deals age or stall | The partner's account manager, with the list of their open deals and the next action for each | Partner confirms a customer contact, goes quiet, or the registration ages out | Share of partner deals reaching a stage within a set time |
| **Self-serve to sales** | A store, free plan or trial exists; high-fit buyers never reach a person | A usage or purchase event on an account that matches the ICP | Fit and usage threshold; buyer accepts or declines a human | Opportunities created from product-qualified accounts |
| **Switching window** | A competitor event (merger, sunset, price change, outage) or a regulation creates a dated reason to move | Proof of what changes for that account and when | Renewal date known or unknown; technical evaluator or signer engages first | Opportunities per 100 accounts in the window |
| **Expansion into the base** | Existing customers lack the product in scope and a trigger applies to them | Their own account data against the trigger | Owner of the relationship (account manager or new-logo rep); customer health | Opportunities created from the base |

If the evidence points to a shape that is not listed, use it and say why.

## From play to experiment

In an audit, the play's test block is the experiment; do not repeat it as a separate table.

The experiment format in scoring.md tests a play. Copy the segment, the first offer and the metric into the hypothesis. Use the play's review date and kill rule. Run at most two plays on the same persona at the same time, or their effects cannot be separated.
