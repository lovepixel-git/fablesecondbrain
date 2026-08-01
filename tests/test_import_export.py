#!/usr/bin/env python3
"""Hermetic tests for the system prompt import and capability matrix adapters."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PY = sys.executable
FIXTURE = REPO / "tests" / "fixtures" / "system-prompt-excerpt.txt"


def run(args: list[str], expect_fail: bool = False) -> subprocess.CompletedProcess:
    proc = subprocess.run([PY, *args], cwd=REPO, capture_output=True, text=True)
    if expect_fail:
        assert proc.returncode != 0, f"expected failure: {' '.join(args)}\n{proc.stdout}"
    else:
        assert proc.returncode == 0, f"command failed: {' '.join(args)}\n{proc.stdout}\n{proc.stderr}"
    return proc


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)

        # parse: sections and tools found
        parsed_path = tmp / "parsed.json"
        run(["scripts/import_system_prompt_export.py", "parse", "--file", str(FIXTURE), "--out", str(parsed_path)])
        parsed = json.loads(parsed_path.read_text())
        tags = [s["tag"] for s in parsed["sections"]]
        assert "claude_behavior" in tags, tags
        assert "product_information" in tags, tags
        assert parsed["tools"] == ["web_search", "web_fetch", "bash_tool"], parsed["tools"]
        assert parsed["sha256"] and parsed["line_count"] > 10
        top = [s for s in parsed["sections"] if s["depth"] == 0]
        assert any(s["tag"] == "claude_behavior" and s["close_line"] for s in top)

        # parse output carries no absolute local paths
        assert str(REPO) not in parsed_path.read_text()

        # diff: detects an added tool and a removed section
        changed = tmp / "changed.txt"
        text = FIXTURE.read_text()
        text = text.replace("`<tone_and_formatting>`", "`<renamed_section>`")
        text = text.replace("`</tone_and_formatting>`", "`</renamed_section>`")
        text += "\n## new_tool\n\nFixture description of a new tool.\n"
        changed.write_text(text)
        proc = run(["scripts/import_system_prompt_export.py", "diff", "--old", str(FIXTURE), "--new", str(changed)])
        assert "- added: renamed_section" in proc.stdout, proc.stdout
        assert "- removed: tone_and_formatting" in proc.stdout, proc.stdout
        assert "- added: new_tool" in proc.stdout, proc.stdout

        # malformed input: empty file fails loudly
        empty = tmp / "empty.txt"
        empty.write_text("")
        run(["scripts/import_system_prompt_export.py", "parse", "--file", str(empty)], expect_fail=True)
        run(["scripts/import_system_prompt_export.py", "parse", "--file", str(tmp / "missing.txt")], expect_fail=True)

        # capability matrix: renders rows from parse plus ledger summary
        ledger = tmp / "ledger.json"
        ledger.write_text(json.dumps({
            "domain": "fixture domain",
            "sources": [
                {"id": "a", "source_type": "official", "refresh_due": "2026-08-01"},
                {"id": "b", "source_type": "practitioner"},
            ],
        }))
        matrix = tmp / "matrix.md"
        run(["scripts/render_capability_matrix.py", "--file", str(FIXTURE), "--ledger", str(ledger), "--out", str(matrix)])
        report = matrix.read_text()
        assert "| claude_behavior |" in report, report
        assert "- official: 1" in report and "- practitioner: 1" in report, report
        assert "2026-08-01 (a)" in report, report
        assert "\u2014" not in report and "\u2013" not in report

        # matrix with missing ledger fails loudly
        run(["scripts/render_capability_matrix.py", "--file", str(FIXTURE), "--ledger", str(tmp / "no.json")], expect_fail=True)

    print("test_import_export: all assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
