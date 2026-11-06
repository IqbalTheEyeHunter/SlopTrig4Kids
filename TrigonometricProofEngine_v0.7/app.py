"""Professional offline desktop interface for Trigonometric Proof Engine."""
from __future__ import annotations

import json
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from pathlib import Path

import sympy as sp
import engine
from exercises import EXERCISES

from engine import (
    prove_identity, ExpressionInputError, load_rule_catalogue,
    parse_theorem_premises, catalogue_rule_statistics,
)
from geometry import geometric_proof_steps

APP_NAME = "Trigonometric Proof Engine"
VERSION = "0.7.0"


def resource_path(relative: str) -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base / relative


def user_data_dir() -> Path:
    """Return a writable per-user data directory (outside PyInstaller's bundle)."""
    if os.name == "nt":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:
        base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    folder = base / "TrigonometricProofEngine"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


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
        self.geometry("1180x760")
        self.minsize(900, 600)
        self.configure(bg=self.BG)
        self.last_result = None
        self.theorem_bank_path = user_data_dir() / "theorem_bank.json"
        self.theorem_bank = self._load_theorem_bank()
        self._configure_style()
        self._build_header()
        self._build_tabs()
        self._build_statusbar()
        # Route mouse-wheel input to the active page or to an inner text/table view.
        self.bind_all("<MouseWheel>", self._on_mousewheel, add="+")
        self.bind_all("<Button-4>", self._on_mousewheel, add="+")
        self.bind_all("<Button-5>", self._on_mousewheel, add="+")

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
        self.theorem_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.proof_tab, text="  PROOF WORKSPACE  ")
        self.notebook.add(self.theorem_tab, text="  THEOREM BANK  ")
        self.notebook.add(self.library_tab, text="  IDENTITY LIBRARY  ")

        # Each notebook page has its own vertical scroll area. This keeps the
        # complete workspace accessible on smaller displays and short windows.
        self.proof_page, self.proof_canvas = self._create_scrollable_page(self.proof_tab)
        self.theorem_page, self.theorem_canvas = self._create_scrollable_page(self.theorem_tab)
        self.library_page, self.library_canvas = self._create_scrollable_page(self.library_tab)
        self._page_canvases = {
            str(self.proof_tab): self.proof_canvas,
            str(self.theorem_tab): self.theorem_canvas,
            str(self.library_tab): self.library_canvas,
        }

        self._build_proof_workspace()
        self._build_theorem_bank()
        self._build_library()

    def _create_scrollable_page(self, page):
        """Create a vertically scrollable content frame inside a notebook page."""
        shell = tk.Frame(page, bg=self.BG)
        shell.pack(fill="both", expand=True)
        canvas = tk.Canvas(shell, bg=self.BG, highlightthickness=0, bd=0)
        scrollbar = ttk.Scrollbar(shell, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        content = tk.Frame(canvas, bg=self.BG)
        window_id = canvas.create_window((0, 0), window=content, anchor="nw")
        content.bind(
            "<Configure>",
            lambda _event, c=canvas: c.configure(scrollregion=c.bbox("all")),
        )
        canvas.bind(
            "<Configure>",
            lambda event, c=canvas, item=window_id: c.itemconfigure(item, width=event.width),
        )
        return content, canvas

    def _on_mousewheel(self, event):
        """Scroll the hovered text/table widget, otherwise the active notebook page."""
        if getattr(event, "num", None) == 4:
            units = -3
        elif getattr(event, "num", None) == 5:
            units = 3
        else:
            delta = getattr(event, "delta", 0)
            if not delta:
                return "break"
            units = -int(delta / 120) * 3 if abs(delta) >= 120 else (-1 if delta > 0 else 1)

        target = self.winfo_containing(event.x_root, event.y_root)
        if isinstance(target, (tk.Text, ttk.Treeview, tk.Listbox)):
            target.yview_scroll(units, "units")
        else:
            selected = self.notebook.select()
            canvas = self._page_canvases.get(selected)
            if canvas is not None:
                canvas.yview_scroll(units, "units")
        return "break"

    def _scroll_to_report(self):
        """Bring the report heading into view after a proof has been generated."""
        if not hasattr(self, "result_card"):
            return
        self.update_idletasks()
        total = self.proof_canvas.bbox("all")
        if not total:
            return
        content_height = max(1, total[3] - total[1])
        report_top = max(0, self.result_card.winfo_y() - 8)
        self.proof_canvas.yview_moveto(min(1.0, report_top / content_height))

    def _scroll_to_input(self):
        self.proof_canvas.yview_moveto(0.0)

    def _card(self, parent, **kwargs):
        frame = tk.Frame(parent, bg=self.WHITE, highlightbackground=self.BORDER,
                         highlightthickness=1, bd=0, **kwargs)
        return frame

    def _load_theorem_bank(self):
        if not self.theorem_bank_path.exists():
            return []
        try:
            records = json.loads(self.theorem_bank_path.read_text(encoding="utf-8"))
            if not isinstance(records, list):
                return []
            valid = []
            for record in records:
                if not isinstance(record, dict):
                    continue
                try:
                    parse_theorem_premises([record])
                    valid.append(record)
                except Exception:
                    continue
            return valid
        except (OSError, json.JSONDecodeError):
            return []

    def _save_theorem_bank(self):
        try:
            self.theorem_bank_path.parent.mkdir(parents=True, exist_ok=True)
            self.theorem_bank_path.write_text(
                json.dumps(self.theorem_bank, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            self._refresh_theorem_bank_view()
            self.bank_check.configure(
                text=f"Include saved theorem bank ({len(self.theorem_bank)} available)"
            )
            return True
        except OSError as exc:
            messagebox.showerror("Theorem bank save failed", str(exc))
            return False

    def _build_theorem_bank(self):
        root = self.theorem_page
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Reusable theorem bank", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(
            intro,
            text="Store identities and results from earlier proofs. Only audited identities or replayable geometric, rotation or v4 certificates can support a proof. The bank is saved locally and remains available offline.",
            foreground=self.MUTED,
        ).pack(anchor="w", pady=(3, 0))

        add_card = self._card(root)
        add_card.pack(fill="x", pady=(0, 12))
        form = tk.Frame(add_card, bg=self.WHITE)
        form.pack(fill="x", padx=16, pady=14)
        ttk.Label(form, text="ADD A REUSABLE IDENTITY", style="Section.TLabel").grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 9)
        )
        ttk.Label(form, text="Name").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=4)
        self.bank_name_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.bank_name_var).grid(row=1, column=1, sticky="ew", pady=4)
        ttk.Label(form, text="Left side").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=4)
        self.bank_lhs_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.bank_lhs_var, font=("Cambria Math", 10)).grid(
            row=2, column=1, sticky="ew", pady=4
        )
        ttk.Label(form, text="Right side").grid(row=3, column=0, sticky="w", padx=(0, 8), pady=4)
        self.bank_rhs_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.bank_rhs_var, font=("Cambria Math", 10)).grid(
            row=3, column=1, sticky="ew", pady=4
        )
        form.columnconfigure(1, weight=1)
        form_actions = tk.Frame(form, bg=self.WHITE)
        form_actions.grid(row=4, column=1, sticky="e", pady=(8, 0))
        ttk.Button(form_actions, text="Add identity", style="Primary.TButton",
                   command=self.add_theorem_to_bank).pack(side="right")
        ttk.Button(form_actions, text="Clear fields", style="Secondary.TButton",
                   command=self.clear_theorem_fields).pack(side="right", padx=(0, 8))

        list_card = self._card(root)
        list_card.pack(fill="both", expand=True)
        list_top = tk.Frame(list_card, bg=self.WHITE)
        list_top.pack(fill="x", padx=14, pady=(12, 8))
        ttk.Label(list_top, text="SAVED IDENTITIES", style="Section.TLabel").pack(side="left")
        self.bank_count_label = ttk.Label(list_top, text="", style="Muted.TLabel")
        self.bank_count_label.pack(side="left", padx=(10, 0))
        tree_frame = tk.Frame(list_card, bg=self.WHITE)
        tree_frame.pack(fill="both", expand=True, padx=12, pady=(0, 8))
        columns = ("name", "identity", "source")
        self.theorem_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=9)
        self.theorem_tree.heading("name", text="THEOREM / RESULT")
        self.theorem_tree.heading("identity", text="IDENTITY")
        self.theorem_tree.heading("source", text="SOURCE")
        self.theorem_tree.column("name", width=190, minwidth=130)
        self.theorem_tree.column("identity", width=570, minwidth=250)
        self.theorem_tree.column("source", width=150, minwidth=100)
        scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.theorem_tree.yview)
        self.theorem_tree.configure(yscrollcommand=scroll.set)
        self.theorem_tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        bank_actions = tk.Frame(list_card, bg=self.WHITE)
        bank_actions.pack(fill="x", padx=14, pady=(0, 12))
        ttk.Button(bank_actions, text="Remove selected", style="Secondary.TButton",
                   command=self.remove_selected_theorem).pack(side="left")
        ttk.Button(bank_actions, text="Import JSON", style="Secondary.TButton",
                   command=self.import_theorem_bank).pack(side="left", padx=(8, 0))
        ttk.Button(bank_actions, text="Export JSON", style="Secondary.TButton",
                   command=self.export_theorem_bank).pack(side="left", padx=(8, 0))
        self._refresh_theorem_bank_view()

    def _refresh_theorem_bank_view(self):
        if not hasattr(self, "theorem_tree"):
            return
        for item in self.theorem_tree.get_children():
            self.theorem_tree.delete(item)
        for index, theorem in enumerate(self.theorem_bank):
            equation = f"{theorem.get('lhs', '')} = {theorem.get('rhs', '')}"
            self.theorem_tree.insert(
                "", "end", iid=str(index),
                values=(theorem.get("name", f"Theorem {index + 1}"), equation,
                        theorem.get("source", "User supplied")),
            )
        if hasattr(self, "bank_count_label"):
            self.bank_count_label.configure(text=f"{len(self.theorem_bank)} saved")

    def add_theorem_to_bank(self):
        record = {
            "name": self.bank_name_var.get().strip() or f"User identity {len(self.theorem_bank) + 1}",
            "lhs": self.bank_lhs_var.get().strip(),
            "rhs": self.bank_rhs_var.get().strip(),
            "source": "User theorem bank",
        }
        try:
            parse_theorem_premises([record])
        except ExpressionInputError as exc:
            messagebox.showerror("Identity not accepted", str(exc))
            return
        self.theorem_bank.append(record)
        if self._save_theorem_bank():
            self.clear_theorem_fields()
            self.status_var.set("THEOREM BANK UPDATED  ·  Identity symbolically validated")

    def clear_theorem_fields(self):
        self.bank_name_var.set("")
        self.bank_lhs_var.set("")
        self.bank_rhs_var.set("")

    def remove_selected_theorem(self):
        selection = self.theorem_tree.selection()
        if not selection:
            messagebox.showinfo("Select an identity", "Choose an identity in the theorem bank first.")
            return
        indices = sorted((int(item) for item in selection), reverse=True)
        for index in indices:
            if 0 <= index < len(self.theorem_bank):
                self.theorem_bank.pop(index)
        self._save_theorem_bank()

    def import_theorem_bank(self):
        path = filedialog.askopenfilename(
            title="Import theorem bank", filetypes=[("JSON theorem bank", "*.json"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            records = json.loads(Path(path).read_text(encoding="utf-8"))
            if not isinstance(records, list):
                raise ValueError("The selected file must contain a JSON list of theorem records.")
            # Validate the entire import before changing the local bank.
            parse_theorem_premises(records)
            self.theorem_bank.extend(records)
            self._save_theorem_bank()
        except Exception as exc:
            messagebox.showerror("Import failed", str(exc))

    def export_theorem_bank(self):
        path = filedialog.asksaveasfilename(
            title="Export theorem bank", defaultextension=".json",
            filetypes=[("JSON theorem bank", "*.json"), ("All files", "*.*")],
            initialfile="trigonometric_theorem_bank.json",
        )
        if not path:
            return
        try:
            Path(path).write_text(json.dumps(self.theorem_bank, indent=2, ensure_ascii=False), encoding="utf-8")
        except OSError as exc:
            messagebox.showerror("Export failed", str(exc))

    def _build_proof_workspace(self):
        root = self.proof_page
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Identity verification", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(intro, text="Enter both sides of an identity. Catalogue-guided mode shows every established identity substitution and each algebraic step.",
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

        ttk.Label(input_inner, text="ADDITIONAL IDENTITIES / PREVIOUSLY ESTABLISHED RESULTS",
                  style="Section.TLabel").pack(anchor="w", pady=(12, 6))
        self.premises_text = tk.Text(
            input_inner, height=3, wrap="word", bg="#FBFCFE", fg=self.TEXT,
            font=("Consolas", 9), relief="solid", bd=1, highlightthickness=0,
            padx=8, pady=6, insertbackground=self.TEXT,
        )
        self.premises_text.pack(fill="x")
        tk.Label(
            input_inner,
            text="Only catalogue identities with audited, independent dependencies are searched. "
                 "You may add extra identities here; use one per line: Name: left expression = right expression.",
            bg=self.WHITE, fg=self.MUTED, font=("Segoe UI", 8), anchor="w",
        ).pack(fill="x", pady=(5, 0))
        theorem_options = tk.Frame(input_inner, bg=self.WHITE)
        theorem_options.pack(fill="x", pady=(7, 0))
        self.use_saved_bank_var = tk.BooleanVar(value=True)
        self.bank_check = ttk.Checkbutton(
            theorem_options,
            text=f"Include saved theorem bank ({len(self.theorem_bank)} available)",
            variable=self.use_saved_bank_var,
        )
        self.bank_check.pack(side="left")
        ttk.Button(theorem_options, text="Manage theorem bank", style="Secondary.TButton",
                   command=lambda: self.notebook.select(self.theorem_tab)).pack(side="right")

        controls = tk.Frame(root, bg=self.BG)
        controls.pack(fill="x", pady=(0, 12))
        ttk.Label(controls, text="Proof strategy:").pack(side="left", padx=(2, 8))
        self.method_var = tk.StringVar(value="Use full identity catalogue")
        method = ttk.Combobox(controls, textvariable=self.method_var, state="readonly", width=34,
                              values=["Use full identity catalogue", "Automatic", "LHS to RHS", "RHS to LHS", "Both sides to common form",
                                      "Difference method", "Use supplied identities", "Angle expansion first", "Fu transformations first",
                                      "Algebraic reduction first"])
        method.pack(side="left")
        ttk.Button(controls, text="PROVE IDENTITY", style="Primary.TButton", command=self.run_proof).pack(side="right")
        ttk.Button(controls, text="Load example", style="Secondary.TButton", command=self.load_example).pack(side="right", padx=(0, 8))
        ttk.Button(controls, text="Clear", style="Secondary.TButton", command=self.clear_inputs).pack(side="right", padx=(0, 8))

        result_card = self._card(root)
        result_card.pack(fill="x", pady=(0, 12))
        self.result_card = result_card
        result_top = tk.Frame(result_card, bg=self.WHITE)
        result_top.pack(fill="x", padx=18, pady=(14, 8))
        ttk.Label(result_top, text="PROOF REPORT", style="Section.TLabel").pack(side="left")
        actions = tk.Frame(result_top, bg=self.WHITE)
        actions.pack(side="right")
        ttk.Button(actions, text="Back to inputs", style="Secondary.TButton",
                   command=self._scroll_to_input).pack(side="left", padx=(0, 6))
        self.export_md_button = ttk.Button(actions, text="Export Markdown", style="Secondary.TButton",
                                           command=self.export_markdown, state="disabled")
        self.export_md_button.pack(side="left", padx=(0, 6))
        self.export_json_button = ttk.Button(actions, text="Export Certificate", style="Secondary.TButton",
                                             command=self.export_certificate, state="disabled")
        self.export_json_button.pack(side="left", padx=(0, 8))
        self.save_theorem_button = ttk.Button(
            actions, text="Save proved result", style="Secondary.TButton",
            command=self.save_current_result_as_theorem, state="disabled",
        )
        self.save_theorem_button.pack(side="left", padx=(0, 8))
        self.result_badge = tk.Label(actions, text="READY", bg="#EAF0FA", fg=self.NAVY_2,
                                     font=("Segoe UI", 8, "bold"), padx=10, pady=5)
        self.result_badge.pack(side="left")
        report_body = tk.Frame(result_card, bg=self.WHITE)
        report_body.pack(fill="x", padx=12, pady=(0, 12))
        self.result_text = tk.Text(report_body, height=16, wrap="word", bg="#FBFCFE", fg=self.TEXT,
                                   font=("Consolas", 10), relief="flat", padx=16, pady=12,
                                   insertbackground=self.TEXT, selectbackground="#CFE0FF")
        report_scroll = ttk.Scrollbar(report_body, orient="vertical", command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=report_scroll.set)
        report_scroll.pack(side="right", fill="y")
        self.result_text.pack(side="left", fill="both", expand=True)
        self.result_text.insert("1.0", "Welcome to version 0.7.0. Enter an identity and select PROVE IDENTITY.\n\n"
                                "The catalogue contains 125 equations; only the audited F01–F12 subset is currently eligible for proof search. "
                                "Each identity substitution is displayed with its ID, followed by separate algebraic steps. "
                                "A numerical test alone is never reported as a proof.")
        self.result_text.configure(state="disabled")
        self.bind("<Control-Return>", lambda event: self.run_proof())

    def _build_library(self):
        root = self.library_page
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Six-function identity reference", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        stats = catalogue_rule_statistics(resource_path("knowledge/SKILL.md"))
        ttk.Label(intro, text=(
            f"Search the bundled mathematical specification · {stats['indexed_entries']} indexed entries · "
            f"{stats['executable_equalities']} executable equality rules · Available offline."
        ), foreground=self.MUTED).pack(anchor="w", pady=(3, 0))
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
        # Always show the beginning of a newly generated report.
        self.result_text.yview_moveto(0.0)
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
            premise_lines = [
                line.strip() for line in self.premises_text.get("1.0", "end").splitlines()
                if line.strip()
            ]
            premises = list(premise_lines)
            if self.use_saved_bank_var.get():
                premises.extend(self.theorem_bank)
            result = prove_identity(lhs_text, rhs_text, self.method_var.get(), premises=premises)
        except ExpressionInputError as exc:
            self._set_report(f"INPUT ERROR\n\n{exc}\n\nSupported functions: sin, cos, tan, cot, sec, csc, sqrt.\nUse explicit multiplication, e.g. 2*sin(x).", "ERROR")
            self.after_idle(self._scroll_to_report)
            return
        except Exception as exc:
            self._set_report(f"ENGINE ERROR\n\n{type(exc).__name__}: {exc}", "ERROR")
            self.after_idle(self._scroll_to_report)
            return
        self.last_result = result
        self.export_md_button.configure(state="normal")
        self.export_json_button.configure(state="normal")
        self.save_theorem_button.configure(state="normal" if result.status == "PROVED" else "disabled")
        self._set_report(self._format_result(result), result.status)
        self.after_idle(self._scroll_to_report)
        geo_certificate = result.certificate_override if getattr(result, "certificate_override", None) else None
        refs = ("  ·  replayed proof certificate" if geo_certificate else
                (f"  ·  {len(result.rule_ids)} identity rule(s)" if result.rule_ids else ""))
        theorem_refs = f"  ·  {len(result.used_theorems)} established result(s)" if result.used_theorems else ""
        self.status_var.set(f"ANALYSIS COMPLETE  ·  {result.status}{refs}{theorem_refs}  ·  Offline symbolic engine")

    def _format_result(self, result):
        certificate = getattr(result, "certificate_override", None)
        if certificate and certificate.get('schema') == engine.ROTATION_SCHEMA:
            return "\n".join([
                "TRIGONOMETRIC IDENTITY REPORT", "=" * 84,
                f"Claim: {result.lhs} = {result.rhs}", "Status: PROVED",
                "Selected route: " + result.selected_route, "",
                "ORIGINAL COMMON-DOMAIN CONDITIONS", *result.domain_conditions, "",
                *engine.rotation_report_lines(certificate), "", "CONCLUSION", result.message,
                "", "ENGINE SCOPE",
                "Rotation route: rational expressions; rational affine angles; up to 4 angle variables, multipliers 24, base denominators 120, and pi/12 shifts.",
                "Unsupported expressions fall back to the bounded catalogue search. INCONCLUSIVE does not establish falsity.",
                "Numerical sampling never certifies an identity."
            ])
        geo_steps = geometric_proof_steps(certificate) if certificate else None
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

        if geo_steps:
            lines += ["", "GEOMETRIC PROOF CHAIN", "-" * 84,
                      "The following are the actual mathematical steps checked by the geometric certificate.", ""]
            for index, geo_step in enumerate(geo_steps, 1):
                lines.append(f"{index}. {geo_step['title']}")
                for detail in geo_step["details"]:
                    lines.append(f"   {detail}")
                lines.append("")
            lines += ["GEOMETRIC CERTIFICATE REPLAY", "-" * 84,
                      f"Schema: {certificate['schema']}",
                      f"Checker: {certificate['checker_version']}",
                      f"Certificate digest: {certificate['certificate_digest']}",
                      "Replay status: VERIFIED",
                      "Trigonometric catalogue premises: none",
                      "Trusted foundations: AX.REAL, AX.EUCLID, AX.AREA, D.UNIT", ""]
            if result.status == "PROVED":
                lines += ["CONCLUSION", "-" * 84,
                          "The independently replayed geometric certificate establishes LHS − RHS = 0 on the original common domain.",
                          "G01 derives the Pythagorean theorem by dissection; G03 derives Cartesian squared distance; G04 applies that result to the unit circle.",
                          "The proof is relative to AX.REAL, AX.EUCLID, AX.AREA and D.UNIT. No F08/F09/F10 catalogue identity is assumed as a premise."]
        else:
            if result.rule_ids:
                identity_count = sum(bool(step.theorem_ref) for step in result.steps)
                chain = " → ".join(result.rule_ids)
                lines += ["", "DERIVATION CHAIN", "-" * 84,
                          f"Identity sequence: {chain}",
                          f"The selected route uses {identity_count} explicit identity application(s). Each application is shown in the proof steps below."]
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
                if getattr(step, "substitution", ()):
                    mapping = ", ".join(f"{name} → {value}" for name, value in step.substitution)
                    lines.append(f"   Variable substitution: {mapping}")
                if step.previous_expression is not None:
                    if step.theorem_ref:
                        lines.append("   Check: identity was validated; the variable substitution matched this subexpression")
                    else:
                        lines.append("   Check: exact algebraic equivalence tested")
                lines.append("")
            if result.rule_ids:
                lines += ["IDENTITY DATABASE REFERENCES", "-" * 84,
                          ", ".join(result.rule_ids),
                          "Each listed ID is attached to an explicit identity-application step in the selected proof route.", ""]
            if result.used_theorems:
                lines += ["IDENTITIES / THEOREMS USED", "-" * 84]
                for theorem in result.used_theorems:
                    lines.append(
                        f"• {theorem['name']}: {theorem['lhs']} = {theorem['rhs']} "
                        f"[{theorem.get('source', 'User supplied')}]"
                    )
                lines.append("Proof search excludes the target and its dependent identities. Unknown provenance and uncertified saved results are not proof authority.")
                lines.append("")
            if result.alternative_routes:
                lines += ["ALTERNATIVE PROOF ROUTES", "-" * 84]
                for index, route in enumerate(result.alternative_routes, 1):
                    refs = f"  [IDs: {', '.join(route.rule_ids)}]" if route.rule_ids else ""
                    theorem_refs = f"  [Theorems: {', '.join(route.used_theorems)}]" if route.used_theorems else ""
                    lines.append(f"{index}. {route.name}{refs}{theorem_refs}")
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
                  "Real-angle expressions using sin, cos, tan, cot, sec and csc, arithmetic, powers, pi and real square roots."]
        if geo_steps:
            lines += ["For this result, the fixed G01/G03/G04 geometric schema was independently replayed against the certificate.",
                      "Its proof is relative to AX.REAL, AX.EUCLID, AX.AREA and D.UNIT."]
        else:
            lines += ["User premises are validated as identities before use. Each theorem rewrite is checked symbolically.",
                      "The independent rotation route supports rational affine angles. Catalogue fallback is bounded: up to 7 identity applications and 260 visited expression states in full-catalogue mode.",
                      "An INCONCLUSIVE result may mean the proof chain exceeds these search limits; it does not establish falsity."]
        lines.append("Numerical sampling is used only to find counterexamples; it is never used to certify an identity.")
        return "\n".join(lines)

    def save_current_result_as_theorem(self):
        if self.last_result is None or self.last_result.status != "PROVED":
            return
        name = simpledialog.askstring(
            "Save proved result", "Give this established identity a reusable name:", parent=self
        )
        if not name or not name.strip():
            return
        record = {
            "name": name.strip(),
            "lhs": sp.sstr(self.last_result.lhs),
            "rhs": sp.sstr(self.last_result.rhs),
            "source": f"Proved by Trigonometric Proof Engine v{VERSION}",
            "domain_conditions": list(self.last_result.domain_conditions),
            "proof_certificate": self.last_result.to_certificate(),
        }
        try:
            parse_theorem_premises([record])
        except ExpressionInputError as exc:
            messagebox.showerror("Cannot save result", str(exc))
            return
        self.theorem_bank.append(record)
        if self._save_theorem_bank():
            self.status_var.set(f"SAVED RESULT  ·  {name.strip()} is now reusable in future proofs")
            self.notebook.select(self.theorem_tab)

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
        examples = [(lhs, rhs, "", "Use full identity catalogue") for _, lhs, rhs in EXERCISES] + [
            ("sin(x)**2 + cos(x)**2", "1", "", "Use full identity catalogue"),
            ("(1 - cos(2*x))/sin(2*x)", "tan(x)", "", "Use full identity catalogue"),
            ("(sec(x) - tan(x))*(sec(x) + tan(x))", "1", "", "Use full identity catalogue"),
            ("sin(x + y)", "sin(x)*cos(y) + cos(x)*sin(y)", "", "Use full identity catalogue"),
            (
                "sin(x)**2 + cos(x)**2", "sec(y)**2 - tan(y)**2",
                "Pythagorean result: sin(t)**2 + cos(t)**2 = 1\n"
                "Secant-tangent result: 1 = sec(u)**2 - tan(u)**2",
                "Use supplied identities",
            ),
            ("sin(x)", "cos(x)", "", "Automatic"),
        ]
        index = getattr(self, "example_index", -1) + 1
        self.example_index = index % len(examples)
        self.lhs_var.set(examples[self.example_index][0])
        self.rhs_var.set(examples[self.example_index][1])
        self.premises_text.delete("1.0", "end")
        self.premises_text.insert("1.0", examples[self.example_index][2])
        self.method_var.set(examples[self.example_index][3])
        self.status_var.set(f"EXAMPLE {self.example_index + 1} OF {len(examples)} LOADED")

    def clear_inputs(self):
        self.lhs_var.set("")
        self.rhs_var.set("")
        self.premises_text.delete("1.0", "end")
        self.last_result = None
        self.export_md_button.configure(state="disabled")
        self.export_json_button.configure(state="disabled")
        self.save_theorem_button.configure(state="disabled")
        self._set_report("Enter a new identity to begin.", "READY")
        self.status_var.set("READY  ·  Offline symbolic engine")


def main():
    app = TrigProofApp()
    app.mainloop()


if __name__ == "__main__":
    main()
