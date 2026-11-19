#!/usr/bin/env python3
"""Write made-up CRM exports with known answers.

Every row is invented. No client data belongs in this repository. The files are
built from fixed counts, with no randomness, so every expected figure in
EXPECTED below can be worked out by hand from PRE_WINDOW and WINDOW.

Shape of the data:
  - Eight quarters, 2025Q1 to 2026Q4.
  - Through 2026Q1, half of all closes are "Closed Cancelled". From 2026Q2 none
    are. That is the planted definition break. The analysis window is
    2026Q2 to 2026Q4.
  - Inside the window the win rate differs by team, industry and partner, and one
    industry (Retail) has only six decided deals.

Usage:
  python3 tests/fixtures.py <output directory>
"""
import csv
import os
import sys

PRE_QUARTERS = [(2025, 2), (2025, 5), (2025, 8), (2025, 11), (2026, 2)]
WINDOW_QUARTERS = [(2026, 5), (2026, 8), (2026, 11)]

# (team, industry, partner, stage, rows per quarter)
PRE_WINDOW = [
    ("Enterprise", "Software", "", "Closed Won", 20),
    ("Enterprise", "Software", "", "Closed Lost", 30),
    ("Enterprise", "Software", "", "Closed Cancelled", 50),
]
WINDOW = [
    ("Enterprise", "Health", "Acme Partners", "Closed Won", 20),
    ("Enterprise", "Health", "", "Closed Won", 5),
    ("Enterprise", "Software", "", "Closed Won", 15),
    ("Enterprise", "Health", "Acme Partners", "Closed Lost", 10),
    ("Enterprise", "Health", "", "Closed Lost", 10),
    ("Enterprise", "Software", "", "Closed Lost", 40),
    ("SMB", "Software", "", "Closed Won", 20),
    ("SMB", "Software", "", "Closed Lost", 78),
    ("SMB", "Retail", "", "Closed Lost", 2),
]
# Loss reasons for the 140 lost rows of each window quarter, in row order.
WINDOW_REASONS = [("Went dark", 70), ("Price", 28), ("Chose competitor", 28), ("Duplicate", 14)]

EXPECTED = {
    "rows": 1100,
    "window_start": "2026Q2",
    "window_end": "2026Q4",
    "break_between": ["2026Q1", "2026Q2"],
    "window": {"won": 180, "lost": 420, "other_closed": 0, "win_rate": 0.30},
    # The two wrong answers a blended calculation gives.
    "blended_won_over_decided": round(280 / 850, 4),
    "blended_won_over_all_closed": round(280 / 1100, 4),
    "team": {"Enterprise": (120, 180), "SMB": (60, 240)},
    "industry": {"Health": (75, 60), "Software": (105, 354), "Retail": (0, 6)},
    "partner": {"partner on the deal": (60, 30), "no partner": (120, 390)},
    "loss_groups": {"no decision": 210, "price or budget": 84, "competitor": 84, "duplicate": 42},
    "win_rate_excluding_duplicates": round(180 / (180 + 378), 4),
    "roles_partner": {"1": (30, 30), "2": (30, 0)},
    "roles_no_partner": {"0": (0, 6), "1": (120, 384)},
    "window_opps_without_roles": 6,
    "lost_exits": {"Qualify": 300, "Proposal": 120},
    "open": {"count": 40, "aged_over_180": 10},
}


def build_closed():
    rows = []
    n = 0
    for quarters, spec, in_window in ((PRE_QUARTERS, PRE_WINDOW, False), (WINDOW_QUARTERS, WINDOW, True)):
        for (y, m) in quarters:
            reasons = [r for r, c in WINDOW_REASONS for _ in range(c)]
            lost_seen = 0
            for team, industry, partner, stage, count in spec:
                for _ in range(count):
                    n += 1
                    reason = ""
                    if stage == "Closed Lost":
                        reason = reasons[lost_seen] if in_window else "Went dark"
                        lost_seen += 1
                    rows.append({
                        "Opportunity ID": f"OPP{n:05d}",
                        "Stage": stage,
                        "Close Date": f"{y}-{m:02d}-15",
                        "Amount": 10000,
                        "Owner Role": team,
                        "Industry": industry,
                        "Lead Source": "Inbound" if n % 2 else "Outbound",
                        "Partner Account": partner,
                        "Closed Lost Reason": reason,
                        "_window": in_window,
                    })
    return rows


def write(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def make(outdir):
    os.makedirs(outdir, exist_ok=True)
    closed = build_closed()
    closed_fields = ["Opportunity ID", "Stage", "Close Date", "Amount", "Owner Role", "Industry",
                     "Lead Source", "Partner Account", "Closed Lost Reason"]
    paths = {k: os.path.join(outdir, f"{k}.csv") for k in
             ("closed", "open", "stage_history", "contact_roles", "pipeline_by_source", "won_report")}
    write(paths["closed"], closed, closed_fields)

    # Contact roles, window deals only. Every partner deal also carries a
    # "Partner Contact" role, which is not a buyer role and must not be counted.
    roles = []
    second_role_left = 30  # half of the 60 partner wins get a second buyer role
    for r in closed:
        if not r["_window"]:
            continue
        if r["Industry"] == "Retail":
            continue  # six deals with no role at all
        roles.append({"Opportunity ID": r["Opportunity ID"], "Contact Role": "Decision Maker", "Title": "Director"})
        if r["Partner Account"]:
            roles.append({"Opportunity ID": r["Opportunity ID"], "Contact Role": "Partner Contact", "Title": "Partner Manager"})
            if r["Stage"] == "Closed Won" and second_role_left:
                second_role_left -= 1
                roles.append({"Opportunity ID": r["Opportunity ID"], "Contact Role": "Economic Buyer", "Title": "CFO"})
    write(paths["contact_roles"], roles, ["Opportunity ID", "Contact Role", "Title"])

    # Stage history: one closing row per lost window deal.
    hist = []
    for q in range(len(WINDOW_QUARTERS)):
        lost = [r for r in closed if r["_window"] and r["Stage"] == "Closed Lost"][q * 140:(q + 1) * 140]
        for i, r in enumerate(lost):
            hist.append({"Opportunity ID": r["Opportunity ID"], "From Stage": "Qualify" if i < 100 else "Proposal",
                         "To Stage": "Closed Lost", "Changed Date": r["Close Date"]})
    write(paths["stage_history"], hist, ["Opportunity ID", "From Stage", "To Stage", "Changed Date"])

    # Open pipeline.
    open_rows = [{"Opportunity ID": f"OPEN{i:04d}", "Stage": "Qualify" if i < 25 else "Proposal",
                  "Close Date": "2027-06-30", "Amount": 10000, "Age": 200 if i < 10 else 40,
                  "Owner Role": "Enterprise"} for i in range(40)]
    write(paths["open"], open_rows, ["Opportunity ID", "Stage", "Close Date", "Amount", "Age", "Owner Role"])

    # A summary-style export with no opportunity ID, covering all eight quarters.
    write(paths["pipeline_by_source"], closed, ["Lead Source", "Stage", "Close Date", "Amount"])

    # A second export of the same deals that is ten wins short.
    dropped = 0
    short = []
    for r in closed:
        if r["Stage"] == "Closed Won" and dropped < 10:
            dropped += 1
            continue
        short.append(r)
    write(paths["won_report"], short, closed_fields)
    return paths


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    for name, p in make(sys.argv[1]).items():
        print(f"{name}: {p}")
