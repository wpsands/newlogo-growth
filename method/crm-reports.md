# CRM reports to pull

Use this when the user offers CRM data, or asks what to export. Hand them this list as written. The audit still runs from a URL alone; these reports turn `inferred` findings into measured ones and give every play a baseline.

Four reports are required for a useful read. Three more are optional. Ask for all of them in one request so the user makes one trip to sales operations.

## Rules for every report

- **One population.** Every report uses the same filter for motion and deal type (for example: new business only, enterprise record type, renewals and upsells excluded). Write the filter at the top of each file name or in a note.
- **The opportunity ID in every report.** Use the 18-character ID in Salesforce or the record ID in HubSpot. Without it the reports cannot be joined, and figures from two reports cannot be compared.
- **Detail rows, not a summary.** One row per record. Export the full detail as CSV, not the grouped on-screen view.
- **Eight quarters by close date** for closed opportunities, so a change in definitions or practice shows up. State whether the date filter is on close date or created date.
- **Include every closed outcome.** Won, lost and any other closed stage (cancelled, disqualified, no decision, duplicate). Leaving one out hides how the win rate is built.
- **Include owner team or role.** Reports named for one motion often contain other teams. The audit splits by team before it says anything about the ICP.
- **One currency, stated.** Use the converted amount field and name the currency. Say whether the amount is ACV, first-year value or total contract value.
- **No personal data that is not needed.** Contact reports need the role and job title, not names, emails or phone numbers. Use the contact ID.

## Required

### 1. Closed opportunities
Every opportunity in the population that closed in the last eight quarters, any closed stage.

| Field | Why |
|---|---|
| Opportunity ID, account name or ID | joins and account-level counts |
| Stage, close date, created date | outcomes by quarter, cycle length, definition breaks |
| Amount (ACV, converted) and contract term | deal size, value-weighted win rate |
| Deal type and record type | confirms the population |
| Owner, owner role or team, region | team split, coverage |
| Account industry, employee count, billing country | segment cuts for the ICP |
| Lead source and primary campaign | source cuts |
| Partner account on the opportunity, partner deal type | partner-involved versus partner-sourced |
| Closed reason, loss reason, competitor | loss mix: no decision, disqualified, price, feature, competitor |
| Forecast category, age | hygiene checks |

Salesforce: an Opportunities report with these columns. HubSpot: a deals export with the same properties.

### 2. Open pipeline
Every open opportunity in the same population, with the fields from report 1 plus next step, last activity date and last stage change date. Used for aged and stale pipeline, past-due close dates and stage mix. It also shows which accounts a play would touch.

### 3. Stage history
One row per stage change for the opportunities in reports 1 and 2: opportunity ID, from stage, to stage, change date, and days in the earlier stage if the CRM stores it. Used for where lost deals leave, time in stage and legacy stage names.

Salesforce: an Opportunity History report. HubSpot: the "date entered" and "date exited" properties for each deal stage on the deals export.

### 4. Contact roles
One row per contact role on the opportunities in reports 1 and 2: opportunity ID, contact ID, job title, role, and whether the contact is primary. Add the date the role was added if the CRM stores it; that separates roles added early from roles added to deals already won. Used for buying-group coverage on won versus lost deals.

Salesforce: an Opportunities with Contact Roles report. HubSpot: deal-to-contact associations with job title and any buying-role property.

## Optional

### 5. Leads and conversion
Leads or contacts created in the same eight quarters: created date, source, status or lifecycle stage with dates, owner, converted date, converted opportunity ID, and the date of the first sales activity. Used for speed to first human response, lead-to-opportunity conversion by source, and whether leads are worked at all.

### 6. Meetings and activities
First meeting date per opportunity or account, or the task and event log with type, date and related opportunity ID. Used for the first-meetings baseline that most plays measure against.

### 7. Campaign responses
Campaign members with response date and related opportunity ID, or the campaign influence report. Used only to see which programs already run against a segment, so a play does not propose something already in market.

## Ask sales operations these five questions

The exports cannot answer these, and the audit needs them to read the data correctly.

1. What does each closed stage mean today, and has that changed in the last two years? If so, when?
2. How is lead source set, and does any other field (a BDR or SDR flag, a partner field) override it in reporting?
3. Which teams and owner roles belong to the motion being audited?
4. What are the stage entry and exit rules, and which stage names are retired?
5. What changed in headcount, territories or segment ownership in the period?

## What happens with the files

Run `scripts/crm_profile.py` on the exports first (layers.md, "Reading CRM exports"). It reports what each file contains, whether the files agree, where the closed definition changed, and the standard cuts inside one consistent window. Supplied data is used for this run only, is labeled `supplied` in the report, and never goes into a public output or the plugin directory.

## If the user can pull only one report

Pull report 1 with every field listed. It supports the win-rate window, the team split, segment and source cuts, the partner comparison and the loss mix. Say in the coverage line that stage, contact-role and open-pipeline findings are `needs data`.
