# v0.5.1 Knowledge Source Manifest

This project bundles the following three source documents unchanged:

1. `SKILL.md` — the six-function trigonometric identity catalogue, derivation bank, worked examples and proof discipline.
2. `SKILL-2.md` — Malaysian KSSM Additional Mathematics Form 5 Topic 6.0 cognitive scope, task recognition and the 55 EQREC structural classes.
3. `V0.5_Proof_Knowledge_Handbook.md` — proof foundations, geometric proof bank, algebraic/vector/discrete methods, optional analytic methods, equation-solving methods, dependency safety and implementation acceptance contract.

## How v0.5.1 uses them

- `engine.py` continues to load `SKILL.md` for the audited identity catalogue.
- `recognition.py` loads EQREC headings from `SKILL-2.md`, implements their structural signatures and associates candidate methods with the v0.5 handbook.
- `app.py` exposes all three documents in the offline Knowledge Base tab.

## Authority boundary

A recognition match is not a theorem. A method recommendation is not an executable inference rule. The geometric and analytic recipes in the v0.5 handbook remain documented methods until a dedicated typed checker validates their proof certificates. The current engine must not label F08 PROVED through self-use or through a dependent identity.
