# Pipeline audit: Outreach

2026-11-15 · outside-in, public data only · prepared with newlogo-growth v0.2.0 · by Page Sands

Coverage: Firecrawl scrape and search, direct HTTP fetches of raw page source, the public GTM container and Marketo form definitions, the Lever postings API, and the Google Ads Transparency Center (through a Firecrawl data provider, ad text read by OCR). Semrush failed ("API UNITS BALANCE IS ZERO") and Ahrefs failed ("Insufficient plan"), so there is no keyword, ranking or paid-spend data; search positions come from single web-search runs and are `directional`. No AI assistant (ChatGPT, Perplexity, Gemini, Claude) was queried directly; story sync surface 6 rests on search-engine results only and is `directional`. No enrichment was run, so customer sizes and regions are `inferred` from general knowledge. The LinkedIn company page was read through a data-provider mirror dated 2026-11-12, not the live page.

This is a public example. It uses public sources only and has not been reviewed by Outreach. It contains no internal performance data.

## Summary

Outreach has moved its story from sales engagement to an agentic AI platform for revenue teams, and its own site, press and LinkedIn tell the new story. The biggest constraint on new-logo pipeline sits upstream of that story: no public surface names a segment or trigger narrow enough to build an account list, so the clearest switching moment in the category (Salesloft and Clari merged in December 2025 and moved to one brand in September 2026) reaches buyers only as a comparison page that ends in a 12-field demo form. Buyers who meet Outreach off its own site still read "sales engagement platform" or "Sales Execution Platform" on all five third-party surfaces checked.

Top priorities:
1. Name a list-able segment and trigger, starting with accounts running Salesloft and Clari.
2. Add an offer between content and the demo form, starting with the product tour Outreach already has.
3. Carry the current story to third-party surfaces, and use third-party proof with in-market accounts.
4. Give the security and procurement reviewers a path that does not wait for an account executive.

## Profile

Stage: enterprise (`inferred`). Founded 2014, $489M raised, $4.4B valuation after its Series G (outreach.ai/company/about); enterprise logos in press boilerplate (Databricks, SAP, Siemens, Verizon); named a Leader by Gartner (Revenue Action Orchestration, 2026-10-15), Forrester (2026-09-24) and IDC (2026-09-21) per the newsroom; offices in Seattle, Prague, Hyderabad and Atlanta; a three-track partner program. Open roles include both a Commercial AE (10 to 1,000 employees) and an Enterprise AE (5,000 to 10,000 employees), so it sells across segments.

Motion: sales-led (`observed`). No public prices, trial or self-serve purchase; every primary call to action is "Get a demo" or "Request pricing". An AWS Marketplace listing gives a procurement route that is still sales-assisted.

Stated ICP: "revenue teams" adopting AI, with enterprise-weighted proof (Siemens, Avis Budget Group, SAP, Verizon) and pricing copy that steers CROs of "enterprise revenue teams" to Amplify Pro (`observed`).
Observed ICP: B2B software, security, data and payments companies with SDR and AE teams, mostly 1,000+ employees in the named-customer set, on top of a public reviewer base that is mostly mid-market software (`inferred`; sizes not enriched).

## Layer scores

| Layer | Score (0 to 3) | Why (finding IDs) |
|---|---|---|
| ICP | 1 | P1 L1-1 (no list-able segment or trigger stated); L1-2, L1-3, L1-4 |
| Audiences | 2 | No P1. Strength L2-1 (six role pages with distinct arguments); gaps L2-2, L2-3, L2-4 |
| Messaging (story sync 4 of 10; owned 4 of 5; third-party 0 of 5) | 1 | P1 L3-1 (owned story current, every third-party surface old or mixed); L3-2, L3-3, L3-4 |
| Offers | 1 | P1 L4-1 (no step between content and a 12-field demo form); L4-2, L4-3, L4-4, L4-5 |
| Motion and channels | 2 | No P1. L5-1 (directional), L5-2 |
| Measurement (outside-in only) | 2 | No P1. L6-1, L6-2, L6-3. Strength: hidden source fields, GCLID capture and Marketo Measure (Bizible) are in place |

Measurement scores 2, so a measurement fix is not forced to priority 1. Two of its findings (L6-1, L6-2) are prerequisites for reading the experiments below and are scheduled as week-0 checks.

## Priorities

### 1. The ICP cannot produce an account list or a reason to call now
- Findings: L1-1, L1-2, L1-3, L1-4
- Pipeline effect: accounts reached, opportunities created · Impact 4 · Effort S
- Play: Play 1, Merger-window consolidation review
- Depends on: none

### 2. Nothing sits between content and the demo form
- Findings: L4-1, L4-2, L4-3, L4-4
- Pipeline effect: first meetings, opportunities created · Impact 4 · Effort M
- Play: Play 2, Tour first, readout second
- Depends on: 1 (the readout needs a segment to benchmark against)

### 3. The current story stops at Outreach's own surfaces
- Findings: L3-1, L3-2, L3-3, L3-4, L5-1
- Pipeline effect: first meetings (shortlist inclusion), win rate · Impact 4 · Effort M
- Play: Play 3, Third-party proof for accounts already comparing
- Depends on: 1 (proof should match the segment)

### 4. Security and procurement reviewers wait for an account executive
- Findings: L2-2, L2-3, L4-5
- Pipeline effect: cycle length, win rate · Impact 3 · Effort S
- Play: Play 4, Committee pack before the second meeting
- Depends on: none (can run in parallel with 1)

