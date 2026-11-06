from __future__ import annotations

import json
from pathlib import Path
import sympy as sp
import engine

ROOT = Path(__file__).resolve().parent
catalog = json.loads((ROOT / "candidate_catalog.json").read_text(encoding="utf-8"))
proofs = json.loads((ROOT / "candidate_proofs.json").read_text(encoding="utf-8"))

TEMPLATE_TITLES = {
    "a + b = c": "Addition",
    "a - b = c": "Subtraction",
    "ab = c": "Multiplication",
    "a/b = c": "Division",
    "ab + c = d": "Product plus a term",
    "ab - c = d": "Product minus a term",
    "abc = d": "Triple product",
    "ab/c = d": "Product divided by a term",
    "ab + cd = e": "Sum of two products",
    "ab - cd = e": "Difference of two products",
    "ab/cd = e": "Product divided by another product",
}


def md_code(value: str) -> str:
    return f"`{value}`"


def domain_text(conditions):
    if conditions:
        return "; ".join(f"`{condition}`" for condition in conditions)
    return "All real values of the variables in the stated claim."


def proof_steps(proof: dict) -> list[str]:
    route = proof.get("route", "")
    cert = proof.get("certificate", {})
    if cert.get("schema") == engine.ROTATION_SCHEMA:
        return engine.rotation_report_lines(cert)
    if route.startswith("GEO:") or cert.get("schema") == engine.GEO_CERTIFICATE_SCHEMA:
        return [
            "1. **G01 — Euclidean Pythagorean theorem.** A square-dissection proof establishes the non-trigonometric relation `u**2 + v**2 = r**2` for a right triangle.",
            "2. **G03 — Cartesian squared distance.** Perpendicular projections of a point `(u,v)` give `OP**2 = u**2 + v**2`, with signed coordinates and axis cases handled.",
            "3. **G04 — Unit-circle substitution.** The point `(cos(x), sin(x))` has radius `1`; hence `cos(x)**2 + sin(x)**2 = 1` for every real `x`.",
            "4. **Conclusion.** The requested F08 instance follows from the checked geometric certificate. F08 is not used as a premise in its own proof.",
        ]

    out = []
    number = 0
    for step in proof.get("steps", []):
        before = step.get("previous_expression")
        after = step.get("expression")
        title = step.get("title", "")
        if before is None or title.startswith("Start with") or title.startswith("Match the target"):
            continue
        if before == after:
            continue
        number += 1
        refs = step.get("rule_ids") or []
        theorem = step.get("theorem_ref") or ""
        line = f"{number}. {md_code(before)} → {md_code(after)}"
        if refs:
            line += f" — **{', '.join(refs)}**"
        out.append(line)
        if theorem:
            out.append(f"   - Applied theorem: {theorem}")
        if step.get("note"):
            out.append(f"   - Justification: {step['note']}")
        substitution = step.get("substitution") or {}
        if substitution:
            out.append("   - Variable substitution: " + ", ".join(
                f"`{name} → {value}`" for name, value in substitution.items()
            ))
        if step.get("domain_conditions"):
            out.append("   - Conditions: " + "; ".join(
                f"`{condition}`" for condition in step["domain_conditions"]
            ))
    if not out:
        out.append("The claim is established by exact algebraic equality; the certificate records the checked transformation.")
    return out


# Render the finite template corpus in the original operation order.
question_sections = []
solution_sections = []
per_stats = []
question_number = 0

