"""Executable lab for lesson 205."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="205", kind="delivery", title='Hosting progresivo con Amplify, S3 y CloudFront', artifact="aws-static-platform"))
