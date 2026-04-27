"""
Day-by-day tasks for Level 1 (Week 1-4).
Each entry: (day_num, slug, title, description, hints).

Editable: feel free to change tasks anytime — script picks up changes.
"""

LEVEL_1_TASKS = [
    (1, "hello-embedded",
     "Hello, embedded world",
     "Print a list of sensor names: ['temp_motor', 'vibration', 'current'].",
     "Use a Python list and a for-loop. ~5 lines of code."),

    (2, "csv-read",
     "Read motor temperature CSV",
     "Read sample_temp.csv (provided) and print each row.",
     "Use the `csv` module from stdlib. csv.reader(open(path))."),

    (3, "stats-basic",
     "Compute mean / max / min",
     "From the same CSV, print average, max, min temperature.",
     "sum() and len() for mean. max() and min() built-ins."),

    (4, "plot-temp",
     "Plot temperature over time",
     "Plot temperature vs time, save as PNG.",
     "pip install matplotlib. plt.plot, plt.savefig('plot.png')."),

    (5, "cli-args",
     "CLI tool with argparse",
     "Make the script accept --csv path as an argument.",
     "Use argparse from stdlib. python main.py --csv data.csv."),

    (6, "threshold-alarm",
     "Detect threshold crossings",
     "Print a warning whenever temperature > 80 degrees.",
     "Loop through readings, if val > 80: print(...). Real motor protection logic!"),

    (7, "miniproject-1",
     "Mini-project: motor temp analyzer",
     "Combine days 1-6 into one polished script with proper README.",
     "Refactor into functions. Write README with usage, screenshot, sample output."),

    (8, "fake-data-gen",
     "Generate fake sensor data",
     "Generate 1000 readings with normal distribution + slow upward drift.",
     "Use random.gauss(mean, stdev). Add `i*0.01` for drift."),

    (9, "csv-write-timestamp",
     "Save sensor data with timestamps",
     "Write generated data to CSV with ISO 8601 timestamps.",
     "datetime.now().isoformat(). csv.writer."),

    (10, "anomaly-rolling",
     "Anomaly detection: rolling mean + 2 sigma",
     "Detect points more than 2 standard deviations from rolling mean.",
     "Window of last 20 readings. Compute mean, stdev. Flag if val > mean + 2*stdev."),

    (11, "plot-anomalies",
     "Plot anomalies highlighted in red",
     "Same plot as day 4, but mark anomalies as red dots.",
     "plt.scatter for the anomaly points after plt.plot for the line."),

    (12, "multi-sensor",
     "Multi-sensor dataset",
     "Generate temperature + vibration + current. Save as CSV.",
     "Each row: timestamp, temp, vib, current. Useful realistic dataset."),

    (13, "oop-sensor-class",
     "Object-oriented sensor reader",
     "Wrap loading + analysis in a Sensor class with .load() and .stats().",
     "class Sensor: with __init__ taking csv_path. Methods return dicts."),

    (14, "miniproject-2",
     "Mini-project: 3-sensor anomaly detector",
     "Combine days 8-13. CLI tool that takes CSV with 3 sensors, reports anomalies per sensor.",
     "Update README. Add example output. Tag git: `git tag week-2-done`."),

    (15, "rich-cli-1",
     "Pretty CLI output with Rich",
     "Use the `rich` library to print a colored table of sensor stats.",
     "pip install rich. from rich.table import Table. Looks pro instantly."),

    (16, "rich-cli-2",
     "Live dashboard with Rich",
     "Update sensor stats in terminal every 1 second (simulated live).",
     "rich.live.Live + a loop. Looks like real SCADA."),

    (17, "logging",
     "Add proper logging",
     "Replace print() with logging module. Log to file + console.",
     "import logging. logging.basicConfig(level=INFO, filename='app.log')."),

    (18, "config-file",
     "External config (YAML or JSON)",
     "Move thresholds and CSV path to config.json. Load at startup.",
     "json.load(open('config.json')). Keeps code clean."),

    (19, "error-handling",
     "Error handling and validation",
     "Handle: file not found, empty CSV, malformed rows. Don't crash.",
     "try/except. Log errors. Continue with valid data."),

    (20, "type-hints",
     "Add type hints",
     "Annotate all function signatures with types. Run mypy if you want.",
     "def stats(values: list[float]) -> dict[str, float]:"),

    (21, "miniproject-3",
     "Mini-project: production-quality sensor analyzer",
     "Combine days 15-20. Pretty CLI, logging, config, error handling, types.",
     "This is your first 'shippable' tool. README with screenshots."),

    (22, "pytest-intro",
     "First unit tests with pytest",
     "Write 3 tests: test_mean, test_max, test_anomaly_detection.",
     "pip install pytest. tests/test_stats.py. Run: pytest -v."),

    (23, "pytest-fixtures",
     "Test fixtures + edge cases",
     "Use @pytest.fixture for sample data. Test empty list, single value, all same.",
     "Edge cases catch real bugs. This is industrial-grade thinking."),

    (24, "github-actions",
     "CI: run tests on every push (GitHub Actions)",
     "Add .github/workflows/test.yml that runs pytest on every push.",
     "Free CI from GitHub. Green checkmark on every commit."),

    (25, "readme-polish",
     "Polish the README — recruiter view",
     "Add badges (CI, Python version), screenshots, install instructions, example.",
     "shields.io for badges. Pretend a recruiter reads this in 30 seconds."),

    (26, "documentation",
     "Add docstrings + inline docs",
     "Every function gets a docstring. Use Google or NumPy style.",
     "def f(x): \\\"\\\"\\\"Short description.\\n\\nArgs: x: ...\\nReturns: ...\\\"\\\"\\\""),

    (27, "linkedin-post",
     "Write LinkedIn post about week 1-4",
     "Draft a post: 'I committed to coding daily. Here's what I learned in 4 weeks.' Save as posts/week-4-linkedin.md.",
     "3-5 sentences. 1 screenshot. End with a question. Don't post yet — review next week."),

    (28, "level-1-retrospective",
     "Level 1 retrospective + plan Level 2",
     "Write reflections.md: what worked, what didn't, time per day, top 3 learnings. Skim Level 2 roadmap.",
     "End with: 'Day 29 starts Modbus.' Tag: `git tag level-1-complete`. Celebrate small."),
]


def get_task(day_num: int):
    """Return (day, slug, title, description, hints) or None if out of range."""
    for entry in LEVEL_1_TASKS:
        if entry[0] == day_num:
            return entry
    return None


def total_days() -> int:
    return len(LEVEL_1_TASKS)
