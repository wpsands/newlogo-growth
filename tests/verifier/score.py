#!/usr/bin/env python3
"""Score a verifier report against a case's planted mistakes.

Standard library only.

Usage:
  python3 tests/verifier/score.py tests/verifier/case-01 path/to/verifier-report.md

The report is the verifier agent's returned text, saved to a file. It must use
the verifier's own headings: Must fix, Should fix, Confirmed, Could not check.

A planted mistake counts as caught when one item under Must fix or Should fix
names its finding or play ID and matches one of its patterns. A control fails
when its ID appears in an item under Must fix. Exit code 0 means the case
passed, 1 means it did not, 2 means the report could not be read.
"""
import json
import os
import re
import sys

SECTIONS = ["must fix", "should fix", "confirmed", "could not check"]
ITEM_START = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+")


def split_sections(text):
    """Return {section name: [items]} using the verifier's four headings."""
    out = {s: [] for s in SECTIONS}
    current = None
    item = None

    def close():
        nonlocal item
        if current and item and item.strip():
            out[current].append(item.strip())
        item = None

    for line in text.splitlines():
        bare = re.sub(r"[#*_:`>\-\s]+", " ", line).strip().lower()
        heading = next((s for s in SECTIONS if bare == s or bare.startswith(s + " (") or
                        re.match(rf"^{s}\b.{{0,12}}$", bare)), None)
        is_item = bool(ITEM_START.match(line))
        if heading and not (is_item and len(bare) > len(heading) + 12):
            close()
            current = heading
            # text on the heading line after the label, e.g. "**Must fix**: none"
            rest = re.split(heading, line, flags=re.I, maxsplit=1)[-1].strip(" *:_-")
            item = rest if rest else None
            continue
        if current is None:
            continue
        if is_item:
            close()
            item = ITEM_START.sub("", line)
        elif not line.strip():
            close()
        else:
            item = (item + " " + line.strip()) if item else line.strip()
    close()
    return out


def id_pattern(ident):
    parts = [re.escape(p) for p in re.split(r"[\s-]+", ident)]
    return re.compile(r"(?<![\w-])" + r"[\s-]*".join(parts) + r"(?![\w-]|\.\d)", re.I)


def score(case_dir, report_text):
    with open(os.path.join(case_dir, "expected.json"), encoding="utf-8") as fh:
        exp = json.load(fh)
    sec = split_sections(report_text)
    flagged = sec["must fix"] + sec["should fix"]
    results = {"caught": [], "missed": [], "controls_flagged": [], "sections": {k: len(v) for k, v in sec.items()}}
    for p in exp["planted"]:
        idp = id_pattern(p["id"])
        pats = [re.compile(x, re.I) for x in p["any"]]
        hit = next((it for it in flagged if idp.search(it) and any(x.search(it) for x in pats)), None)
        named = any(idp.search(it) for it in flagged)
        (results["caught"] if hit else results["missed"]).append(
            {"key": p["key"], "id": p["id"], "mistake": p["mistake"], "id_was_named": named})
    for c in exp["controls"]:
        idp = id_pattern(c["id"])
        if any(idp.search(it) for it in sec["must fix"]):
            results["controls_flagged"].append(c)
    results["passed"] = not results["missed"] and not results["controls_flagged"]
    return results


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    case_dir, report = sys.argv[1], sys.argv[2]
    try:
        with open(report, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as e:
        print(f"Could not read the report: {e}")
        sys.exit(2)
    r = score(case_dir, text)
    if not (r["sections"]["must fix"] or r["sections"]["should fix"]):
        print("No items found under Must fix or Should fix. Check the report uses the verifier's headings.")
    total = len(r["caught"]) + len(r["missed"])
    print(f"Planted mistakes caught: {len(r['caught'])} of {total}")
    for m in r["caught"]:
        print(f"  caught  {m['id']:<7} {m['key']}")
    for m in r["missed"]:
        why = "ID named, but not this mistake" if m["id_was_named"] else "ID not named under Must fix or Should fix"
        print(f"  MISSED  {m['id']:<7} {m['key']} ({why})")
        print(f"          {m['mistake']}")
    print(f"Correct findings wrongly listed under Must fix: {len(r['controls_flagged'])}")
    for c in r["controls_flagged"]:
        print(f"  FLAGGED {c['id']:<7} {c['note']}")
    print("PASS" if r["passed"] else "FAIL")
    sys.exit(0 if r["passed"] else 1)


if __name__ == "__main__":
    main()
