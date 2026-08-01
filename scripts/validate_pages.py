"""Smoke-test the public GitHub Pages deployment."""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_URL = "https://vladimiracunadev-create.github.io/multi-cloud-engineering-program/"


def fetch(base_url: str, path: str, *, byte_range: str | None = None) -> bytes:
    url = urllib.parse.urljoin(base_url.rstrip("/") + "/", path)
    separator = "&" if "?" in url else "?"
    url = f"{url}{separator}smoke={int(time.time())}"
    if urllib.parse.urlsplit(url).scheme not in {"http", "https"}:
        raise ValueError("Pages URL must use HTTP or HTTPS")
    headers = {"Cache-Control": "no-cache", "User-Agent": "multi-cloud-pages-smoke-test"}
    if byte_range:
        headers["Range"] = byte_range
    request = urllib.request.Request(url, headers=headers)
    # The explicit scheme allowlist above makes urlopen safe for this smoke test.
    with urllib.request.urlopen(request, timeout=30) as response:  # nosec B310
        return response.read(5) if byte_range else response.read()


def validate(base_url: str) -> None:
    index = fetch(base_url, "").decode("utf-8")
    for marker in ("Multi-Cloud Engineering Program", "curriculum-view", "288 clases"):
        if marker not in index:
            raise ValueError(f"homepage is missing marker: {marker}")

    catalog = json.loads(fetch(base_url, "catalog.json"))
    if len(catalog) != 288:
        raise ValueError(f"catalog has {len(catalog)} classes instead of 288")

    for class_id in ("001", "288"):
        page = fetch(base_url, f"classes/{class_id}.html").decode("utf-8")
        if "assessment" not in page or "data-lesson-complete" not in page:
            raise ValueError(f"class {class_id} is incomplete")

    worker = fetch(base_url, "service-worker.js").decode("utf-8")
    if "multicloud-program-v2.0.0-r3" not in worker:
        raise ValueError("the deployed service worker cache is obsolete")

    manual = fetch(
        base_url,
        "downloads/multi-cloud-engineering-manual-v2.0.pdf",
        byte_range="bytes=0-4",
    )
    if not manual.startswith(b"%PDF-"):
        raise ValueError("the complete manual is not available as a PDF")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--attempts", type=int, default=1)
    parser.add_argument("--delay", type=int, default=10)
    args = parser.parse_args()

    for attempt in range(1, args.attempts + 1):
        try:
            validate(args.url)
            print(f"Pages valid at {args.url}: portal, 288 classes, PWA and manual are online.")
            return 0
        except (OSError, ValueError, json.JSONDecodeError, urllib.error.HTTPError) as error:
            print(f"Pages check {attempt}/{args.attempts} failed: {error}")
            if attempt < args.attempts:
                time.sleep(args.delay)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
