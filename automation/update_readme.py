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
    lines.append("# soft-port")
    lines.append("")
    lines.append("Latihan harian saya buat naikin skill Python dan embedded.")
    lines.append("")
    lines.append("Saya 10 tahun kerja di blower plant Krakatau Posco (banyak motor sinkron besar), sekarang nyelesain MSc Electrical Engineering di Hochschule Kempten. Tujuannya: pindah ke role testing / commissioning / lab engineering di Jerman.")
    lines.append("")
    lines.append("Targetnya 15-30 menit per hari. Kalau sibuk, skip aja, gak masalah.")
    lines.append("")
    lines.append("## Progress")
    lines.append("")
    if last_day:
        day_num, slug, _ = last_day
        nice = slug.replace("-", " ")
        lines.append(f"Saat ini di Day {day_num:02d} ({nice}). Total {total} commit, aktif {active_30} hari dalam 30 hari terakhir.")
    else:
        lines.append("Belum mulai. Setup baru selesai.")
    lines.append("")
    lines.append("Plan lengkap ada di [ROADMAP.md](ROADMAP.md).")
    lines.append("")

    if days:
        lines.append("## Folder per hari")
        lines.append("")
        for day_num, slug, path in days:
            nice = slug.replace("-", " ")
            rel = path.relative_to(ROOT).as_posix()
            lines.append(f"- [Day {day_num:02d} - {nice}]({rel}/)")
        lines.append("")

    if commits:
        lines.append("## Commit terakhir")
        lines.append("")
        for h, d, msg in commits[:5]:
            lines.append(f"- `{h}` {d} - {msg}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"_Last updated: {datetime.now().strftime('%Y-%m-%d')}_")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    content = build_readme()
    (ROOT / "README.md").write_text(content, encoding="utf-8")
    print(f"[+] Updated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
