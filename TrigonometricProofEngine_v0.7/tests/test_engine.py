import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import engine as e


class ParserTests(unittest.TestCase):
    def test_basic_expression(self):
        self.assertTrue(str(e.parse_expression("sin(x)**2 + cos(x)**2")))

    def test_pi_and_caret(self):
        self.assertEqual(str(e.parse_expression("sin(π/2)^2")), "1")

    def test_textbook_squared_function_notation(self):
        expr = e.parse_expression("sin^2(x) + cos²(x)")
        self.assertEqual(str(sp.trigsimp(expr)), "1")

    def test_superscript_four(self):
        expr = e.parse_expression("sin⁴(x)")
        self.assertEqual(expr, sp.sin(sp.Symbol("x", real=True))**4)

    def test_implicit_numeric_coefficient(self):
        self.assertEqual(str(e.parse_expression("2sin(x)")), "2*sin(x)")

    def test_reject_unsupported_function(self):
        with self.assertRaises(e.ExpressionInputError):
            e.parse_expression("asin(x)")

    def test_reject_attribute_access(self):
        with self.assertRaises(e.ExpressionInputError):
            e.parse_expression("x.__class__")


class FoundationalProofTests(unittest.TestCase):
    def test_f08_has_independent_geometric_proof(self):
        result = e.prove_identity("sin(x)**2 + cos(x)**2", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("G01", "G03", "G04"))
        self.assertEqual(result.used_theorems, [])
        self.assertEqual(result.to_certificate()["schema"], e.GEO_CERTIFICATE_SCHEMA)

    def test_f08_reverse_direction_is_geometrically_proved(self):
        result = e.prove_identity("1", "sin(x)**2 + cos(x)**2", "RHS to LHS")
        self.assertEqual(result.status, "PROVED")
        self.assertTrue(result.selected_route.startswith("GEO:"))
        self.assertEqual(result.used_theorems, [])

    def test_f09_is_derived_from_f08_and_definitions(self):
        result = e.prove_identity("1+tan(x)**2", "sec(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F08", result.rule_ids)
        self.assertNotIn("F09", result.rule_ids)
        self.assertTrue({"F01", "F03"}.issubset(result.rule_ids))

    def test_f10_is_derived_from_f08_and_definitions(self):
        result = e.prove_identity("1+cot(x)**2", "csc(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F08", result.rule_ids)
        self.assertNotIn("F10", result.rule_ids)
        self.assertTrue({"F02", "F04"}.issubset(result.rule_ids))

    def test_f08_constant_scaled_rearrangement_is_not_self_used(self):
        result = e.prove_identity("2*sin(x)**2+2*cos(x)**2", "2")
        self.assertEqual(result.status, "PROVED")
        self.assertTrue(result.selected_route.startswith("GEO:"))
        self.assertEqual(result.used_theorems, [])