Sequence: week 0 tag checks (L6-1, L6-2), then priority 1 and priority 4 together, priority 2 from week 2, priority 3's surface fixes from week 1 and its outbound step once priority 1's list exists. Plays 1 and 2 both reach RevOps and the CRO; run them on separate account lists so their effects can be read apart.

## Plays

### Play 1. Merger-window consolidation review
Acts on: L1-1, L1-4, L4-1, L4-3 · Priority: 1
Segment: US and EMEA B2B companies with 200 to 5,000 employees whose sales team runs Salesloft, Clari or both, on Salesforce (list built from job posts that name the tools, technographic data and the intent tools already on outreach.ai) · Trigger: the Salesloft and Clari merger (completed December 2025, one brand September 2026), visible in the account's own job posts and at contract renewal
Personas: Revenue operations lead (feels the cost of running two merging products) · CRO or VP Sales (signs) · IT or security reviewer (blocks)

Step 1. RevOps lead gets a short written stack review: which of their engagement, forecasting and conversation tools overlap, and what changes as the two products merge, plus a link to the self-guided product tour. Email and LinkedIn from the account executive who owns the territory. Owner AE (Commercial or Enterprise by size band).
  If they reply or open the tour, then offer a 30-minute working session with a solutions consultant to map their workflows onto one platform, owner AE, stage first meeting.
  If no response in 7 days, then send the same review to the CRO with a one-paragraph summary of the decision they face at renewal, owner AE.
  If the CRO engages first, then go to step 2.
Step 2. CRO gets a consolidation business case built from the working session: tools retired, seats, AI credit tier, and a named reference customer that consolidated (Freshworks is the public example on outreach.ai). Owner AE.
  If they agree to a call, then propose a scoped pilot on one team with a success criterion agreed in writing, owner AE, stage opportunity.
  If they say their renewal is more than 9 months away, then set a reminder 120 days before renewal and send quarterly product updates only, owner AE, stage nurture.
  If they raise security or procurement, then send the committee pack from Play 4 before the call, owner AE.
Step 3. Pilot runs 30 days on one team. Owner solutions consultant.
  If the success criterion is met, then commercial proposal, owner AE, stage proposal.
  If it is not met, then close with a written readout and a re-review at renewal, owner AE.
Exit. Opportunity created, or disqualified because the account has no renewal inside 12 months or has fewer than the minimum seats for a pilot.
Stops when. Three touches per persona with no response, or 30 days from first touch.

Why it should work: buyers prefer to get useful information without a rep (67% of B2B buyers prefer a rep-free experience [E-03]), so step 1 gives a written review and a tour before asking for time; and 73% of B2B buyers avoid suppliers who send irrelevant outreach [E-09], so the merger trigger gives every touch a reason specific to the account. No third-party evidence found that a vendor merger raises switching rates; that part rests on Outreach's own comparison page and the dates above.
Metric: opportunities created per 100 accounts worked · Leading indicator: replies and tour opens from RevOps leads in weeks 2 and 3
Review: week 10 · Kill rule: list accounts book no more first meetings than a matched holdout of Salesloft and Clari accounts worked with the standard demo offer by week 6 · Scale rule: opportunity rate above holdout at two reviews; extend to accounts running Gong only

### Play 2. Tour first, readout second
Acts on: L4-1, L4-2, L4-4, L2-4 · Priority: 2
Segment: B2B software and IT services companies with 51 to 1,000 employees on Salesforce or HubSpot, not in Play 1's list (matches the largest G2 reviewer group and the Commercial AE territory) · Trigger: a visitor from the account completes one of Outreach's tools (pipeline generation calculator, sales ROI calculator, AI maturity quiz) or attends the AI maturity webinar, or the account shows an intent surge in the intent tools already on the site
Personas: Sales development or sales operations manager (feels the prospecting and reporting load) · VP Sales or CRO (signs)

Step 1. The manager gets the self-guided product tour and a one-page benchmark readout comparing their tool inputs with the Outreach Insights Group benchmarks, by email within one business day of the trigger. Owner marketing operations.
  If they open the tour and reply or book, then a 30-minute readout with a solutions consultant on where agents would change their numbers, owner Commercial AE, stage first meeting.
  If no response in 5 days, then send one follow-up with a customer story from a company of the same size band (WithMe or Rootly are public examples), owner marketing operations.
  If the VP Sales engages first, then go to step 2.
Step 2. VP Sales gets the readout summary with a cost model at the right AI credit tier. Owner AE.
  If they agree to a call, then a scoped pilot proposal with one success criterion, owner AE, stage opportunity.
  If they ask for price first, then share the tier and a price range in writing before the call, owner AE.
Exit. Opportunity created, or disqualified because seat count is below the smallest viable deal.
Stops when. Two touches per persona with no response, or 21 days.

Why it should work: two out of three software buyers prefer to engage vendor salespeople only in the later stages of their buying journey [E-16, vendor-own], and 40% of technology buyers name "having to contact sales for a demo or free trial" among the top three things that make them less likely to buy [E-15, vendor-own, 2022]. A tour and a readout give these buyers a step that does not require a sales conversation first.
Metric: first meetings per 100 triggered accounts, then opportunities · Leading indicator: tour completions and readout bookings in weeks 2 and 3
Review: week 8 · Kill rule: triggered accounts given the tour and readout produce no more first meetings than triggered accounts sent to the demo form, by week 6 · Scale rule: more first meetings and an equal or better meeting-to-opportunity rate at week 8

