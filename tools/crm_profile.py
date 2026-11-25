#!/usr/bin/env python3
"""Profile CRM opportunity exports before any rate is used in a finding.

Optional tool for the newlogo-growth plugin (layers.md, "Reading CRM exports"; the reports
are described in method/crm-reports.md). Standard library only. Reads CSV files,
prints a markdown report and can write the same tables as JSON.

What it does:
  1. Inventory: rows, unique IDs, date range, which columns were found.
  2. Reconciliation: ID overlap and won totals across the files supplied.
  3. Outcomes by quarter: won, lost, other closed, both win-rate ratios, won value.
  4. Definition break: finds the quarter where the share of "other closed"
     outcomes changes, and picks the most recent run of quarters on one definition.
  5. Standard cuts inside that window: team, region, industry, company size,
     deal size, lead source, partner on the deal. Each rate shows its counts and a
     95% interval, and is marked "low n" below --min-n decided deals.
  6. Loss mix inside the window, grouped into no decision, disqualified,
     duplicate, price, product, competitor and other.
  7. Contact roles (optional): win rate by number of buyer roles, with partner
     and placeholder roles removed, split by partner involvement.
  8. Stage history (optional): the stage lost deals left from, inside the window.
  9. Open pipeline (optional): count, value, aged and past-due.

The script reports; it does not interpret. Rates are correlations. Output holds
client data: keep it in the run's working directory, never in the plugin or a
public file.

Example:
  python3 crm_profile.py --closed closed.csv --open open.csv \
    --history stage_history.csv --roles contact_roles.csv --json profile.json

Columns are found by name. Override any of them with --map, for example:
  --map amount="Year 1 ACV" --map team="Sales Team"
Keys: id stage close created amount team owner region industry employees
      country source partner reason competitor role from_stage to_stage age
"""
import argparse
import csv
import json
import math
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date, datetime

CANDIDATES = {
    "id": ["opportunity id 18", "opportunity id", "deal id", "record id", "opportunity id (18)"],
    "stage": ["stage", "deal stage", "stage name"],
    "close": ["close date"],
    "created": ["created date", "create date"],
    "amount": ["acv (converted)", "acv", "amount (converted)", "amount", "amount in company currency"],
    "team": ["owner role", "opportunity owner role", "team", "sales team", "hubspot team"],
    "owner": ["opportunity owner", "deal owner", "owner"],
    "region": ["user region", "region", "owner region"],
    "industry": ["industry", "account industry"],
    "employees": ["employees", "number of employees", "employee count"],
    "country": ["billing country", "country", "country/region"],
    "source": ["lead source", "original source", "deal source"],
    "partner": ["enterprise partner", "partner account", "partner", "partner name"],
    "reason": ["closed reason", "closed lost reason", "loss reason", "lost reason"],
    "competitor": ["competitor lost to", "competitor", "lost to competitor"],
    "role": ["contact role", "role", "buying role"],
    "from_stage": ["from stage", "old value", "previous stage"],
    "to_stage": ["to stage", "new value", "stage"],
    "age": ["age", "deal age"],
}

DATE_FORMATS = ("%m/%d/%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%m/%d/%y", "%Y-%m-%d %H:%M:%S")
DAYFIRST_FORMATS = ("%d/%m/%Y", "%Y-%m-%d", "%d/%m/%y", "%d.%m.%Y")

LOSS_GROUPS = [
    ("duplicate", ["duplicate"]),
    ("data clean-up", ["clean-up", "cleanup", "clean up", "stagnant", "test"]),
    ("disqualified", ["qualif", "not a fit", "no fit", "authority"]),
    ("no decision", ["unresponsive", "no response", "lost contact", "no decision", "delayed",
                     "deprioriti", "cancelled", "canceled", "timing", "momentum", "went dark",
                     "no longer funded", "priorit"]),
    ("price or budget", ["price", "pricing", "budget", "expensive", "cost"]),
    ("product", ["feature", "missing", "poc", "proof of concept", "functionality", "product"]),
    ("competitor", ["competitor", "chose", "incumbent", "lost to"]),
]

