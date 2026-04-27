"""
weekly_report.py — generate a Sunday-night progress report.

Reads git log for past 7 days, summarizes commits, lists day folders touched,
writes reports/week-YYYY-WW.md.

Run by Windows Task Scheduler every Sunday 20:00.
"""

from __future__ import annotations

import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "reports"


def run(cmd: list[str]) -> str:
    r = subprocess.run(cmd, cwd=ROOT, check=False, text=True, capture_output=True)
    return r.stdout


def commits_since(days: int) -> list[tuple[str, str, str]]:
    """Return [(hash, date, message), ...] for commits in last N days."""
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    out = run([
        "git", "log",
        f"--since={since}",
        "--pretty=format:%h|%ad|%s",
        "--date=short",
    ])
    rows = []
    for line in out.splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3:
            rows.append(tuple(parts))
    return rows


def files_changed_since(days: int) -> set[str]:
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    out = run(["git", "log", f"--since={since}", "--name-only", "--pretty=format:"])
    return {line.strip() for line in out.splitlines() if line.strip()}


def days_worked(days: int) -> set[str]:
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    out = run(["git", "log", f"--since={since}", "--pretty=format:%ad", "--date=short"])
    return {line.strip() for line in out.splitlines() if line.strip()}


def project_days_touched(files: set[str]) -> list[tuple[int, str]]:
    pattern = re.compile(r"projects/level-\d+[^/]*/day-(\d{2,})-([^/]+)")
    seen = {}
    for f in files:
        m = pattern.search(f.replace("\\", "/"))
        if m:
            day_num = int(m.group(1))
            slug = m.group(2)
            seen[day_num] = slug
    return sorted(seen.items())


def main() -> int:
    REPORTS_DIR.mkdir(exist_ok=True)

    now = datetime.now()
    iso_year, iso_week, _ = now.isocalendar()
    week_label = f"{iso_year}-W{iso_week:02d}"

    commits = commits_since(7)
    files = files_changed_since(7)
    days_active = days_worked(7)
    project_days = project_days_touched(files)

    lines = []
    lines.append(f"# Weekly Report — {week_label}")
    lines.append("")
    lines.append(f"Generated: {now.strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Commits this week**: {len(commits)}")
    lines.append(f"- **Days active**: {len(days_active)} / 7")
    lines.append(f"- **Project days touched**: {len(project_days)}")
    lines.append("")

    if project_days:
        lines.append("## Days completed")
        lines.append("")
        for day_num, slug in project_days:
            nice = slug.replace("-", " ")
            lines.append(f"- Day {day_num:02d}: {nice}")
        lines.append("")

    if commits:
        lines.append("## Commits")
        lines.append("")
        for h, d, msg in commits:
            lines.append(f"- `{h}` {d} — {msg}")
        lines.append("")

    lines.append("## Reflection")
    lines.append("")
    lines.append("_(Fill this in. Even one sentence helps. This becomes interview material.)_")
    lines.append("")
    lines.append("- What I'm proud of:")
    lines.append("- What slowed me down:")
    lines.append("- One specific thing I learned:")
    lines.append("- Plan for next week:")
    lines.append("")

    out_path = REPORTS_DIR / f"week-{week_label}.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {out_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
