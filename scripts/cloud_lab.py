"""Cost-safe lifecycle controller for optional provider sandboxes."""

import argparse
import json
import os
from datetime import datetime, timezone


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["plan", "deploy", "verify", "destroy"])
    parser.add_argument("--lesson", required=True)
    parser.add_argument("--provider", choices=["aws", "azure", "gcp"], default="aws")
    args = parser.parse_args()
    allowed = os.getenv("CLOUD_LAB_ALLOW_COST") == "1"
    if args.action == "deploy" and not allowed:
        parser.error("deploy blocked; set CLOUD_LAB_ALLOW_COST=1 after budget and identity checks")
    result = {"action": args.action, "lesson": args.lesson, "provider": args.provider, "cost_gate": allowed, "time": datetime.now(timezone.utc).isoformat()}
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
