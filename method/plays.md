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
- **Every branch has an owner and a stage.** Use roles (SDR, AE, marketing operations, solutions engineer), never names. Use the company's stage names when known; otherwise use first meeting, opportunity, closed.
- **A silent branch.** Say what happens when nobody responds, and when the play stops contacting the account.
- **Evidence for the mechanism.** Each play carries at least one third-party, data-based citation for why its mechanism works (for example how buyers research, how response speed affects qualification, how many people sign off), following evidence.md. The citation supports the mechanism. It never stands in for the company's own baseline, and it never becomes a promised lift.
- **Grounded in the findings.** Every play cites the finding IDs it acts on. A play with no finding behind it goes in the parking lot.
- **Measurable.** Each play names one pipeline metric, a review date and a kill rule, so it can become an experiment.
- **Observe-only still applies.** Plays describe what the company would do. Drafted messages are for review; the plugin never sends them.

## Internal fixes

Some priorities are repairs inside the company, such as a measurement or routing fix, with no buyer to reach. Write these as a fix, not a play: the owner, the steps in order, the done criterion, the date, and what it unblocks. A fix needs no personas, trigger or evidence citation, and it runs as a week-0 prerequisite for the plays that depend on it.

## Play format

```
### Play {n}. {Name}
Acts on: {finding IDs} · Priority: {n}
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
Metric: {one pipeline metric} · Leading indicator: {what moves in 2 to 3 weeks}
Review: week {n} · Kill rule: {result that stops it} · Scale rule: {result that earns more investment}
```

## Example

This example is generic. It shows the shape, not a recommendation for any company.

```
### Play 1. Renewal deadline diagnostic
Acts on: L1-3, L4-4 · Priority: 2
Segment: existing customers of the core product with no automation subscription, 3+ vendors in use
Trigger: an industry deadline that multiplies their manual work within 12 months, visible in public records
Personas: operations engineer (feels the renewal work) · head of IT or security (signs) · procurement (blocks)

Step 1. Operations engineer gets a free report on their own public footprint against the deadline, by email from the SDR. Owner SDR.
  If they open it and reply, then offer a 30 minute review of the full inventory with a solutions engineer, owner SDR, stage first meeting.
  If no response in 7 days, then send the same report to the head of IT with a one-line summary of the workload change, owner SDR.
  If the head of IT replies first, then go to step 2.
Step 2. Head of IT gets a cost of inaction summary built from the report, plus a reference customer in their industry. Owner AE.
  If they agree to a call, then scoped pilot proposal with a success criterion, owner AE, stage opportunity.
  If they cite procurement or security review, then send the security and procurement pack before the call, owner AE.
Step 3. Pilot runs 30 days on one business unit. Owner solutions engineer.
  If the success criterion is met, then commercial proposal, owner AE.
Exit. Opportunity created, or disqualified if the account has fewer than the minimum footprint.
Stops when. Three touches per persona with no response, or 30 days.

Why it should work: buyers spend a small share of their buying time with suppliers, so the first step gives them something useful to bring to the rest of the committee [E-xx].
Metric: opportunities created per 100 accounts worked · Leading indicator: report replies in weeks 2 and 3
Review: week 10 · Kill rule: no difference from a matched holdout at week 8 · Scale rule: above holdout for two reviews
```

## From play to experiment

The experiment format in scoring.md tests a play. Copy the segment, the first offer and the metric into the hypothesis. Use the play's review date and kill rule. Run at most two plays on the same persona at the same time, or their effects cannot be separated.
