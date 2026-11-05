import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import app
import engine


class MalayLocalizationTests(unittest.TestCase):
    def test_application_name_and_version(self):
        self.assertEqual(app.APP_NAME, "Enjin Pembuktian Trigonometri")
        self.assertEqual(app.VERSION, "0.6.1")

    def test_malay_strategy_labels_map_to_unchanged_engine_methods(self):
        self.assertEqual(app.METHOD_LABEL_TO_ENGINE["Katalog identiti penuh"], "Use full identity catalogue")
        self.assertEqual(app.METHOD_LABEL_TO_ENGINE["Automatik"], "Automatic")
        self.assertEqual(app.METHOD_LABEL_TO_ENGINE["Gunakan identiti yang dibekalkan"], "Use supplied identities")
        for label, method in app.METHOD_LABEL_TO_ENGINE.items():
            result = engine.prove_identity("sin(x)**2+cos(x)**2", "1", method)
            self.assertEqual(result.status, "PROVED", label)

    def test_status_codes_have_malay_display_labels(self):
        self.assertEqual(app.STATUS_LABELS_MS["PROVED"], "TERBUKTI")
        self.assertEqual(app.STATUS_LABELS_MS["DISPROVED"], "DISANGKAL")
        self.assertEqual(app.STATUS_LABELS_MS["INCONCLUSIVE"], "BELUM DAPAT DIPASTIKAN")
        self.assertEqual(app.STATUS_LABELS_MS["ERROR"], "RALAT")

    def test_input_error_messages_are_malay(self):
        from engine import ExpressionInputError
        self.assertEqual(app.translate_input_error_ms(ExpressionInputError("Please enter an expression.")),
                         "Sila masukkan ungkapan matematik.")
        translated = app.translate_input_error_ms(ExpressionInputError("Unsupported function 'sinh'. Use sin, cos, tan, cot, sec, csc or sqrt."))
        self.assertIn("Fungsi 'sinh' tidak disokong", translated)

    def test_malay_identity_library_contains_all_indexed_rows(self):
        content = (ROOT / "knowledge" / "Panduan_Identiti_MS.md").read_text(encoding="utf-8")
        ids = {line.split("|")[1].strip() for line in content.splitlines()
               if line.startswith("| ") and len(line.split("|")) > 3
               and re.fullmatch(r"[A-Z]\d{2}", line.split("|")[1].strip())}
        self.assertEqual(len(ids), 136)
        self.assertIn("Pustaka Rujukan Identiti Trigonometri", content)
        self.assertIn("Syarat domain", content)
        stats = engine.catalogue_rule_statistics(ROOT / "knowledge" / "Panduan_Identiti_MS.md")
        self.assertEqual(stats["indexed_entries"], 136)
        self.assertEqual(stats["executable_equalities"], 125)

    def test_malay_question_and_solution_ids_still_match(self):
        questions = (ROOT / "question-bank.md").read_text(encoding="utf-8")
        solutions = (ROOT / "proof-solutions.md").read_text(encoding="utf-8")
        qids = set(re.findall(r"^### ((?:QB-\d+-\d+)|(?:SUP-\d+)) —", questions, re.M))
        sids = set(re.findall(r"^### ((?:QB-\d+-\d+)|(?:SUP-\d+)) —", solutions, re.M))
        self.assertEqual(qids, sids)
        self.assertEqual(len(qids), 258)


if __name__ == "__main__":
    unittest.main(verbosity=2)