for template_index, group in enumerate(catalog["per_template"], 1):
    template = group["template"]
    proved_entries = []
    for candidate in group["entries"]:
        key = "|".join(candidate["key"])
        proof = proofs.get(key, {})
        if proof.get("status") == "PROVED":
            proved_entries.append((candidate, proof))

    per_stats.append({
        "template": template,
        "raw_assignments": group["raw_assignments"],
        "unique_candidates": group["unique_candidates"],
        "proved_entries": len(proved_entries),
    })

    qbody = [f"## {template}", ""]
    sbody = [f"## {template}", ""]
    if not proved_entries:
        qbody.append("No identity in this finite search space was returned as `PROVED` by v0.6.0.")
        sbody.append("No proved entry was generated for this operation template in the stated finite search space.")
        question_sections.append("\n".join(qbody))
        solution_sections.append("\n".join(sbody))
        continue

    for local_index, (candidate, proof) in enumerate(proved_entries, 1):
        question_number += 1
        qid = f"QB-{template_index:02d}-{local_index:03d}"
        claim = f"{candidate['lhs']} = {candidate['rhs']}"
        assignment = candidate.get("assignment", {})
        conditions = proof.get("domain", [])
        route = proof.get("route", "")
        rule_ids = proof.get("rule_ids", [])
        cert = proof.get("certificate", {})

        qbody += [f"### {qid} — {md_code(claim)}", "", "**Variable assignment**"]
        for variable in ("a", "b", "c", "d", "e"):
            if variable in assignment:
                qbody.append(f"- `{variable} = {assignment[variable]}`")
        qbody += ["", f"**Original common domain:** {domain_text(conditions)}", ""]

        sbody += [f"### {qid} — {md_code(claim)}", "",
                  "**Status:** `PROVED`  ",
                  f"**Selected route:** `{route}`  ",
                  f"**Identity/proof IDs:** `{', '.join(rule_ids) if rule_ids else 'Algebra only'}`  ",
                  f"**Original common domain:** {domain_text(conditions)}", "",
                  "**Proof**", ""]
        sbody.extend(proof_steps(proof))
        sbody += ["", f"**Certificate:** `{cert.get('schema', 'not recorded')}` — `{cert.get('status', 'unknown')}`."]
        provenance = cert.get("dependency_provenance") or []
        if provenance:
            sbody.append("**Dependency provenance**")
            sbody.extend(f"- {item}" for item in provenance)
        sbody.append("")

    question_sections.append("\n".join(qbody))
    solution_sections.append("\n".join(sbody))

raw_total = sum(row["raw_assignments"] for row in catalog["per_template"])
unique_candidate_total = len(catalog["global"])
unique_proved_total = sum(1 for proof in proofs.values() if proof.get("status") == "PROVED")
template_entry_total = sum(row["proved_entries"] for row in per_stats)

# Supplementary examples explicitly test reusable F08/F09/F10 premises.
supplementary = [
    {
        "id": "SUP-001",
        "title": "Orthogonal linear-combination identity",
        "lhs": "(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2",
        "rhs": "p**2+q**2",
        "description": "The corrected parameterised identity; it is not an F08/F09/F10 goal.",
    },
    {
        "id": "SUP-002",
        "title": "Using F09 in a different identity",
        "lhs": "(1+tan(x)**2)*cos(x)**2",
        "rhs": "sec(x)**2*cos(x)**2",
        "description": "F09 is used as a lemma for a distinct target.",
    },
    {
        "id": "SUP-003",
        "title": "Using F10 in a different identity",
        "lhs": "(1+cot(x)**2)*sin(x)**2",
        "rhs": "csc(x)**2*sin(x)**2",
        "description": "F10 is used as a lemma for a distinct target.",
    },
]

supplementary_proofs = {}
for item in supplementary:
    result = engine.prove_identity(item["lhs"], item["rhs"], "Use full identity catalogue")
    supplementary_proofs[item["id"]] = result
    if result.status != "PROVED":
        raise RuntimeError(f"Supplementary example {item['id']} was not proved: {result.status}")

