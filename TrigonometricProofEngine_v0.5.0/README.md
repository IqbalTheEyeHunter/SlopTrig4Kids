# Trigonometric Proof Engine v0.5.0

**Windows desktop project · Offline · Python 3.11+**

Version 0.5.0 builds on the v0.4.1 desktop interface and introduces the first replayable geometric proof certificate. The main target is the former circularity failure:

\[
\sin^2(x)+\cos^2(x)=1.
\]

The engine now proves this identity through the independent route:

**G01 → G03 → G04 → F08**

- **G01 — Pythagorean theorem by dissection.** A Euclidean area argument establishes the non-trigonometric Pythagorean theorem.
- **G03 — Cartesian squared distance.** Orthogonal projections give \(OP^2=u^2+v^2\), including signed coordinates and axis cases.
- **G04 — Unit-circle substitution.** The point \(P=(\cos x,\sin x)\) has radius one, so the G03 relation gives F08.
- **F08 — Conclusion.** It is never admitted as a premise while it is the open goal.

## What is new in v0.5.0

1. **Independent F08 proof:** F08 is proved before catalogue search using a geometric certificate, not a catalogue rewrite.
2. **Certificate replay:** a narrow GEO checker verifies the schema, dependency chain, exact area algebra, signed-coordinate distance obligations, unit-radius substitution, original-domain ledger and certificate digest.
3. **Circularity protection:** F08 is no longer an unexplained root in the dependency manifest. F09–F12 can depend on F08 only after the built-in geometric certificate successfully replays.
4. **Certificate-safe theorem bank:** v0.5 geometric certificates can be reused only after replay. Legacy v3 certificates remain untrusted; v4 symbolic certificates retain their existing replay path.
5. **Two knowledge databases:** the inherited `knowledge/SKILL.md` catalogue and the new `knowledge/V0.5_Proof_Knowledge_Handbook.md` are bundled and browsable separately.
6. **New UI pages:** Foundation Lab explains and replays the F08 route; v0.5 Handbook supports offline full-text search.
7. **Preserved interface:** the v0.4.1 proof workspace, theorem bank, identity library, report export and certificate export remain available.

## Important trust boundary

The result is **PROVED relative to an explicit Euclidean foundation**. The checker validates the fixed G01 dissection schema and its exact area-algebra consequence, G03's signed-coordinate distance relation, and G04's unit-circle substitution. The underlying Euclidean construction, congruence, angle and area-additivity facts are declared trusted foundations (`AX.EUCLID`, `AX.AREA`); this release does not formalise all of Euclidean geometry from set-theoretic axioms.

The v0.5 handbook documents 30 geometric methods, 20 algebraic/discrete methods, 10 optional analytic methods and 18 equation-solving methods. **Only G01/G03/G04 for F08 are enabled as a new geometric proof route in this release.** The remaining recipes are knowledge/specification, not executable proof rules. The legacy identity catalogue also remains dependency-gated; indexing a formula does not make it an admissible premise.

## Run on Windows

1. Extract the ZIP archive.
2. Install Python 3.11 or newer.
3. Run `run_windows.bat` to launch the application, or `build_windows.bat` to build a standalone executable.
4. The executable is created at `dist\TrigonometricProofEngine.exe`.

The project is offline after dependencies are installed. The ZIP contains the source, both knowledge databases, tests, sample reports and Windows build scripts. A Windows-native `.exe` is not built in this Linux build environment; use the included batch script on Windows. The test suite currently contains 58 passing tests.

## Verify an exported F08 certificate

```bash
python verify_certificate.py examples/F08_geometric_proof_certificate.json
```

The checker reports `VERIFIED` only after replaying the supported GEO schema and its exact obligations. It is currently specific to v0.5 F08 certificates.

## Run tests

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## Project structure

```text
TrigonometricProofEngine_v0.5/
├── app.py
├── engine.py
├── geometry.py
├── verify_certificate.py
├── knowledge/
│   ├── SKILL.md
│   ├── V0.5_Proof_Knowledge_Handbook.md
│   └── SOURCE_INDEX.md
├── tests/
│   ├── test_engine.py
│   ├── test_circularity.py
│   └── test_geometry.py
├── examples/
│   ├── F08_geometric_proof_report.md
│   ├── F08_geometric_proof_certificate.json
│   ├── F09_dependency_proof_report.md
│   └── F09_dependency_proof_certificate.json
├── requirements.txt
├── run_windows.bat
└── build_windows.bat
```

## Certificate format

F08 uses `trigonometric-geometric-proof-certificate-v1`. The certificate records the exact claim, angle, formal coefficient, original domain, profile, trusted foundations, proof nodes, dependency list and SHA-256 integrity digest. The checker reconstructs the expected schema and replays each supported obligation; a status label or digest alone is never proof authority.