### Play 3. Third-party proof for accounts already comparing
Acts on: L3-1, L3-2, L3-3, L3-4, L5-1 · Priority: 3
Prerequisite (owner product marketing, weeks 1 to 4): update the Gartner Peer Insights description, the AWS Marketplace listing and marketplace.outreach.io tile, and the Crunchbase profile to the current positioning and domain; change the request-demo page title and meta description; retire sampled ads that use older copy and pick one customer count.
Segment: ICP accounts from Play 1 or Play 2 lists that are researching the category: visits to Outreach's comparison pages, G2 category or compare pages, or the Gartner Peer Insights Revenue Action Orchestration market · Trigger: one of those research signals in the last 14 days
Personas: Revenue operations lead or sales operations manager (runs the evaluation) · CRO (signs) · procurement (blocks, when a shortlist is formal)

Step 1. The evaluator gets a third-party proof pack: the 2026 Gartner Magic Quadrant, Forrester Wave and IDC MarketScape placements (public summaries or licensed reprints), Gartner Peer Insights and G2 reviews from companies of their size band, and a side-by-side that states the one-platform versus merging-products point. Owner AE, supported by product marketing.
  If they reply or ask a comparison question, then offer a 30-minute session with a customer reference or a solutions consultant, owner AE, stage first meeting.
  If no response in 7 days, then send the CRO a two-line summary of the analyst placements with the same pack attached, owner AE.
  If procurement contacts first, then send the committee pack from Play 4, owner AE.
Step 2. CRO gets a reference call with a customer in the same industry and size band. Owner AE.
  If they agree, then a scoped evaluation plan with dates, owner AE, stage opportunity.
Exit. Opportunity created, or disqualified because the account has already signed with another vendor.
Stops when. Three touches per persona or 30 days.

Why it should work: B2B buyers value third-party interactions such as reviews and references 1.4 times more than digital supplier interactions [E-17]; software buyers now name AI chatbots as the top shortlist influence [E-19, vendor-own], and those answers draw on the third-party pages that still describe the older product; and 69% of B2B buyers report inconsistencies between a supplier's website and what its sellers say [E-26], which the prerequisite fixes reduce.
Metric: first meetings from accounts with a research signal · Leading indicator: Outreach named in third-party answers to five buyer questions (3 runs each, monthly) and reference-call requests by week 4
Review: week 12 · Kill rule: no change in third-party answer inclusion after the prerequisite fixes by week 8, and no difference in first meetings versus research-signal accounts not sent the pack · Scale rule: inclusion rises and first meetings beat the comparison group at week 12

### Play 4. Committee pack before the second meeting
Acts on: L2-2, L2-3, L4-5 · Priority: 4
Segment: accounts that request a demo or pricing in the 751 to 4,999 or 5,000+ employee bands on the demo form · Trigger: the form submission itself, or a contact-form request routed to Security
Personas: Revenue operations lead (feels the problem, runs the evaluation) · CRO (signs) · security reviewer and procurement (block)

Step 1. After the first meeting, the RevOps lead gets a committee pack to forward: security summary (SOC 2 Type II, ISO 27001, 27701 and 42001, HIPAA, CSA STAR), sub-processor list on the production domain, AI data-use terms, an order-form outline and the AI credit model explained in plain terms. Owner AE.
  If they forward it to security, then offer the security reviewer trust-center access the same day under NDA, owner solutions consultant, stage opportunity.
  If no response in 5 days, then ask the CRO who signs off on security and procurement, owner AE.
Step 2. Procurement gets the order-form outline and a written price range for the tier discussed. Owner AE.
  If they raise terms, then legal review starts in parallel with the evaluation, owner deal desk, stage proposal.
Exit. Security review cleared, or disqualified because the account requires a control Outreach does not hold.
Stops when. The opportunity closes, or 60 days with no security contact.

Why it should work: buying groups range "from five to 16 people across as many as four functions" [E-10], and buyers who experience buying-group relevance are three times more likely to report a high-quality deal [E-07]. A pack the first contact can forward reaches the rest of the group before they are in the room.
Metric: days from first meeting to security approval, and cycle length · Leading indicator: share of opportunities with a security contact engaged by day 14
Review: week 12 · Kill rule: no reduction in days to security approval versus the prior quarter's opportunities in the same bands · Scale rule: shorter time to approval with no fall in win rate; make the pack standard for all bands

## Experiments

### X1. Merger-window consolidation review
| Field | Content |
|---|---|
| Name | Merger-window consolidation review |
| Layer | ICP, Offers |
| Hypothesis | If RevOps leads at 200 to 5,000-employee companies running Salesloft or Clari get a written stack review and the product tour through AE outreach, then opportunities created per 100 accounts will move from unknown (baseline to be measured on the holdout) to above the holdout within 10 weeks, because the merger forces a platform decision at renewal and buyers prefer useful information before a rep conversation [E-03]. |
| Play | Play 1 |
| Finding(s) addressed | L1-1, L1-4, L4-1, L4-3 |
| Pipeline metric | Opportunities created |
| Leading indicator | Replies and tour opens from RevOps leads in weeks 2 and 3 |
| Expected lift | Low: no difference from holdout at this volume; the result is the list and the trigger, which priority 1 needs anyway. Mid: more first meetings than holdout, opportunity rate equal. High: higher opportunity rate than holdout. Sizes unknown outside-in; plan on the low case. |
| Supporting evidence | E-03 (analyst), E-09 (analyst). No third-party evidence found for merger-driven switching. |
| Window | 10 weeks |
| Owner | Sales leadership with revenue operations |
| Prerequisites | Account list with tool data; a matched holdout; opportunity source recorded at creation |
| Review date | Week 10 |
| Kill rule | No more first meetings than holdout by week 6 |
| Scale rule | Opportunity rate above holdout at two reviews |

