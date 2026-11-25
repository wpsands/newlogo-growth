#!/usr/bin/env python3
"""Tests for tools/crm_profile.py on made-up exports with known answers.

Standard library only. Run from the repository root:
  python3 tests/test_crm_profile.py
"""
import csv
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCRIPT = os.path.join(ROOT, "tools", "crm_profile.py")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))

import fixtures  # noqa: E402
import crm_profile  # noqa: E402

E = fixtures.EXPECTED


def run(args, expect_ok=True):
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "profile.json")
        p = subprocess.run([sys.executable, "-B", SCRIPT] + args + ["--json", out],
                           capture_output=True, text=True)
        if not expect_ok:
            return p, None
        if p.returncode != 0:
            raise AssertionError(f"crm_profile.py failed:\n{p.stderr}")
        with open(out, encoding="utf-8") as fh:
            return p, json.load(fh)


def by_value(rows):
    return {r["value"]: r for r in rows}


class FullProfile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.paths = fixtures.make(cls.tmp.name)
        cls.proc, cls.res = run([
            "--closed", cls.paths["closed"], "--open", cls.paths["open"],
            "--history", cls.paths["stage_history"], "--roles", cls.paths["contact_roles"],
            "--extra", cls.paths["pipeline_by_source"], "--extra", cls.paths["won_report"],
        ])

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def check_cut(self, rows, expected):
        got = by_value(rows)
        for value, (won, lost) in expected.items():
            self.assertIn(value, got)
            self.assertEqual((got[value]["won"], got[value]["lost"]), (won, lost), value)
            self.assertEqual(got[value]["decided"], won + lost, value)
            self.assertAlmostEqual(got[value]["win_rate"], won / (won + lost), places=3, msg=value)

    def test_inventory(self):
        inv = self.res["inventory"]
        self.assertEqual(inv["rows"], E["rows"])
        self.assertEqual(inv["unique_ids"], E["rows"])
        self.assertEqual(inv["duplicate_ids"], 0)
        self.assertEqual(inv["close_date_range"], ["2025-02-15", "2026-11-15"])

    def test_definition_break_is_found(self):
        breaks = self.res["window"]["breaks"]
        self.assertEqual(len(breaks), 1)
        self.assertEqual(breaks[0]["between"], E["break_between"])

    def test_window_starts_after_the_break(self):
        w = self.res["window"]
        self.assertEqual(w["start"], E["window_start"])
        self.assertEqual(w["end"], E["window_end"])

    def test_window_rate_is_not_blended(self):
        w = self.res["window"]
        self.assertEqual((w["won"], w["lost"], w["other_closed"]), (180, 420, 0))
        self.assertAlmostEqual(w["win_rate"], 0.30, places=4)
        self.assertNotAlmostEqual(w["win_rate"], E["blended_won_over_decided"], places=2)
        self.assertNotAlmostEqual(w["win_rate"], E["blended_won_over_all_closed"], places=2)
        self.assertLess(w["ci"][0], 0.30)
        self.assertGreater(w["ci"][1], 0.30)

    def test_quarter_table_shows_both_ratios(self):
        q = {r["quarter"]: r for r in self.res["by_quarter"]}
        self.assertEqual(len(q), 8)
        self.assertEqual((q["2025Q1"]["won"], q["2025Q1"]["lost"], q["2025Q1"]["other_closed"]), (20, 30, 50))
        self.assertAlmostEqual(q["2025Q1"]["won_over_decided"], 0.40)
        self.assertAlmostEqual(q["2025Q1"]["won_over_all_closed"], 0.20)
        self.assertAlmostEqual(q["2026Q3"]["other_share"], 0.0)

    def test_cuts_use_the_window_only(self):
        cuts = self.res["cuts"]
        self.check_cut(cuts["team"], E["team"])
        self.check_cut(cuts["industry"], E["industry"])
        self.check_cut(cuts["partner"], E["partner"])
        for name in ("team", "industry", "partner", "source"):
            self.assertEqual(sum(r["decided"] for r in cuts[name]), 600, name)

    def test_low_n_is_marked(self):
        ind = by_value(self.res["cuts"]["industry"])
        self.assertTrue(ind["Retail"]["low_n"])
        self.assertFalse(ind["Health"]["low_n"])
        self.assertIn("low n", self.proc.stdout)

    def test_intervals_stay_between_zero_and_one(self):
        for rows in self.res["cuts"].values():
            for r in rows:
                self.assertGreaterEqual(r["ci_low"], 0.0)
                self.assertLessEqual(r["ci_high"], 1.0)
                self.assertLessEqual(r["ci_low"], r["win_rate"])
                self.assertGreaterEqual(r["ci_high"], r["win_rate"])
        self.assertNotIn("-0.0%", self.proc.stdout)

    def test_loss_mix(self):
        lm = self.res["loss_mix"]
        self.assertEqual(lm["lost"], 420)
        for group, n in E["loss_groups"].items():
            self.assertEqual(lm["groups"].get(group), n, group)
        self.assertAlmostEqual(lm["win_rate_excluding_dq_dup"], E["win_rate_excluding_duplicates"], places=4)

    def test_buyer_roles_leave_out_partner_roles(self):
        roles = self.res["roles"]
        self.assertEqual(roles["window_opps_without_roles"], E["window_opps_without_roles"])
        partner = by_value(roles["by_buyer_roles_partner"])
        self.assertEqual(set(partner), {"1", "2"})  # a counted partner role would create "3+"
        self.check_cut(roles["by_buyer_roles_partner"], E["roles_partner"])
        self.check_cut(roles["by_buyer_roles_no_partner"], E["roles_no_partner"])

    def test_lost_exits(self):
        self.assertEqual(self.res["lost_exits"], E["lost_exits"])

    def test_open_pipeline(self):
        o = self.res["open"]
        self.assertEqual(o["count"], E["open"]["count"])
        self.assertEqual(o["amount"], 400000)
        self.assertEqual(o["aged_over_180"], E["open"]["aged_over_180"])

    def test_reconciliation_flags_missing_id_and_differing_totals(self):
        rec = {os.path.basename(e["file"]): e for e in self.res["reconciliation"]}
        self.assertFalse(rec["pipeline_by_source.csv"]["has_id"])
        short = rec["won_report.csv"]
        self.assertTrue(short["has_id"])
        self.assertEqual(short["won_count"], 270)
        self.assertEqual(short["ids_not_in_closed"], 0)
        self.assertIn("280 won", self.proc.stdout)