class AlgebraAndDomainTests(unittest.TestCase):
    def test_algebraic_identity(self):
        result = e.prove_identity("2*sin(x)", "sin(x)+sin(x)")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "Algebra only")

    def test_false_identity_counterexample(self):
        result = e.prove_identity("sin(x)", "cos(x)")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)

    def test_original_parameter_typo_is_disproved(self):
        lhs = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-p*cos(x))**2"
        result = e.prove_identity(lhs, "p**2+q**2", "Use full identity catalogue")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)

    def test_domain_restrictions_preserved_through_f09_and_f03(self):
        result = e.prove_identity("1+tan(x)**2", "1/cos(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("cos(x) ≠ 0", result.domain_conditions)

    def test_domain_restrictions_preserved_through_f10_and_f04(self):
        result = e.prove_identity("1+cot(x)**2", "1/sin(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("sin(x) ≠ 0", result.domain_conditions)

    def test_cancelled_original_denominator_is_still_tracked(self):
        result = e.prove_identity("sin(x)/sin(x)", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("sin(x) ≠ 0", result.domain_conditions)

    def test_markdown_export_has_valid_math_delimiters(self):
        result = e.prove_identity("sin(x)", "sin(x)")
        report = result.to_markdown()
        self.assertIn("\\[", report)
        self.assertIn("\\]", report)
        self.assertNotIn('\\"]', report)


class CatalogueProofTests(unittest.TestCase):
    def test_catalogue_statistics_and_index(self):
        stats = e.catalogue_rule_statistics()
        rules = e.load_catalogue_theorems()
        self.assertEqual(stats["indexed_entries"], 136)
        self.assertEqual(stats["executable_equalities"], 125)
        self.assertEqual(len(rules), 125)
        ids = {rule.identity_id for rule in rules}
        self.assertTrue({"F08", "A01", "D03", "H15", "R18"}.issubset(ids))

    def test_f09_and_f03_chain_proves_a_different_claim(self):
        result = e.prove_identity("1+tan(x)**2", "1/cos(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("F09", "F03"))
        self.assertEqual([item["identity_id"] for item in result.used_theorems], ["F09", "F03"])
        identity_steps = [step for step in result.steps if step.theorem_ref]
        self.assertEqual(len(identity_steps), 2)
        self.assertEqual([step.rule_ids[0] for step in identity_steps], ["F09", "F03"])
        self.assertTrue(all(step.substitution for step in identity_steps))
        self.assertIn("F09 → F03", result.to_markdown())
        cert = result.to_certificate()
        self.assertEqual(
            [step["identity_ids"][0] for step in cert["steps"] if step["theorem_reference"]],
            ["F09", "F03"],
        )
        self.assertTrue(all(
            step["symbolic_equivalence_check"] is True
            for step in cert["steps"] if step["from"] is not None
        ))

    def test_f10_and_f04_chain_proves_a_different_claim(self):
        result = e.prove_identity("1+cot(x)**2", "1/sin(x)**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("F10", "F04"))

    def test_f08_is_available_for_a_different_parameter_identity(self):
        lhs = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2"
        result = e.prove_identity(lhs, "p**2+q**2", "Use full identity catalogue")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("F08",))
        self.assertEqual([item["identity_id"] for item in result.used_theorems], ["F08"])
        self.assertIn("Expand squared sums", [step.title for step in result.steps])
        self.assertIn("Factor by parameter groups", [step.title for step in result.steps])
        self.assertTrue(all(
            step.get("symbolic_equivalence_check") is not False
            for step in result.to_certificate()["steps"]
        ))

    def test_f09_as_a_lemma_for_another_claim(self):
        result = e.prove_identity(
            "(1+tan(x)**2)*cos(x)**2", "sec(x)**2*cos(x)**2", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F09", result.rule_ids)
        self.assertIn("cos(x) ≠ 0", result.domain_conditions)

    def test_f10_as_a_lemma_for_another_claim(self):
        result = e.prove_identity(
            "(1+cot(x)**2)*sin(x)**2", "csc(x)**2*sin(x)**2", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertIn("F10", result.rule_ids)
        self.assertIn("sin(x) ≠ 0", result.domain_conditions)

    def test_reverse_f08_uses_unique_shared_context_angle(self):
        cases = [
            ("-sin(x)*tan(x)+sec(x)", "cos(x)", {"F01", "F03", "F08"}),
            ("-cos(x)*cot(x)+csc(x)", "sin(x)", {"F02", "F04", "F08"}),
        ]
        for lhs, rhs, expected_ids in cases:
            with self.subTest(lhs=lhs):
                result = e.prove_identity(lhs, rhs, "Use full identity catalogue")
                self.assertEqual(result.status, "PROVED")
                self.assertTrue(expected_ids.issubset(set(result.rule_ids)))
                self.assertIn("F08", result.rule_ids)

    def test_f08_and_f11_chain_with_variable_substitution(self):
        result = e.prove_identity(
            "sin(x)**2 + cos(x)**2", "sec(y)**2 - tan(y)**2", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("F08", "F11"))
        identity_steps = [step for step in result.steps if step.theorem_ref]
        self.assertEqual(len(identity_steps), 2)
        self.assertEqual(identity_steps[1].substitution, (("x", "y"),))
        self.assertIn("cos(y) ≠ 0", result.domain_conditions)

    def test_angle_addition_is_derived_without_unaudited_catalogue(self):
        result = e.prove_identity(
            "sin(x+y)", "sin(x)*cos(y)+cos(x)*sin(y)", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.to_certificate()["schema"], e.ROTATION_SCHEMA)
        self.assertEqual(result.used_theorems, [])

    def test_half_angle_is_derived_by_rotation_coordinates(self):
        result = e.prove_identity(
            "(1-cos(2*x))/sin(2*x)", "tan(x)", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.to_certificate()["schema"], e.ROTATION_SCHEMA)

    def test_counterexample_precedes_catalogue_search(self):
        result = e.prove_identity("sin(x)", "cos(x)", "Use full identity catalogue")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)

    def test_unknown_dependencies_are_not_admitted(self):
        cat = e.load_catalogue_theorems()
        allowed = e._independent_premises(
            e.parse_expression("sin(x)"), e.parse_expression("cos(x)"), [], cat
        )
        ids = {theorem.identity_id for theorem in allowed}
        self.assertFalse({"A01", "D01", "R01"} & ids)

    def test_certificate_records_f08_provenance(self):
        result = e.prove_identity(
            "(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2",
            "p**2+q**2", "Use full identity catalogue"
        )
        cert = result.to_certificate()
        self.assertEqual(cert["status"], "PROVED")
        self.assertIn("F08 depends on GEO.F08", cert["dependency_provenance"])
        self.assertIn("GEO.F08 is admitted only after replaying G01 -> G03 -> G04",
                      cert["dependency_provenance"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
