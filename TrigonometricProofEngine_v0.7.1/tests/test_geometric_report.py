import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import app
import engine
from geometry import (
    _digest,
    build_f08_geometric_certificate,
    verify_geometric_certificate,
)


class GeometricReportTests(unittest.TestCase):
    def setUp(self):
        self.result = engine.prove_identity("sin(x)**2 + cos(x)**2", "1")
        self.assertEqual(self.result.status, "PROVED")
        self.assertTrue(self.result.selected_route.startswith("GEO:"))

    def test_desktop_report_shows_actual_geometric_derivation(self):
        report = app.TrigProofApp._format_result(None, self.result)
        required = [
            "GEOMETRIC PROOF CHAIN",
            "G01 — Pythagorean theorem by geometric dissection",
            "(a+b)² = 4(ab/2) + c²",
            "a² + b² = c²",
            "G03 — Cartesian squared-distance theorem",
            "OP² = |u|² + |v|² = u² + v²",
            "G04 — Unit-circle substitution",
            "P=(cos(x), sin(x))",
            "1² = cos²(x) + sin²(x)",
            "Final step — Match the geometric theorem to the requested claim",
            "LHS − RHS = (1)×0 = 0",
            "GEOMETRIC CERTIFICATE REPLAY",
            "Replay status: VERIFIED",
            "Trusted foundations: AX.REAL, AX.EUCLID, AX.AREA, D.UNIT",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, report)

    def test_desktop_report_does_not_mislabel_geo_nodes_as_identity_rewrites(self):
        report = app.TrigProofApp._format_result(None, self.result)
        forbidden = [
            "DERIVATION CHAIN",
            "Identity sequence:",
            "explicit identity application(s)",
            "PROOF / ANALYSIS STEPS",
            "No symbolic proof steps were established",
            "IDENTITY DATABASE REFERENCES",
            "Each listed ID is attached to an explicit identity-application step",
            "The route is heuristic rather than a complete formal proof certificate",
        ]
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, report)

    def test_markdown_export_shows_same_geometric_steps(self):
        report = self.result.to_markdown()
        for phrase in [
            "## Geometric proof steps",
            "G01 — Pythagorean theorem by geometric dissection",
            "(a+b)² = 4(ab/2) + c².",
            "G03 — Cartesian squared-distance theorem",
            "G04 — Unit-circle substitution",
            "Final step — Match the geometric theorem to the requested claim",
            "## Certificate replay",
            "- **Replay:** VERIFIED",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, report)
        self.assertNotIn("Identity applications:** 0", report)
        self.assertNotIn("## Proof / analysis steps", report)

    def test_scaled_and_rearranged_f08_reports_include_goal_matching(self):
        for lhs, rhs in [
            ("sin(t)**2", "1-cos(t)**2"),
            ("2*sin(t)**2+2*cos(t)**2", "2"),
        ]:
            with self.subTest(lhs=lhs, rhs=rhs):
                result = engine.prove_identity(lhs, rhs)
                report = app.TrigProofApp._format_result(None, result)
                self.assertEqual(result.status, "PROVED")
                self.assertIn("Final step — Match the geometric theorem", report)
                self.assertIn("LHS − RHS", report)
                self.assertIn("GEOMETRIC CERTIFICATE REPLAY", report)

    def test_non_geometric_catalogue_report_keeps_identity_steps(self):
        result = engine.prove_identity("1+tan(x)**2", "sec(x)**2", "Use full identity catalogue")
        report = app.TrigProofApp._format_result(None, result)
        self.assertEqual(result.status, "PROVED")
        self.assertIn("DERIVATION CHAIN", report)
        self.assertIn("PROOF / ANALYSIS STEPS", report)
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

    def test_v061_geometric_certificates_remain_replayable(self):
        cert = copy.deepcopy(self.result.to_certificate())
        cert["engine_version"] = "0.6.1"
        cert["certificate_digest"] = _digest(cert)
        valid, reason = verify_geometric_certificate(
            cert, engine.parse_expression, self.result.lhs, self.result.rhs,
            self.result.domain_conditions,
        )
        self.assertTrue(valid, reason)

    def test_new_certificates_identify_v071_engine(self):
        self.assertEqual(app.VERSION, "0.7.1")
        self.assertEqual(engine.ENGINE_VERSION, "0.7.1")
        self.assertEqual(self.result.to_certificate()["engine_version"], "0.7.1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
