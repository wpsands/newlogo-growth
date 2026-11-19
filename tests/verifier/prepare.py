#!/usr/bin/env python3
"""Lay out a verifier test case in a scratch folder and print the brief.

The verifier must not see the answer key, so the case is copied to a folder
outside the repository with only the draft, the captures and the made-up data.

Usage:
  python3 tests/verifier/prepare.py tests/verifier/case-01 /tmp/verifier-case-01
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))

import fixtures  # noqa: E402

BRIEF = """You are the `verifier` agent of the newlogo-growth plugin. Your instructions are in
{root}/agents/verifier.md. Read that file and follow it exactly. Where it says
${{CLAUDE_PLUGIN_ROOT}}, use {root}.

Check this draft:
- Draft: {out}/draft.md
- Raw captures folder: {out}/captures
- Supplied data files: {out}/data/closed.csv (closed opportunities),
  {out}/data/open.csv (open pipeline), {out}/data/stage_history.csv,
  {out}/data/contact_roles.csv, and two extra reports,
  {out}/data/pipeline_by_source.csv and {out}/data/won_report.csv
- Notes file to write: {out}/verifier-notes.md

The company and the cited research firm are fictional. Their pages exist only as
the files in the captures folder, so check sources and citations against those
files and do not browse the web. Do not read anything under {root}/tests.

Return your report in the format your instructions give, with the four headings
Must fix, Should fix, Confirmed and Could not check, and the finding or play ID
on every item."""


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    case, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if os.path.commonpath([out, ROOT]) == ROOT:
        sys.exit("Choose an output folder outside the repository, so the verifier cannot see the answer key.")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(os.path.join(case, "draft.md"), os.path.join(out, "draft.md"))
    cap = os.path.join(out, "captures")
    if os.path.isdir(cap):
        shutil.rmtree(cap)
    shutil.copytree(os.path.join(case, "captures"), cap)
    fixtures.make(os.path.join(out, "data"))
    brief = BRIEF.format(root=ROOT, out=out)
    with open(os.path.join(out, "brief.txt"), "w", encoding="utf-8") as fh:
        fh.write(brief + "\n")
    print(brief)


if __name__ == "__main__":
    main()
