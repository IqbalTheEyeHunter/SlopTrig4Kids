# Trigonometric Proof Engine v0.7.1

Complete Windows desktop **source project**, including the GUI, proof engine, geometric foundation, identity catalogue, historical question bank, tests, examples and Windows build scripts. This is a standalone replacement project; no v0.6.1 installation or patch application is required.

## Start on Windows

1. Extract the entire ZIP.
2. With Python 3.11 or newer installed, double-click `run_windows.bat`.
3. Select **Use full identity catalogue** or **Automatic** and enter an identity.
4. Click **Load example** to cycle through the fourteen exercises first.

The launcher installs SymPy if necessary. Installation requires internet access; the installed application runs offline. You can also run `python app.py` directly after `python -m pip install -r requirements.txt`.

To produce a standalone Windows executable, run `build_windows.bat` on Windows. The output is `dist/TrigonometricProofEngine.exe`. The GitHub Actions workflow also builds it on Windows. **This archive contains source and build scripts, not a prebuilt EXE.** The Windows executable build and native Windows GUI were not run in the Linux validation environment.

## SPM algebraic explanations

The default desktop and Markdown reports now show a chain from LHS to RHS using familiar trigonometric identities and ordinary algebra. Quotient/reciprocal substitutions, Pythagorean identities, double/compound angles, common denominators, factoring and cancellation are displayed with reasons. No rotation-coordinate terminology appears in these student reports.

All fourteen exercises have checked algebraic chains. The generator is general: it chooses among normalization paths from both sides rather than storing answers for the exercise list. Original compound-angle notation is preserved in the explanation. When the target is a double-angle identity, its proof cites the independently established parent compound-angle formula instead of the target itself.

The internal exact certificate check is retained. Export certificate includes both the verification data and a replay-checked `student_proof` trace. Edited trace expressions, reasons or mathematical formatting are rejected. v0.7 certificates remain replayable.

For an input beyond the explanation generator's scope, the report explicitly says that no SPM-style explanation was found; it does not invent an algebraic chain. The existing independent geometric route remains available for F08 itself, because assuming F08 to prove F08 would be circular.

## Underlying proof engine

The previous engine lacked audited angle-expansion rules, so even the first exercise could be inconclusive. v0.7 adds a general rotation-coordinate proof algorithm with exact polynomial witnesses. It covers the fourteen exercises, including double angles, shifted angles and half-angles. It does not look up their answers or lift the circularity restrictions.

The original domain ledger is retained. Decimal input such as `0.5` is now exact. The new exported certificates are replayed before acceptance and can be saved/reused in the theorem bank for distinct goals.

See [algorithm and trust boundary](V0.7_Algorithm_and_Trust.md) for the geometric foundations, computational checks and limits. The new route is a replayable proof relative to explicit geometric assumptions, not a general-purpose formal theorem prover. Unsupported cases may still return INCONCLUSIVE.

## Validation and reports

- [Fourteen exercise results](SPM_VALIDATION.md)
- `SPM_VALIDATION.json` — machine-readable results and timings.
- `examples/spm_*.md`, `.txt`, `.json` — full reports and replayable certificates.
- `TEST_RESULTS.txt` — complete test run and environment/limitations.

```text
python -m unittest discover -s tests -v
python validate_spm.py
python verify_certificate.py examples/spm_01_2003.json
```

## Main files

| File | Purpose |
|---|---|
| `app.py` | Desktop GUI and report/export integration |
| `engine.py` | Parser, domain tracking, proof selection and theorem admission |
| `school_algebra.py` | General SPM algebraic explanations, checked trace replay and report formatting |
| `rotation_proof.py` | New geometric rotation expansions and exact polynomial certificates |
| `geometry.py` | Existing independently replayed F08 geometric foundation |
| `exercises.py` | Fourteen exercise inputs for UI and tests; never proof authority |
| `verify_certificate.py` | Standalone geometric/rotation certificate replay |
| `validate_spm.py` | Reproduce all fourteen reports and certificates |
| `knowledge/SKILL.md` | Existing six-function identity catalogue and proof knowledge |
| `build_windows.bat` | Build a Windows executable using PyInstaller |

The earlier question-bank files, candidate data, proof solutions and handbook remain included as historical material. They have not been silently regenerated or relabeled as v0.7. Their previous provenance and counts remain in `question_bank_generation_summary.json`. Regenerate them with `python generate_question_bank.py`; `--clean` discards its candidate cache. Historical v0.6.1 release notes and test results are under `archive/v0.6.1/`.