# Question bank: questions and domain only, no derivations.
qheader = [
    "# Trigonometric Proof Engine v0.6.0 — Question Bank", "",
    "**File:** `question-bank.md`  ",
    "**Companion:** `proof-solutions.md`  ",
    "**Purpose:** a question-only training corpus. Full checked derivations are kept in the companion solutions file.", "",
    "## 1. Finite search scope", "",
    "Each metavariable `a`, `b`, `c`, `d`, or `e` is assigned one atom from the following seven-element alphabet, all at the same real angle `x`: ",
    "`sin(x)`, `cos(x)`, `tan(x)`, `cot(x)`, `sec(x)`, `csc(x)`, `1`.", "",
    "All ordered assignments were enumerated for the eleven requested operation templates. This is exhaustive only over this finite alphabet and those templates; it is not a claim of exhaustiveness over arbitrary compound trigonometric expressions, multiple angles, or compound arguments.", "",
    "## 2. Admission rules", "",
    "- Only claims whose v0.6.0 proof route returned `PROVED` are included.",
    "- Candidate discovery is not proof: exact rational/unit-circle reduction only identifies candidates; the proof engine must construct and validate a derivation.",
    "- F08 itself is admitted only through its independent geometric certificate `G01 → G03 → G04`.",
    "- F08, F09 and F10 may be reused as established theorems for different goals, with their audited dependency chains.",
    "- A goal that is F08/F09/F10 itself, including a constant-scaled or rearranged instance, cannot use that same theorem as a premise.",
    "- Original common-domain conditions are retained. Omitted candidates are not thereby proved false.", "",
    "## 3. Search summary", "",
    "| Operation template | Raw assignments | Unique candidates checked | Proved entries |",
    "|---|---:|---:|---:|",
]
for row in per_stats:
    qheader.append(f"| `{row['template']}` | {row['raw_assignments']:,} | {row['unique_candidates']:,} | {row['proved_entries']:,} |")
qheader += [
    "",
    f"**Raw assignments searched:** {raw_total:,}.  ",
    f"**Unique candidate claims checked:** {unique_candidate_total:,}.  ",
    f"**Unique claims returned as PROVED:** {unique_proved_total:,}.  ",
    f"**Template entries recorded (including repeated claims under different templates):** {template_entry_total:,}.",
    "",
    "## 4. Proved questions", "",
    "Only proved questions are listed below. Repeated claims under different operation templates retain separate IDs because the original question structure and variable assignments differ.", "",
]
supplementary_questions = []
for item in supplementary:
    result = supplementary_proofs[item["id"]]
    supplementary_questions.append("\n".join([
        f"### {item['id']} — {item['title']}", "",
        f"**Question:** {md_code(item['lhs'] + ' = ' + item['rhs'])}", "",
        f"**Purpose:** {item['description']}", "",
        f"**Original common domain:** {domain_text(result.domain_conditions)}",
    ]))

question_content = "\n".join(qheader)
question_content += "\n\n---\n\n" + "\n\n---\n\n".join(question_sections)
question_content += "\n\n## 5. Supplementary theorem-reuse questions\n\n"
question_content += "\n\n---\n\n".join(supplementary_questions) + "\n"
(ROOT / "question-bank.md").write_text(question_content, encoding="utf-8")

