#!/usr/bin/env python3
"""Parse and diff Claude system prompt exports.

parse: split an export into tagged sections and list tool headings, emit JSON.
diff:  compare two parsed exports and emit a markdown change report.

Exports are immutable inputs under .raw/; this tool never writes to them.
Outputs contain only repo-relative names, never absolute local paths.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

OPEN_TAG = re.compile(r"^\s*`?<([a-zA-Z_][\w:.-]*)>`?\s*$")
CLOSE_TAG = re.compile(r"^\s*`?</([a-zA-Z_][\w:.-]*)>`?\s*$")
TOOL_HEADING = re.compile(r"^## ([a-z][a-z0-9_:.-]*)$")
TOOLS_MARKER = "functions available in JSONSchema format"


def parse_export(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"ERROR: export not found: {path.name}")
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines:
        raise SystemExit(f"ERROR: export is empty: {path.name}")

    sections: list[dict] = []
    stack: list[dict] = []
    tools: list[str] = []
    in_tools = False
    for lineno, line in enumerate(lines, start=1):
        if TOOLS_MARKER in line:
            in_tools = True
        opened = OPEN_TAG.match(line)
        closed = CLOSE_TAG.match(line)
        if opened and not closed:
            entry = {"tag": opened.group(1), "open_line": lineno, "close_line": None, "depth": len(stack)}
            sections.append(entry)
            stack.append(entry)
            continue
        if closed:
            tag = closed.group(1)
            for entry in reversed(stack):
                if entry["tag"] == tag and entry["close_line"] is None:
                    entry["close_line"] = lineno
                    stack.remove(entry)
                    break
            continue
        if in_tools:
            tool = TOOL_HEADING.match(line)
            if tool:
                tools.append(tool.group(1))

    for entry in sections:
        end = entry["close_line"] if entry["close_line"] else len(lines)
        entry["lines"] = end - entry["open_line"] + 1

    return {
        "schema": "fable-5-brain.system-prompt-parse.v1",
        "file": path.name,
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "line_count": len(lines),
        "section_count": len(sections),
        "tool_count": len(tools),
        "sections": sections,
        "tools": tools,
    }


def render_diff(old: dict, new: dict) -> str:
    old_tags = {s["tag"]: s for s in old["sections"]}
    new_tags = {s["tag"]: s for s in new["sections"]}
    added = sorted(set(new_tags) - set(old_tags))
    removed = sorted(set(old_tags) - set(new_tags))
    resized = sorted(
        tag for tag in set(old_tags) & set(new_tags)
        if old_tags[tag]["lines"] != new_tags[tag]["lines"]
    )
    tools_added = sorted(set(new["tools"]) - set(old["tools"]))
    tools_removed = sorted(set(old["tools"]) - set(new["tools"]))

    out = [
        "# System Prompt Export Diff",
        "",
        f"Old: {old['file']} ({old['line_count']} lines, sha256 {old['sha256'][:12]})",
        f"New: {new['file']} ({new['line_count']} lines, sha256 {new['sha256'][:12]})",
        "",
        "## Sections",
        "",
    ]
    out += [f"- added: {t}" for t in added] or []
    out += [f"- removed: {t}" for t in removed] or []
    out += [
        f"- resized: {t} ({old_tags[t]['lines']} -> {new_tags[t]['lines']} lines)"
        for t in resized
    ]
    if not (added or removed or resized):
        out.append("- no section changes")
    out += ["", "## Tools", ""]
    out += [f"- added: {t}" for t in tools_added]
    out += [f"- removed: {t}" for t in tools_removed]
    if not (tools_added or tools_removed):
        out.append("- no tool changes")
    out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_parse = sub.add_parser("parse", help="parse one export to JSON")
    p_parse.add_argument("--file", required=True)
    p_parse.add_argument("--out", help="write JSON here instead of stdout")
    p_diff = sub.add_parser("diff", help="diff two exports to markdown")
    p_diff.add_argument("--old", required=True)
    p_diff.add_argument("--new", required=True)
    p_diff.add_argument("--out", help="write markdown here instead of stdout")
    args = parser.parse_args(argv)

    if args.cmd == "parse":
        parsed = parse_export(Path(args.file))
        payload = json.dumps(parsed, indent=2, sort_keys=True) + "\n"
        if args.out:
            Path(args.out).write_text(payload, encoding="utf-8")
        else:
            sys.stdout.write(payload)
        return 0

    report = render_diff(parse_export(Path(args.old)), parse_export(Path(args.new)))
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
