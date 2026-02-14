from __future__ import annotations

import pathlib
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

try:
    from agid_accessibilita_kit.service import Config, write_project
except ModuleNotFoundError:
    import sys

    ROOT = pathlib.Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from agid_accessibilita_kit.service import Config, write_project


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("AGID Accessibilita Kit (bozze)")
        self.geometry("760x420")
        self.minsize(720, 380)

        self.ente = tk.StringVar(value="Nome organizzazione")
        self.sito = tk.StringVar(value="https://www.esempio.it")
        self.email = tk.StringVar(value="accessibilita@esempio.it")
        self.base_path = tk.StringVar(value="/accessibilita")
        self.out_dir = tk.StringVar(value=str(pathlib.Path("accessibilita").resolve()))

        self._build()

    def _build(self) -> None:
        frame = ttk.Frame(self, padding=12)
        frame.pack(fill="both", expand=True)

        form = ttk.LabelFrame(frame, text="Dati")
        form.pack(fill="x")

        def row(r: int, label: str, var: tk.StringVar, browse: bool = False) -> None:
            ttk.Label(form, text=label).grid(row=r, column=0, sticky="w", padx=8, pady=6)
            ttk.Entry(form, textvariable=var).grid(row=r, column=1, sticky="ew", padx=8, pady=6)
            if browse:
                ttk.Button(form, text="Scegli...", command=self._choose_out_dir).grid(row=r, column=2, padx=8, pady=6)

        row(0, "Organizzazione", self.ente)
        row(1, "URL sito", self.sito)
        row(2, "Email accessibilita", self.email)
        row(3, "Percorso pubblico (base)", self.base_path)
        row(4, "Cartella output", self.out_dir, browse=True)

        form.columnconfigure(1, weight=1)

        actions = ttk.Frame(frame)
        actions.pack(fill="x", pady=(12, 0))
        ttk.Button(actions, text="Genera file", command=self._run).pack(side="left")

        self.out = tk.Text(frame, height=10, wrap="word")
        self.out.pack(fill="both", expand=True, pady=(12, 0))
        self.out.configure(state="disabled")

    def _choose_out_dir(self) -> None:
        p = filedialog.askdirectory(title="Seleziona cartella output")
        if p:
            self.out_dir.set(p)

    def _set_out(self, text: str) -> None:
        self.out.configure(state="normal")
        self.out.delete("1.0", tk.END)
        self.out.insert(tk.END, text)
        self.out.configure(state="disabled")

    def _run(self) -> None:
        try:
            files = write_project(
                Config(
                    ente=self.ente.get().strip(),
                    sito=self.sito.get().strip(),
                    email=self.email.get().strip(),
                    base_path=self.base_path.get().strip(),
                    out_dir=self.out_dir.get().strip(),
                )
            )
        except Exception as exc:  # noqa: BLE001
            messagebox.showerror("Errore", str(exc))
            return

        lines = ["OK. File generati:"]
        for k, v in files.items():
            lines.append(f"- {k}: {v}")
        self._set_out("\n".join(lines))
        messagebox.showinfo("Completato", "File generati correttamente.")


def main() -> int:
    app = App()
    app.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
