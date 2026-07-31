"""Command-line interface for browsing and running the course."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .labs import run_lab
from .progress import certificate, load, mark

ROOT = Path(__file__).resolve().parents[2]


def catalog() -> list[dict]:
    return json.loads((ROOT / "curriculum" / "catalog.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(prog="multicloud-program")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("catalog", help="list the 288 classes")
    run = sub.add_parser("run", help="run a class laboratory")
    run.add_argument("lesson_id")
    run.add_argument("--seed", type=int, default=7)
    show = sub.add_parser("show", help="show class metadata")
    show.add_argument("lesson_id")
    progress = sub.add_parser("progress", help="show or mark portable progress")
    progress.add_argument("--complete")
    cert = sub.add_parser("certificate", help="create certificate after full completion")
    cert.add_argument("--name", required=True)
    args = parser.parse_args()
    items = catalog()
    progress_path = ROOT / ".learning-progress.json"
    if args.command == "progress":
        data = mark(progress_path, args.complete.zfill(3)) if args.complete else load(progress_path)
        print(json.dumps({**data, "total": len(items)}, ensure_ascii=False, indent=2)); return 0
    if args.command == "certificate":
        data = load(progress_path); output = certificate(ROOT / "certificate.html", args.name, len(data["completed"]), len(items)); print(output); return 0
    if args.command == "catalog":
        for item in items:
            print(f"{item['id']}  P{item['part']}  {item['title']}")
        return 0
    item = next((x for x in items if x["id"] == args.lesson_id.zfill(3)), None)
    if item is None:
        parser.error(f"unknown lesson: {args.lesson_id}")
    if args.command == "show":
        print(json.dumps(item, ensure_ascii=False, indent=2))
        return 0
    result = run_lab(item["id"], item["lab_kind"], args.seed)
    output = ROOT / "lab_result.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"\nEvidence written to {output}")
    return 0
