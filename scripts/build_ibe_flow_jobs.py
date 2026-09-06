#!/usr/bin/env python3
"""Build Google Flow still-image jobs for InnerBalancEmporium from flow/image-queue.json."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "flow" / "ibe-flow-pipeline.config.json"
DEFAULT_QUEUE = ROOT / "flow" / "image-queue.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def assemble_prompt(scene: str, template: str) -> str:
    return template.replace("{scene}", scene.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--max", type=int, default=3)
    parser.add_argument("--slug")
    parser.add_argument("--priority", help="Filter pending by priority (banner, category, product, journal)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    queue_path = Path(cfg["imageQueueFile"])
    jobs_dir = Path(cfg["imageJobsDir"])
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    pending = list(queue.get("pending", []))

    if args.slug:
        pending = [p for p in pending if p["slug"] == args.slug]
    if args.priority:
        pending = [p for p in pending if p.get("priority") == args.priority]
    pending = pending[: args.max]

    if not pending:
        print("No pending items")
        return 0

    template = cfg.get("visualPromptTemplate", "Scene: {scene}")
    flow_url = cfg.get("flowProjectUrl") or cfg.get("flowUrl")
    assets_dir = Path(cfg["heroAssetsDir"])
    jobs_dir.mkdir(parents=True, exist_ok=True)

    for item in pending:
        slug = item["slug"]
        scene = item.get("scene") or item.get("title") or slug
        aspect = item.get("aspect") or cfg.get("defaultAspect", "16:9")
        job = {
            "slug": slug,
            "title": item.get("title") or slug,
            "slot": item.get("slot"),
            "priority": item.get("priority"),
            "scene_prompt": scene,
            "visual_prompt": assemble_prompt(scene, template),
            "output_png": str(assets_dir / f"{slug}.png"),
            "flow_url": flow_url,
            "aspect": aspect,
            "built_at": utc_now(),
        }
        if args.dry_run:
            print(json.dumps(job, indent=2))
        else:
            out = jobs_dir / f"{slug}.json"
            out.write_text(json.dumps(job, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"Wrote {out.name}")

    print(f"Built {len(pending)} job(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
