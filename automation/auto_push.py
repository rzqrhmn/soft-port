"""
auto_push.py — hourly background task: push any unpushed commits to GitHub.

Does NOT auto-commit. Only pushes commits you've already made.
This avoids creating fake / mid-edit commits.

Run by Windows Task Scheduler (see setup_windows_tasks.ps1).
Logs to logs/auto_push.log so you can debug if something fails silently.
"""

from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "auto_push.log"


def log(msg: str) -> None:
    LOG_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(cmd: list[str], check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, check=check, text=True, capture_output=True)


def has_unpushed_commits() -> bool:
    """Return True if local main is ahead of origin/main."""
    # Make sure we have remote refs
    run(["git", "fetch", "origin"])
    r = run(["git", "rev-list", "--count", "@{u}..HEAD"], check=False)
    if r.returncode != 0:
        # No upstream set yet, or other error
        log(f"git rev-list failed: {r.stderr.strip()}")
        return False
    try:
        return int(r.stdout.strip()) > 0
    except ValueError:
        return False


def main() -> int:
    # Check we're in a git repo
    r = run(["git", "rev-parse", "--is-inside-work-tree"])
    if r.returncode != 0:
        log("Not a git repo. Skipping.")
        return 1

    if not has_unpushed_commits():
        # Quiet success — don't log every hour if nothing to do.
        # Uncomment if you want to confirm task is firing:
        # log("Nothing to push.")
        return 0

    log("Unpushed commits detected. Pushing...")
    push = run(["git", "push"])
    if push.returncode == 0:
        log("Push succeeded.")
        return 0
    else:
        log(f"Push failed: {push.stderr.strip()}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
