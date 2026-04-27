"""
save.py — one-command "save my work" for the day.

Stages all changes, commits with a sensible message, pushes to GitHub.

Usage:
    python automation/save.py                              # auto-generate message
    python automation/save.py "Day 5: add CSV reader"      # custom message
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str], check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        check=check,
        text=True,
        capture_output=capture,
    )


def has_changes() -> bool:
    out = run(["git", "status", "--porcelain"]).stdout
    return bool(out.strip())


def changed_paths() -> list[str]:
    out = run(["git", "status", "--porcelain"]).stdout
    paths = []
    for line in out.splitlines():
        # format: "XY path"
        line = line.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            paths.append(parts[1].replace("\\", "/"))
    return paths


def auto_message() -> str:
    """Generate a useful commit message from changed paths."""
    paths = changed_paths()
    if not paths:
        return "wip"

    # Detect day folders
    day_re = re.compile(r"projects/level-\d+[^/]*/day-(\d{2,})-([^/]+)")
    day_hits = []
    other = []
    for p in paths:
        m = day_re.search(p)
        if m:
            day_hits.append((int(m.group(1)), m.group(2)))
        else:
            other.append(p)

    if day_hits:
        # Pick the most-changed day
        day_hits.sort()
        day_num, slug = day_hits[-1]
        nice = slug.replace("-", " ")
        return f"Day {day_num:02d}: progress on {nice}"

    # Otherwise summarize areas
    areas = set()
    for p in paths:
        first = p.split("/", 1)[0]
        areas.add(first)
    return "Update " + ", ".join(sorted(areas))


def main() -> int:
    if not has_changes():
        print("[=] No changes to commit. Nothing to save.")
        # Still try push in case there are unpushed commits
        try:
            r = run(["git", "push"], check=False)
            if r.returncode == 0:
                if "Everything up-to-date" in (r.stderr or ""):
                    print("[=] Already in sync with GitHub.")
                else:
                    print("[+] Pushed pending commits.")
            else:
                print(f"[!] Push failed:\n{r.stderr}")
        except Exception as e:
            print(f"[!] Push error: {e}")
        return 0

    # Refresh README before staging so it's always in sync with state
    try:
        subprocess.run(
            [sys.executable, str(ROOT / "automation" / "update_readme.py")],
            cwd=ROOT, check=False, text=True, capture_output=True,
        )
    except Exception as e:
        print(f"[!] update_readme failed (continuing): {e}")

    message = sys.argv[1] if len(sys.argv) > 1 else auto_message()

    print(f"[i] Commit message: {message}")
    run(["git", "add", "-A"])
    run(["git", "commit", "-m", message])
    print("[+] Committed.")

    push = run(["git", "push"], check=False)
    if push.returncode == 0:
        print("[+] Pushed to GitHub.")
    else:
        print(f"[!] Push failed (commit is saved locally):\n{push.stderr}")
        print("    Try: git pull --rebase && git push")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
