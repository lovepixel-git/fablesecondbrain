#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run([PY, *args], cwd=REPO, text=True, capture_output=True, env={**os.environ, **(env or {})}, check=False)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"command failed: {' '.join(args)}")
    return proc


def run_cmd(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(args, cwd=REPO, text=True, capture_output=True, env={**os.environ, **(env or {})}, check=False)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"command failed: {' '.join(args)}")
    return proc


def main() -> int:
    run(["-m", "compileall", "scripts", "fable_5_brain", "tests"])
    run(["scripts/lint_vault.py", "--vault", "assets/template-brain", "--template"])
    with tempfile.TemporaryDirectory(prefix="fable-5-brain-test-") as tmp:
        out_dir = Path(tmp) / "vaults"
        run(["scripts/scaffold_vault.py", "--client", "acme", "--client-name", "Acme Co", "--owner", "Test Owner", "--out-dir", str(out_dir)])
        vault = out_dir / "acme"
        run(["scripts/ingest_source.py", "--vault", str(vault), "--file", "tests/fixtures/sample-source.md"])
        run(["scripts/synthesize_brain.py", "--vault", str(vault)])
        run(["scripts/generate_vault_visuals.py", "--vault", str(vault)])
        run(["scripts/render_brain_report.py", "--vault", str(vault), "--html-only"])
        run(["scripts/lint_vault.py", "--vault", str(vault)])
        assert (vault / "weekly-report.html").exists()
    run(["scripts/build_demo_vault.py"])
    run(["scripts/audit_brain.py", "--json", "--report-only"])
    # This brain passes the market-ready audit gate, so a market-ready release must be allowed.
    ready = subprocess.run([PY, "scripts/package_release.py", "--version", "0.1.0", "--release-type", "market-ready"], cwd=REPO, text=True, capture_output=True, check=False)
    assert ready.returncode == 0, f"market-ready gate should pass for this brain: {ready.stderr}"
    run(["scripts/package_release.py", "--version", "0.1.0"])
    assert (REPO / "dist" / "RELEASE_MANIFEST.json").exists()
    with tempfile.TemporaryDirectory(prefix="fable-5-brain-install-") as tmp:
        env = {"FABLE_5_BRAIN_INSTALL_HOME": tmp}
        run_cmd(["bash", "install.sh", "--target", "all"], env=env)
        assert (Path(tmp) / ".codex" / "skills" / "fable-5-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".openclaw" / "skills" / "fable-5-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".agent-skills" / "fable-5-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".gemini" / "fable-5-brain" / "GEMINI.md").exists()
        assert "fable-5-brain-install:start" in (Path(tmp) / ".gemini" / "GEMINI.md").read_text(encoding="utf-8")
        custom_root = Path(tmp) / "custom-skills"
        run_cmd(["bash", "install.sh", "--target", "custom", "--path", str(custom_root)], env=env)
        assert (custom_root / "fable-5-brain" / "SKILL.md").exists()
        run_cmd(["bash", "uninstall.sh", "--target", "all"], env=env)
        assert not (Path(tmp) / ".codex" / "skills" / "fable-5-brain").exists()
        assert not (Path(tmp) / ".gemini" / "fable-5-brain").exists()
        assert not (Path(tmp) / ".gemini" / "GEMINI.md").exists()
        run_cmd(["bash", "uninstall.sh", "--target", "custom", "--path", str(custom_root)], env=env)
        assert not (custom_root / "fable-5-brain").exists()
    print("Pipeline tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