### X2. Tour first, readout second
| Field | Content |
|---|---|
| Name | Tour and readout versus demo form |
| Layer | Offers |
| Hypothesis | If sales managers at 51 to 1,000-employee software companies who complete an Outreach tool get the product tour and a benchmark readout by email, then first meetings per 100 triggered accounts will move from unknown to above the demo-form group within 8 weeks, because most software buyers prefer to meet sales late [E-16]. |
| Play | Play 2 |
| Finding(s) addressed | L4-1, L4-2, L4-4 |
| Pipeline metric | First meetings, then opportunities created |
| Leading indicator | Tour completions and readout bookings in weeks 2 and 3 |
| Expected lift | Low: same first meetings, fewer form fields asked. Mid: more first meetings, same opportunity rate. High: more first meetings and opportunities. Unknown baseline; plan on the low case. |
| Supporting evidence | E-16 (vendor-own, G2), E-15 (vendor-own, TrustRadius, 2022) |
| Window | 8 weeks |
| Owner | Marketing operations with the Commercial sales team |
| Prerequisites | Tool completions captured against the account; demo conversion counted once (L6-1) |
| Review date | Week 8 |
| Kill rule | No more first meetings than the demo-form group by week 6 |
| Scale rule | More first meetings and equal or better meeting-to-opportunity rate at week 8 |

### X3. Third-party story sync and proof pack
| Field | Content |
|---|---|
| Name | Third-party story sync and proof pack |
| Layer | Messaging |
| Hypothesis | If Gartner Peer Insights, AWS Marketplace and Crunchbase carry the current positioning and researching ICP accounts get a third-party proof pack through AE outreach, then first meetings from research-signal accounts will move from unknown to above a comparison group within 12 weeks, because buyers weight third-party interactions above supplier channels [E-17]. |
| Play | Play 3 |
| Finding(s) addressed | L3-1, L3-2, L3-3, L3-4, L5-1 |
| Pipeline metric | First meetings |
| Leading indicator | Inclusion in answers to five buyer questions, 3 runs each, monthly, queried directly in the assistants buyers use |
| Expected lift | Low: third-party surfaces updated, no change in meetings inside 12 weeks. Mid: answer inclusion rises. High: inclusion rises and meetings beat comparison. Plan on the low case. |
| Supporting evidence | E-17 (analyst), E-19 (vendor-own, G2), E-26 (analyst) |
| Window | 12 weeks |
| Owner | Product marketing with sales leadership |
| Prerequisites | Direct AI-assistant baseline (not run in this audit); research signals mapped to accounts |
| Review date | Week 12 |
| Kill rule | No inclusion change by week 8 and no meeting difference |
| Scale rule | Inclusion and meetings both up at week 12 |

### X4. Committee pack
| Field | Content |
|---|---|
| Name | Committee pack before the second meeting |
| Layer | Audiences |
| Hypothesis | If RevOps leads at 751+ employee accounts get a forwardable security and procurement pack after the first meeting, then days from first meeting to security approval will fall from the prior-quarter baseline within 12 weeks, because buying groups span up to four functions [E-10]. |
| Play | Play 4 |
| Finding(s) addressed | L2-2, L2-3, L4-5 |
| Pipeline metric | Cycle length |
| Leading indicator | Share of opportunities with a security contact engaged by day 14 |
| Expected lift | Low: no change in cycle length; security contact engaged earlier. Mid: shorter time to security approval. High: shorter cycle and higher win rate. Plan on the low case. |
| Supporting evidence | E-10 (analyst), E-07 (analyst) |
| Window | 12 weeks |
| Owner | Sales leadership with security and deal desk |
| Prerequisites | Date of security approval recorded on the opportunity |
| Review date | Week 12 |
| Kill rule | No reduction in days to security approval versus prior quarter |
| Scale rule | Shorter approval time with no fall in win rate |

Results on counts of opportunities in the tens are `directional`. Compare with matched holdouts; do not claim significance.

## Findings

### Layer 1. ICP

