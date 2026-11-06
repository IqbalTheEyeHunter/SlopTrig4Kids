import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class QuestionBankArtifactTests(unittest.TestCase):
    def test_question_bank_and_solution_ids_match(self):
        questions = (ROOT / "question-bank.md").read_text(encoding="utf-8")
        solutions = (ROOT / "proof-solutions.md").read_text(encoding="utf-8")
        question_ids = set(re.findall(r"^### ((?:QB-\d+-\d+)|(?:SUP-\d+)) —", questions, re.M))
        solution_ids = set(re.findall(r"^### ((?:QB-\d+-\d+)|(?:SUP-\d+)) —", solutions, re.M))
        self.assertEqual(question_ids, solution_ids)
        self.assertEqual(len([value for value in question_ids if value.startswith("QB-")]), 255)
        self.assertEqual(len([value for value in question_ids if value.startswith("SUP-")]), 3)

    def test_question_bank_is_question_only(self):
        questions = (ROOT / "question-bank.md").read_text(encoding="utf-8")
        self.assertNotIn("**Proof**", questions)
        self.assertNotIn("Applied theorem:", questions)

    def test_generation_summary_matches_artifacts(self):
        summary = json.loads((ROOT / "question_bank_generation_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["engine_version"], "0.6.0")
        self.assertEqual(summary["raw_assignments"], 61397)
        self.assertEqual(summary["unique_candidates"], 156)
        self.assertEqual(summary["unique_proved"], 150)
        self.assertEqual(summary["template_entries"], 255)
        self.assertEqual(summary["supplementary_proved"], 3)
        self.assertEqual(summary["question_bank_total_entries"], 258)
        self.assertEqual(summary["original_misprint_status"], "DISPROVED")

    def test_false_near_miss_is_not_in_question_bank(self):
        questions = (ROOT / "question-bank.md").read_text(encoding="utf-8")
        solutions = (ROOT / "proof-solutions.md").read_text(encoding="utf-8")
        wrong = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-p*cos(x))**2"
        self.assertNotIn(wrong, questions)
        self.assertIn(wrong, solutions)
        self.assertIn("**Status:** `DISPROVED`", solutions)


if __name__ == "__main__":
    unittest.main(verbosity=2)