# Proof solutions: complete proof steps for every question-bank entry.
sheader = [
    "# Trigonometric Proof Engine v0.6.0 — Proof Solutions", "",
    "**Companion question bank:** `question-bank.md`  ",
    "**Purpose:** checked proof derivations for all entries in the v0.6.0 question bank.", "",
    "## 1. Proof policy", "",
    "- Every listed solution corresponds to a question whose engine status is `PROVED`.",
    "- Each algebraic expansion, factorisation and theorem application is shown as a separate step.",
    "- F08/F09/F10 are reusable premises only when the requested goal is not the same theorem (or a constant-scaled/rearranged version of it).",
    "- F08 has an independent geometric certificate; F09 and F10 inherit that audited foundation through F01/F03 and F02/F04 respectively.",
    "- Domain restrictions from the original expressions remain in force throughout the proof.", "",
    "## 2. Solutions for the finite operation-template bank", "",
]
supplementary_solutions = []
for item in supplementary:
    result = supplementary_proofs[item["id"]]
    cert = result.to_certificate()
    body = [f"### {item['id']} — {item['title']}", "",
            f"**Claim:** {md_code(item['lhs'] + ' = ' + item['rhs'])}", "",
            "**Status:** `PROVED`  ",
            f"**Route:** `{result.selected_route}`  ",
            f"**Identity/proof IDs:** `{', '.join(result.rule_ids)}`  ",
            f"**Original common domain:** {domain_text(result.domain_conditions)}", "",
            "**Proof**", ""]
    body.extend(proof_steps({"route": result.selected_route, "certificate": cert,
                             "steps": [{
                                 "title": st.title,
                                 "previous_expression": None if st.previous_expression is None else sp.sstr(st.previous_expression),
                                 "expression": sp.sstr(st.expression),
                                 "note": st.note,
                                 "rule_ids": list(st.rule_ids),
                                 "theorem_ref": st.theorem_ref,
                                 "substitution": {a: b for a, b in st.substitution},
                                 "domain_conditions": list(st.domain_conditions),
                             } for st in result.steps]}))
    body += ["", f"**Certificate:** `{cert.get('schema')}` — `{cert.get('status')}`."]
    provenance = cert.get("dependency_provenance") or []
    if provenance:
        body.append("**Dependency provenance**")
        body.extend(f"- {row}" for row in provenance)
    supplementary_solutions.append("\n".join(body))

# Explicitly document the typo as rejected, never as a proved bank entry.
wrong_lhs = "(p*cos(x)+q*sin(x))**2+(p*sin(x)-p*cos(x))**2"
wrong_result = engine.prove_identity(wrong_lhs, "p**2+q**2", "Use full identity catalogue")
solution_content = "\n".join(sheader)
solution_content += "\n\n---\n\n" + "\n\n---\n\n".join(solution_sections)
solution_content += "\n\n## 3. Supplementary solutions demonstrating theorem reuse\n\n"
solution_content += "\n\n---\n\n".join(supplementary_solutions)
solution_content += "\n\n## 4. Rejected near-miss — not a proved question\n\n"
solution_content += "\n".join([
    f"**Claim as originally typed:** {md_code(wrong_lhs + ' = p**2+q**2')}", "",
    "**Status:** `DISPROVED`", "",
    "The second bracket contains `p*cos(x)` instead of `q*cos(x)`. A single exact counterexample is sufficient:", "",
    "Take `p = 1`, `q = 0`, `x = 0`.", "",
    "- LHS = `(1*1 + 0*0)**2 + (1*0 - 1*1)**2 = 1 + 1 = 2`.",
    "- RHS = `1**2 + 0**2 = 1`.",
    "- Therefore the statement is false as written and must not be marked `PROVED`.", "",
    "The corrected identity in `SUP-001` is proved using F08.", "",
])
(ROOT / "proof-solutions.md").write_text(solution_content, encoding="utf-8")

summary = {
    "engine_version": engine.ENGINE_VERSION,
    "alphabet": ["sin(x)", "cos(x)", "tan(x)", "cot(x)", "sec(x)", "csc(x)", "1"],
    "raw_assignments": raw_total,
    "unique_candidates": unique_candidate_total,
    "unique_proved": unique_proved_total,
    "template_entries": template_entry_total,
    "supplementary_proved": len(supplementary),
    "question_bank_total_entries": template_entry_total + len(supplementary),
    "template_summary": per_stats,
    "proof_status_counts": {
        status: sum(1 for item in proofs.values() if item.get("status") == status)
        for status in sorted({item.get("status") for item in proofs.values()})
    },
    "supplementary_rule_ids": {
        item["id"]: list(supplementary_proofs[item["id"]].rule_ids)
        for item in supplementary
    },
    "original_misprint_status": wrong_result.status,
}
(ROOT / "question_bank_generation_summary.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
)

print("Wrote question-bank.md and proof-solutions.md")
print(json.dumps(summary, indent=2))
