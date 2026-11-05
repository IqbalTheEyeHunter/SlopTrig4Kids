import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine import ExpressionInputError, parse_expression, prove_identity
from recognition import (
    recognize_problem,
    recognition_catalogue_stats,
    recognition_catalogue,
)


class RecognitionCatalogueTests(unittest.TestCase):
    def test_all_55_skill2_classes_have_implemented_routes(self):
        stats = recognition_catalogue_stats(ROOT / "knowledge" / "SKILL-2.md")
        self.assertEqual(stats["knowledge_entries"], 55)
        self.assertEqual(stats["implemented_class_routes"], 55)
        self.assertEqual(stats["missing_implementations"], 0)
        self.assertEqual(stats["unlisted_routes"], 0)
        self.assertEqual(len(recognition_catalogue()), 55)

    def test_each_eqrec_class_has_a_structural_acceptance_case(self):
        cases = {
            "EQREC-001": ("sin(x)=1/2", "Solve for x."),
            "EQREC-002": ("cos(x)=1/2", "Solve for x."),
            "EQREC-003": ("tan(x)=2", "Solve for x."),
            "EQREC-004": ("cot(x)=2", "Solve for x."),
            "EQREC-005": ("sec(x)=2", "Solve for x."),
            "EQREC-006": ("sin(2*x+pi/3)=1/2", "Solve for x."),
            "EQREC-007": ("sin(x)=sin(2*x)", "Solve for x."),
            "EQREC-008": ("cos(x)=cos(2*x)", "Solve for x."),
            "EQREC-009": ("tan(x)=tan(2*x)", "Solve for x."),
            "EQREC-010": ("cot(x)=cot(2*x)", "Solve for x."),
            "EQREC-011": ("sin(x)=cos(pi/2-x)", "Solve for x."),
            "EQREC-012": ("3*sin(x)+4*cos(x)=2", "Solve for x."),
            "EQREC-013": ("3*sin(x)+4*cos(x)=tan(x)", "Solve for x."),
            "EQREC-014": ("sin(x+pi/3)=1/2", "Solve for x."),
            "EQREC-015": ("2*sin(x)**2-3*sin(x)+1=0", "Solve for x."),
            "EQREC-016": ("2*sin(x)**2+3*cos(x)**2=1", "Solve for x."),
            "EQREC-017": ("sin(x)**2=cos(x)**2", "Solve for x."),
            "EQREC-018": ("sin(x)*cos(x)=1/4", "Solve for x."),
            "EQREC-019": ("sin(x)**2+cos(x)**2=1", "Prove the identity."),
            "EQREC-020": ("tan(x)**2-3*tan(x)+2=0", "Solve for x."),
            "EQREC-021": ("sin(x)/(1+cos(x))=tan(x)", "Prove the identity."),
            "EQREC-022": ("sin(2*x)=1/2", "Solve for x."),
            "EQREC-023": ("sin(x+y)=1/2", "Solve for x."),
            "EQREC-024": ("sin(3*x)=1/2", "Solve for x."),
            "EQREC-025": ("sin(x/2)=1/2", "Solve for x."),
            "EQREC-026": ("sin(pi/6)=1/2", "Find the exact value."),
            "EQREC-027": ("sin(x)/(1-cos(x))=0", "Solve for x."),
            "EQREC-028": ("sec(x)+tan(x)=2", "Solve for x."),
            "EQREC-029": ("(1-cos(x))/sin(x)=1", "Solve for x."),
            "EQREC-030": ("abs(cos(2*x))=1/2", "Solve for x."),
            "EQREC-031": ("sqrt(1-cos(x)**2)=sin(x)", "Solve for x."),
            "EQREC-032": ("sin(x)/sin(x)=1", "Identify the original domain before cancellation."),
            "EQREC-033": ("tan(x/2)=2", "Solve for x."),
            "EQREC-034": ("y=a*sin(b*x)+c", "Sketch the graph."),
            "EQREC-035": ("y=a*cos(b*x)+c", "Sketch the graph."),
            "EQREC-036": ("y=a*tan(b*x)+c", "Sketch the graph."),
            "EQREC-037": ("y=abs(cos(2*x))", "Sketch the graph."),
            "EQREC-038": ("sin(x)=1/2", "Graph y=sin(x) and y=1/2."),
            "EQREC-039": ("sin(x)=x/pi", "Solve graphically."),
            "EQREC-040": ("sin(x)=m", "Find the range of m for which there is no solution."),
            "EQREC-041": ("sin(x)=1/2", "State the number of solutions."),
            "EQREC-042": ("sin(x)<=1/2", "Solve the inequality."),
            "EQREC-043": ("sin(x)=1/2", "Solve for 0<=x<=4*pi."),
            "EQREC-044": ("sin(x)=1/2", "Solve for -pi<=x<=pi."),
            "EQREC-045": ("sin(x)=1/2", "Find x in quadrant II."),
            "EQREC-046": ("a*sin(x)=b", "Find conditions on parameters a and b."),
            "EQREC-047": ("tan(A)+tan(B)+tan(C)=tan(A)*tan(B)*tan(C)", "Given A, B and C are angles of a triangle."),
            "EQREC-048": ("sin(x)+sin(2*x)=0", "Solve for x."),
            "EQREC-049": ("sin(x)*cos(2*x)=0", "Solve for x."),
            "EQREC-050": ("sec(x)+tan(x)=2", "Solve for x."),
            "EQREC-051": ("sin(x)=1/2\ncos(x)=1/2", "Solve the simultaneous equations."),
            "EQREC-052": ("sin(cos(x))=1/2", "Solve for x."),
            "EQREC-053": ("sin(x)=x/pi", "Find all roots."),
            "EQREC-054": ("sin(2*x)=2*sin(x)*cos(x)", "Prove the identity."),
            "EQREC-055": (
                "sin(x)**2+cos(x)**2=1\nsin(x)=1/2",
                "Prove the identity, hence solve the equation.",
            ),
        }
        self.assertEqual(len(cases), 55)
        for class_id, (equation, prompt) in cases.items():
            with self.subTest(class_id=class_id, equation=equation):
                result = recognize_problem(equation, prompt)
                self.assertIn(class_id, {match.id for match in result.matches})


