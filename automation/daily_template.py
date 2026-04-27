"""
daily_template.py — generate today's project folder + starter files.

Run manually or via Windows Task Scheduler each morning.

Logic:
- Scan projects/level-1-foundations/day-XX-*
- Find next missing day number
- Create folder with README.md (task description) + main.py (starter)
- If today's folder already exists, do nothing.

Usage:
    python automation/daily_template.py
    python automation/daily_template.py --day 5    # force specific day
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVEL_1_DIR = ROOT / "projects" / "level-1-foundations"

sys.path.insert(0, str(ROOT / "automation"))
from roadmap_tasks import get_task, total_days  # noqa: E402


README_TEMPLATE = """# Day {day:02d} — {title}

**Date created**: {date}
**Estimated time**: 15-30 minutes

## Task

{description}

## Hints

{hints}

## What "done" looks like

- [ ] Code runs without errors
- [ ] You understand each line you wrote (no copy-paste-magic)
- [ ] Brief note added below in `## Reflection`

## Reflection

_(Fill this in when done — even one sentence.)_

What I learned:

What was hard:

What I'd do differently:
"""

MAIN_PY_TEMPLATE = '''"""
Day {day:02d} — {title}

{description}
"""


def main() -> None:
    # TODO: write your code here
    print("Day {day:02d}: starter ready. Replace this with your work.")


if __name__ == "__main__":
    main()
'''


def find_next_day() -> int:
    """Return the next day number to create."""
    if not LEVEL_1_DIR.exists():
        return 1
    pattern = re.compile(r"^day-(\d{2,})-")
    existing = []
    for p in LEVEL_1_DIR.iterdir():
        if p.is_dir():
            m = pattern.match(p.name)
            if m:
                existing.append(int(m.group(1)))
    if not existing:
        return 1
    return max(existing) + 1


def folder_for_day(day: int, slug: str) -> Path:
    return LEVEL_1_DIR / f"day-{day:02d}-{slug}"


def create_day_folder(day: int) -> Path | None:
    task = get_task(day)
    if task is None:
        print(f"[!] No task defined for day {day}. Reached end of Level 1 ({total_days()} days).")
        print("[i] Open ROADMAP.md and start Level 2, or extend automation/roadmap_tasks.py.")
        return None

    _, slug, title, desc, hints = task
    folder = folder_for_day(day, slug)
    if folder.exists():
        print(f"[=] Day {day:02d} folder already exists: {folder.relative_to(ROOT)}")
        return folder

    folder.mkdir(parents=True, exist_ok=True)

    readme = folder / "README.md"
    readme.write_text(
        README_TEMPLATE.format(
            day=day,
            title=title,
            description=desc,
            hints=hints,
            date=datetime.now().strftime("%Y-%m-%d"),
        ),
        encoding="utf-8",
    )

    main_py = folder / "main.py"
    main_py.write_text(
        MAIN_PY_TEMPLATE.format(day=day, title=title, description=desc),
        encoding="utf-8",
    )

    print(f"[+] Created Day {day:02d}: {folder.relative_to(ROOT)}")
    print(f"    {title}")
    print(f"    {desc}")
    return folder


def main() -> int:
    parser = argparse.ArgumentParser(description="Create today's daily project folder.")
    parser.add_argument("--day", type=int, default=None, help="Force specific day number.")
    args = parser.parse_args()

    day = args.day if args.day is not None else find_next_day()
    folder = create_day_folder(day)
    return 0 if folder is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
