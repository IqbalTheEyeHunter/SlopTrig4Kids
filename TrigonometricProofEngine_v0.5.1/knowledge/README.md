# v0.5.1 Knowledge Source Manifest

This project bundles the following three source documents unchanged:

1. `SKILL.md` — the six-function trigonometric identity catalogue, derivation bank, worked examples and proof discipline.
2. `SKILL-2.md` — Malaysian KSSM Additional Mathematics Form 5 Topic 6.0 cognitive scope, task recognition and the 55 EQREC structural classes.
3. `V0.5_Proof_Knowledge_Handbook.md` — proof foundations, geometric proof bank, algebraic/vector/discrete methods, optional analytic methods, equation-solving methods, dependency safety and implementation acceptance contract.
4. `v0.5.1_manifest.json` — machine-readable authority map, enabled G01/G03/G04 route, F08 dependency policy and documented-only methods.

## How v0.5.1 uses them

- `engine.py` continues to load `SKILL.md` for the audited identity catalogue.
- `recognition.py` loads EQREC headings from `SKILL-2.md`, implements their structural signatures and associates candidate methods with the v0.5 handbook.
- `app.py` exposes all three documents in the offline Knowledge Base tab.

## Authority boundary

A recognition match is not a theorem. A method recommendation is not an executable inference rule. The v0.5.1 engine enables one narrowly scoped geometric certificate route: G01 → G03 → G04 for F08. Its checker replays a fixed dissection schema and exact algebraic obligations relative to AX.REAL, AX.EUCLID, AX.AREA and D.UNIT. Other geometric and analytic recipes remain documented methods until their own typed checkers validate proof certificates.

F08 is never admitted as its own premise. F08-shaped saved theorems require the v0.5.1 GEO certificate; a legacy/v4 status label or symbolic simplifier result cannot supply that dependency. F09–F12 inherit F08 only after the geometric foundation certificate successfully replays.