| ID | Finding | Evidence (observed 2026-11-15) | Status | Severity | Pipeline effect | Root cause |
|---|---|---|---|---|---|---|
| L1-1 | No public surface names a segment, size band, region or trigger narrow enough to build an account list; the stated buyer is "revenue teams". | outreach.ai homepage title "Agentic AI Platform for Revenue Teams | Outreach"; pricing tiers framed by team maturity; site JSON-LD "sales, marketing, RevOps, and GTM teams" | observed | P1 | accounts reached, win rate | Positioning written for the category, not for a segment |
| L1-2 | Three size schemes are in use: demo and pricing forms (1-200, 201-750, 751-4999, 5,000+), the contact form (1-20, 21-500, 501-1,000, 1,001-3,000, 3,001+), and open AE roles (10 to 1,000; 5,000 to 10,000). | raw/marketo-form-1029.json; contact form 1081 descriptor; api.lever.co/v0/postings/outreach | observed | P2 | opportunities (segment results cannot be compared) | L1-1 |
| L1-3 | Proof leads with large industrial and transport enterprises (Siemens and Avis Budget Group on the homepage and demo page; SAP, Siemens, Verizon in press boilerplate) while the public reviewer base is mostly mid-market software: 2,163 of 3,662 G2 reviewers with a size (59%) work at 51 to 1,000 employees, and Computer Software plus IT and Services is 1,990 of 3,639 with an industry (55%). | g2.com/products/outreach/reviews (re-opened 2026-11-15); outreach.ai home and request-demo; Business Wire 2026-10-14 | inferred (G2 counts observed; reviews are cumulative and skew to users; customer sizes not enriched) | P2 | win rate | L1-1 |
| L1-4 | The clearest trigger in the category, the Salesloft and Clari merger, appears on the comparison page only. The homepage triggers are "AI is a board mandate" and tool sprawl. | outreach.ai/salesloft-vs-outreach: "Salesloft and Clari merged in December 2025 and consolidated under one brand in September 2026." (re-opened 2026-11-15); outreach.ai home | observed | P2 | first meetings | L1-1 |
| L1-5 | Story-hub industry tags look mis-assigned (Quantcast and Avanan tagged Telecommunications; two Siemens stories under different industries), so the hub filter is not a reliable segment signal. | outreach.ai/resources/stories | observed | P3 | none directly | none |

### Layer 2. Audiences

| ID | Finding | Evidence | Status | Severity | Pipeline effect | Root cause |
|---|---|---|---|---|---|---|
| L2-1 | Strength: six role pages (RevOps, Sales Leaders, Account Executives, Sales Managers, Sales Development, Customer Success) give the signer and the practitioner different arguments (forecasting and consolidation versus time saved). | outreach.ai homepage "Find your role"; /persona/ pages | observed | strength | win rate | n/a |
| L2-2 | Security reviewers see the certification list but cannot reach the trust center without a deal: "For Trust Center Access, Please Contact Your Account Executive." Two trust-page links point to outreach-staging.com (governance, sub-processors). | raw/trust.html (outreach.ai/platform/trust) | observed | P2 | cycle length | No path for the blocker before a deal |
| L2-3 | Procurement and finance get no prices, seat price or credit-pack price; two pricing FAQ answers open with the same sentence, "Reach out to your Outreach account executive, who can do a full walkthrough of the new packages and create a customized proposal for you." | raw/pricing.html | observed | P2 | cycle length | Same as L2-2 |
| L2-4 | Every role page ends in the same next step (Get a demo, Request a demo, View pricing info); the one CRO-level consolidation asset is written for existing customers (L4-3). | outreach.ai /persona/ pages; ICP notes | inferred | P2 | first meetings | L4-1 |
| L2-5 | Executive buyers are rare in third-party reviews: 98 of 3,544 G2 reviewers with a role are Executive Sponsors (2.8%). | g2.com/products/outreach/reviews (re-opened 2026-11-15) | observed (count); inferred (effect on signers) | P3 | win rate | none |

### Layer 3. Messaging

Current positioning, in one sentence: Outreach is an agentic AI platform for revenue teams whose AI agents work across prospecting, deal execution, conversation intelligence, coaching and forecasting in one platform ("Stop buying software. Start hiring AI agents."). Sources: outreach.ai homepage title, meta and H2, 2026-11-15; press release 2026-10-15.

Story sync table

| # | Surface | Score | Evidence (2026-11-15) |
|---|---|---|---|
| 1 | Homepage | new | Title "Agentic AI Platform for Revenue Teams | Outreach"; H2 "Stop buying software. Start hiring AI agents." (raw/home.html) |
| 2 | Pricing page | new | Title "Outreach Pricing & Plans | AI Credits Consumption Model"; H1 "AI Agent Platform Pricing for Revenue Teams" (raw/pricing.html) |
| 3 | Press releases, last six months | new | All releases May to October 2026 use agentic or revenue-orchestration framing (outreach.ai newsroom) |
| 4 | LinkedIn company page | new | Headline "Outreach Is the Only Complete Agentic AI Platform for Revenue Teams" (data-provider mirror dated 2026-11-12, not the live page); domain field still outreach.io |
| 5 | Paid search ads and landing pages | mixed | 12 most recent text ads in Google Ads Transparency Center: 2 current ("The #1 Agentic AI Platform for Revenue Teams"), 2 previous AI story ("AI revenue workflow platform"), 8 generic or older (email templates, discovery calls, meeting transcription). Landing page title "Request a Demo - AI Sales Engagement Platform | Outreach" |
| 6 | AI and search answers (directional) | old | Search results for five buyer questions frame Outreach as sales engagement or sales execution; no third-party list for "best agentic AI platform for revenue teams" named it. No assistant queried directly |
| 7 | Review sites | mixed | G2 vendor description is current. Gartner Peer Insights lists "Outreach Agentic AI Platform" (4.4, 198 ratings) with the description "Outreach Sales Execution Platform is a software designed to assist sales teams..." (re-opened 2026-11-15) |
| 8 | Comparison and alternatives pages | mixed | Of about 10 third-party pages read, 2 use current language (apollo.io, salescloser.ai); the rest say sales engagement or execution. Salesloft's own comparison page is titled "(2025)" |
| 9 | Wikipedia and Crunchbase | old | No Wikipedia article. Crunchbase: "Outreach is a sales engagement platform that uses AI for predictive analytics as it relates to sales." with www.outreach.io as the website (re-opened 2026-11-15) |
| 10 | Marketplaces and partner listings | mixed | Salesforce AppExchange listing is current. AWS Marketplace title "Outreach Sales Execution Platform" (re-opened 2026-11-15); marketplace.outreach.io AWS tile says "Sales Execution Platform" |

