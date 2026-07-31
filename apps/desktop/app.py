"""Small offline desktop navigator for the course."""
import json
import tkinter as tk
from pathlib import Path
from tkinter import ttk

ROOT = Path(__file__).resolve().parents[2]
items = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
root = tk.Tk(); root.title("Multi-Cloud Engineering Program"); root.geometry("920x620")
query = tk.StringVar(); ttk.Entry(root, textvariable=query).pack(fill="x", padx=12, pady=12)
tree = ttk.Treeview(root, columns=("part", "title", "level"), show="headings")
for key, label in [("part", "Parte"), ("title", "Clase"), ("level", "Nivel")]: tree.heading(key, text=label)
tree.pack(fill="both", expand=True, padx=12, pady=(0, 12))
def render(*_: object) -> None:
    tree.delete(*tree.get_children()); term=query.get().casefold()
    for item in items:
        if term in (item["id"]+" "+item["title"]+" "+item["part_title"]).casefold(): tree.insert("", "end", values=(item["part"], item["id"]+" — "+item["title"], item["level"]))
query.trace_add("write", render); render(); root.mainloop()
