#!/usr/bin/env python3
"""Check repository Markdown targets and JSON syntax (stdlib only).

External URLs and fragment identifiers are intentionally not validated.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+['\"][^'\"]+['\"])?\)")
FENCE = re.compile(r"^\s*([\x60]{3,}|~{3,})")
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def walk(suffix: str) -> list[Path]:
    return sorted(
        p for p in ROOT.rglob(f"*{suffix}")
        if p.is_file() and not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def local_target(source: Path, href: str) -> Path | None:
    href = href.strip().removeprefix("<").removesuffix(">")
    parts = urlsplit(href)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    path = unquote(parts.path)
    target = (ROOT / path.lstrip("/") if path.startswith("/") else source.parent / path)
    return target.resolve()


def check_markdown(source: Path) -> tuple[int, list[str]]:
    problems: list[str] = []
    checked = 0
    active_fence: str | None = None
    content = source.read_text(encoding="utf-8-sig")
    for line_number, line in enumerate(content.splitlines(), 1):
        fence = FENCE.match(line)
        if fence:
            token = fence.group(1)
            if active_fence is None:
                active_fence = token[0]
            elif token[0] == active_fence:
                active_fence = None
            continue
        if active_fence:
            continue
        # Inline code is not an active Markdown link.
        line = re.sub(r"\x60[^\x60]*\x60", "", line)
        for match in LINK.finditer(line):
            href = match.group(1)
            target = local_target(source, href)
            if target is None:
                continue
            checked += 1
            try:
                display = target.relative_to(ROOT)
            except ValueError:
                problems.append(f"{source.relative_to(ROOT)}:{line_number}: outside repository: {href}")
                continue
            if not target.exists():
                problems.append(f"{source.relative_to(ROOT)}:{line_number}: missing {display} ({href})")
    return checked, problems


def main() -> int:
    problems: list[str] = []
    link_count = 0
    markdown_files = walk(".md")
    json_files = walk(".json")
    for path in markdown_files:
        try:
            count, errors = check_markdown(path)
            link_count += count
            problems.extend(errors)
        except (OSError, UnicodeError) as exc:
            problems.append(f"{path.relative_to(ROOT)}: failed to read: {exc}")
    for path in json_files:
        try:
            with path.open(encoding="utf-8-sig") as f:
                json.load(f)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            problems.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        print(f"FAIL: {len(problems)} issue(s); {link_count} local links scanned; "
              f"{len(markdown_files)} Markdown and {len(json_files)} JSON files",
              file=sys.stderr)
        return 1
    print(f"PASS: {link_count} local links; {len(markdown_files)} Markdown; "
          f"{len(json_files)} JSON files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
