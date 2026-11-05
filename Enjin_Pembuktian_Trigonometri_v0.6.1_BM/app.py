"""Professional offline desktop interface for Trigonometric Proof Engine."""
from __future__ import annotations

import json
import os
import re
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from pathlib import Path

import sympy as sp

from engine import (
    prove_identity, ExpressionInputError, load_rule_catalogue,
    parse_theorem_premises, catalogue_rule_statistics,
)
from geometry import geometric_proof_steps

APP_NAME = "Enjin Pembuktian Trigonometri"
VERSION = "0.6.1"

METHOD_LABEL_TO_ENGINE = {
    "Katalog identiti penuh": "Use full identity catalogue",
    "Automatik": "Automatic",
    "LHS ke RHS": "LHS to RHS",
    "RHS ke LHS": "RHS to LHS",
    "Kedua-dua belah kepada bentuk sepunya": "Both sides to common form",
    "Kaedah perbezaan": "Difference method",
    "Gunakan identiti yang dibekalkan": "Use supplied identities",
    "Pengembangan sudut didahulukan": "Angle expansion first",
    "Transformasi Fu didahulukan": "Fu transformations first",
    "Pengurangan algebra didahulukan": "Algebraic reduction first",
}
METHOD_ENGINE_TO_LABEL = {value: key for key, value in METHOD_LABEL_TO_ENGINE.items()}
STATUS_LABELS_MS = {
    "PROVED": "TERBUKTI",
    "DISPROVED": "DISANGKAL",
    "INCONCLUSIVE": "BELUM DAPAT DIPASTIKAN",
    "ERROR": "RALAT",
    "READY": "SEDIA",
}



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



