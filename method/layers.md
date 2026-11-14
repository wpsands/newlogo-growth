# The six layers

Audit in this order. Each layer depends on the ones above it. Score each layer 0 to 3 (definitions at the end) and stop recommending downstream fixes when an upstream layer scores 0 or 1. Tool references use `~~category` placeholders; see CONNECTORS.md.

---

## 1. ICP: who actually buys

**Question:** Does the company aim at the accounts that actually buy and win, defined tightly enough to build a list from?

**Outside-in checks**
- Compare the stated ICP (homepage, pricing page, about page, job posts) with the evidence of who buys: logos, case studies, review-site reviewer profiles, integrations, and customer job titles in testimonials.
- Use `~~enrichment` to firmographic-profile 10 to 20 visible customers (industry, size, region, tech stack). Note where they cluster and where the stated ICP is wider than that cluster.
- Look for situational fit, not only firmographics: what has to be true or have just happened for an account to buy (a new regulation, a security incident, a funding round, a new executive, a migration, a tool being sunset).
- Check whether the ICP could produce a named-account list. "Mid-market companies that care about security" cannot; "US healthcare providers with 500 to 5,000 employees running a certificate inventory in spreadsheets" can.

**Inside-out checks (if CRM data is supplied)**
- Win rate, deal size and cycle length by segment. Blended rates hide the real ICP.
- Closed-won accounts compared with the stated ICP. In many diagnostics, about half show a material mismatch.

**Common failures**
- Stated ICP is the market the company wants; actual customers are a different, narrower set.
- ICP described only by size and industry, with no trigger that makes an account ready now.
- Too many segments at once for the stage.

---

## 2. Audiences: who is in the room

**Question:** Within ICP accounts, does the company know who feels the problem, who signs, who blocks and who uses, and does it speak to each?

**Outside-in checks**
- Infer the buying committee from the product category, pricing tier, case-study quotes, job posts the company hires for, and the titles its content targets.
- Map which audiences the site, content and ads actually address. Note who is missing.
- Check whether the economic buyer and the person who feels the pain receive different arguments.
- For enterprise, check for distinct paths for security, procurement, IT and the business owner.

**Inside-out checks (if supplied)**
- Contact roles on won vs lost opportunities. Deals lost where a key role was never engaged.

**Common failures**
- One generic persona ("IT leaders").
- Messaging aimed at the signer while the person who feels the pain, and starts the search, is ignored.
- No content or offer for the blocker (security review, procurement, finance).

---

## 3. Messaging: the story each audience hears

**Question:** Does each audience get a clear, current story with proof, and is that story the same everywhere buyers meet it?

**Outside-in checks: the story sync check**

Score each surface `new` (current positioning), `mixed`, or `old` (a previous story still runs):

1. Homepage and top product pages (`~~web scraper`)
2. What AI assistants say about the company for buyer questions in the category (`~~AI visibility`, or run prompts directly). Run each prompt 3+ times; report consensus only.
3. Review sites (G2, Gartner Peer Insights, TrustRadius) category placement and review language
4. Wikipedia, Crunchbase, LinkedIn company page
5. Paid search ads and their landing pages (`~~SEO tool` paid research)
6. Organic search: which queries the company ranks for, and whether they match the current story (`~~SEO tool`)
7. Recent founder and executive posts, press releases
8. Outbound and the sales deck, if the user can supply samples

Report the **story sync rate**: the share of surfaces scored `new`. Report it three ways: overall, company-owned surfaces (site, ads, press, exec posts), and third-party surfaces (AI answers, review sites, Wikipedia, Crunchbase). The gap between owned and third-party is usually the most useful number, because third-party surfaces are where buyers form shortlists.

AI-answer probes: prefer direct queries to the assistants buyers use (ChatGPT, Perplexity, Gemini, Claude). If only search-engine AI overviews are available, say so at the top of the output and label those findings `directional`.

**Also check**
- Can a buyer tell within 10 seconds what the company does, for whom, and why now?
- Is each claim backed by proof a skeptic would accept (named customer, number with source, third-party validation)?
- Does the language match how buyers describe the problem, or only how the company describes its product?
- Competitive framing: what the 3 to 5 closest competitors claim, and whether this company's story is distinguishable from theirs.

**Common failures**
- Repositioning lag: new story on the homepage, old story in AI answers, review sites, ads and outbound.
- Feature lists in place of a problem the audience recognizes.
- Proof that is generic ("trusted by leading companies").

---

## 4. Offers: what each audience is asked to do

