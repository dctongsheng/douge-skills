#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def extract_config(markdown_path: Path) -> dict[str, Any]:
    text = markdown_path.read_text("utf-8")
    match = re.search(r"```json\s*(.*?)\s*```", text, re.S)
    if not match:
        raise ValueError(f"missing fenced json block in {markdown_path}")
    config = json.loads(match.group(1))
    required = ["pack_id", "display_name", "identity", "behavior_profile", "world_rules"]
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"missing required AgentPackConfig keys: {', '.join(missing)}")
    return config


def request_json(method: str, url: str, api_key: str, payload: dict[str, Any] | None = None) -> Any:
    data = None
    headers = {"X-API-Key": api_key}
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else None
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {url} failed: HTTP {error.code} {body}") from error


def main() -> int:
    parser = argparse.ArgumentParser(description="Import a LifeOS Agent Pack Markdown file.")
    parser.add_argument("markdown", type=Path, help="Path to docs/agent-packs/<pack_id>.md")
    parser.add_argument("--server", default=os.environ.get("LIFEOS_SERVER", "http://127.0.0.1:8000"))
    parser.add_argument("--api-key", default=os.environ.get("LIFEOS_API_KEY", "dev-lifeos-key-change-me"))
    parser.add_argument("--world-name", help="World display name. Defaults to pack display_name.")
    parser.add_argument("--no-world", action="store_true", help="Only create the pack; skip world creation.")
    args = parser.parse_args()

    server = args.server.rstrip("/")
    config = extract_config(args.markdown)
    pack_id = config["pack_id"]
    display_name = config["display_name"]

    packs = request_json("GET", f"{server}/packs", args.api_key)
    existing_pack = next((pack for pack in packs if pack["pack_id"] == pack_id), None)
    if existing_pack:
        print(f"pack_exists\t{pack_id}\t{existing_pack['display_name']}")
    else:
        payload = {key: value for key, value in config.items() if key != "is_preset"}
        created = request_json("POST", f"{server}/packs", args.api_key, payload)
        print(f"pack_created\t{created['pack_id']}\t{created['display_name']}")

    if args.no_world:
        return 0

    world_name = args.world_name or display_name
    worlds = request_json("GET", f"{server}/worlds", args.api_key)
    existing_world = next(
        (world for world in worlds if world["pack_id"] == pack_id and world["display_name"] == world_name),
        None,
    )
    if existing_world:
        print(f"world_exists\t{existing_world['world_id']}\t{pack_id}\t{world_name}")
    else:
        world = request_json(
            "POST",
            f"{server}/worlds",
            args.api_key,
            {"pack_id": pack_id, "display_name": world_name},
        )
        print(f"world_created\t{world['world_id']}\t{pack_id}\t{world_name}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from None
