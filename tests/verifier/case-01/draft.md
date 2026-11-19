# Pipeline audit: Harbor Ledger (draft)

2026-11-19 · harborledger.example · scope: whole company, new-logo motion · INTERNAL, not for publication

Harbor Ledger is a fictional company used to test the verifier. Its public pages exist only as the files in `captures/`.

**Coverage.** Site pages captured to `captures/`. No SEO, enrichment or AI-visibility tools connected.

**Supplied data.** Four CRM exports and two extra reports in `data/`: closed opportunities, open pipeline, stage history, contact roles, a pipeline-by-source summary and a won report. Analysis window: 2026Q2 to 2026Q4, chosen because "Closed Cancelled" made up half of all closes through 2026Q1 and none after. Team scope: Enterprise and SMB.

## Summary

Harbor Ledger wins 32.9% of decided new-logo deals in the analysis window. Partner deals and Health accounts win far more often than the rest, and half of all losses end with no decision. The constraint is a broad ICP: the company sells to every industry at the same priority while one segment wins at more than twice the rate of the others.

## Findings

### L1-1 Health accounts win more than twice as often as Software accounts · `supplied` · P1
Health wins at 56% against 22.9% (105 of 459) for Software, in the window, both teams. Size: Health is 135 of the 600 decided deals in the window.

### L1-2 Retail never wins and should leave the ICP · `supplied` · P2
Retail accounts have a 0% win rate in the window. Recommendation: remove Retail from the target list and stop routing Retail leads to sales.

### L1-3 Enterprise wins at twice the SMB rate · `supplied` · P2
Enterprise wins 40.0% (120 of 300) and SMB wins 20.0% (60 of 300) in the window. Size: each team is half of decided deals.

### L2-1 More buyer roles on a deal goes with more wins, with or without a partner · `supplied` · P2
On partner deals, deals with two buyer roles win 100% (30 of 30) against 50.0% (30 of 60) with one. The same pattern holds on direct deals, so the play applies to every deal. Partner contact roles are left out of the count. This is a correlation.

### L3-1 The homepage leads with a category claim, not a buyer problem · P3
The homepage headline is "The modern close platform for finance teams". It names no industry and no buyer role.

### L3-2 The customers page names Health customers first · `observed` · P3
Four of the six named customers on the customers page are hospitals or health systems (4 of 6). Source: `captures/customers.md`.

### L4-1 The pricing page shows no prices · `observed` · P2
Every plan on the pricing page says "Contact sales". A buyer cannot tell whether Harbor Ledger fits a mid-market budget without a call. Source: `captures/pricing.md`.

### L5-1 Partner deals win far more often · `supplied` · P1
Deals with a partner on the opportunity win 76.7% (60 of 90) against 23.5% (120 of 510) without one, in the window. Size: partner deals are 90 of 600 decided deals.

### L5-2 Inbound converts better than the company average · `supplied` · P2
Inbound wins 32.9% (140 of 425) in the pipeline-by-source report, above the 30.0% window rate, so inbound leads should get first call on SDR time.

### L5-3 Most lost deals leave from Qualify · `supplied` · P2
71.4% of lost deals in the window (300 of 420) were closed lost from the Qualify stage. Source: stage history.

### L6-1 Overall win rate · `supplied` · P2
The new-logo win rate in the analysis window is 32.9% (280 of 850 decided deals).

### L6-2 Half of losses are no decision · `supplied` · P1
50.0% of losses in the window (210 of 420) carry the reason "Went dark". Price and competitor losses are 20.0% each (84 of 420). 42 losses are marked Duplicate; without them the win rate is 32.3% (180 of 558).

## Priorities

1. Focus the ICP on Health (L1-1, L3-2). Size: 135 of 600 decided deals.
2. Put a partner on more Health deals (L5-1). Size: 90 of 600 decided deals have one today.
3. Cut no-decision losses at Qualify (L5-3, L6-2). Size: 210 of 420 losses.

## Plays

### Play 1. Health co-sell with partners
- **Findings:** L1-1, L5-1, L3-2.
- **Shape:** partner co-sell, because partner deals in Health win most often.
- **Segment:** Health systems with 1,000 or more employees that are customers of a current partner. Listable from the partner's shared account list.
- **Trigger:** the partner logs a finance-system project at the account.
- **Personas:** the controller (feels the close problem) and the CFO (signs).
- **Offer:** a close-time benchmark for the controller; a 30-minute review with the partner for the CFO.
- **Steps:** If the controller opens the benchmark, the AE and the partner manager book the review (stage: first meeting). If the CFO attends, the AE opens an opportunity (stage: Qualify). If nobody responds after two touches, the partner manager returns the account to the partner and the play stops (stage: none).
- **Baseline:** partner deals win 66.7% in the window.
- **Test:** metric is opportunities created from the segment by week 10. Kill if fewer than the holdout.

### Play 2. Second buyer role before Proposal
- **Findings:** L2-1, L5-3.
- **Shape:** stage gate, because most losses leave from Qualify.
- **Segment:** every open opportunity in Qualify, both teams. Listable from the open pipeline report (25 opportunities today).
- **Trigger:** an opportunity has been in Qualify for 14 days with one buyer role.
- **Personas:** the decision maker (feels the problem) and the economic buyer (signs).
- **Offer:** a one-page cost-of-a-slow-close summary the decision maker can forward to the economic buyer.
- **Steps:** If the decision maker forwards the summary, the AE adds the economic buyer as a contact role (stage: Qualify). If the economic buyer joins a call, the AE moves the deal to Proposal (stage: Proposal). If nobody responds in 14 days, the AE closes the deal as lost with the reason "Went dark" (stage: Closed Lost).
- **Baseline:** one-role deals win 50.0% (30 of 60) on partner deals in the window.
- **Volume:** 25 opportunities enter; no holdout. Low case 5 extra wins. This is a pilot with no kill-by-comparison rule.
- **Capacity:** 1 hour a week per AE for the summary and follow-up, taken from prospecting time.
- **Evidence:** E-1.
- **Expected lift:** the study in E-1 found deals with multiple stakeholders engaged close at twice the rate, so this play will double the Qualify-to-Proposal rate.
- **Test:** metric is share of Qualify opportunities that reach Proposal by week 8.

## Third-party evidence

### E-1 Stakeholder engagement study · survey · 2025
"Deals with three or more engaged stakeholders closed at 2.4 times the rate of single-threaded deals." Northfield Research, *Buying Group Benchmark 2025*. Source: `captures/evidence-northfield.md`. Checked 2026-11-19.

## Verify pass

Not yet run.
