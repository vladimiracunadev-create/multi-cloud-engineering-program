"""Executable lab for lesson 248."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="248", kind="decision", title='Bedrock, Azure AI Foundry y Vertex AI', artifact="genai-provider-adr"))
