"""Regenerate the v0.6.0 question bank and proof solutions.

By default, cached candidate results are reused and only missing candidates
are replayed. Pass --clean to discard the result cache and replay every claim.
"""
from pathlib import Path
import subprocess
import sys
import json

ROOT = Path(__file__).resolve().parent

def run(script, *args):
    subprocess.run([sys.executable, str(ROOT / script), *map(str, args)], cwd=ROOT, check=True)

run("build_candidate_catalog.py")
catalog = json.loads((ROOT / "candidate_catalog.json").read_text(encoding="utf-8"))
proof_path = ROOT / "candidate_proofs.json"
if "--clean" in sys.argv[1:] and proof_path.exists():
    proof_path.unlink()
run("proof_batch_inprocess.py", 0, len(catalog["global"]))
run("render_question_bank.py")
import engine
print(f"v{engine.ENGINE_VERSION}: generated question-bank.md and proof-solutions.md")