NON_BUYER_ROLE_WORDS = ["partner", "reseller", "contact primary", "primary contact", "other", "internal"]


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    return rows


def find_columns(rows, overrides):
    if not rows:
        return {}
    lower = {c.lower().strip(): c for c in rows[0].keys() if c}
    found = {}
    for key, names in CANDIDATES.items():
        if key in overrides:
            if overrides[key] not in rows[0]:
                sys.exit(f"--map {key}={overrides[key]!r}: no such column")
            found[key] = overrides[key]
            continue
        for n in names:
            if n in lower:
                found[key] = lower[n]
                break
    return found


def num(x):
    try:
        return float(str(x).replace(",", "").replace("$", ""))
    except (TypeError, ValueError):
        return None


def parse_date(x, dayfirst):
    x = (x or "").strip()
    if not x:
        return None
    for f in (DAYFIRST_FORMATS if dayfirst else DATE_FORMATS):
        try:
            return datetime.strptime(x, f).date()
        except ValueError:
            continue
    return None


def quarter(d, fiscal_start):
    m = (d.month - fiscal_start) % 12
    y = d.year if d.month >= fiscal_start else d.year - 1
    if fiscal_start != 1:
        y += 1
    return f"{y}Q{m // 3 + 1}"


def outcome(stage):
    s = (stage or "").lower()
    if "won" in s:
        return "won"
    if "lost" in s:
        return "lost"
    if s.startswith("closed") or s.startswith("close ") or "cancel" in s or "disqualif" in s:
        return "other"
    return "open"


def wilson(w, n):
    if n == 0:
        return (0.0, 0.0)
    z = 1.96
    p = w / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - h) / d), min(1.0, (c + h) / d))


def pct(x):
    return f"{100 * x:.1f}%"


def band(v, edges, labels):
    if v is None:
        return "blank"
    for e, lab in zip(edges, labels):
        if v < e:
            return lab
    return labels[-1]


def loss_group(text):
    t = (text or "").lower().strip()
    if not t:
        return "blank"
    for name, words in LOSS_GROUPS:
        if any(w in t for w in words):
            return name
    return "other"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def cut(rows, keyf, min_n, top=25):
    g = defaultdict(lambda: {"won": 0, "lost": 0, "amt": []})
    for r in rows:
        k = keyf(r)
        k = k if k not in (None, "") else "blank"
        if r["_o"] == "won":
            g[k]["won"] += 1
            if r["_amt"] is not None:
                g[k]["amt"].append(r["_amt"])
        elif r["_o"] == "lost":
            g[k]["lost"] += 1
    out = []
    for k, v in g.items():
        n = v["won"] + v["lost"]
        if n == 0:
            continue
        lo, hi = wilson(v["won"], n)
        out.append({
            "value": k, "won": v["won"], "lost": v["lost"], "decided": n,
            "win_rate": round(v["won"] / n, 4), "ci_low": round(lo, 4), "ci_high": round(hi, 4),
            "median_won_amount": round(statistics.median(v["amt"])) if v["amt"] else None,
            "won_amount": round(sum(v["amt"])), "low_n": n < min_n,
        })
    out.sort(key=lambda d: -d["decided"])
    return out[:top]


def cut_table(rows):
    return table(
        ["Value", "Won", "Lost", "Decided", "Win rate", "95% interval", "Median won", "Won value", "Note"],
        [[d["value"], d["won"], d["lost"], d["decided"], pct(d["win_rate"]),
          f"{pct(d['ci_low'])} to {pct(d['ci_high'])}", d["median_won_amount"] if d["median_won_amount"] is not None else "",
          d["won_amount"], "low n" if d["low_n"] else ""] for d in rows])


