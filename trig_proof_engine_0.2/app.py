"""Professional offline desktop interface for Trigonometric Proof Engine."""
from __future__ import annotations

import json
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

import sympy as sp

from engine import prove_identity, ExpressionInputError, load_rule_catalogue

APP_NAME = "Trigonometric Proof Engine"
VERSION = "0.2.0"


def resource_path(relative: str) -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base / relative


class TrigProofApp(tk.Tk):
    BG = "#F3F6FB"
    NAVY = "#10233F"
    NAVY_2 = "#18385F"
    BLUE = "#2563EB"
    TEXT = "#17263C"
    MUTED = "#66758A"
    WHITE = "#FFFFFF"
    BORDER = "#DCE4EF"
    GREEN = "#16845B"
    RED = "#C2413A"
    AMBER = "#A66A12"

    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME} · {VERSION}")
        self.geometry("1180x820")
        self.minsize(980, 700)
        self.configure(bg=self.BG)
        self.last_result = None
        self._configure_style()
        self._build_header()
        self._build_tabs()
        self._build_statusbar()

    def _configure_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("TNotebook", background=self.BG, borderwidth=0)
        style.configure("TNotebook.Tab", padding=(18, 10), background="#E8EEF7",
                        foreground=self.NAVY_2, font=("Segoe UI", 10, "bold"), borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", self.WHITE)],
                  foreground=[("selected", self.BLUE)])
        style.configure("TFrame", background=self.BG)
        style.configure("Card.TFrame", background=self.WHITE, relief="flat")
        style.configure("TLabel", background=self.BG, foreground=self.TEXT, font=("Segoe UI", 10))
        style.configure("Card.TLabel", background=self.WHITE, foreground=self.TEXT, font=("Segoe UI", 10))
        style.configure("Muted.TLabel", background=self.WHITE, foreground=self.MUTED, font=("Segoe UI", 9))
        style.configure("Section.TLabel", background=self.WHITE, foreground=self.NAVY,
                        font=("Segoe UI", 11, "bold"))
        style.configure("Title.TLabel", background=self.NAVY, foreground=self.WHITE,
                        font=("Segoe UI", 20, "bold"))
        style.configure("Subtitle.TLabel", background=self.NAVY, foreground="#C6D4E8",
                        font=("Segoe UI", 9))
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=(16, 10),
                        background=self.BLUE, foreground=self.WHITE, borderwidth=0)
        style.map("Primary.TButton", background=[("active", "#1D4ED8"), ("disabled", "#9BB8F3")])
        style.configure("Secondary.TButton", font=("Segoe UI", 9, "bold"), padding=(12, 9),
                        background="#EAF0FA", foreground=self.NAVY_2, borderwidth=0)
        style.map("Secondary.TButton", background=[("active", "#DCE7F7")])
        style.configure("TEntry", padding=9, fieldbackground=self.WHITE, bordercolor=self.BORDER)
        style.configure("TCombobox", padding=7, fieldbackground=self.WHITE)

    def _build_header(self):
        header = tk.Frame(self, bg=self.NAVY, height=94)
        header.pack(fill="x")
        header.pack_propagate(False)
        mark = tk.Canvas(header, width=54, height=54, bg=self.NAVY, highlightthickness=0)
        mark.pack(side="left", padx=(24, 14), pady=18)
        mark.create_oval(4, 4, 50, 50, outline="#6FA4FF", width=2)
        mark.create_text(27, 27, text="∑", fill="#FFFFFF", font=("Cambria Math", 27, "bold"))
        title_area = tk.Frame(header, bg=self.NAVY)
        title_area.pack(side="left", pady=17)
        ttk.Label(title_area, text="TRIGONOMETRIC PROOF ENGINE", style="Title.TLabel").pack(anchor="w")
        ttk.Label(title_area, text="Offline symbolic verification · Six elementary trigonometric functions",
                  style="Subtitle.TLabel").pack(anchor="w", pady=(2, 0))
        version = tk.Label(header, text=f"WINDOWS DESKTOP  |  v{VERSION}", bg=self.NAVY,
                           fg="#AFC3DF", font=("Segoe UI", 8, "bold"))
        version.pack(side="right", padx=24)

    def _build_tabs(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=(16, 8))
        self.proof_tab = ttk.Frame(self.notebook)
        self.library_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.proof_tab, text="  PROOF WORKSPACE  ")
        self.notebook.add(self.library_tab, text="  IDENTITY LIBRARY  ")
        self._build_proof_workspace()
        self._build_library()

    def _card(self, parent, **kwargs):
        frame = tk.Frame(parent, bg=self.WHITE, highlightbackground=self.BORDER,
                         highlightthickness=1, bd=0, **kwargs)
        return frame

    def _build_proof_workspace(self):
        root = self.proof_tab
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Identity verification", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(intro, text="Enter both sides of an identity. The engine checks the symbolic difference and preserves original-domain restrictions.",
                  foreground=self.MUTED).pack(anchor="w", pady=(3, 0))

        input_card = self._card(root)
        input_card.pack(fill="x", pady=(0, 12))
        input_inner = tk.Frame(input_card, bg=self.WHITE)
        input_inner.pack(fill="x", padx=18, pady=16)
        columns = tk.Frame(input_inner, bg=self.WHITE)
        columns.pack(fill="x")
        left = tk.Frame(columns, bg=self.WHITE)
        left.pack(side="left", fill="x", expand=True, padx=(0, 10))
        right = tk.Frame(columns, bg=self.WHITE)
        right.pack(side="left", fill="x", expand=True, padx=(10, 0))
        ttk.Label(left, text="LEFT-HAND SIDE (LHS)", style="Section.TLabel").pack(anchor="w", pady=(0, 7))
        ttk.Label(right, text="RIGHT-HAND SIDE (RHS)", style="Section.TLabel").pack(anchor="w", pady=(0, 7))
        self.lhs_var = tk.StringVar(value="sin(x)**2 + cos(x)**2")
        self.rhs_var = tk.StringVar(value="1")
        self.lhs_entry = ttk.Entry(left, textvariable=self.lhs_var, font=("Cambria Math", 12))
        self.rhs_entry = ttk.Entry(right, textvariable=self.rhs_var, font=("Cambria Math", 12))
        self.lhs_entry.pack(fill="x", ipady=4)
        self.rhs_entry.pack(fill="x", ipady=4)
        hint = tk.Label(input_inner, text="Syntax: sin(x), cos(x), tan(x), cot(x), sec(x), csc(x), sqrt(...), pi, +  −  *  /  **. Use explicit multiplication, e.g. 2*sin(x).",
                        bg=self.WHITE, fg=self.MUTED, font=("Segoe UI", 8), anchor="w")
        hint.pack(fill="x", pady=(10, 0))

        controls = tk.Frame(root, bg=self.BG)
        controls.pack(fill="x", pady=(0, 12))
        ttk.Label(controls, text="Proof strategy:").pack(side="left", padx=(2, 8))
        self.method_var = tk.StringVar(value="Automatic")
        method = ttk.Combobox(controls, textvariable=self.method_var, state="readonly", width=31,
                              values=["Automatic", "LHS to RHS", "RHS to LHS", "Both sides to common form",
                                      "Difference method", "Angle expansion first", "Fu transformations first",
                                      "Algebraic reduction first"])
        method.pack(side="left")
        ttk.Button(controls, text="PROVE IDENTITY", style="Primary.TButton", command=self.run_proof).pack(side="right")
        ttk.Button(controls, text="Load example", style="Secondary.TButton", command=self.load_example).pack(side="right", padx=(0, 8))
        ttk.Button(controls, text="Clear", style="Secondary.TButton", command=self.clear_inputs).pack(side="right", padx=(0, 8))

        result_card = self._card(root)
        result_card.pack(fill="both", expand=True)
        result_top = tk.Frame(result_card, bg=self.WHITE)
        result_top.pack(fill="x", padx=18, pady=(14, 8))
        ttk.Label(result_top, text="PROOF REPORT", style="Section.TLabel").pack(side="left")
        actions = tk.Frame(result_top, bg=self.WHITE)
        actions.pack(side="right")
        self.export_md_button = ttk.Button(actions, text="Export Markdown", style="Secondary.TButton",
                                           command=self.export_markdown, state="disabled")
        self.export_md_button.pack(side="left", padx=(0, 6))
        self.export_json_button = ttk.Button(actions, text="Export Certificate", style="Secondary.TButton",
                                             command=self.export_certificate, state="disabled")
        self.export_json_button.pack(side="left", padx=(0, 8))
        self.result_badge = tk.Label(actions, text="READY", bg="#EAF0FA", fg=self.NAVY_2,
                                     font=("Segoe UI", 8, "bold"), padx=10, pady=5)
        self.result_badge.pack(side="left")
        self.result_text = tk.Text(result_card, wrap="word", bg="#FBFCFE", fg=self.TEXT,
                                   font=("Consolas", 10), relief="flat", padx=16, pady=12,
                                   insertbackground=self.TEXT, selectbackground="#CFE0FF")
        self.result_text.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.result_text.insert("1.0", "Welcome to version 0.2. Enter an identity and select PROVE IDENTITY.\n\n"
                                "Choose a proof direction or let Automatic compare multiple routes. "
                                "Recognised transformations are linked to identity IDs in SKILL.md. "
                                "A numerical test alone is never reported as a proof.")
        self.result_text.configure(state="disabled")
        self.bind("<Control-Return>", lambda event: self.run_proof())

    def _build_library(self):
        root = self.library_tab
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Six-function identity reference", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        rule_count = len(load_rule_catalogue(resource_path("knowledge/SKILL.md")))
        ttk.Label(intro, text=f"Search the bundled mathematical specification · {rule_count} indexed identities · Available offline.",
                  foreground=self.MUTED).pack(anchor="w", pady=(3, 0))
        bar = tk.Frame(root, bg=self.BG)
        bar.pack(fill="x", pady=(0, 10))
        self.search_var = tk.StringVar()
        search = ttk.Entry(bar, textvariable=self.search_var)
        search.pack(side="left", fill="x", expand=True)
        search.insert(0, "Search identity IDs, formulas or keywords...")
        search.bind("<FocusIn>", lambda e: self._clear_search_placeholder())
        ttk.Button(bar, text="Search", style="Secondary.TButton", command=self.search_library).pack(side="left", padx=(8, 0))
        ttk.Button(bar, text="Show all", style="Secondary.TButton", command=self.show_library).pack(side="left", padx=(8, 0))
        card = self._card(root)
        card.pack(fill="both", expand=True)
        self.library_text = tk.Text(card, wrap="word", bg=self.WHITE, fg=self.TEXT,
                                    font=("Consolas", 9), relief="flat", padx=14, pady=12)
        scroll = ttk.Scrollbar(card, orient="vertical", command=self.library_text.yview)
        self.library_text.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.library_text.pack(side="left", fill="both", expand=True)
        self.library_text.tag_configure("heading", foreground=self.NAVY, font=("Segoe UI", 11, "bold"))
        self.library_text.tag_configure("match", background="#FFF0B8", foreground="#6B4C00")
        self._load_library_content()

    def _load_library_content(self):
        path = resource_path("knowledge/SKILL.md")
        try:
            self.library_content = path.read_text(encoding="utf-8")
        except Exception as exc:
            self.library_content = f"Unable to load bundled SKILL.md: {exc}"
        self.show_library()

    def _clear_search_placeholder(self):
        if self.search_var.get() == "Search identity IDs, formulas or keywords...":
            self.search_var.set("")

    def show_library(self):
        self.library_text.configure(state="normal")
        self.library_text.delete("1.0", "end")
        self.library_text.insert("1.0", self.library_content)
        self.library_text.configure(state="disabled")

    def search_library(self):
        query = self.search_var.get().strip()
        if not query or query == "Search identity IDs, formulas or keywords...":
            self.show_library()
            return
        lines = self.library_content.splitlines()
        found = [line for line in lines if query.casefold() in line.casefold()]
        self.library_text.configure(state="normal")
        self.library_text.delete("1.0", "end")
        if found:
            self.library_text.insert("1.0", f"SEARCH RESULTS FOR: {query}\n{len(found)} matching line(s)\n\n")
            for line in found:
                self.library_text.insert("end", line + "\n")
            start = "1.0"
            while True:
                pos = self.library_text.search(query, start, stopindex="end", nocase=True)
                if not pos: break
                end = f"{pos}+{len(query)}c"
                self.library_text.tag_add("match", pos, end)
                start = end
        else:
            self.library_text.insert("1.0", f"No matching lines found for '{query}'.")
        self.library_text.configure(state="disabled")

    def _build_statusbar(self):
        bar = tk.Frame(self, bg="#E8EEF7", height=28)
        bar.pack(fill="x", side="bottom")
        self.status_var = tk.StringVar(value="OFFLINE MODE  ·  Six-function scope  ·  Radians  ·  No cloud services")
        tk.Label(bar, textvariable=self.status_var, bg="#E8EEF7", fg=self.MUTED,
                 font=("Segoe UI", 8), anchor="w").pack(fill="x", padx=20, pady=5)

    def _set_report(self, content: str, status: str = "READY"):
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", content)
        self.result_text.configure(state="disabled")
        palette = {
            "PROVED": ("#DDF5E9", self.GREEN),
            "DISPROVED": ("#FDE8E7", self.RED),
            "INCONCLUSIVE": ("#FFF3D8", self.AMBER),
            "ERROR": ("#FDE8E7", self.RED),
            "READY": ("#EAF0FA", self.NAVY_2),
        }
        bg, fg = palette.get(status, palette["READY"])
        self.result_badge.configure(text=status, bg=bg, fg=fg)

    def run_proof(self):
        lhs_text, rhs_text = self.lhs_var.get().strip(), self.rhs_var.get().strip()
        try:
            result = prove_identity(lhs_text, rhs_text, self.method_var.get())
        except ExpressionInputError as exc:
            self._set_report(f"INPUT ERROR\n\n{exc}\n\nSupported functions: sin, cos, tan, cot, sec, csc, sqrt.\nUse explicit multiplication, e.g. 2*sin(x).", "ERROR")
            return
        except Exception as exc:
            self._set_report(f"ENGINE ERROR\n\n{type(exc).__name__}: {exc}", "ERROR")
            return
        self.last_result = result
        self.export_md_button.configure(state="normal")
        self.export_json_button.configure(state="normal")
        self._set_report(self._format_result(result), result.status)
        refs = f"  ·  {len(result.rule_ids)} identity reference(s)" if result.rule_ids else ""
        self.status_var.set(f"ANALYSIS COMPLETE  ·  {result.status}{refs}  ·  Offline symbolic engine")

    def _format_result(self, result):
        lines = [
            "TRIGONOMETRIC IDENTITY REPORT",
            "=" * 84,
            f"Claim:  {sp.sstr(result.lhs)}  =  {sp.sstr(result.rhs)}",
            f"Status: {result.status}",
            f"Selected route: {result.selected_route or 'None'}",
            "",
        ]
        if result.message:
            lines += [result.message, ""]
        lines += ["ORIGINAL COMMON-DOMAIN CONDITIONS", "-" * 84]
        if result.domain_conditions:
            lines.extend(f"• {condition}" for condition in result.domain_conditions)
        else:
            lines.append("No additional restrictions detected; both sides are defined for all real values of their variables.")
        lines += ["", "PROOF / ANALYSIS STEPS", "-" * 84]
        if not result.steps:
            lines.append("No symbolic proof steps were established by the selected strategy.")
        for i, step in enumerate(result.steps, 1):
            side = f" [{step.side}]" if step.side else ""
            refs = f"  [Identity IDs: {', '.join(step.rule_ids)}]" if step.rule_ids else ""
            lines.append(f"{i}. {step.title}{side}{refs}")
            if step.previous_expression is not None:
                lines.append(f"   From: {sp.sstr(step.previous_expression)}")
            lines.append(f"   To:   {sp.sstr(step.expression)}")
            if step.note:
                lines.append(f"   Reason: {step.note}")
            if step.previous_expression is not None:
                lines.append("   Check: exact symbolic equivalence tested")
            lines.append("")
        if result.rule_ids:
            lines += ["IDENTITY DATABASE REFERENCES", "-" * 84,
                      ", ".join(result.rule_ids),
                      "References are attached only when a recognised transformation pattern is detected.", ""]
        if result.alternative_routes:
            lines += ["ALTERNATIVE PROOF ROUTES", "-" * 84]
            for index, route in enumerate(result.alternative_routes, 1):
                refs = f"  [IDs: {', '.join(route.rule_ids)}]" if route.rule_ids else ""
                lines.append(f"{index}. {route.name}{refs}")
                lines.append(f"   {route.summary}")
                lines.append(f"   Steps: {len(route.steps)}")
            lines.append("")
        if result.status == "PROVED":
            lines += ["CONCLUSION", "-" * 84,
                      "The symbolic route establishes LHS − RHS = 0 on the common domain of the original expressions.",
                      "Original domain restrictions remain in force even if a later algebraic form appears defined more broadly.",
                      "The route is heuristic rather than a complete formal proof certificate; each recorded step is checked symbolically."]
        elif result.status == "DISPROVED":
            lines += ["COUNTEREXAMPLE", "-" * 84]
            if result.counterexample:
                lines.append(", ".join(f"{name} = {value:.8g}" for name, value in result.counterexample.items()))
            lines.append(f"LHS ≈ {result.lhs_value:.12g}; RHS ≈ {result.rhs_value:.12g}")
            lines.append("This point is a numerical counterexample to the proposed identity.")
        else:
            lines += ["LIMITATION", "-" * 84,
                      "No proof was found by the selected strategy. No counterexample was found in the numerical checks. The result is inconclusive, not a proof of truth or falsity."]
        lines += ["", "ENGINE SCOPE", "-" * 84,
                  "Real-angle expressions using sin, cos, tan, cot, sec and csc, arithmetic, powers, pi and real square roots.",
                  "Numerical sampling is used only to find counterexamples; it is never used to certify an identity."]
        return "\n".join(lines)

    def export_markdown(self):
        if self.last_result is None:
            return
        path = filedialog.asksaveasfilename(
            title="Export proof report", defaultextension=".md",
            filetypes=[("Markdown report", "*.md"), ("All files", "*.*")],
            initialfile="trigonometric_proof.md",
        )
        if not path:
            return
        try:
            Path(path).write_text(self.last_result.to_markdown(), encoding="utf-8")
            self.status_var.set(f"EXPORTED MARKDOWN  ·  {Path(path).name}")
        except OSError as exc:
            messagebox.showerror("Export failed", str(exc))

    def export_certificate(self):
        if self.last_result is None:
            return
        path = filedialog.asksaveasfilename(
            title="Export symbolic proof certificate", defaultextension=".json",
            filetypes=[("JSON certificate", "*.json"), ("All files", "*.*")],
            initialfile="trigonometric_proof_certificate.json",
        )
        if not path:
            return
        try:
            Path(path).write_text(json.dumps(self.last_result.to_certificate(), indent=2, ensure_ascii=False), encoding="utf-8")
            self.status_var.set(f"EXPORTED CERTIFICATE  ·  {Path(path).name}")
        except OSError as exc:
            messagebox.showerror("Export failed", str(exc))

    def load_example(self):
        examples = [
            ("sin(x)**2 + cos(x)**2", "1"),
            ("(1 - cos(2*x))/sin(2*x)", "tan(x)"),
            ("(sec(x) - tan(x))*(sec(x) + tan(x))", "1"),
            ("sin(x + y)", "sin(x)*cos(y) + cos(x)*sin(y)"),
            ("sin(x)", "cos(x)"),
        ]
        index = getattr(self, "example_index", -1) + 1
        self.example_index = index % len(examples)
        self.lhs_var.set(examples[self.example_index][0])
        self.rhs_var.set(examples[self.example_index][1])
        self.status_var.set(f"EXAMPLE {self.example_index + 1} OF {len(examples)} LOADED")

    def clear_inputs(self):
        self.lhs_var.set("")
        self.rhs_var.set("")
        self.last_result = None
        self.export_md_button.configure(state="disabled")
        self.export_json_button.configure(state="disabled")
        self._set_report("Enter a new identity to begin.", "READY")
        self.status_var.set("READY  ·  Offline symbolic engine")


def main():
    app = TrigProofApp()
    app.mainloop()


if __name__ == "__main__":
    main()
