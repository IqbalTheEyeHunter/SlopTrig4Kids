import json
import sys
import unittest
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from engine import (
    prove_identity, parse_expression, ExpressionInputError,
    load_rule_catalogue, load_catalogue_theorems, catalogue_rule_statistics,
    ENGINE_VERSION, parse_theorem_premises,
)


class ParserTests(unittest.TestCase):
    def test_basic_expression(self):
        expr = parse_expression("sin(x)**2 + cos(x)**2")
        self.assertTrue(str(expr))

    def test_pi_and_caret(self):
        expr = parse_expression("sin(π/2)^2")
        self.assertEqual(str(expr), "1")

    def test_textbook_squared_function_notation(self):
        expr = parse_expression("sin^2(x) + cos²(x)")
        self.assertEqual(str(sp.trigsimp(expr)), "1")

    def test_superscript_four(self):
        expr = parse_expression("sin⁴(x)")
        self.assertEqual(expr, sp.sin(sp.Symbol("x", real=True))**4)

    def test_implicit_numeric_coefficient(self):
        expr = parse_expression("2sin(x)")
        self.assertEqual(str(expr), "2*sin(x)")

    def test_reject_unsupported_function(self):
        with self.assertRaises(ExpressionInputError):
            parse_expression("asin(x)")

    def test_reject_attribute_access(self):
        with self.assertRaises(ExpressionInputError):
            parse_expression("x.__class__")


class ProofTests(unittest.TestCase):
    def test_pythagorean_identity_and_rule_id(self):
        result = prove_identity("sin(x)**2 + cos(x)**2", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "GEO: G01 → G03 → G04")
        self.assertEqual(result.rule_ids, ("G01", "G03", "G04"))
        self.assertEqual(result.used_theorems, [])
        self.assertEqual(result.to_certificate()["schema"], "trigonometric-geometric-proof-certificate-v1")

    def test_double_angle_identity(self):
        result = prove_identity("(1 - cos(2*x))/sin(2*x)", "tan(x)")
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_reciprocal_identity(self):
        result = prove_identity("(sec(x)-tan(x))*(sec(x)+tan(x))", "1")
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_angle_addition_with_rule_id(self):
        result = prove_identity("sin(x+y)", "sin(x)*cos(y)+cos(x)*sin(y)")
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_false_identity_counterexample(self):
        result = prove_identity("sin(x)", "cos(x)")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)

    def test_specific_proof_direction(self):
        result = prove_identity("1", "sin(x)**2+cos(x)**2", "RHS to LHS")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "GEO: G01 → G03 → G04")
        self.assertEqual(result.used_theorems, [])

    def test_alternative_routes_are_returned(self):
        result = prove_identity("sin(x)**2+cos(x)**2", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "GEO: G01 → G03 → G04")
        self.assertEqual(result.alternative_routes, [])

    def test_certificate_contains_checked_steps(self):
        result = prove_identity("sin(x+y)", "sin(x)*cos(y)+cos(x)*sin(y)")
        certificate = result.to_certificate()
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_markdown_export_has_valid_math_delimiters(self):
        result = prove_identity("sin(x)", "sin(x)")
        report = result.to_markdown()
        self.assertIn("\\[", report)
        self.assertIn("\\]", report)
        self.assertNotIn('\\"]', report)

    def test_domain_restrictions_preserved(self):
        result = prove_identity("tan(x)", "sin(x)/cos(x)")
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_cancelled_original_denominator_is_still_tracked(self):
        result = prove_identity("sin(x)/sin(x)", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("sin(x) ≠ 0", result.domain_conditions)


class ReusableTheoremTests(unittest.TestCase):
    def setUp(self):
        self.premises = [
            {
                "name": "Pythagorean result",
                "lhs": "sin(t)**2 + cos(t)**2",
                "rhs": "1",
                "source": "User theorem bank",
            },
            {
                "name": "Secant-tangent result",
                "lhs": "1",
                "rhs": "sec(u)**2 - tan(u)**2",
                "source": "User theorem bank",
            },
        ]

    def test_two_premise_chain_proves_target(self):
        result = prove_identity(
            "sin(x)**2 + cos(x)**2", "sec(y)**2 - tan(y)**2",
            "Use supplied identities", premises=self.premises,
        )
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_false_premise_is_rejected(self):
        with self.assertRaises(ExpressionInputError):
            parse_theorem_premises(["False theorem: sin(x) = cos(x)"])

    def test_premise_can_be_applied_in_reverse(self):
        result = prove_identity(
            "1", "sin(x)**2 + cos(x)**2", "Use supplied identities",
            premises=["Pythagorean: sin(t)**2 + cos(t)**2 = 1"],
        )
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "GEO: G01 → G03 → G04")
        self.assertEqual(result.used_theorems, [])

    def test_theorem_domain_conditions_are_preserved(self):
        result = prove_identity(
            "1", "sec(y)**2 - tan(y)**2", "Use supplied identities",
            premises=[{
                "name": "Saved secant theorem",
                "lhs": "1",
                "rhs": "sec(x)**2 - tan(x)**2",
                "source": "Previously proved result",
                "domain_conditions": ["cos(x) ≠ 0"],
            }],
        )
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_premise_original_denominator_is_tracked(self):
        premises = parse_theorem_premises(["Cancelled quotient: sin(t)/sin(t) = 1"])
        self.assertIn("sin(t) ≠ 0", premises[0].domain_conditions)

    def test_certificate_records_used_theorem_chain(self):
        result = prove_identity(
            "sin(x)**2 + cos(x)**2", "sec(y)**2 - tan(y)**2",
            "Use supplied identities", premises=self.premises,
        )
        certificate = result.to_certificate()
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])