Story sync: 4 of 10. Owned 4 of 5. Third-party 0 of 5. No surface scored `needs data`.

| ID | Finding | Evidence | Status | Severity | Pipeline effect | Root cause |
|---|---|---|---|---|---|---|
| L3-1 | The current story runs on 4 of 5 owned surfaces and 0 of 5 third-party surfaces; Crunchbase, AWS Marketplace and the Gartner Peer Insights description still describe a sales engagement or sales execution platform. | Story sync table, surfaces 7, 9, 10 re-opened 2026-11-15 | observed | P1 | first meetings (shortlist inclusion) | Repositioning updated owned surfaces; third-party profiles were not in scope of the change |
| L3-2 | In search results for five buyer questions, Outreach appears in sales-engagement lists and is absent from third-party lists for "best agentic AI platform for revenue teams". | Firecrawl web search, US, 1 to 3 phrasings per question, 2026-11-15 | inferred, directional | P2 | first meetings | L3-1 |
| L3-3 | The page every "Get a demo" button leads to carries the older category in its title ("Request a Demo - AI Sales Engagement Platform | Outreach") and different proof numbers in its meta description ("boost productivity 30%, book 19% more meetings, and increase win rates 26%") from the homepage tiles (90% less prospecting time, 45% larger deals, 50% less meeting prep). Sampled ads give two customer counts, "Trusted By 5k+ Customers" and "6000+ Customers Trust Us". | raw/demo.html, raw/request-demo.html, raw/home.html; ads a04, a06, a12 re-read by OCR 2026-11-15 | observed | P2 | first meetings | L3-1 |
| L3-4 | "One platform", agents, acting on signals and MCP support appear on the Salesloft, Gong, Apollo and Revenue.io homepages; Outreach's most specific differentiator (Salesloft and Clari still bringing two products together) lives only on its comparison page. | Competitor homepages fetched 2026-11-15; outreach.ai/salesloft-vs-outreach | observed | P2 | win rate | L1-4 |
| L3-5 | The homepage recognition strip shows the 2024 Forrester Wave and a 2025 Constellation ShortList; the 2026 Gartner, Forrester and IDC Leader placements are not in it. Claim wording differs across surfaces ("#1", "only complete", "a leading"). | raw/home.html image alt text; ads; LinkedIn mirror; press boilerplate | observed | P3 | none directly | none |

### Layer 4. Offers

| ID | Finding | Evidence | Status | Severity | Pipeline effect | Root cause |
|---|---|---|---|---|---|---|
| L4-1 | Between content and the demo form there is no offer for a new-logo buyer: no trial, sandbox, scoped pilot, migration offer or assessment. The next step on the home, pricing, enterprise, role and comparison pages is a demo or pricing request with 12 required fields; the comparison page repeats "Request a demo" 6 times. | raw/marketo-form-1029.json (12 required fields: email, first and last name, title, phone, company, employees, seat count, country, email provider, CRM, terms checkbox); /free-trial returns 404; raw fetch of /salesloft-vs-outreach 2026-11-15 | observed | P1 | first meetings, opportunities | Offer ladder built for content and for sales, with no middle step |
| L4-2 | Two sampled ads promise "See the platform for yourself, without even talking to sales", and a self-guided tour exists at demo.outreach.io (linked from a blog post), but the home, platform, AI agents, pricing, enterprise and request-demo pages do not link it. | ads a01, a04 (OCR); outreach.ai/resources/blog/roll-out-ai-workflows-with-confidence links demo.outreach.io/share/4hrdfgd5s92i (returns 200); no demo.outreach.io link in any of the 41 captured pages (Outreach and competitor pages) | observed | P2 | first meetings | L4-1 |
| L4-3 | The consolidation content is written for existing customers ("If your team runs on Outreach, the data and workflows AI needs to create real value are already in place."), so the consolidation argument has no offer for a new logo. | raw/resources_reports-guides_ai-consolidation-playbook.html | observed | P2 | opportunities | L4-1 |
| L4-4 | After a demo request the confirmation page says "We'll follow up shortly to schedule time with our team." with no stated response time and no calendar; form data is passed to Qualified, so instant routing may exist but was not observed. | raw/demo-confirmed.html; raw/demo.html Qualified handler | observed (page); needs data (routing) | P2 | first meetings | none |
| L4-5 | Prices are not public; third-party pricing pages publish their own estimates, which do not agree with each other. | outreach.ai/pricing; third-party pricing pages listed in story-sync notes | observed | P2 | cycle length | L2-3 |
| L4-6 | Whether the calculators and quizzes gate their results behind a form could not be seen (rendered client-side). | outreach.ai/resources/tools | needs data | P3 | first meetings | none |

### Layer 5. Motion and channels