def main():
    ap = argparse.ArgumentParser(description="Profile CRM opportunity exports.")
    ap.add_argument("--closed", required=True, help="closed opportunities CSV (report 1)")
    ap.add_argument("--open", dest="open_", help="open pipeline CSV (report 2)")
    ap.add_argument("--history", help="stage history CSV (report 3)")
    ap.add_argument("--roles", help="contact roles CSV (report 4)")
    ap.add_argument("--extra", action="append", default=[], help="another opportunity export to reconcile against (repeatable)")
    ap.add_argument("--map", action="append", default=[], help="column override, key=Column Name (repeatable)")
    ap.add_argument("--min-n", type=int, default=30, help="decided deals below this are marked low n (default 30)")
    ap.add_argument("--window-start", help="first quarter of the analysis window, e.g. 2026Q2 (default: detected)")
    ap.add_argument("--break-points", type=float, default=0.10, help="share change that counts as a definition break (default 0.10)")
    ap.add_argument("--fiscal-start-month", type=int, default=1, help="first month of the fiscal year (default 1)")
    ap.add_argument("--dayfirst", action="store_true", help="dates are day/month/year")
    ap.add_argument("--exclude-team", action="append", default=[], help="team or role substring to leave out of the window cuts (repeatable)")
    ap.add_argument("--json", help="write the tables to this JSON file")
    a = ap.parse_args()

    overrides = {}
    for m in a.map:
        if "=" not in m:
            sys.exit(f"--map needs key=Column, got {m!r}")
        k, v = m.split("=", 1)
        overrides[k.strip()] = v.strip()

    res = {"generated": date.today().isoformat(), "min_n": a.min_n}
    P = print

    closed = load(a.closed)
    col = find_columns(closed, overrides)
    for need in ("stage", "close"):
        if need not in col:
            sys.exit(f"closed file: no {need} column found; pass --map {need}=\"Column Name\"")
    for r in closed:
        r["_o"] = outcome(r[col["stage"]])
        r["_d"] = parse_date(r[col["close"]], a.dayfirst)
        r["_q"] = quarter(r["_d"], a.fiscal_start_month) if r["_d"] else None
        r["_amt"] = num(r[col["amount"]]) if "amount" in col else None
        r["_id"] = r[col["id"]] if "id" in col else None
        r["_partner"] = bool(r[col["partner"]].strip()) if "partner" in col else None
    undated = sum(r["_d"] is None for r in closed)
    still_open = sum(r["_o"] == "open" for r in closed)
    cl = [r for r in closed if r["_o"] != "open" and r["_q"]]

    P("# CRM profile\n")
    P(f"Generated {res['generated']}. Rates below --min-n {a.min_n} decided deals are marked `low n`. Every figure is `supplied` data.\n")

    # 1. inventory
    P("## 1. Inventory\n")
    ids = [r["_id"] for r in closed if r["_id"]]
    dates = [r["_d"] for r in closed if r["_d"]]
    inv = {
        "file": a.closed, "rows": len(closed), "unique_ids": len(set(ids)) if ids else None,
        "duplicate_ids": len(ids) - len(set(ids)) if ids else None,
        "close_date_range": [min(dates).isoformat(), max(dates).isoformat()] if dates else None,
        "rows_without_close_date": undated, "rows_not_closed": still_open,
        "columns_found": col, "columns_missing": sorted(k for k in CANDIDATES if k not in col and k not in ("role", "from_stage", "to_stage")),
        "stages": dict(Counter(r[col["stage"]] for r in closed).most_common()),
    }
    res["inventory"] = inv
    P(f"- Closed file: {inv['rows']} rows, {inv['unique_ids']} unique IDs, {inv['duplicate_ids']} duplicate IDs.")
    if dates:
        P(f"- Close dates {inv['close_date_range'][0]} to {inv['close_date_range'][1]}; {undated} rows without a readable close date; {still_open} rows not in a closed stage (left out).")
    P(f"- Columns found: {', '.join(f'{k}={v!r}' for k, v in col.items())}.")
    if inv["columns_missing"]:
        P(f"- Columns not found (cuts that need them are skipped): {', '.join(inv['columns_missing'])}.")
    P(f"- Stage values: {', '.join(f'{k} {v}' for k, v in inv['stages'].items())}.")
    if "id" not in col:
        P("- No opportunity ID column: this file cannot be joined to the others.")
    if "team" in col:
        teams = Counter(r[col["team"]] or "blank" for r in closed)
        res["teams"] = dict(teams.most_common())
        P(f"- Owner teams or roles in the file ({len(teams)}): {', '.join(f'{k} {v}' for k, v in teams.most_common(12))}{' ...' if len(teams) > 12 else ''}. Confirm which belong to the motion being audited.")
    P("")

    # 2. reconciliation
    others = [("open", a.open_), ("history", a.history), ("roles", a.roles)] + [(f"extra {i + 1}", p) for i, p in enumerate(a.extra)]
    loaded = {}
    rec = []
    base_ids = set(ids)
    won_base = [r for r in closed if r["_o"] == "won"]
    for name, path in others:
        if not path:
            continue
        rows = load(path)
        c = find_columns(rows, {})
        loaded[name] = (rows, c)
        entry = {"file": path, "name": name, "rows": len(rows), "has_id": "id" in c}
        if "id" in c and base_ids:
            oid = {r[c["id"]] for r in rows if r[c["id"]]}
            entry.update({"unique_ids": len(oid), "ids_also_in_closed": len(oid & base_ids), "ids_not_in_closed": len(oid - base_ids)})
        if "stage" in c and name.startswith("extra"):
            w = [r for r in rows if outcome(r[c["stage"]]) == "won"]
            entry["won_count"] = len(w)
            if "amount" in c:
                entry["won_amount"] = round(sum(num(r[c["amount"]]) or 0 for r in w))
        rec.append(entry)
    if rec:
        P("## 2. Reconciliation\n")
        P(f"Closed file: {len(won_base)} won, won value {round(sum(r['_amt'] or 0 for r in won_base))}.\n")
        P(table(["File", "Rows", "Has ID", "Unique IDs", "Also in closed", "Not in closed", "Won count", "Won value"],
                [[e["name"], e["rows"], "yes" if e["has_id"] else "NO", e.get("unique_ids", ""), e.get("ids_also_in_closed", ""),
                  e.get("ids_not_in_closed", ""), e.get("won_count", ""), e.get("won_amount", "")] for e in rec]))
        P("\nDo not compare figures from two files whose won totals differ, or from a file with no ID, without stating the difference.\n")
        res["reconciliation"] = rec

    # 3. outcomes by quarter
    P("## 3. Outcomes by quarter\n")
    byq = defaultdict(lambda: {"won": 0, "lost": 0, "other": 0, "amt": 0.0})
    for r in cl:
        byq[r["_q"]][r["_o"]] += 1
        if r["_o"] == "won":
            byq[r["_q"]]["amt"] += r["_amt"] or 0
    qs = sorted(byq)
    qrows = []
    for q in qs:
        v = byq[q]
        n = v["won"] + v["lost"] + v["other"]
        d = v["won"] + v["lost"]
        qrows.append({"quarter": q, "won": v["won"], "lost": v["lost"], "other_closed": v["other"],
                      "other_share": round(v["other"] / n, 4) if n else 0,
                      "won_over_decided": round(v["won"] / d, 4) if d else None,
                      "won_over_all_closed": round(v["won"] / n, 4) if n else None,
                      "won_amount": round(v["amt"])})
    res["by_quarter"] = qrows
    P(table(["Quarter", "Won", "Lost", "Other closed", "Other share", "Won / (won + lost)", "Won / all closed", "Won value"],
            [[d["quarter"], d["won"], d["lost"], d["other_closed"], pct(d["other_share"]),
              pct(d["won_over_decided"]) if d["won_over_decided"] is not None else "", pct(d["won_over_all_closed"]), d["won_amount"]] for d in qrows]))
    last = max(dates) if dates else None
    if last:
        P(f"\nThe last quarter runs to {last.isoformat()} and may be partial. Read the won count and won value columns for the trend; a large change needs an explanation before any play claims a lift.\n")

    # 4. definition break and window
    P("## 4. Definition break and analysis window\n")
    breaks = []
    for prev, cur in zip(qrows, qrows[1:]):
        if abs(cur["other_share"] - prev["other_share"]) >= 2 * a.break_points:
            breaks.append({"between": [prev["quarter"], cur["quarter"]], "other_share": [prev["other_share"], cur["other_share"]]})
    if a.window_start:
        start = a.window_start
        how = "set with --window-start"
    else:
        ref = qrows[-1]["other_share"] if len(qrows) < 2 else qrows[-2]["other_share"]
        if len(qrows) >= 2 and (qrows[-1]["won"] + qrows[-1]["lost"]) >= a.min_n:
            ref = qrows[-1]["other_share"]
        start = qrows[-1]["quarter"]
        for d in reversed(qrows):
            if abs(d["other_share"] - ref) <= a.break_points:
                start = d["quarter"]
            else:
                break
        how = f"detected: most recent run of quarters whose other-closed share stays within {round(100 * a.break_points)} points"
    win = [r for r in cl if r["_q"] >= start]
    excluded_teams = 0
    if a.exclude_team and "team" in col:
        keep = [r for r in win if not any(x.lower() in (r[col["team"]] or "").lower() for x in a.exclude_team)]
        excluded_teams = len(win) - len(keep)
        win = keep
    w = sum(r["_o"] == "won" for r in win)
    l = sum(r["_o"] == "lost" for r in win)
    o = sum(r["_o"] == "other" for r in win)
    lo, hi = wilson(w, w + l)
    res["window"] = {"start": start, "end": qs[-1], "how": how, "breaks": breaks, "won": w, "lost": l, "other_closed": o,
                     "win_rate": round(w / (w + l), 4) if w + l else None, "ci": [round(lo, 4), round(hi, 4)],
                     "excluded_teams": a.exclude_team, "rows_excluded_by_team": excluded_teams}
    if breaks:
        for b in breaks:
            P(f"- Break between {b['between'][0]} and {b['between'][1]}: other-closed share went from {pct(b['other_share'][0])} to {pct(b['other_share'][1])}. Win rates on either side are not comparable.")
    else:
        P("- No quarter-to-quarter change in the other-closed share large enough to flag.")
    P(f"- Window: {start} to {qs[-1]} ({how}).")
    if a.exclude_team:
        P(f"- Teams left out of the window: {', '.join(a.exclude_team)} ({excluded_teams} rows).")
    if w + l:
        P(f"- In the window: {w} won, {l} lost, {o} other closed. Win rate {pct(w / (w + l))} (95% interval {pct(lo)} to {pct(hi)}).")
    if w + l < 200:
        P("- Fewer than 200 decided deals in the window: treat every cut below as `directional`.")
    P("- Use this window for every rate in the report and state it on each finding. Ask sales operations what changed at each break.\n")

    # 5. cuts
    P("## 5. Cuts inside the window\n")
    cuts = {}

    def do(name, title, keyf):
        rows = cut(win, keyf, a.min_n)
        if rows:
            cuts[name] = rows
            P(f"### {title}\n")
            P(cut_table(rows) + "\n")

    if "team" in col:
        do("team", "By owner team or role", lambda r: r[col["team"]])
    if "region" in col:
        do("region", "By region", lambda r: r[col["region"]])
    if "industry" in col:
        do("industry", "By industry", lambda r: r[col["industry"]])
    if "employees" in col:
        do("employees", "By company size (employees)",
           lambda r: band(num(r[col["employees"]]) or None, [200, 1000, 5000, 20000], ["under 200", "200 to 999", "1,000 to 4,999", "5,000 to 19,999", "20,000+"]))
    if "amount" in col:
        wa = sorted(r["_amt"] for r in win if r["_o"] == "won" and r["_amt"])
        if len(wa) >= 8:
            q1, q2, q3 = wa[len(wa) // 4], wa[len(wa) // 2], wa[3 * len(wa) // 4]
            labs = [f"under {round(q1)}", f"{round(q1)} to {round(q2)}", f"{round(q2)} to {round(q3)}", f"{round(q3)}+"]
            do("deal_size", "By deal size (quartiles of won deals)", lambda r: band(r["_amt"], [q1, q2, q3], labs))
    if "source" in col:
        do("source", "By lead source", lambda r: r[col["source"]])
    if "partner" in col:
        do("partner", "By partner on the opportunity", lambda r: "partner on the deal" if r["_partner"] else "no partner")
        if "source" in col:
            def pk(r):
                if "partner" in (r[col["source"]] or "").lower():
                    return "partner-sourced"
                return "partner-involved, other source" if r["_partner"] else "no partner"
            do("partner_source", "By partner involvement and source", pk)
    res["cuts"] = cuts
    P("Rates are correlations. A cut marked `low n`, or one whose interval overlaps the window rate, does not support a segment claim on its own.\n")

    # reasons kept in a separate export: join them by ID
    for key in ("reason", "competitor"):
        if key in col or "id" not in col:
            continue
        for name, (rows, c) in loaded.items():
            if name.startswith("extra") and "id" in c and key in c:
                lookup = {r[c["id"]]: r[c[key]] for r in rows}
                for r in closed:
                    r["_" + key] = lookup.get(r["_id"], "")
                col[key] = "_" + key
                P(f"Note: {key} taken from {name} ({c[key]!r}), joined on the opportunity ID.\n")
                break

    # 6. loss mix
    if "reason" in col:
        P("## 6. Loss mix inside the window\n")
        lost = [r for r in win if r["_o"] == "lost"]
        groups = Counter(loss_group(r[col["reason"]]) for r in lost)
        raw = Counter((r[col["reason"]] or "blank") for r in lost)
        res["loss_mix"] = {"lost": len(lost), "groups": dict(groups.most_common()), "reasons": dict(raw.most_common(15))}
        P(table(["Group", "Lost deals", "Share"], [[k, v, pct(v / len(lost))] for k, v in groups.most_common()]) + "\n")
        P("Top reasons as recorded: " + "; ".join(f"{k} {v}" for k, v in raw.most_common(10)) + ".\n")
        real = len(lost) - groups.get("duplicate", 0) - groups.get("disqualified", 0) - groups.get("data clean-up", 0)
        if w + real and real != len(lost):
            P(f"Leaving duplicates, clean-up and disqualifications out of Lost, the window win rate is {pct(w / (w + real))} against {pct(w / (w + l))}. State which one a finding uses.\n")
            res["loss_mix"]["win_rate_excluding_dq_dup"] = round(w / (w + real), 4)
        if "competitor" in col:
            comp = Counter(r[col["competitor"]].strip() for r in lost if r[col["competitor"]].strip())
            blank = sum(not r[col["competitor"]].strip() for r in lost)
            res["loss_mix"]["competitor_blank_share"] = round(blank / len(lost), 4) if lost else None
            res["loss_mix"]["competitors"] = dict(comp.most_common(10))
            P(f"Competitor field blank on {pct(blank / len(lost)) if lost else 'n/a'} of window losses. Recorded: " + "; ".join(f"{k} {v}" for k, v in comp.most_common(8)) + ".\n")

    win_ids = {r["_id"]: r for r in win if r["_id"]}

    # 7. contact roles
    if "roles" in loaded:
        rows, c = loaded["roles"]
        P("## 7. Contact roles inside the window\n")
        if "id" not in c or "role" not in c or not win_ids:
            P("Skipped: the roles file needs an opportunity ID and a role column, and the closed file needs an ID.\n")
        else:
            buyer = defaultdict(set)
            allr = defaultdict(set)
            for r in rows:
                role = (r[c["role"]] or "").strip()
                allr[r[c["id"]]].add(role)
                if role and not any(wd in role.lower() for wd in NON_BUYER_ROLE_WORDS):
                    buyer[r[c["id"]]].add(role)
            res["roles"] = {"role_values": dict(Counter((r[c["role"]] or "blank") for r in rows).most_common()),
                            "window_opps_without_roles": sum(i not in allr for i in win_ids)}
            P(f"Role values: {', '.join(f'{k} {v}' for k, v in res['roles']['role_values'].items())}.")
            P(f"Window opportunities with no role at all: {res['roles']['window_opps_without_roles']} of {len(win_ids)}.")
            P(f"Buyer roles leave out any role containing: {', '.join(NON_BUYER_ROLE_WORDS)}.\n")
            for r in win_ids.values():
                n = len(buyer.get(r["_id"], ()))
                r["_roles"] = "0" if n == 0 else "1" if n == 1 else "2" if n == 2 else "3+"
            wr = list(win_ids.values())
            t = cut(wr, lambda r: r["_roles"], a.min_n)
            t.sort(key=lambda d: d["value"])
            res["roles"]["by_buyer_roles"] = t
            P("### By number of distinct buyer roles\n")
            P(cut_table(t) + "\n")
            if "partner" in col:
                for flag, lab in ((True, "partner on the deal"), (False, "no partner")):
                    t = cut([r for r in wr if r["_partner"] is flag], lambda r: r["_roles"], a.min_n)
                    t.sort(key=lambda d: d["value"])
                    res["roles"][f"by_buyer_roles_{'partner' if flag else 'no_partner'}"] = t
                    P(f"### By buyer roles, {lab}\n")
                    P(cut_table(t) + "\n")
            P("Reps often add roles to deals that are already advancing. Report this as a correlation.\n")

    # 8. stage history
    if "history" in loaded:
        rows, c = loaded["history"]
        P("## 8. Where lost deals leave, inside the window\n")
        if "id" not in c or "to_stage" not in c or "from_stage" not in c or not win_ids:
            P("Skipped: the history file needs opportunity ID, from-stage and to-stage columns.\n")
        else:
            lost_ids = {i for i, r in win_ids.items() if r["_o"] == "lost"}
            ex = Counter()
            for r in rows:
                if r[c["id"]] in lost_ids and outcome(r[c["to_stage"]]) == "lost":
                    ex[r[c["from_stage"]] or "blank"] += 1
            tot = sum(ex.values())
            res["lost_exits"] = dict(ex.most_common())
            if tot:
                P(table(["Stage left", "Lost deals", "Share"], [[k, v, pct(v / tot)] for k, v in ex.most_common(12)]) + "\n")
            stages = Counter(r[c["to_stage"]] for r in rows)
            res["stage_names"] = dict(stages.most_common())
            P(f"{len(stages)} stage names appear in the history: {', '.join(f'{k} {v}' for k, v in stages.most_common(25))}.\n")

    # 9. open pipeline
    if "open" in loaded:
        rows, c = loaded["open"]
        P("## 9. Open pipeline\n")
        if "stage" not in c:
            P("Skipped: no stage column.\n")
        else:
            op = [r for r in rows if outcome(r[c["stage"]]) == "open"]
            amt = lambda r: (num(r[c["amount"]]) or 0) if "amount" in c else 0
            today = date.today()
            aged = [r for r in op if "age" in c and (num(r[c["age"]]) or 0) > 180]
            past = [r for r in op if "close" in c and (parse_date(r[c["close"]], a.dayfirst) or today) < today]
            res["open"] = {"count": len(op), "amount": round(sum(amt(r) for r in op)), "aged_over_180": len(aged),
                           "aged_amount": round(sum(amt(r) for r in aged)), "past_close_date": len(past),
                           "by_stage": dict(Counter(r[c["stage"]] for r in op).most_common())}
            o_ = res["open"]
            P(f"- {o_['count']} open opportunities, value {o_['amount']}.")
            if "age" in c:
                P(f"- {o_['aged_over_180']} older than 180 days, value {o_['aged_amount']}.")
            if "close" in c:
                P(f"- {o_['past_close_date']} with a close date before {today.isoformat()}.")
            P(f"- By stage: {', '.join(f'{k} {v}' for k, v in o_['by_stage'].items())}.\n")

    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=1, default=str)
        P(f"Wrote {a.json}")


if __name__ == "__main__":
    main()
