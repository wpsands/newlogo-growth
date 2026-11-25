#!/usr/bin/env python3
"""Tests for tests/verifier/score.py, so the scorer itself is checked.

Run from the repository root:
  python3 tests/test_score.py
"""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.join(HERE, "verifier", "case-01")
sys.path.insert(0, os.path.join(HERE, "verifier"))

import score  # noqa: E402

GOOD = """
**Must fix**
- L6-1 and the summary: 32.9% (280 of 850) uses all eight quarters. In the window it is 30.0% (180 of 600).
- L5-1: 60 of 90 is 66.7%, not 76.7%.
- L5-2: the by-source file has no opportunity ID and covers all eight quarters; in the window inbound is 90 of 300.
- L4-1: the pricing capture lists prices for Starter ($900) and Growth ($2,400).
- L2-1: no direct deal has two buyer roles, so the claim is unsupported on direct deals.
- E-1: the capture says 1.6 times and 2024.
- Play 2: the expected lift is copied from a third-party benchmark.

## Should fix
1. L1-1: Health rate has no counts (75 of 135).
2. L1-2: Retail is 0 of 6, low n.
3. L3-1: no status label.
4. Play 1: no volume or capacity line.

**Confirmed**
- L1-3 holds: 120 of 300 and 60 of 300.
- L5-3 holds. L6-2 holds. L3-2 holds.

**Could not check**
- Nothing.
"""


class Scorer(unittest.TestCase):
    def test_full_report_passes(self):
        r = score.score(CASE, GOOD)
        self.assertEqual(r["missed"], [])
        self.assertEqual(r["controls_flagged"], [])
        self.assertTrue(r["passed"])
        self.assertEqual(len(r["caught"]), 11)

    def test_a_missed_mistake_fails(self):
        r = score.score(CASE, GOOD.replace("- L5-1: 60 of 90 is 66.7%, not 76.7%.\n", ""))
        self.assertFalse(r["passed"])
        self.assertEqual([m["key"] for m in r["missed"]], ["arithmetic"])

    def test_naming_the_id_without_the_mistake_fails(self):
        r = score.score(CASE, GOOD.replace("60 of 90 is 66.7%, not 76.7%", "wording could be tighter"))
        self.assertFalse(r["passed"])
        self.assertTrue(r["missed"][0]["id_was_named"])

    def test_a_mistake_listed_only_under_confirmed_fails(self):
        moved = GOOD.replace("- L5-1: 60 of 90 is 66.7%, not 76.7%.\n", "")
        moved = moved.replace("- L1-3 holds", "- L5-1 holds at 66.7%.\n- L1-3 holds")
        self.assertFalse(score.score(CASE, moved)["passed"])

    def test_a_correct_finding_under_must_fix_fails(self):
        r = score.score(CASE, GOOD.replace("**Must fix**\n", "**Must fix**\n- L6-2: the no-decision share is wrong.\n"))
        self.assertFalse(r["passed"])
        self.assertEqual([c["id"] for c in r["controls_flagged"]], ["L6-2"])

    def test_ids_do_not_match_inside_longer_ids(self):
        r = score.score(CASE, "**Must fix**\n- L1-10: Retail is 0 of 6.\n- Play 10 has no capacity line.\n")
        keys = [m["key"] for m in r["caught"]]
        self.assertNotIn("low-n-segment-claim", keys)
        self.assertNotIn("play-missing-volume-capacity", keys)

    def test_empty_report_fails(self):
        r = score.score(CASE, "The draft looks fine.")
        self.assertFalse(r["passed"])
        self.assertEqual(len(r["missed"]), 11)


if __name__ == "__main__":
    unittest.main(verbosity=1)
