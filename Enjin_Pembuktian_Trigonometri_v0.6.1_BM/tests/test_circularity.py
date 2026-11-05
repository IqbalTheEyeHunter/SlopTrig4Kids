import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine as e


class CircularityAndReuseTests(unittest.TestCase):
    def test_f08_is_proved_geometrically_without_self_use(self):
        result = e.prove_identity("sin(x)**2+cos(x)**2", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "GEO: G01 → G03 → G04")
        self.assertEqual(result.rule_ids, ("G01", "G03", "G04"))
        self.assertEqual(result.used_theorems, [])
        self.assertEqual(result.to_certificate()["schema"], e.GEO_CERTIFICATE_SCHEMA)

    def test_f08_rearrangements_and_constant_scalings_are_geometric(self):
        variants = [
            ("1", "sin(t)**2+cos(t)**2"),
            ("sin(t)**2", "1-cos(t)**2"),
            ("2*sin(t)**2+2*cos(t)**2", "2"),
            ("sin(2*t)**2+cos(2*t)**2", "1"),
        ]
        for lhs, rhs in variants:
            with self.subTest(lhs=lhs, rhs=rhs):
                result = e.prove_identity(lhs, rhs)
                self.assertEqual(result.status, "PROVED")
                self.assertEqual(result.used_theorems, [])
                self.assertTrue(result.selected_route.startswith("GEO:"))

    def test_direct_f08_goal_blocks_f08_descendants_as_premises(self):
        catalogue = e.load_catalogue_theorems()
        lhs = e.parse_expression("2*sin(x)**2+2*cos(x)**2")
        rhs = e.parse_expression("2")
        admitted = e._independent_premises(lhs, rhs, [], catalogue)
        ids = {theorem.identity_id for theorem in admitted}
        self.assertFalse({"F08", "F09", "F10", "F11", "F12"} & ids)

    def test_f09_is_proved_from_f08_not_from_itself(self):
        result = e.prove_identity("1+tan(x)**2", "sec(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F08", result.rule_ids)
        self.assertNotIn("F09", result.rule_ids)
        self.assertIn("F08", [item["identity_id"] for item in result.used_theorems])

    def test_f10_is_proved_from_f08_not_from_itself(self):
        result = e.prove_identity("1+cot(x)**2", "csc(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F08", result.rule_ids)
        self.assertNotIn("F10", result.rule_ids)

    def test_derived_parameter_identity_can_use_f08(self):
        lhs = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2"
        rhs = "p**2+q**2"
        result = e.prove_identity(lhs, rhs, "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("F08",))
        self.assertEqual([item["identity_id"] for item in result.used_theorems], ["F08"])
        titles = [step.title for step in result.steps]
        self.assertIn("Expand squared sums", titles)
        self.assertIn("Factor by parameter groups", titles)
        self.assertTrue(any(step.theorem_ref.startswith("F08") for step in result.steps))
        cert = result.to_certificate()
        self.assertIn("F08 depends on GEO.F08", cert["dependency_provenance"])

    def test_f09_can_be_used_for_a_different_goal(self):
        result = e.prove_identity(
            "(1+tan(x)**2)*cos(x)**2", "sec(x)**2*cos(x)**2", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F09", result.rule_ids)
        self.assertEqual(result.rule_ids, ("F09",))
        self.assertNotEqual(str(result.rhs), "sec(x)**2")

    def test_f10_can_be_used_for_a_different_goal(self):
        result = e.prove_identity(
            "(1+cot(x)**2)*sin(x)**2", "csc(x)**2*sin(x)**2", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F10", result.rule_ids)
        self.assertEqual(result.rule_ids, ("F10",))
        self.assertNotEqual(str(result.rhs), "csc(x)**2")

    def test_original_misprinted_parameter_claim_is_false(self):
        lhs = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-p*cos(x))**2"
        result = e.prove_identity(lhs, "p**2+q**2", "Use full identity catalogue")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)

    def test_untrusted_supplied_f08_cannot_prove_an_unrelated_goal(self):
        lhs = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2"
        result = e.prove_identity(
            lhs, "p**2+q**2", "Use supplied identities",
            premises=["Pythagorean: sin(t)**2+cos(t)**2=1"],
        )
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.used_theorems, [])

    def test_legacy_certificate_cannot_bypass_provenance(self):
        premise = {
            "name": "Old F08", "lhs": "sin(x)**2+cos(x)**2", "rhs": "1",
            "proof_certificate": {"schema": "trigonometric-proof-certificate-v3", "status": "PROVED"},
        }
        lhs = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2"
        result = e.prove_identity(lhs, "p**2+q**2", "Use supplied identities", premises=[premise])
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.used_theorems, [])

    def test_cycle_and_missing_provenance_fail_closed(self):
        catalogue = e.load_catalogue_theorems()
        with patch.dict(e.AUDITED_DEPENDENCIES, {"F09": ("F11",), "F11": ("F09",)}):
            allowed = e._independent_premises(
                e.parse_expression("sin(x)"), e.parse_expression("cos(x)"), [], catalogue
            )
            ids = {theorem.identity_id for theorem in allowed}
            self.assertFalse({"F09", "F11"} & ids)

    def test_valid_f08_f09_f10_certificates_keep_provenance(self):
        for lhs, rhs, required in [
            ("1+tan(x)**2", "1/cos(x)**2", "F09"),
            ("1+cot(x)**2", "1/sin(x)**2", "F10"),
        ]:
            result = e.prove_identity(lhs, rhs, "Use full identity catalogue")
            self.assertEqual(result.status, "PROVED")
            self.assertIn(required, result.rule_ids)
            self.assertTrue(all(step.get("symbolic_equivalence_check") is not False
                                for step in result.to_certificate()["steps"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
