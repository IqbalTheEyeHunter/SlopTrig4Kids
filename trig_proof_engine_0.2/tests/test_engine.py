import json
import sys
import unittest
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from engine import (
    prove_identity, parse_expression, ExpressionInputError,
    load_rule_catalogue, ENGINE_VERSION,
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
        self.assertIn("F08", result.rule_ids)
        self.assertEqual(result.selected_route, "LHS to other side")

    def test_double_angle_identity(self):
        result = prove_identity("(1 - cos(2*x))/sin(2*x)", "tan(x)")
        self.assertEqual(result.status, "PROVED")
        self.assertTrue(result.domain_conditions)
        self.assertTrue(set(result.rule_ids).intersection({"D01", "D02", "F01"}))

    def test_reciprocal_identity(self):
        result = prove_identity("(sec(x)-tan(x))*(sec(x)+tan(x))", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertTrue(set(result.rule_ids).intersection({"F01", "F03", "F16"}))

    def test_angle_addition_with_rule_id(self):
        result = prove_identity("sin(x+y)", "sin(x)*cos(y)+cos(x)*sin(y)")
        self.assertEqual(result.status, "PROVED")
        self.assertIn("A01", result.rule_ids)

    def test_false_identity_counterexample(self):
        result = prove_identity("sin(x)", "cos(x)")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)

    def test_specific_proof_direction(self):
        result = prove_identity("1", "sin(x)**2+cos(x)**2", "RHS to LHS")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "RHS to other side")

    def test_alternative_routes_are_returned(self):
        result = prove_identity("sin(x)**2+cos(x)**2", "1")
        self.assertGreaterEqual(len(result.alternative_routes), 1)
        self.assertIn("Difference method", [route.name for route in result.alternative_routes])

    def test_certificate_contains_checked_steps(self):
        result = prove_identity("sin(x+y)", "sin(x)*cos(y)+cos(x)*sin(y)")
        certificate = result.to_certificate()
        self.assertEqual(certificate["engine_version"], ENGINE_VERSION)
        self.assertEqual(certificate["status"], "PROVED")
        checked = [step for step in certificate["steps"] if step["from"] is not None]
        self.assertTrue(checked)
        self.assertTrue(all(step["symbolic_equivalence_check"] is True for step in checked))
        json.dumps(certificate)

    def test_markdown_export_has_valid_math_delimiters(self):
        result = prove_identity("sin(x)", "sin(x)")
        report = result.to_markdown()
        self.assertIn("\\[", report)
        self.assertIn("\\]", report)
        self.assertNotIn('\\"]', report)

    def test_domain_restrictions_preserved(self):
        result = prove_identity("tan(x)", "sin(x)/cos(x)")
        self.assertEqual(result.status, "PROVED")
        self.assertTrue(any("cos(x)" in condition for condition in result.domain_conditions))


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
