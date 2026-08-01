#!/usr/bin/env python3
"""Render the Fable 5 capability matrix from a parsed export and the source ledger.

Rows are top-level export sections (evidence spans); the ledger summary shows
source counts by type and the nearest refresh_due dates. Deterministic output.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_system_prompt_export import parse_export  # noqa: E402


def load_ledger(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"ERROR: ledger not found: {path.name}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: ledger is not valid JSON: {exc}")


def render(parsed: dict, ledger: dict) -> str:
    top = [s for s in parsed["sections"] if s["depth"] == 0]
    sources = ledger.get("sources", [])
    by_type = Counter(s.get("source_type", "unknown") for s in sources)
    due = sorted((s.get("refresh_due", ""), s.get("id", "")) for s in sources if s.get("refresh_due"))

    out = [
        "# Fable 5 Capability Matrix",
        "",
        f"Export: {parsed['file']} ({parsed['line_count']} lines, "
        f"{parsed['section_count']} sections, {parsed['tool_count']} tools)",
        f"Ledger: {len(sources)} sources, domain: {ledger.get('domain', 'unknown')}",
        "",
        "## Capability areas (export evidence)",
        "",
        "| Section | Lines | Span |",
        "|---|---|---|",
    ]
    for s in top:
        close = s["close_line"] if s["close_line"] else parsed["line_count"]
        out.append(f"| {s['tag']} | {s['lines']} | L{s['open_line']}-{close} |")
    out += ["", "## Tools documented in export", ""]
    out += [f"- {t}" for t in parsed["tools"]] or ["- none found"]
    out += ["", "## Source ledger summary", ""]
    out += [f"- {t}: {n}" for t, n in sorted(by_type.items())]
    if due:
        out += ["", "Next refresh due:"]
        out += [f"- {d} ({sid})" for d, sid in due[:5]]
    out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--file", required=True, help="system prompt export to parse")
    parser.add_argument("--ledger", required=True, help="references/source-ledger.json")
    parser.add_argument("--out", help="write markdown here instead of stdout")
    args = parser.parse_args(argv)

    report = render(parse_export(Path(args.file)), load_ledger(Path(args.ledger)))
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
