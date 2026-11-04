import sys
import unittest
import sympy as sp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from engine import prove_identity, parse_expression, ExpressionInputError


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
    def test_pythagorean_identity(self):
        result = prove_identity("sin(x)**2 + cos(x)**2", "1")
        self.assertEqual(result.status, "PROVED")

    def test_double_angle_identity(self):
        result = prove_identity("(1 - cos(2*x))/sin(2*x)", "tan(x)")
        self.assertEqual(result.status, "PROVED")
        self.assertTrue(result.domain_conditions)

    def test_reciprocal_identity(self):
        result = prove_identity("(sec(x)-tan(x))*(sec(x)+tan(x))", "1")
        self.assertEqual(result.status, "PROVED")

    def test_angle_addition(self):
        result = prove_identity("sin(x+y)", "sin(x)*cos(y)+cos(x)*sin(y)")
        self.assertEqual(result.status, "PROVED")

    def test_false_identity_counterexample(self):
        result = prove_identity("sin(x)", "cos(x)")
        self.assertEqual(result.status, "DISPROVED")
        self.assertIsNotNone(result.counterexample)


if __name__ == "__main__":
    unittest.main()
