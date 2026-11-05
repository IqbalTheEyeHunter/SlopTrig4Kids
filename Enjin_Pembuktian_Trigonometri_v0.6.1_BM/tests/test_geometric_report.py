import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import app
import engine
from geometry import _digest, verify_geometric_certificate


class GeometricReportTests(unittest.TestCase):
    def setUp(self):
        self.result = engine.prove_identity("sin(x)**2 + cos(x)**2", "1")
        self.assertEqual(self.result.status, "PROVED")
        self.assertTrue(self.result.selected_route.startswith("GEO:"))

    def test_desktop_report_shows_actual_geometric_derivation_in_malay(self):
        report = app.TrigProofApp._format_result(None, self.result)
        required = [
            "LAPORAN IDENTITI TRIGONOMETRI",
            "Status: TERBUKTI (PROVED)",
            "RANTAIAN PEMBUKTIAN GEOMETRI",
            "G01 — Teorem Pythagoras melalui pembahagian geometri",
            "(a+b)² = 4(ab/2) + c².",
            "a² + b² = c².",
            "G03 — Rumus kuasa dua jarak pada satah Cartes",
            "OP² = |u|² + |v|² = u² + v².",
            "G04 — Penggantian menggunakan bulatan unit",
            "P=(cos(x), sin(x))",
            "1² = cos²(x) + sin²(x).",
            "Langkah akhir — Padankan teorem geometri dengan pernyataan yang hendak dibuktikan",
            "LHS − RHS = (1)×0 = 0",
            "PENGESAHAN SEMULA SIJIL GEOMETRI",
            "Status pengesahan semula: DISAHKAN (VERIFIED)",
            "Asas matematik yang dipercayai: AX.REAL, AX.EUCLID, AX.AREA, D.UNIT",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, report)

    def test_geometric_report_does_not_mislabel_geo_nodes_as_catalogue_rewrites(self):
        report = app.TrigProofApp._format_result(None, self.result)
        forbidden = [
            "Identity sequence:",
            "explicit identity application(s)",
            "LANGKAH PEMBUKTIAN / ANALISIS",
            "No symbolic proof steps were established",
            "RUJUKAN PUSTAKA IDENTITI",
            "Setiap ID yang disenaraikan merujuk kepada langkah penggunaan identiti",
        ]
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, report)

    def test_markdown_export_is_in_malay_and_contains_geometric_steps(self):
        report = app.TrigProofApp._format_markdown_ms(self.result)
        for phrase in [
            "# Laporan Pembuktian Trigonometri",
            "## Rantaian Pembuktian Geometri",
            "G01 — Teorem Pythagoras melalui pembahagian geometri",
            "(a+b)² = 4(ab/2) + c².",
            "G03 — Rumus kuasa dua jarak pada satah Cartes",
            "G04 — Penggantian menggunakan bulatan unit",
            "## Pengesahan Semula Sijil Geometri",
            "Status pengesahan semula: DISAHKAN (VERIFIED)",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, report)
        self.assertNotIn("Geometric proof steps", report)

    def test_scaled_and_rearranged_f08_reports_include_goal_matching(self):
        for lhs, rhs in [
            ("sin(t)**2", "1-cos(t)**2"),
            ("2*sin(t)**2+2*cos(t)**2", "2"),
        ]:
            with self.subTest(lhs=lhs, rhs=rhs):
                result = engine.prove_identity(lhs, rhs)
                report = app.TrigProofApp._format_result(None, result)
                self.assertEqual(result.status, "PROVED")
                self.assertIn("Langkah akhir — Padankan teorem geometri", report)
                self.assertIn("LHS − RHS", report)
                self.assertIn("PENGESAHAN SEMULA SIJIL GEOMETRI", report)

    def test_non_geometric_catalogue_report_keeps_identity_steps_in_malay(self):
        result = engine.prove_identity("1+tan(x)**2", "sec(x)**2", "Use full identity catalogue")
        report = app.TrigProofApp._format_result(None, result)
        self.assertEqual(result.status, "PROVED")
        self.assertIn("RANTAIAN PEMBUKTIAN", report)
        self.assertIn("LANGKAH PEMBUKTIAN / ANALISIS", report)
        self.assertIn("Gunakan identiti", report)
        self.assertNotIn("GEOMETRIC PROOF CHAIN", report)

    def test_v060_geometric_certificates_remain_replayable(self):
        cert = copy.deepcopy(self.result.to_certificate())
        cert["engine_version"] = "0.6.0"
        cert["certificate_digest"] = _digest(cert)
        valid, reason = verify_geometric_certificate(
            cert, engine.parse_expression, self.result.lhs, self.result.rhs,
            self.result.domain_conditions,
        )
        self.assertTrue(valid, reason)

    def test_new_certificates_identify_v061_engine(self):
        self.assertEqual(app.VERSION, "0.6.1")
        self.assertEqual(engine.ENGINE_VERSION, "0.6.1")
        self.assertEqual(self.result.to_certificate()["engine_version"], "0.6.1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
