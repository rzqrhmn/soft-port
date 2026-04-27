"""
Day 02 — Read motor temperature CSV

Read sample_temp.csv (provided) and print each row.
"""
import csv
from pathlib import Path

# Resolve path relative to THIS script's location, not where user runs python from
CSV_PATH = Path(__file__).resolve().parent.parent / "shared" / "sample_temp.csv"


def main() -> None:
    with open(CSV_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()