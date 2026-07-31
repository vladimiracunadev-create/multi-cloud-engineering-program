"""Executable lab for lesson 035."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="035", kind="security", title='KMS, Secrets Manager, WAF y controles de seguridad', artifact="controles-aws"))