class Options(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.paths = fixtures.make(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_exclude_team(self):
        _, res = run(["--closed", self.paths["closed"], "--exclude-team", "SMB"])
        w = res["window"]
        self.assertEqual((w["won"], w["lost"]), (120, 180))
        self.assertAlmostEqual(w["win_rate"], 0.40, places=4)
        self.assertEqual(w["rows_excluded_by_team"], 300)
        self.assertNotIn("SMB", by_value(res["cuts"]["team"]))

    def test_window_start_override(self):
        _, res = run(["--closed", self.paths["closed"], "--window-start", "2026Q3"])
        w = res["window"]
        self.assertEqual(w["start"], "2026Q3")
        self.assertEqual((w["won"], w["lost"]), (120, 280))

    def test_min_n(self):
        _, res = run(["--closed", self.paths["closed"], "--min-n", "5"])
        self.assertFalse(by_value(res["cuts"]["industry"])["Retail"]["low_n"])

    def test_bad_map_column_stops_the_run(self):
        p, _ = run(["--closed", self.paths["closed"], "--map", "amount=No Such Column"], expect_ok=False)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("no such column", p.stderr)


class OtherLayouts(unittest.TestCase):
    def write(self, tmp, name, fields, rows):
        path = os.path.join(tmp, name)
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(fields)
            w.writerows(rows)
        return path

    def test_hubspot_style_columns_with_no_team_or_partner(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = []
            for i in range(120):
                stage = "Closed won" if i % 4 == 0 else "Closed lost"
                rows.append([1000 + i, stage, "2026-08-15", 5000])
            path = self.write(tmp, "deals.csv", ["Record ID", "Deal Stage", "Close Date", "Amount"], rows)
            _, res = run(["--closed", path])
            self.assertEqual((res["window"]["won"], res["window"]["lost"]), (30, 90))
            self.assertIn("team", res["inventory"]["columns_missing"])
            self.assertIn("partner", res["inventory"]["columns_missing"])
            self.assertNotIn("team", res["cuts"])
            self.assertNotIn("partner", res["cuts"])

    def test_duplicate_ids_are_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = [[f"A{i}", "Closed Won" if i % 2 else "Closed Lost", "2026-08-15", 100] for i in range(60)]
            rows.append(["A1", "Closed Won", "2026-08-15", 100])
            path = self.write(tmp, "closed.csv", ["Opportunity ID", "Stage", "Close Date", "Amount"], rows)
            _, res = run(["--closed", path])
            self.assertEqual(res["inventory"]["duplicate_ids"], 1)

    def test_open_rows_are_left_out_of_the_closed_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = [[f"A{i}", "Closed Won" if i % 2 else "Closed Lost", "2026-08-15", 100] for i in range(60)]
            rows += [[f"B{i}", "Negotiation", "2026-08-15", 100] for i in range(10)]
            path = self.write(tmp, "closed.csv", ["Opportunity ID", "Stage", "Close Date", "Amount"], rows)
            _, res = run(["--closed", path])
            self.assertEqual(res["inventory"]["rows_not_closed"], 10)
            self.assertEqual(res["window"]["won"] + res["window"]["lost"], 60)

    def test_missing_stage_column_stops_the_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write(tmp, "closed.csv", ["Opportunity ID", "Close Date"], [["A1", "2026-08-15"]])
            p, _ = run(["--closed", path], expect_ok=False)
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("no stage column", p.stderr)

    def test_dayfirst_dates(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = [[f"A{i}", "Closed Won" if i % 2 else "Closed Lost", "15/08/2026", 100] for i in range(60)]
            path = self.write(tmp, "closed.csv", ["Opportunity ID", "Stage", "Close Date", "Amount"], rows)
            _, res = run(["--closed", path, "--dayfirst"])
            self.assertEqual(res["window"]["start"], "2026Q3")


class Helpers(unittest.TestCase):
    def test_outcome(self):
        self.assertEqual(crm_profile.outcome("Closed Won"), "won")
        self.assertEqual(crm_profile.outcome("closed lost"), "lost")
        self.assertEqual(crm_profile.outcome("Closed Cancelled"), "other")
        self.assertEqual(crm_profile.outcome("Disqualified"), "other")
        self.assertEqual(crm_profile.outcome("Negotiation"), "open")
        self.assertEqual(crm_profile.outcome(""), "open")

    def test_wilson(self):
        self.assertEqual(crm_profile.wilson(0, 0), (0.0, 0.0))
        lo, hi = crm_profile.wilson(50, 100)
        self.assertAlmostEqual(lo, 0.4038, places=3)
        self.assertAlmostEqual(hi, 0.5962, places=3)
        lo, hi = crm_profile.wilson(0, 6)
        self.assertEqual(lo, 0.0)
        self.assertGreater(hi, 0.3)
        lo, hi = crm_profile.wilson(6, 6)
        self.assertEqual(hi, 1.0)

    def test_quarter(self):
        self.assertEqual(crm_profile.quarter(date(2026, 2, 15), 1), "2026Q1")
        self.assertEqual(crm_profile.quarter(date(2026, 11, 15), 1), "2026Q4")
        self.assertEqual(crm_profile.quarter(date(2026, 2, 15), 2), "2027Q1")
        self.assertEqual(crm_profile.quarter(date(2026, 1, 15), 2), "2026Q4")

    def test_loss_group(self):
        self.assertEqual(crm_profile.loss_group("Went dark"), "no decision")
        self.assertEqual(crm_profile.loss_group("Price"), "price or budget")
        self.assertEqual(crm_profile.loss_group("Chose competitor"), "competitor")
        self.assertEqual(crm_profile.loss_group("Duplicate"), "duplicate")
        self.assertEqual(crm_profile.loss_group(""), "blank")


if __name__ == "__main__":
    unittest.main(verbosity=1)