class RecognitionSafetyTests(unittest.TestCase):
    def test_recognition_never_claims_proof_or_solution(self):
        result = recognize_problem("sin(x)=1/2", "Solve for x.")
        data = result.to_dict()
        self.assertEqual(result.status, "RECOGNISED")
        self.assertEqual(data["proof_or_solution_status"], "NOT_ESTABLISHED_BY_RECOGNITION")
        self.assertIn("not a proof", result.to_markdown().casefold())

    def test_cancelled_denominator_is_preserved(self):
        result = recognize_problem("sin(x)/sin(x)=1")
        self.assertIn("sin(x) ≠ 0", result.domain_conditions)
        self.assertIn("EQREC-032", {match.id for match in result.matches})

    def test_half_angle_chart_warns_about_omitted_odd_pi_points(self):
        result = recognize_problem("tan(x/2)=2")
        self.assertTrue(any("odd multiples of π" in caution for caution in result.cautions))

    def test_graph_equation_with_nonconstant_rhs_is_recognised(self):
        result = recognize_problem("sin(x)=x/pi", "Solve graphically.")
        self.assertEqual(result.task_type, "Graphical equation / intersection")
        self.assertIn("EQREC-039", {match.id for match in result.matches})
        self.assertIn("EQREC-053", {match.id for match in result.matches})

    def test_degree_notation_is_converted_exactly(self):
        expr = parse_expression("sin(30°)")
        self.assertEqual(str(expr), "1/2")

    def test_vertical_absolute_value_bars_are_supported(self):
        result = recognize_problem("|cos(2*x)|=1/2")
        self.assertIn("EQREC-030", {match.id for match in result.matches})

    def test_malformed_relation_is_rejected(self):
        with self.assertRaises(ExpressionInputError):
            recognize_problem("sin(x) + cos(x)")

    def test_recognition_and_geometric_proof_are_separate_but_both_available(self):
        recognised = recognize_problem("sin(x)**2+cos(x)**2=1", "Prove the identity.")
        self.assertEqual(recognised.status, "RECOGNISED")
        result = prove_identity("sin(x)**2+cos(x)**2", "1")
        self.assertEqual(result.status, "PROVED")
        self.assertEqual(result.selected_route, "GEO: G01 → G03 → G04")
        self.assertEqual(result.used_theorems, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
