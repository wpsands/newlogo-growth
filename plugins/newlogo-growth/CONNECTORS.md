# Connectors

## How tool references work

Plugin files use `~~category` placeholders for whatever tool you connect in that category. The skills fall back to web search and page fetching when a category is not connected, and they say which checks lost coverage.

## Connectors for this plugin

| Category | Placeholder | Used for | Options |
|---|---|---|---|
| Web scraper | `~~web scraper` | Site pages, pricing, careers, case studies, review sites | Firecrawl, built-in web fetch |
| SEO tool | `~~SEO tool` | Organic keywords, paid search ads, competitor overlap | Ahrefs, Semrush, Similarweb |
| Enrichment | `~~enrichment` | Firmographics for customers and target accounts | Clay, Apollo, ZoomInfo, Crunchbase |
| AI visibility | `~~AI visibility` | What AI assistants say about the company for buyer questions | Ahrefs Brand Radar; Semrush AI toolkit; or the optional `ai_probe.py` tool (method/tools.md) |
| Research (optional) | `~~research` | Analyst and consultancy research behind plays | Gartner, Forrester or IDC subscriptions; otherwise public summaries via web search |
| CRM (optional) | `~~CRM` | Win rate by segment, source definitions, stage hygiene | HubSpot, Salesforce, or CSV exports. The reports to pull are listed in `method/crm-reports.md`; the optional `crm_profile.py` tool profiles them (method/tools.md) |
| Analytics (optional) | `~~analytics` | Traffic sources, cross-domain journeys, signup to sales routing | GA4, PostHog, Amplitude, or a CSV export |

Only the company URL is required. Everything else improves coverage.
