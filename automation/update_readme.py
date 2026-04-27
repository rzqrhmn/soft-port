"""
update_readme.py — refresh root README.md with current portfolio status.

Reads:
- existing project day folders
- recent commits
- current level

Writes: README.md at repo root.

Run after each save, or by daily scheduled task.
"""

from __future__ import annotations

import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVEL_1_DIR = ROOT / "projects" / "level-1-foundations"


def run(cmd: list[str]) -> str:
    r = subprocess.run(cmd, cwd=ROOT, check=False, text=True, capture_output=True)
    return r.stdout


def list_days() -> list[tuple[int, str, Path]]:
    if not LEVEL_1_DIR.exists():
        return []
    pattern = re.compile(r"^day-(\d{2,})-(.+)$")
    out = []
    for p in sorted(LEVEL_1_DIR.iterdir()):
        if p.is_dir():
            m = pattern.match(p.name)
            if m:
                out.append((int(m.group(1)), m.group(2), p))
    return out


def recent_commits(n: int = 7) -> list[tuple[str, str, str]]:
    out = run(["git", "log", f"-{n}", "--pretty=format:%h|%ad|%s", "--date=short"])
    rows = []
    for line in out.splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3:
            rows.append(tuple(parts))
    return rows


def days_active_last_30() -> int:
    since = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    out = run(["git", "log", f"--since={since}", "--pretty=format:%ad", "--date=short"])
    return len({l.strip() for l in out.splitlines() if l.strip()})


def total_commits() -> int:
    out = run(["git", "rev-list", "--count", "HEAD"])
    try:
        return int(out.strip())
    except ValueError:
        return 0


def build_readme() -> str:
    days = list_days()
    completed = len(days)
    last_day = days[-1] if days else None
    commits = recent_commits()
    total = total_commits()
    active_30 = days_active_last_30()

    lines = []
    lines.append("# Soft — Embedded & Firmware Engineering Portfolio")
    lines.append("")
    lines.append("Daily 15-30 minute practice toward testing / commissioning / lab engineer roles in Germany.")
    lines.append("")
    lines.append("**Background**: 10 years industrial experience (Krakatau Posco — blower plant, large synchronous motors). Currently MSc Electrical Engineering at Hochschule Kempten.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Current status")
    lines.append("")
    lines.append(f"- Level 1 progress: **{completed} / 28 days**")
    if last_day:
        day_num, slug, _ = last_day
        nice = slug.replace("-", " ")
        lines.append(f"- Latest: **Day {day_num:02d}** — {nice}")
    lines.append(f"- Active days last 30: **{active_30}**")
    lines.append(f"- Total commits: **{total}**")
    lines.append(f"- Last update: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Roadmap (high level)")
    lines.append("")
    lines.append("| Level | Focus | Status |")
    lines.append("|-------|-------|--------|")
    l1_status = "in progress" if 0 < completed < 28 else ("not started" if completed == 0 else "complete")
    lines.append(f"| 1 — Foundations | Python + Git + sensor data | {l1_status} ({completed}/28) |")
    lines.append("| 2 — Industrial Protocols | Modbus, CAN, MQTT | pending |")
    lines.append("| 3 — Firmware Simulation | Arduino/ESP32 in Wokwi, C/C++ | pending |")
    lines.append("| 4 — Real Hardware | ESP32 + sensors, IoT | pending |")
    lines.append("| 5 — Capstone | Predictive maintenance edge device | pending |")
    lines.append("")
    lines.append("Full plan: see [`ROADMAP.md`](ROADMAP.md).")
    lines.append("")

    if commits:
        lines.append("## Recent commits")
        lines.append("")
        for h, d, msg in commits:
            lines.append(f"- `{h}` {d} — {msg}")
        lines.append("")

    if days:
        lines.append("## Days completed")
        lines.append("")
        for day_num, slug, path in days:
            nice = slug.replace("-", " ")
            rel = path.relative_to(ROOT).as_posix()
            lines.append(f"- [Day {day_num:02d} — {nice}]({rel}/)")
        lines.append("")

    lines.append("## Daily flow")
    lines.append("")
    lines.append("1. Morning: laptop auto-creates today's task folder (Task Scheduler)")
    lines.append("2. 15-30 min: open the folder, read README, code in main.py")
    lines.append("3. Before sleep: `python automation/save.py` — commits + pushes")
    lines.append("4. Sunday 20:00: weekly report auto-generated to `reports/`")
    lines.append("")
    lines.append("Setup: see [`SETUP.md`](SETUP.md). Git basics: [`GIT_CHEATSHEET.md`](GIT_CHEATSHEET.md).")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("_This README is auto-updated by `automation/update_readme.py`._")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    content = build_readme()
    (ROOT / "README.md").write_text(content, encoding="utf-8")
    print(f"[+] Updated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