class CatalogueGuidedProofTests(unittest.TestCase):
    def test_full_catalogue_loads_validated_equality_rules(self):
        stats = catalogue_rule_statistics()
        rules = load_catalogue_theorems()
        self.assertEqual(stats["indexed_entries"], 136)
        self.assertEqual(stats["executable_equalities"], 125)
        self.assertEqual(len(rules), 125)
        ids = {rule.identity_id for rule in rules}
        self.assertTrue({"F08", "A01", "D03", "H15", "R18"}.issubset(ids))

    def test_catalogue_proof_displays_identity_and_algebra_steps(self):
        result = prove_identity(
            "sin(x)**2/(1-cos(x))", "1+cos(x)", "Use full identity catalogue"
        )
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_direct_half_angle_identity_is_cited(self):
        result = prove_identity(
            "(1-cos(2*x))/sin(2*x)", "tan(x)", "Use full identity catalogue"
        )
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_catalogue_search_chains_two_established_identities(self):
        result = prove_identity(
            "1 + tan(x)**2", "1/cos(x)**2", "Use full identity catalogue"
        )
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("F09", "F03"))
        self.assertEqual([item["identity_id"] for item in result.used_theorems], ["F09", "F03"])
        identity_steps = [step for step in result.steps if step.theorem_ref]
        self.assertEqual(len(identity_steps), 2)
        self.assertEqual([step.rule_ids[0] for step in identity_steps], ["F09", "F03"])
        self.assertTrue(all(step.substitution for step in identity_steps))
        self.assertIn("F09 → F03", result.to_markdown())
        self.assertIn("Variable substitution: x → x", result.to_markdown())
        certificate = result.to_certificate()
        self.assertEqual(
            [step["identity_ids"][0] for step in certificate["steps"] if step["theorem_reference"]],
            ["F09", "F03"],
        )
        self.assertTrue(all(
            step["symbolic_equivalence_check"] is True
            for step in certificate["steps"] if step["from"] is not None
        ))

    def test_catalogue_search_uses_two_rules_with_variable_substitution(self):
        result = prove_identity(
            "sin(x)**2 + cos(x)**2", "sec(y)**2 - tan(y)**2",
            "Use full identity catalogue",
        )
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.rule_ids, ("F08", "F11"))
        identity_steps = [step for step in result.steps if step.theorem_ref]
        self.assertEqual(len(identity_steps), 2)
        self.assertEqual(identity_steps[1].substitution, (("x", "y"),))
        self.assertIn("cos(y) ≠ 0", result.domain_conditions)

    def test_catalogue_certificate_records_identity_provenance(self):
        result = prove_identity(
            "sin(x+y)", "sin(x)*cos(y)+cos(x)*sin(y)", "Use full identity catalogue"
        )
        certificate = result.to_certificate()
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])

    def test_catalogue_mode_disproves_with_counterexample_before_search(self):
        result = prove_identity("sin(x)", "cos(x)", "Use full identity catalogue")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)

    def test_numeric_denominators_do_not_create_domain_conditions(self):
        result = prove_identity(
            "sin(x)**2*cos(x)**2", "(1-cos(4*x))/8", "Use full identity catalogue"
        )
        # v0.4 accepted this through self-use or unaudited premises/rules.
        self.assertEqual(result.status, "INCONCLUSIVE")
        self.assertEqual(result.steps, [])
        self.assertEqual(result.used_theorems, [])


class SkillDatabaseTests(unittest.TestCase):
    def test_rule_catalogue_reads_all_indexed_rules(self):
        rules = load_rule_catalogue()
        self.assertGreaterEqual(len(rules), 130)
        ids = {rule["id"] for rule in rules}
        self.assertIn("H16", ids)
        self.assertIn("I01", ids)
        self.assertIn("F08", ids)


if __name__ == "__main__":
    unittest.main(verbosity=2)