> **DRAFT: method owner to confirm.** This layer is written from general practice plus the offer-ladder principle in the method owner's own work. Replace or edit with your own criteria.

**Question:** At each stage of the buying journey, is there an offer worth the buyer's time and matched to their readiness?

**Outside-in checks**
- List every call to action on the site, in ads and in visible outbound. Map each to a stage: unaware, problem-aware, evaluating, ready to buy.
- Check for an offer at each stage. A company whose only offer is "Book a demo" has nothing for the 90%+ of the ICP that is not ready to talk to sales.
- Judge each offer on four tests:
  1. **Value before commitment.** Does the buyer get something useful (a diagnosis, a benchmark, a working result) before they give their time?
  2. **Cost to the buyer.** How much time, data, or internal political capital does accepting it take? Lower is better at early stages.
  3. **Fit to audience.** Is it built for a specific audience from layer 2, or for everyone?
  4. **Path to pipeline.** Does accepting it create a natural reason for a sales conversation, and is that hand-off defined?
- Pricing and packaging framing: is pricing visible or explained? Is there a clear entry point for the ICP's smallest viable deal? Do prices and terms match across surfaces?
- For product-led and hybrid: what the free or self-serve offer gives, and what moves a high-fit user toward sales.

**Strong offers usually look like**
- A short diagnostic or assessment that tells the buyer something true about their situation (the first look is free; the full answer is paid).
- A scoped pilot with a success criterion agreed up front.
- A calculator or benchmark grounded in sourced data.
- For self-serve: a frictionless first purchase, with account creation after payment, not before.

**Common failures**
- "Book a demo" as the only offer.
- Gated content as the main early-stage offer, scored on form fills.
- Free trial with no route from high-fit signups to a human.
- Offers that require the buyer to do work before getting value.
- Prices or terms that differ between the site, the store and sales.

---

## 5. Motion and channels: how the offer reaches the audience

**Question:** Given layers 1 to 4, which motions should carry the offer to the ICP, and are the current ones doing that?

Choose channels last. A channel is justified only by the audience it reaches and the offer it carries.

**Outside-in checks**
- What the company actually runs: paid search and paid social (`~~SEO tool` paid research, ad libraries), organic search footprint, partner and marketplace listings, events, community and founder presence, visible outbound signals (SDR job posts, sequences shared by the user).
- Whether each motion targets the ICP and carries a fitting offer, or buys volume.
- Speed and route of response: what happens after a buyer raises a hand (public SLAs, chat, calendar booking on the page).
- For hybrid companies: whether self-serve and enterprise teams compete for the same accounts or branded search terms.

**Inside-out checks (if supplied)**
- Time to first human response by segment.
- MQL to SQL conversion and whether MQLs are worked at all.
- Pipeline by source, with source definitions stated.

**Patterns this method favors**
- Signal-based outbound to a named-account list, with the reason for each account visible to the rep.
- Speed-to-first-human-response SLAs tiered by segment.
- Routing low-ACV buyers to self-serve and high-fit self-serve buyers to sales.
- Founder-led content and teardowns at seed to Series A, measured on meetings.

**Patterns this method discounts**
- Generic cold lists, and AI that sends more generic email.
- Paid programs optimized for the cheapest form fill.
- Event booths with no meetings booked in advance.
- A/B tests and landing-page tweaks presented as a growth strategy.
- Adding a new motion before the weakest existing one is fixed.

---

## 6. Measurement: can the pipeline effect be seen

**Question:** If an experiment worked, would the company be able to tell?

**Outside-in checks**
- Analytics and tag presence on key pages (tag manager, analytics, CRM forms) via page source.
- Cross-domain journeys (site to store to app) that would break attribution.

**Inside-out checks (if supplied)**
- Definitions of sourced vs influenced pipeline, and whether they have changed.
- A permanent first-touch stamp on contacts and accounts.
- Stage definitions with entry and exit criteria; phantom or stale opportunities.
- Organic and AI-referral traffic visible in the CRM.

**Common failures**
- Deal-source logic changed mid-year; trends are not comparable.
- No first-touch capture; every source fight is opinion.
- Dashboards built before definitions.

**Rule:** if measurement scores 0 or 1, the first priority in the plan is a measurement fix, and no lift may be claimed until it ships.

---

## Layer scores

| Score | Meaning |
|---|---|
| 0 | Missing or broken. Downstream work on this basis will fail. |
| 1 | Present but weak or inconsistent. Fix before scaling anything that depends on it. |
| 2 | Sound with specific gaps. Targeted fixes. |
| 3 | Strong. Use as a base for experiments. |

Each score must cite the findings that justify it.