| ID | Finding | Evidence | Status | Severity | Pipeline effect | Root cause |
|---|---|---|---|---|---|---|
| L5-1 | Outreach product pages were absent from page 1 for 5 of 5 non-brand category and comparison queries checked; Gong and Salesloft product pages ranked for 3 of 4 category queries. | Firecrawl web search, US, one run per query, 2026-11-15; Semrush and Ahrefs unavailable | inferred, directional | P2 | accounts reached | L3-1 |
| L5-2 | Of 15 open roles, the GTM roles are two AEs, a solutions consultant, a CSM, a sales operations manager and a forward deployed engineer; none are SDR, BDR, demand generation, ABM or partner roles. The Commercial AE post lists "pipeline generation" among its KPIs. Intent and visitor-identification tags (6sense, Terminus, ZoomInfo WebSights, Intentsify) run on the site. | api.lever.co/v0/postings/outreach (15 postings, re-counted); raw/gtm-MVB4J5L.js | observed (roles, tags); inferred (AEs carry much of new-logo sourcing) | P2 | accounts reached | none |
| L5-3 | Webinars run at about 1.5 a month (9 from 2026-05-27 to 2026-11-10), gated. | outreach.ai/resources/webinars-videos | observed | P3 | first meetings | none |

### Layer 6. Measurement

| ID | Finding | Evidence | Status | Severity | Pipeline effect | Root cause |
|---|---|---|---|---|---|---|
| L6-1 | The Google Ads demo conversion tag (tag 429) fires on the demo form's success event and again through three rules on the /demo-confirmed page (page view, window load, trigger group), so one request can fire it more than once. Whether Google Ads counts it once depends on a setting not visible outside. | raw/gtm-MVB4J5L.js.resource.json, rules 4, 29, 30, 31 (re-parsed 2026-11-15) | inferred from observed config | P2 | opportunities (paid-search reporting) | none |
| L6-2 | The UTM cookie script writes 30-day cookies and overwrites them on every visit that carries UTM parameters, so the cookie-fed source fields record the most recent campaign and do not keep a permanent first touch; the script runs only with marketing consent. Marketo Measure (Bizible) is present and may hold first touch; its setup is not visible. | GTM tag 403 (43200-minute expiry); raw/marketo-form-1029.json hidden fields | observed (script); needs data (Bizible) | P2 | opportunities (source reporting) | none |
| L6-3 | The two LinkedIn conversion IDs fire only on a custom event named ga_event, and no captured page pushes that event, so LinkedIn may not record demo requests. | GTM rule 12; grep of raw/home.html, demo.html, pricing.html finds no ga_event | inferred | P2 | opportunities (paid-social reporting) | none |
| L6-4 | Microsoft UET and the G2 tag are classed functional in the consent setup, so they may fire for visitors who declined marketing cookies. | raw/gtm-MVB4J5L.js | inferred | P3 | none | none |
| L6-5 | The Google Ads conversion linker domain list includes staging and preview hosts and leaves out outreach.io subdomains, including demo.outreach.io where the product tour lives. | GTM tag 333 linker domains | observed | P3 | opportunities (tour attribution) | none |

## Parking lot

- L1-5: fix story-hub industry tags.
- L2-3: remove the repeated sentence from the pricing FAQ answers.
- L2-2: point trust-page links to the production domain.
- L2-5: ask executive sponsors for G2 and Peer Insights reviews.
- L3-5: put the 2026 analyst placements in the homepage strip; pick one claim wording.
- L5-3: measure webinars on first meetings from ICP accounts.
- L6-3, L6-4, L6-5: tag debug session; consent categories; linker domains.
- The MAIA AI demo agent (/speak-with-maia) is not in the main navigation; test it as a tour alternative after Play 2 reads out.
- Two home-page links still point to outreach.io/request-demo (a redirect hop).

## What we could not see

- What happens after a demo or pricing request (routing, response time, meeting booking). Would resolve: lead-to-first-touch timestamps by size band.
- Customer firmographics. Would resolve: enrichment of the 32 named customers.
- Which accounts run Salesloft, Clari or Gong. Would resolve: technographic or job-post data (Sumble was not authenticated).
- Win rate, cycle length and deal size by segment, and deals lost to Salesloft or Gong. Would resolve: CRM export of closed opportunities with segment and competitor fields.
- Paid search keywords and spend. Would resolve: a funded Semrush or Ahrefs plan, or the Google Ads account.
- AI assistant answers. Would resolve: direct queries to ChatGPT, Perplexity, Gemini and Claude, 3 runs per prompt.
- Google Ads conversion counting, Bizible configuration and Salesforce lead-source logic. Would resolve: admin access or a tag debug session.
- Whether calculators and quizzes gate results.

## Verify pass

- Re-opened 2026-11-15: Crunchbase, AWS Marketplace, Gartner Peer Insights market page, G2 reviews page, outreach.ai/salesloft-vs-outreach (live and raw). All held.
- Rechecked against raw files: page titles and meta descriptions, the 12 required demo-form fields, the trust-page text and staging links, the pricing FAQ sentence, the consolidation playbook sentence, the confirmation-page text, the GTM rules for the demo conversion and LinkedIn tags, the 43200-minute cookie, the Lever role list, and the 12 ad images (OCR re-run).
- Corrections from the evidence notes: home page links to outreach.io/request-demo 2 times, not 3; the demo form has 14 hidden fields, not 13; the AWS Marketplace product page reads "Outreach Sales Execution Platform" (the "only AI-powered Sales Execution Platform" wording in the notes is from the seller profile, not re-opened).
- Not a finding: scraper metadata reported noindex on /salesloft-vs-outreach; the raw page has no robots meta and no X-Robots-Tag header, and its canonical is self. The tag comes from the embedded Wistia player.
- Downgraded: L1-3 kept as `inferred` (no enrichment); L3-2 and L5-1 kept `directional`; L4-4 routing marked `needs data`.
- Recomputed: G2 size shares 702, 2,163 and 797 of 3,662 (19%, 59%, 22%); industries 1,990 of 3,639 (55%); Executive Sponsor 98 of 3,544 (2.8%); story sync 4 of 10.
- Dropped from evidence: Gong's multi-threading data (E-13) was re-opened and holds, but Gong is a direct competitor, so it is not used in an Outreach audit.

