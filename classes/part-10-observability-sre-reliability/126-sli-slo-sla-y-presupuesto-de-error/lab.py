"""Executable lab for lesson 126."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="126", kind="sre", title='SLI, SLO, SLA y presupuesto de error', artifact="slo-servicio"))