def translate_input_error_ms(exc):
    text = str(exc)
    replacements = {
        "Please enter an expression.": "Sila masukkan ungkapan matematik.",
        "Only real numeric constants are supported.": "Hanya pemalar angka nyata disokong.",
        "Invalid variable name.": "Nama pemboleh ubah tidak sah.",
        "Only unary + and - are supported.": "Hanya operator positif (+) dan negatif (−) tunggal disokong.",
        "Supported operators are +, -, *, / and **.": "Operator yang disokong ialah +, -, *, / dan **.",
        "Only direct calls to the six trig functions and sqrt are supported.": "Hanya panggilan terus kepada enam fungsi trigonometri dan sqrt disokong.",
        "Exponent is too large for this first version.": "Nilai eksponen terlalu besar untuk versi ini.",
        "Unbalanced superscript group in catalogue identity.": "Kumpulan superskrip dalam identiti katalog tidak seimbang.",
        "This catalogue entry requires a parameter or branch assumption.": "Entri katalog ini memerlukan parameter atau andaian cabang.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"Unsupported function '([^']+)'. Use sin, cos, tan, cot, sec, csc or sqrt\.",
                  r"Fungsi '\1' tidak disokong. Gunakan sin, cos, tan, cot, sec, csc atau sqrt.", text)
    text = re.sub(r"Use ([A-Za-z_][A-Za-z0-9_]*)\(\.\.\.\) with an argument\.",
                  r"Gunakan \1(...) bersama-sama satu argumen.", text)
    text = re.sub(r"Premise '([^']+)' needs both sides of an identity\.",
                  r"Premis '\1' mesti mengandungi kedua-dua belah identiti.", text)
    if text.startswith("Cannot read this expression:"):
        text = text.replace("Cannot read this expression:", "Ungkapan ini tidak dapat dibaca:", 1)
    if text.startswith("Unsupported syntax:"):
        text = text.replace("Unsupported syntax:", "Sintaks tidak disokong:", 1)
    if text.startswith("Unsupported premise format"):
        text = text.replace("Unsupported premise format", "Format premis tidak disokong", 1)
    return text

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
        ttk.Label(title_area, text="ENJIN PEMBUKTIAN TRIGONOMETRI", style="Title.TLabel").pack(anchor="w")
        ttk.Label(title_area, text="Pengesahan simbolik luar talian · Enam fungsi trigonometri asas",
                  style="Subtitle.TLabel").pack(anchor="w", pady=(2, 0))
        version = tk.Label(header, text=f"APLIKASI DESKTOP WINDOWS · EDISI BAHASA MELAYU  |  v{VERSION}", bg=self.NAVY,
                           fg="#AFC3DF", font=("Segoe UI", 8, "bold"))
        version.pack(side="right", padx=24)

    def _build_tabs(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=(16, 8))
        self.proof_tab = ttk.Frame(self.notebook)
        self.library_tab = ttk.Frame(self.notebook)
        self.theorem_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.proof_tab, text="  RUANG PEMBUKTIAN  ")
        self.notebook.add(self.theorem_tab, text="  BANK TEOREM  ")
        self.notebook.add(self.library_tab, text="  PUSTAKA IDENTITI  ")

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
                text=f"Sertakan bank teorem tersimpan ({len(self.theorem_bank)} tersedia)"
            )
            return True
        except OSError as exc:
            messagebox.showerror("Gagal menyimpan bank teorem", str(exc))
            return False

    def _build_theorem_bank(self):
        root = self.theorem_page
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Bank teorem untuk penggunaan semula", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(
            intro,
            text="Simpan identiti dan hasil daripada pembuktian terdahulu. Hanya identiti yang telah diaudit atau sijil v4 yang boleh disemak semula boleh digunakan sebagai asas pembuktian. Bank ini disimpan pada komputer anda dan boleh digunakan tanpa sambungan Internet.",
            foreground=self.MUTED,
        ).pack(anchor="w", pady=(3, 0))

        add_card = self._card(root)
        add_card.pack(fill="x", pady=(0, 12))
        form = tk.Frame(add_card, bg=self.WHITE)
        form.pack(fill="x", padx=16, pady=14)
        ttk.Label(form, text="TAMBAH IDENTITI UNTUK DIGUNAKAN SEMULA", style="Section.TLabel").grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 9)
        )
        ttk.Label(form, text="Nama").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=4)
        self.bank_name_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.bank_name_var).grid(row=1, column=1, sticky="ew", pady=4)
        ttk.Label(form, text="Sebelah kiri (LHS)").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=4)
        self.bank_lhs_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.bank_lhs_var, font=("Cambria Math", 10)).grid(
            row=2, column=1, sticky="ew", pady=4
        )
        ttk.Label(form, text="Sebelah kanan (RHS)").grid(row=3, column=0, sticky="w", padx=(0, 8), pady=4)
        self.bank_rhs_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.bank_rhs_var, font=("Cambria Math", 10)).grid(
            row=3, column=1, sticky="ew", pady=4
        )
        form.columnconfigure(1, weight=1)
        form_actions = tk.Frame(form, bg=self.WHITE)
        form_actions.grid(row=4, column=1, sticky="e", pady=(8, 0))
        ttk.Button(form_actions, text="Tambah identiti", style="Primary.TButton",
                   command=self.add_theorem_to_bank).pack(side="right")
        ttk.Button(form_actions, text="Kosongkan medan", style="Secondary.TButton",
                   command=self.clear_theorem_fields).pack(side="right", padx=(0, 8))

        list_card = self._card(root)
        list_card.pack(fill="both", expand=True)
        list_top = tk.Frame(list_card, bg=self.WHITE)
        list_top.pack(fill="x", padx=14, pady=(12, 8))
        ttk.Label(list_top, text="IDENTITI TERSIMPAN", style="Section.TLabel").pack(side="left")
        self.bank_count_label = ttk.Label(list_top, text="", style="Muted.TLabel")
        self.bank_count_label.pack(side="left", padx=(10, 0))
        tree_frame = tk.Frame(list_card, bg=self.WHITE)
        tree_frame.pack(fill="both", expand=True, padx=12, pady=(0, 8))
        columns = ("name", "identity", "source")
        self.theorem_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=9)
        self.theorem_tree.heading("name", text="TEOREM / HASIL")
        self.theorem_tree.heading("identity", text="IDENTITI")
        self.theorem_tree.heading("source", text="SUMBER")
        self.theorem_tree.column("name", width=190, minwidth=130)
        self.theorem_tree.column("identity", width=570, minwidth=250)
        self.theorem_tree.column("source", width=150, minwidth=100)
        scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.theorem_tree.yview)
        self.theorem_tree.configure(yscrollcommand=scroll.set)
        self.theorem_tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        bank_actions = tk.Frame(list_card, bg=self.WHITE)
        bank_actions.pack(fill="x", padx=14, pady=(0, 12))
        ttk.Button(bank_actions, text="Buang pilihan", style="Secondary.TButton",
                   command=self.remove_selected_theorem).pack(side="left")
        ttk.Button(bank_actions, text="Import fail JSON", style="Secondary.TButton",
                   command=self.import_theorem_bank).pack(side="left", padx=(8, 0))
        ttk.Button(bank_actions, text="Eksport JSON", style="Secondary.TButton",
                   command=self.export_theorem_bank).pack(side="left", padx=(8, 0))
        self._refresh_theorem_bank_view()

    def _refresh_theorem_bank_view(self):
        if not hasattr(self, "theorem_tree"):
            return
        for item in self.theorem_tree.get_children():
            self.theorem_tree.delete(item)
        for index, theorem in enumerate(self.theorem_bank):
            equation = f"{theorem.get('lhs', '')} = {theorem.get('rhs', '')}"
            source = theorem.get("source", "Diberikan oleh pengguna")
            if source.startswith("Proved by Trigonometric Proof Engine"):
                source = source.replace("Proved by Trigonometric Proof Engine", "Dibuktikan oleh Enjin Pembuktian Trigonometri")
            elif source == "Bundled SKILL.md identity catalogue":
                source = "Katalog identiti SKILL.md yang disertakan"
            self.theorem_tree.insert(
                "", "end", iid=str(index),
                values=(theorem.get("name", f"Teorem {index + 1}"), equation, source),
            )
        if hasattr(self, "bank_count_label"):
            self.bank_count_label.configure(text=f"{len(self.theorem_bank)} tersimpan")

    def add_theorem_to_bank(self):
        record = {
            "name": self.bank_name_var.get().strip() or f"Identiti pengguna {len(self.theorem_bank) + 1}",
            "lhs": self.bank_lhs_var.get().strip(),
            "rhs": self.bank_rhs_var.get().strip(),
            "source": "Bank teorem pengguna",
        }
        try:
            parse_theorem_premises([record])
        except ExpressionInputError as exc:
            messagebox.showerror("Identiti tidak diterima", translate_input_error_ms(exc))
            return
        self.theorem_bank.append(record)
        if self._save_theorem_bank():
            self.clear_theorem_fields()
            self.status_var.set("BANK TEOREM DIKEMAS KINI  ·  Identiti telah disahkan secara simbolik")

    def clear_theorem_fields(self):
        self.bank_name_var.set("")
        self.bank_lhs_var.set("")
        self.bank_rhs_var.set("")

    def remove_selected_theorem(self):
        selection = self.theorem_tree.selection()
        if not selection:
            messagebox.showinfo("Pilih satu identiti", "Pilih satu identiti dalam bank teorem terlebih dahulu.")
            return
        indices = sorted((int(item) for item in selection), reverse=True)
        for index in indices:
            if 0 <= index < len(self.theorem_bank):
                self.theorem_bank.pop(index)
        self._save_theorem_bank()

    def import_theorem_bank(self):
        path = filedialog.askopenfilename(
            title="Import bank teorem", filetypes=[("Bank teorem JSON", "*.json"), ("Semua fail", "*.*")]
        )
        if not path:
            return
        try:
            records = json.loads(Path(path).read_text(encoding="utf-8"))
            if not isinstance(records, list):
                raise ValueError("Fail yang dipilih mestilah mengandungi senarai rekod teorem dalam format JSON.")
            # Validate the entire import before changing the local bank.
            parse_theorem_premises(records)
            self.theorem_bank.extend(records)
            self._save_theorem_bank()
        except Exception as exc:
            messagebox.showerror("Import gagal", f"Fail tidak dapat diimport. Pastikan fail JSON mengandungi senarai rekod teorem yang sah.\n\nButiran teknikal: {exc}")

    def export_theorem_bank(self):
        path = filedialog.asksaveasfilename(
            title="Eksport bank teorem", defaultextension=".json",
            filetypes=[("Bank teorem JSON", "*.json"), ("Semua fail", "*.*")],
            initialfile="trigonometric_theorem_bank.json",
        )
        if not path:
            return
        try:
            Path(path).write_text(json.dumps(self.theorem_bank, indent=2, ensure_ascii=False), encoding="utf-8")
        except OSError as exc:
            messagebox.showerror("Eksport gagal", f"Fail tidak dapat dieksport.\n\nButiran: {exc}")

    def _build_proof_workspace(self):
        root = self.proof_page
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Pengesahan identiti", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(intro, text="Masukkan kedua-dua belah identiti. Mod berpandukan katalog memaparkan setiap penggantian identiti yang telah dibuktikan serta setiap langkah algebra.",
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
        ttk.Label(left, text="SEBELAH KIRI (LHS)", style="Section.TLabel").pack(anchor="w", pady=(0, 7))
        ttk.Label(right, text="SEBELAH KANAN (RHS)", style="Section.TLabel").pack(anchor="w", pady=(0, 7))
        self.lhs_var = tk.StringVar(value="sin(x)**2 + cos(x)**2")
        self.rhs_var = tk.StringVar(value="1")
        self.lhs_entry = ttk.Entry(left, textvariable=self.lhs_var, font=("Cambria Math", 12))
        self.rhs_entry = ttk.Entry(right, textvariable=self.rhs_var, font=("Cambria Math", 12))
        self.lhs_entry.pack(fill="x", ipady=4)
        self.rhs_entry.pack(fill="x", ipady=4)
        hint = tk.Label(input_inner, text="Sintaks: sin(x), cos(x), tan(x), cot(x), sec(x), csc(x), sqrt(...), pi, +  −  *  /  **. Gunakan simbol darab secara jelas, contohnya 2*sin(x).",
                        bg=self.WHITE, fg=self.MUTED, font=("Segoe UI", 8), anchor="w")
        hint.pack(fill="x", pady=(10, 0))

        ttk.Label(input_inner, text="IDENTITI TAMBAHAN / HASIL YANG TELAH DIBUKTIKAN",
                  style="Section.TLabel").pack(anchor="w", pady=(12, 6))
        self.premises_text = tk.Text(
            input_inner, height=3, wrap="word", bg="#FBFCFE", fg=self.TEXT,
            font=("Consolas", 9), relief="solid", bd=1, highlightthickness=0,
            padx=8, pady=6, insertbackground=self.TEXT,
        )
        self.premises_text.pack(fill="x")
        tk.Label(
            input_inner,
            text="Carian hanya menggunakan identiti katalog yang mempunyai rantaian kebergantungan bebas dan telah diaudit. "
                 "Anda boleh menambah identiti lain di sini. Masukkan satu identiti pada setiap baris dengan format: Nama: ungkapan kiri = ungkapan kanan.",
            bg=self.WHITE, fg=self.MUTED, font=("Segoe UI", 8), anchor="w",
        ).pack(fill="x", pady=(5, 0))
        theorem_options = tk.Frame(input_inner, bg=self.WHITE)
        theorem_options.pack(fill="x", pady=(7, 0))
        self.use_saved_bank_var = tk.BooleanVar(value=True)
        self.bank_check = ttk.Checkbutton(
            theorem_options,
            text=f"Sertakan bank teorem tersimpan ({len(self.theorem_bank)} tersedia)",
            variable=self.use_saved_bank_var,
        )
        self.bank_check.pack(side="left")
        ttk.Button(theorem_options, text="Urus bank teorem", style="Secondary.TButton",
                   command=lambda: self.notebook.select(self.theorem_tab)).pack(side="right")

        controls = tk.Frame(root, bg=self.BG)
        controls.pack(fill="x", pady=(0, 12))
        ttk.Label(controls, text="Strategi pembuktian:").pack(side="left", padx=(2, 8))
        self.method_display_var = tk.StringVar(value="Katalog identiti penuh")
        method = ttk.Combobox(controls, textvariable=self.method_display_var, state="readonly", width=38,
                              values=list(METHOD_LABEL_TO_ENGINE))
        method.pack(side="left")
        ttk.Button(controls, text="BUKTIKAN IDENTITI", style="Primary.TButton", command=self.run_proof).pack(side="right")
        ttk.Button(controls, text="Muatkan contoh", style="Secondary.TButton", command=self.load_example).pack(side="right", padx=(0, 8))
        ttk.Button(controls, text="Kosongkan", style="Secondary.TButton", command=self.clear_inputs).pack(side="right", padx=(0, 8))

        result_card = self._card(root)
        result_card.pack(fill="x", pady=(0, 12))
        self.result_card = result_card
        result_top = tk.Frame(result_card, bg=self.WHITE)
        result_top.pack(fill="x", padx=18, pady=(14, 8))
        ttk.Label(result_top, text="LAPORAN PEMBUKTIAN", style="Section.TLabel").pack(side="left")
        actions = tk.Frame(result_top, bg=self.WHITE)
        actions.pack(side="right")
        ttk.Button(actions, text="Kembali ke input", style="Secondary.TButton",
                   command=self._scroll_to_input).pack(side="left", padx=(0, 6))
        self.export_md_button = ttk.Button(actions, text="Eksport Markdown", style="Secondary.TButton",
                                           command=self.export_markdown, state="disabled")
        self.export_md_button.pack(side="left", padx=(0, 6))
        self.export_json_button = ttk.Button(actions, text="Eksport sijil pembuktian", style="Secondary.TButton",
                                             command=self.export_certificate, state="disabled")
        self.export_json_button.pack(side="left", padx=(0, 8))
        self.save_theorem_button = ttk.Button(
            actions, text="Simpan hasil yang terbukti", style="Secondary.TButton",
            command=self.save_current_result_as_theorem, state="disabled",
        )
        self.save_theorem_button.pack(side="left", padx=(0, 8))
        self.result_badge = tk.Label(actions, text="SEDIA", bg="#EAF0FA", fg=self.NAVY_2,
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
        self.result_text.insert("1.0", "Selamat datang ke versi 0.6.1. Masukkan satu identiti dan pilih BUKTIKAN IDENTITI.\n\n"
                                "Katalog mengandungi 136 entri berindeks, termasuk 125 peraturan kesamaan yang boleh digunakan dalam carian pembuktian. Hanya peraturan yang telah diaudit dibenarkan. "
                                "Setiap penggantian identiti dipaparkan bersama-sama ID, diikuti langkah algebra secara berasingan. "
                                "Ujian berangka semata-mata tidak akan dianggap sebagai pembuktian.")
        self.result_text.configure(state="disabled")
        self.bind("<Control-Return>", lambda event: self.run_proof())

    def _build_library(self):
        root = self.library_page
        intro = tk.Frame(root, bg=self.BG)
        intro.pack(fill="x", pady=(4, 12))
        ttk.Label(intro, text="Rujukan identiti enam fungsi trigonometri", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        stats = catalogue_rule_statistics(resource_path("knowledge/SKILL.md"))
        ttk.Label(intro, text=(
            f"Cari spesifikasi matematik yang disertakan · {stats['indexed_entries']} entri berindeks · "
            f"{stats['executable_equalities']} peraturan kesamaan yang boleh digunakan dalam pembuktian · Tersedia tanpa talian."
        ), foreground=self.MUTED).pack(anchor="w", pady=(3, 0))
        bar = tk.Frame(root, bg=self.BG)
        bar.pack(fill="x", pady=(0, 10))
        self.search_var = tk.StringVar()
        search = ttk.Entry(bar, textvariable=self.search_var)
        search.pack(side="left", fill="x", expand=True)
        search.insert(0, "Cari ID identiti, rumus atau kata kunci...")
        search.bind("<FocusIn>", lambda e: self._clear_search_placeholder())
        ttk.Button(bar, text="Cari", style="Secondary.TButton", command=self.search_library).pack(side="left", padx=(8, 0))
        ttk.Button(bar, text="Paparkan semua", style="Secondary.TButton", command=self.show_library).pack(side="left", padx=(8, 0))
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
        path = resource_path("knowledge/Panduan_Identiti_MS.md")
        try:
            self.library_content = resource_path("knowledge/Panduan_Identiti_MS.md").read_text(encoding="utf-8")
        except Exception as exc:
            self.library_content = f"Tidak dapat memuatkan pustaka identiti bahasa Melayu: {exc}"
        self.show_library()

    def _clear_search_placeholder(self):
        if self.search_var.get() == "Cari ID identiti, rumus atau kata kunci...":
            self.search_var.set("")

    def show_library(self):
        self.library_text.configure(state="normal")
        self.library_text.delete("1.0", "end")
        self.library_text.insert("1.0", self.library_content)
        self.library_text.configure(state="disabled")

    def search_library(self):
        query = self.search_var.get().strip()
        if not query or query == "Cari ID identiti, rumus atau kata kunci...":
            self.show_library()
            return
        lines = self.library_content.splitlines()
        found = [line for line in lines if query.casefold() in line.casefold()]
        self.library_text.configure(state="normal")
        self.library_text.delete("1.0", "end")
        if found:
            self.library_text.insert("1.0", f"HASIL CARIAN UNTUK: {query}\n{len(found)} baris sepadan\n\n")
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
            self.library_text.insert("1.0", f"Tiada baris yang sepadan dengan '{query}'.")
        self.library_text.configure(state="disabled")

    def _build_statusbar(self):
        bar = tk.Frame(self, bg="#E8EEF7", height=28)
        bar.pack(fill="x", side="bottom")
        self.status_var = tk.StringVar(value="MOD LUAR TALIAN  ·  Skop enam fungsi  ·  Unit radian  ·  Tiada perkhidmatan awan")
        tk.Label(bar, textvariable=self.status_var, bg="#E8EEF7", fg=self.MUTED,
                 font=("Segoe UI", 8), anchor="w").pack(fill="x", padx=20, pady=5)

    def _set_report(self, content: str, status: str = "SEDIA"):
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
            "SEDIA": ("#EAF0FA", self.NAVY_2),
        }
        bg, fg = palette.get(status, palette["SEDIA"])
        self.result_badge.configure(text=STATUS_LABELS_MS.get(status, status), bg=bg, fg=fg)

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
            result = prove_identity(lhs_text, rhs_text, METHOD_LABEL_TO_ENGINE[self.method_display_var.get()], premises=premises)
        except ExpressionInputError as exc:
            self._set_report(f"RALAT INPUT\n\n{translate_input_error_ms(exc)}\n\nFungsi yang disokong: sin, cos, tan, cot, sec, csc, sqrt.\nGunakan simbol darab secara jelas, contohnya 2*sin(x).", "ERROR")
            self.after_idle(self._scroll_to_report)
            return
        except Exception as exc:
            self._set_report(f"RALAT ENJIN\n\n{type(exc).__name__}: {exc}", "ERROR")
            self.after_idle(self._scroll_to_report)
            return
        self.last_result = result
        self.export_md_button.configure(state="normal")
        self.export_json_button.configure(state="normal")
        self.save_theorem_button.configure(state="normal" if result.status == "PROVED" else "disabled")
        self._set_report(self._format_result(result), result.status)
        self.after_idle(self._scroll_to_report)
        geo_certificate = result.certificate_override if getattr(result, "certificate_override", None) else None
        refs = ("  ·  3 nod pembuktian geometri" if geo_certificate else
                (f"  ·  {len(result.rule_ids)} peraturan identiti" if result.rule_ids else ""))
        theorem_refs = f"  ·  {len(result.used_theorems)} hasil yang telah dibuktikan" if result.used_theorems else ""
        self.status_var.set(f"ANALISIS SELESAI  ·  {STATUS_LABELS_MS.get(result.status, result.status)}{refs}{theorem_refs}  ·  Enjin simbolik luar talian")

    @staticmethod
    def _translate_route_ms(route):
        if not route:
            return "Belum ditentukan"
        if route.startswith("GEO:"):
            return route.replace("GEO:", "GEOMETRI:", 1)
        mapping = {
            "LHS using identity catalogue": "LHS menggunakan katalog identiti",
            "RHS using identity catalogue": "RHS menggunakan katalog identiti",
            "Both sides to common form using identity catalogue": "Kedua-dua belah kepada bentuk sepunya menggunakan katalog identiti",
            "LHS using supplied identities": "LHS menggunakan identiti yang dibekalkan",
            "RHS using supplied identities": "RHS menggunakan identiti yang dibekalkan",
            "Both sides to common form using supplied identities": "Kedua-dua belah kepada bentuk sepunya menggunakan identiti yang dibekalkan",
            "Both sides to common form": "Kedua-dua belah kepada bentuk sepunya",
            "LHS to other side": "LHS ditransformasikan kepada RHS",
            "RHS to other side": "RHS ditransformasikan kepada LHS",
            "Algebra only": "Algebra sahaja",
            "Difference method": "Kaedah perbezaan",
            "Automatic": "Automatik",
            "Use full identity catalogue": "Katalog identiti penuh",
            "Use supplied identities": "Gunakan identiti yang dibekalkan",
            "Angle expansion first": "Pengembangan sudut didahulukan",
            "Fu transformations first": "Transformasi Fu didahulukan",
            "Algebraic reduction first": "Pengurangan algebra didahulukan",
        }
        return mapping.get(route, route)

    @staticmethod
    def _translate_route_summary_ms(summary):
        mapping = {
            "Both expressions reduce to the same symbolic form.": "Kedua-dua ungkapan diringkaskan kepada bentuk simbolik yang sama.",
            "The initial symbolic difference is zero.": "Beza simbolik pada peringkat awal ialah sifar.",
            "The claim follows by algebra alone.": "Pernyataan ini dapat dibuktikan menggunakan kaedah algebra sahaja.",
        }
        if summary in mapping:
            return mapping[summary]
        dynamic = re.match(r"The (LHS|RHS) reaches the target through (\d+) explicit identity application\(s\) and displayed algebraic steps\.", summary or "")
        if dynamic:
            side = "sebelah kiri (LHS)" if dynamic.group(1) == "LHS" else "sebelah kanan (RHS)"
            return f"{side.capitalize()} mencapai bentuk sasaran melalui {dynamic.group(2)} penggunaan identiti yang jelas serta langkah algebra yang dipaparkan."
        return "Laluan ini menghasilkan bentuk yang setara melalui langkah yang direkodkan."

    @staticmethod
    def _translate_step_title_ms(title):
        exact = {
            "Start with the LHS": "Mulakan dengan LHS",
            "Start with the RHS": "Mulakan dengan RHS",
            "Expand squared sums": "Kembangkan kuasa dua hasil tambah",
            "Factor by parameter groups": "Faktorkan mengikut kumpulan parameter",
            "Match the target side": "Padankan dengan sebelah sasaran",
            "Factor numerator and denominator": "Faktorkan pengangka dan penyebut",
            "Establish a common form": "Bentukkan ungkapan sepunya",
            "Reduce the difference": "Ringkaskan beza",
            "Apply the distributive law": "Gunakan hukum pengagihan",
            "Algebraic equality": "Kesamaan algebra",
            "Distribute a negative sign": "Agihkan tanda negatif",
            "Combine algebraic fractions": "Gabungkan pecahan algebra",
            "Cancel common algebraic factors": "Batalkan faktor algebra sepunya",
            "Apply quotient and reciprocal identities": "Gunakan identiti hasil bahagi dan fungsi salingan",
            "Expand compound angles": "Kembangkan sudut majmuk",
            "Apply trigonometric identities": "Gunakan identiti trigonometri",
            "Apply Fu trigonometric transformations": "Gunakan transformasi trigonometri Fu",
            "Factor algebraic expressions": "Faktorkan ungkapan algebra",
            "Final symbolic simplification": "Pemudahan simbolik akhir",
            "Form LHS − RHS": "Bentuk LHS − RHS",
            "Original expression": "Ungkapan asal",
            "Rearrange algebraically to the target form": "Susun semula secara algebra kepada bentuk sasaran",
        }
        if title in exact:
            return exact[title]
        match = re.match(r"Apply identity (F\d+):\s*(.*)", title)
        if match:
            return f"Gunakan identiti {match.group(1)}: {match.group(2)}"
        match = re.match(r"Apply supplied identity:\s*(.*)", title)
        if match:
            return f"Gunakan identiti yang dibekalkan: {match.group(1)}"
        return title

    @staticmethod
    def _translate_step_note_ms(note):
        exact = {
            "Original expression in the claim.": "Ungkapan asal dalam pernyataan yang hendak dibuktikan.",
            "Original expression in the requested identity.": "Ungkapan asal dalam identiti yang diminta.",
            "Apply the distributive law to expand squared linear combinations; trigonometric functions are treated as algebraic factors.": "Gunakan hukum pengagihan untuk mengembangkan kuasa dua gabungan linear; fungsi trigonometri dianggap sebagai faktor algebra.",
            "Collect common parameter factors to expose the sum sin(x)**2 + cos(x)**2 for an established identity application.": "Kumpulkan faktor parameter sepunya untuk menzahirkan hasil tambah sin(x)**2 + cos(x)**2 supaya identiti yang telah dibuktikan dapat digunakan.",
            "The displayed identity substitutions establish the requested target form.": "Penggantian identiti yang dipaparkan menghasilkan bentuk sasaran yang diminta.",
            "Both sides reach exactly the same expression through the displayed identity and algebra steps.": "Kedua-dua belah menghasilkan ungkapan yang sama tepat melalui penggantian identiti dan langkah algebra yang dipaparkan.",
            "The transformed expression is symbolically equivalent to the target side.": "Ungkapan yang ditransformasikan setara secara simbolik dengan sebelah sasaran.",
            "The symbolic difference reduces exactly to zero.": "Beza simbolik diringkaskan tepat kepada sifar.",
            "The claim follows by algebra alone.": "Pernyataan ini dapat dibuktikan menggunakan kaedah algebra sahaja.",
            "Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.": "Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.",
            "Distribute the factor -1 over an additive expression; no trigonometric identity is used.": "Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.",
            "Combine rational terms over a common denominator without applying another trigonometric identity.": "Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.",
            "Use F01–F04 to express tangent, cotangent, secant and cosecant using sine and cosine.": "Gunakan F01–F04 untuk menulis tangen, kotangen, sekan dan kosekan dalam sebutan sinus dan kosinus.",
            "Use angle addition, subtraction and multiple-angle identities where applicable.": "Gunakan identiti penambahan sudut, penolakan sudut dan sudut gandaan apabila berkenaan.",
            "Simplify using the six-function identity catalogue, especially Pythagorean relationships.": "Permudahkan menggunakan katalog identiti enam fungsi, khususnya hubungan Pythagoras.",
            "Apply an independent set of trigonometric transformation rules.": "Gunakan satu set peraturan transformasi trigonometri yang berasingan.",
            "Put rational terms over a common denominator.": "Satukan sebutan pecahan menggunakan penyebut sepunya.",
            "Cancel common factors while retaining the original domain restrictions.": "Batalkan faktor sepunya sambil mengekalkan syarat domain asal.",
            "Factor the resulting algebraic expression.": "Faktorkan ungkapan algebra yang terhasil.",
            "Apply exact symbolic simplification.": "Gunakan pemudahan simbolik yang tepat.",
            "Distribute the factor -1 over an additive expression; no trigonometric identity is used.": "Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.",
            "Combine rational terms over a common denominator without applying another trigonometric identity.": "Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.",
            "Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.": "Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.",
            "Cancel a genuine common numerator/denominator factor. The original and intermediate denominator restrictions remain in force.": "Batalkan faktor sepunya sebenar pada pengangka dan penyebut. Syarat penyebut bagi ungkapan asal dan ungkapan perantaraan kekal terpakai.",
            "First expression in the claim.": "Ungkapan pertama dalam pernyataan yang hendak dibuktikan.",
            "Second expression in the claim.": "Ungkapan kedua dalam pernyataan yang hendak dibuktikan.",
            "An identity is established when the difference is exactly zero on the original common domain.": "Identiti terbukti apabila beza tersebut tepat sifar pada domain sepunya asal.",
            "Both sides reduce to symbolically equivalent expressions.": "Kedua-dua belah diringkaskan kepada ungkapan yang setara secara simbolik.",
            "The initial symbolic difference is zero.": "Beza simbolik pada peringkat awal ialah sifar.",
            "Rational algebra with trigonometric expressions treated as atoms.": "Manipulasi algebra bagi ungkapan rasional dengan ungkapan trigonometri dianggap sebagai unsur algebra asas.",
            "Original expression from the claim.": "Ungkapan asal daripada pernyataan yang hendak dibuktikan.",
            "The expressions differ only by algebraic ordering or grouping; the trigonometric subexpressions are unchanged.": "Kedua-dua ungkapan hanya berbeza dari segi susunan atau pengelompokan algebra; subungkapan trigonometri tidak berubah.",
            "Reorder terms or rewrite the same algebraic fraction. The trigonometric subexpressions are unchanged.": "Susun semula sebutan atau tulis semula pecahan algebra yang sama. Subungkapan trigonometri tidak berubah.",
            "The displayed identity substitutions and algebraic steps establish the requested target form.": "Penggantian identiti dan langkah algebra yang dipaparkan menghasilkan bentuk sasaran yang diminta.",
        }
        if note in exact:
            return exact[note]
        if note and note.startswith("Apply established identity "):
            match = re.match(r"Apply established identity (F\d+) in the (forward|reverse) direction to (?:a matching|the matched) subexpression\.?(.*)", note)
        else:
            match = None
        if match:
            direction = "arah hadapan" if match.group(2) == "forward" else "arah songsang"
            tail = match.group(3).strip()
            extra = " Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan." if "checked against the recorded step" in tail else ""
            return f"Gunakan identiti {match.group(1)} yang telah dibuktikan dalam {direction} pada subungkapan yang sepadan.{extra}"
        dynamic = re.match(r"The (LHS|RHS) reaches the target through (\d+) explicit identity application\(s\) and displayed algebraic steps\.", note or "")
        if dynamic:
            side = "sebelah kiri (LHS)" if dynamic.group(1) == "LHS" else "sebelah kanan (RHS)"
            return f"{side.capitalize()} mencapai bentuk sasaran melalui {dynamic.group(2)} penggunaan identiti yang jelas serta langkah algebra yang dipaparkan."
        return note or ""

    @staticmethod
    def _translate_message_ms(message):
        if not message:
            return ""
        if message.startswith("An independent geometric proof establishes the identity"):
            return ("Pembuktian geometri bebas membuktikan identiti ini melalui G01 (pembuktian Teorem Pythagoras menggunakan kaedah pembahagian luas), "
                    "G03 (hubungan kuasa dua jarak pada satah Cartes) dan G04 (penggantian koordinat bulatan unit). Sijil geometri telah disemak semula dan disahkan. "
                    "Tiada identiti daripada katalog trigonometri digunakan sebagai premis. Pembuktian ini berasaskan AX.REAL, AX.EUCLID, AX.AREA dan D.UNIT.")
        match = re.search(r"found a derivation using (\d+) explicit established identity application", message)
        if match:
            return (f"Carian identiti menemukan satu terbitan yang menggunakan {match.group(1)} penggunaan identiti yang telah dibuktikan secara jelas. "
                    "Setiap penggantian dan transformasi algebra direkodkan secara berasingan pada domain sepunya asal.")
        if message.startswith("A valid numerical counterexample was found"):
            return "Satu contoh balas berangka yang sah telah ditemukan. Identiti yang dicadangkan adalah palsu."
        if message.startswith("No independent derivation was found"):
            return ("Tiada terbitan bebas ditemukan. Sasaran, identiti yang bergantung padanya, premis tanpa sijil yang sah dan peraturan katalog "
                    "yang mempunyai kebergantungan belum diaudit tidak dibenarkan sebagai asas pembuktian. Pemudahan simbolik sahaja tidak diterima sebagai pembuktian. "
                    "Keputusan ini tidak bermaksud pernyataan tersebut palsu.")
        if message.startswith("A symbolic transformation route established equality"):
            return ("Laluan transformasi simbolik telah membuktikan kesamaan pada domain sepunya asal. "
                    "Setiap penggunaan identiti dan langkah algebra dipaparkan secara jelas dalam laluan yang dipilih.")
        if message.startswith("The claim follows by algebra alone"):
            return "Pernyataan ini dapat dibuktikan menggunakan kaedah algebra sahaja."
        return "Pembuktian selesai. Rujuk langkah dan justifikasi yang dipaparkan di bawah."

    @staticmethod
    def _format_markdown_ms(result):
        report = TrigProofApp._format_result(None, result)
        source = report.splitlines()
        out = ["# Laporan Pembuktian Trigonometri", ""]
        i = 0
        while i < len(source):
            line = source[i]
            if i == 0:
                i += 1
                continue
            if line and set(line) <= {"="}:
                i += 1
                continue
            if line and i + 1 < len(source) and source[i + 1] and set(source[i + 1]) <= {"-"}:
                out.extend([f"## {line.title()}", ""])
                i += 2
                continue
            out.append(line)
            i += 1
        return "\n".join(out).rstrip() + "\n"

    def _format_result(self, result):
        certificate = getattr(result, "certificate_override", None)
        geo_steps = geometric_proof_steps(certificate) if certificate else None
        status_ms = STATUS_LABELS_MS.get(result.status, result.status)
        lines = [
            "LAPORAN IDENTITI TRIGONOMETRI",
            "=" * 84,
            f"Pernyataan:  {sp.sstr(result.lhs)}  =  {sp.sstr(result.rhs)}",
            f"Status: {status_ms} ({result.status})",
            f"Laluan pembuktian terpilih: {TrigProofApp._translate_route_ms(result.selected_route)}",
            "",
        ]
        message_ms = TrigProofApp._translate_message_ms(result.message)
        if message_ms:
            lines += [message_ms, ""]
        lines += ["SYARAT DOMAIN SEPUNYA ASAL", "-" * 84]
        if result.domain_conditions:
            lines.extend(f"• {condition.replace('(real square root)', '(punca kuasa dua nyata)')}" for condition in result.domain_conditions)
        else:
            lines.append("Tiada syarat tambahan dikesan; kedua-dua belah ditakrifkan bagi semua nilai nyata pemboleh ubah yang terlibat.")

        if geo_steps:
            geo_title = {
                "G01 — Pythagorean theorem by geometric dissection": "G01 — Teorem Pythagoras melalui pembahagian geometri",
                "G03 — Cartesian squared-distance theorem": "G03 — Rumus kuasa dua jarak pada satah Cartes",
                "G04 — Unit-circle substitution": "G04 — Penggantian menggunakan bulatan unit",
                "Final step — Match the geometric theorem to the requested claim": "Langkah akhir — Padankan teorem geometri dengan pernyataan yang hendak dibuktikan",
            }
            geo_exact = {
                "Let a right triangle have perpendicular legs a and b, and hypotenuse c.": "Ambil sebuah segi tiga bersudut tegak yang mempunyai dua sisi yang saling berserenjang, masing-masing sepanjang a dan b, serta hipotenus c.",
                "Arrange four congruent copies inside a square whose side is a+b. Their hypotenuses form the four sides of a central square of side c.": "Susun empat segi tiga yang kongruen di dalam sebuah segi empat sama bersisi a+b. Hipotenus keempat-empat segi tiga itu membentuk empat sisi segi empat sama di bahagian tengah yang bersisi c.",
                "Each central angle is 90° because the two acute angles of a right triangle sum to 90°.": "Setiap sudut di bahagian tengah ialah 90° kerana jumlah dua sudut tirus bagi segi tiga bersudut tegak ialah 90°.",
                "Area of the outer square = area of four triangles + area of the central square:": "Luas segi empat sama di bahagian luar = jumlah luas empat segi tiga + luas segi empat sama di bahagian tengah:",
                "Expand: a² + 2ab + b² = 2ab + c².": "Kembangkan: a² + 2ab + b² = 2ab + c².",
                "Subtract 2ab from both sides: a² + b² = c².": "Tolak 2ab daripada kedua-dua belah: a² + b² = c².",
                "Therefore G01 establishes the Pythagorean theorem from Euclidean geometry and area additivity.": "Oleh itu, G01 membuktikan Teorem Pythagoras berdasarkan geometri Euclid dan sifat tambah luas.",
                "Take an arbitrary Cartesian point P=(u,v), with O=(0,0).": "Ambil sebarang titik Cartes P=(u,v), dengan O=(0,0).",
                "Perpendicular projections onto the coordinate axes have lengths |u| and |v|; OP is the hypotenuse of the resulting right triangle.": "Unjuran serenjang pada paksi koordinat mempunyai panjang |u| dan |v|; OP ialah hipotenus bagi segi tiga bersudut tegak yang terbentuk.",
                "The same formula holds on either axis (u=0 or v=0) by direct evaluation.": "Rumus yang sama turut terpakai pada kedua-dua paksi (u=0 atau v=0) melalui penggantian secara langsung.",
                "By D.UNIT, the point has radius OP=1 and signed Cartesian coordinates u=cos(x), v=sin(x).": "Berdasarkan D.UNIT, titik tersebut mempunyai jejari OP=1 dan koordinat Cartes bertanda u=cos(x), v=sin(x).",
                "Apply G03: OP² = u² + v².": "Gunakan G03: OP² = u² + v².",
            }
            lines += ["", "RANTAIAN PEMBUKTIAN GEOMETRI", "-" * 84,
                      "Berikut ialah langkah matematik sebenar yang disemak oleh sijil pembuktian geometri.", ""]
            for index, geo_step in enumerate(geo_steps, 1):
                lines.append(f"{index}. {geo_title.get(geo_step['title'], geo_step['title'])}")
                for detail in geo_step["details"]:
                    translated = geo_exact.get(detail, detail)
                    translated = translated.replace("Let θ =", "Ambil θ =")
                    translated = translated.replace("Let ", "Ambil ")
                    translated = translated.replace("be any real angle and choose the unit-circle point", "sebagai sebarang sudut nyata dan pilih titik pada bulatan unit")
                    translated = translated.replace("By G01:", "Berdasarkan G01:")
                    translated = translated.replace("Apply G01:", "Gunakan G01:")
                    translated = translated.replace("Substitute:", "Gantikan:")
                    translated = translated.replace("Hence ", "Oleh itu, ")
                    translated = translated.replace("for every real angle", "bagi setiap sudut nyata")
                    translated = translated.replace("The certificate's exact factorisation is:", "Pemfaktoran tepat dalam sijil ialah:")
                    translated = translated.replace("This residual equals", "Baki ini bersamaan dengan")
                    translated = translated.replace("By G04, the parenthesised expression is zero; therefore", "Berdasarkan G04, ungkapan dalam kurungan bernilai sifar; oleh itu")
                    translated = translated.replace("Thus ", "Maka ")
                    translated = translated.replace(" on the original common domain.", " pada domain sepunya asal.")
                    lines.append(f"   {translated}")
                lines.append("")
            lines += ["PENGESAHAN SEMULA SIJIL GEOMETRI", "-" * 84,
                      f"Skema sijil: {certificate['schema']}",
                      f"Versi pemeriksa: {certificate['checker_version']}",
                      f"Ringkasan sijil (SHA-256): {certificate['certificate_digest']}",
                      "Status pengesahan semula: DISAHKAN (VERIFIED)",
                      "Premis daripada katalog identiti trigonometri: Tiada",
                      "Asas matematik yang dipercayai: AX.REAL, AX.EUCLID, AX.AREA, D.UNIT", ""]
            if result.status == "PROVED":
                lines += ["KESIMPULAN", "-" * 84,
                          "Sijil pembuktian geometri yang telah disemak semula membuktikan LHS − RHS = 0 pada domain sepunya asal.",
                          "G01 membuktikan Teorem Pythagoras melalui pembahagian geometri; G03 memperoleh hubungan kuasa dua jarak pada satah Cartes; G04 menggunakan hubungan tersebut pada bulatan unit.",
                          "Pembuktian ini berasaskan AX.REAL, AX.EUCLID, AX.AREA dan D.UNIT. Tiada identiti katalog F08/F09/F10 diandaikan sebagai premis."]
        else:
            if result.rule_ids:
                identity_count = sum(bool(step.theorem_ref) for step in result.steps)
                chain = " → ".join(result.rule_ids)
                lines += ["", "RANTAIAN PEMBUKTIAN", "-" * 84,
                          f"Urutan identiti: {chain}",
                          f"Laluan terpilih menggunakan {identity_count} penggunaan identiti yang telah dibuktikan secara jelas. Setiap penggunaan ditunjukkan dalam langkah pembuktian di bawah."]
            lines += ["", "LANGKAH PEMBUKTIAN / ANALISIS", "-" * 84]
            if not result.steps:
                lines.append("Tiada langkah pembuktian simbolik dapat dibentuk menggunakan strategi yang dipilih.")
            side_map = {"LHS": "Sebelah kiri (LHS)", "RHS": "Sebelah kanan (RHS)", "Both sides": "Kedua-dua belah", "Difference": "Beza"}
            for i, step in enumerate(result.steps, 1):
                side = f" [{side_map.get(step.side, step.side)}]" if step.side else ""
                refs = f"  [ID identiti: {', '.join(step.rule_ids)}]" if step.rule_ids else ""
                lines.append(f"{i}. {TrigProofApp._translate_step_title_ms(step.title)}{side}{refs}")
                if step.previous_expression is not None:
                    lines.append(f"   Sebelum: {sp.sstr(step.previous_expression)}")
                lines.append(f"   Selepas: {sp.sstr(step.expression)}")
                note = TrigProofApp._translate_step_note_ms(step.note)
                if note:
                    lines.append(f"   Justifikasi: {note}")
                if getattr(step, "substitution", ()):
                    mapping = ", ".join(f"{name} → {value}" for name, value in step.substitution)
                    lines.append(f"   Penggantian pemboleh ubah: {mapping}")
                if step.previous_expression is not None:
                    if step.theorem_ref:
                        lines.append("   Semakan: identiti telah disahkan; penggantian pemboleh ubah sepadan dengan subungkapan ini.")
                    else:
                        lines.append("   Semakan: kesetaraan algebra yang tepat telah diuji.")
                lines.append("")
            if result.rule_ids:
                lines += ["RUJUKAN PUSTAKA IDENTITI", "-" * 84,
                          ", ".join(result.rule_ids),
                          "Setiap ID yang disenaraikan merujuk kepada langkah penggunaan identiti yang jelas dalam laluan pembuktian terpilih.", ""]
            if result.used_theorems:
                lines += ["IDENTITI / TEOREM YANG DIGUNAKAN", "-" * 84]
                for theorem in result.used_theorems:
                    source = theorem.get("source", "User supplied")
                    if source == "User supplied":
                        source = "Diberikan oleh pengguna"
                    lines.append(f"• {theorem['name']}: {theorem['lhs']} = {theorem['rhs']} [{source}]")
                lines.append("Carian pembuktian mengecualikan sasaran dan identiti yang bergantung padanya. Asal usul yang tidak diketahui serta hasil tersimpan tanpa sijil yang boleh disemak semula tidak diterima sebagai asas pembuktian.")
                lines.append("")
            if result.alternative_routes:
                lines += ["LALUAN PEMBUKTIAN ALTERNATIF", "-" * 84]
                for index, route in enumerate(result.alternative_routes, 1):
                    refs = f"  [ID: {', '.join(route.rule_ids)}]" if route.rule_ids else ""
                    theorem_refs = f"  [Teorem: {', '.join(route.used_theorems)}]" if route.used_theorems else ""
                    lines.append(f"{index}. {TrigProofApp._translate_route_ms(route.name)}{refs}{theorem_refs}")
                    lines.append(f"   {TrigProofApp._translate_route_summary_ms(route.summary)}")
                    lines.append(f"   Bilangan langkah: {len(route.steps)}")
                lines.append("")
            if result.status == "PROVED":
                lines += ["KESIMPULAN", "-" * 84,
                          "Laluan simbolik membuktikan LHS − RHS = 0 pada domain sepunya bagi ungkapan asal.",
                          "Syarat domain asal kekal terpakai walaupun bentuk algebra yang terhasil kelihatan ditakrifkan pada domain yang lebih luas.",
                          "Laluan ini menggunakan kaedah heuristik dan bukan sijil pembuktian formal yang lengkap; setiap langkah yang direkodkan telah disemak secara simbolik."]
            elif result.status == "DISPROVED":
                lines += ["CONTOH BALAS", "-" * 84]
                if result.counterexample:
                    lines.append(", ".join(f"{name} = {value:.8g}" for name, value in result.counterexample.items()))
                lines.append(f"LHS ≈ {result.lhs_value:.12g}; RHS ≈ {result.rhs_value:.12g}")
                lines.append("Titik ini ialah contoh balas berangka terhadap identiti yang dicadangkan.")
            else:
                lines += ["BATASAN", "-" * 84,
                          "Strategi yang dipilih tidak menemukan pembuktian. Ujian berangka juga tidak menemukan contoh balas. Keputusan ini belum dapat dipastikan dan bukan bukti bahawa pernyataan itu benar atau palsu."]

        lines += ["", "SKOP ENJIN", "-" * 84,
                  "Ungkapan sudut nyata yang menggunakan sin, cos, tan, cot, sec dan csc, operasi aritmetik, kuasa, pi serta punca kuasa dua nyata."]
        if geo_steps:
            lines += ["Bagi keputusan ini, skema geometri tetap G01/G03/G04 telah disemak semula secara bebas terhadap sijil pembuktian.",
                      "Pembuktian ini berasaskan AX.REAL, AX.EUCLID, AX.AREA dan D.UNIT."]
        else:
            lines += ["Premis pengguna disahkan sebagai identiti sebelum digunakan. Setiap penggantian teorem disemak secara simbolik.",
                      "Carian katalog dihadkan kepada maksimum 7 penggunaan identiti dan 260 keadaan ungkapan yang dilawati dalam mod katalog penuh.",
                      "Keputusan BELUM DAPAT DIPASTIKAN mungkin berlaku apabila rantaian pembuktian melebihi had carian; keputusan ini tidak membuktikan bahawa pernyataan itu palsu."]
        lines.append("Pensampelan berangka hanya digunakan untuk mencari contoh balas; kaedah ini tidak pernah digunakan untuk mengesahkan identiti.")
        return "\n".join(lines)

    def save_current_result_as_theorem(self):
        if self.last_result is None or self.last_result.status != "PROVED":
            return
        name = simpledialog.askstring(
            "Simpan hasil yang terbukti", "Berikan nama untuk identiti yang telah dibuktikan ini:", parent=self
        )
        if not name or not name.strip():
            return
        record = {
            "name": name.strip(),
            "lhs": sp.sstr(self.last_result.lhs),
            "rhs": sp.sstr(self.last_result.rhs),
            "source": f"Dibuktikan oleh Enjin Pembuktian Trigonometri v{VERSION}",
            "domain_conditions": list(self.last_result.domain_conditions),
            "proof_certificate": self.last_result.to_certificate(),
        }
        try:
            parse_theorem_premises([record])
        except ExpressionInputError as exc:
            messagebox.showerror("Tidak dapat menyimpan hasil", translate_input_error_ms(exc))
            return
        self.theorem_bank.append(record)
        if self._save_theorem_bank():
            self.status_var.set(f"HASIL DISIMPAN  ·  {name.strip()} kini boleh digunakan dalam pembuktian seterusnya")
            self.notebook.select(self.theorem_tab)

    def export_markdown(self):
        if self.last_result is None:
            return
        path = filedialog.asksaveasfilename(
            title="Eksport laporan pembuktian", defaultextension=".md",
            filetypes=[("Laporan Markdown", "*.md"), ("Semua fail", "*.*")],
            initialfile="laporan_pembuktian_trigonometri.md",
        )
        if not path:
            return
        try:
            Path(path).write_text(self._format_markdown_ms(self.last_result), encoding="utf-8")
            self.status_var.set(f"MARKDOWN DIEKSPORT  ·  {Path(path).name}")
        except OSError as exc:
            messagebox.showerror("Eksport gagal", f"Fail tidak dapat dieksport.\n\nButiran: {exc}")

    def export_certificate(self):
        if self.last_result is None:
            return
        path = filedialog.asksaveasfilename(
            title="Eksport sijil pembuktian simbolik", defaultextension=".json",
            filetypes=[("Sijil JSON", "*.json"), ("Semua fail", "*.*")],
            initialfile="sijil_pembuktian_trigonometri.json",
        )
        if not path:
            return
        try:
            Path(path).write_text(json.dumps(self.last_result.to_certificate(), indent=2, ensure_ascii=False), encoding="utf-8")
            self.status_var.set(f"SIJIL DIEKSPORT  ·  {Path(path).name}")
        except OSError as exc:
            messagebox.showerror("Eksport gagal", f"Fail tidak dapat dieksport.\n\nButiran: {exc}")

    def load_example(self):
        examples = [
            ("sin(x)**2 + cos(x)**2", "1", "", "Use full identity catalogue"),
            ("(1 - cos(2*x))/sin(2*x)", "tan(x)", "", "Use full identity catalogue"),
            ("(sec(x) - tan(x))*(sec(x) + tan(x))", "1", "", "Use full identity catalogue"),
            ("sin(x + y)", "sin(x)*cos(y) + cos(x)*sin(y)", "", "Use full identity catalogue"),
            (
                "sin(x)**2 + cos(x)**2", "sec(y)**2 - tan(y)**2",
                "Identiti Pythagoras: sin(t)**2 + cos(t)**2 = 1\n"
                "Identiti sekan-tangen: 1 = sec(u)**2 - tan(u)**2",
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
        self.method_display_var.set(METHOD_ENGINE_TO_LABEL.get(examples[self.example_index][3], "Katalog identiti penuh"))
        self.status_var.set(f"CONTOH {self.example_index + 1} DARIPADA {len(examples)} TELAH DIMUATKAN")

    def clear_inputs(self):
        self.lhs_var.set("")
        self.rhs_var.set("")
        self.premises_text.delete("1.0", "end")
        self.last_result = None
        self.export_md_button.configure(state="disabled")
        self.export_json_button.configure(state="disabled")
        self.save_theorem_button.configure(state="disabled")
        self._set_report("Masukkan identiti baharu untuk bermula.", "SEDIA")
        self.status_var.set("SEDIA  ·  Enjin simbolik luar talian")


def main():
    app = TrigProofApp()
    app.mainloop()


if __name__ == "__main__":
    main()