## Sources

Company sources (all observed 2026-11-15 unless noted):
- https://www.outreach.ai (home), /pricing, /enterprise, /request-demo, /demo-confirmed, /platform, /ai-agents, /platform/trust, /company/about, /company/contact, /company/newsroom, /resources/stories, /resources/tools and its calculators and quizzes, /resources/reports-guides/ai-consolidation-playbook, /resources/webinars-videos, /partners, /salesloft-vs-outreach, /speak-with-maia
- https://www.outreach.ai/resources/blog/roll-out-ai-workflows-with-confidence and https://demo.outreach.io/share/4hrdfgd5s92i
- Marketo form descriptors 1029, 1037, 1081 (insights.outreach.io); GTM container GTM-MVB4J5L
- https://api.lever.co/v0/postings/outreach
- Google Ads Transparency Center, advertiser "Outreach Corporation", 12 most recent text ads
- https://www.g2.com/products/outreach/reviews; https://www.gartner.com/reviews/market/revenue-action-orchestration; https://www.crunchbase.com/organization/outreach; https://aws.amazon.com/marketplace/pp/prodview-hm7n4y6z3x36i; Salesforce AppExchange listing; LinkedIn company page via data-provider mirror (2026-11-12)
- Business Wire release 2026-10-14; competitor homepages salesloft.com, gong.io, apollo.io, revenue.io
- Firecrawl web searches for the buyer questions and category queries listed in the findings

Third-party evidence (all re-opened and quotes confirmed 2026-11-15):
- E-03. Gartner, "Gartner Sales Survey Finds 67% of B2B Buyers Prefer a Rep-Free Experience", 2026-03-09. "67% of B2B buyers state that they prefer a rep‑free experience". 646 B2B buyers, Aug to Sep 2025. https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience (analyst, primary)
- E-09 and E-26. Gartner, "Gartner Sales Survey Finds 61% of B2B Buyers Prefer a Rep-Free Buying Experience", 2025-06-25. "73% of B2B buyers actively avoid suppliers who send irrelevant outreach." and "69% of B2B buyers report inconsistencies between information on the sales organization's website and that provided by sellers." 632 B2B buyers, Aug to Sep 2024. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience (analyst, primary)
- E-15. TrustRadius, "2022 B2B Buying Disconnect: The Age of the Self-Serve Buyer", 2022-06-14. "40% of buyers named “having to contact sales for a demo or free trial” among the top three things vendors do to make them less likely to buy." 2,185 buyers. https://www.trustradius.com/blog/2022-b2b-buying-disconnect-the-age-of-the-self-serve-buyer (vendor-own, primary; 2022, older than the three-year preference, so the year is shown)
- E-16. G2, "New G2 Research: How AI is Redefining the Buyer Journey in 2025 and How Sellers Can Adapt", 2025-05-14. Buyers "now prefer engaging with vendor salespeople only in the later stages of their buying journey". https://company.g2.com/news/buyer-behavior-in-2025 (vendor-own, primary)
- E-17. Gartner, "Gartner Marketing Survey Finds B2B Buyers Value Third-Party Interactions More Than Digital Supplier Interactions", 2023-06-08. "B2B buyers report that they value third-party interactions 1.4x more than digital supplier interactions". 771 B2B buyers, Nov to Dec 2022. https://www.gartner.com/en/newsroom/press-releases/2023-06-08-gartner-marketing-survey-finds-b2b-buyers-value-third-party-interactions-more-than-digital-supplier-interactions (analyst, primary)
- E-19. G2, "In the Answer Economy, Don't Win the Click, Win the Answer", 2026-04-15. "AI chatbots are now the top source influencing buyer shortlists, ahead of review sites, analyst firms, and vendor websites". 1,076 B2B software buyers, March 2026. https://company.g2.com/news/g2-research-the-answer-economy (vendor-own, primary; G2 sells reviews)
- E-07 and E-10. Gartner, "Gartner Sales Survey Finds 74% of B2B Buyer Teams Demonstrate 'Unhealthy Conflict' During The Decision Process", 2025-05-07. "Buying groups are more diverse than ever, ranging from five to 16 people across as many as four functions." and "when buyers experience buying group relevance, they are three times more likely to report a high-quality deal." 632 B2B buyers, Aug to Sep 2024. https://www.gartner.com/en/newsroom/press-releases/2025-05-07-gartner-sales-survey-finds-74-percent-of-b2b-buyer-teams-demonstrate-unhealthy-conflict-during-the-decision-process (analyst, primary)

Gartner multiples (3x, 1.4x) are self-reported survey outcomes. None of these figures is a forecast of Outreach's results.

Method: https://newlogogrowth.ai
