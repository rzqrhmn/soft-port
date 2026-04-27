# Day 02 - Read motor temperature CSV

Tanggal: 2026-04-27

## Yang dikerjain

Baca file `shared/sample_temp.csv` (CSV motor temperature 30 baris), terus print setiap row ke terminal.

## Hint kalau buntu

Pakai modul `csv` dari stdlib. Pattern dasarnya:

```python
import csv
with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Path ke CSV-nya pakai `pathlib.Path(__file__).resolve().parent.parent / "shared" / "sample_temp.csv"` biar script jalan dari folder mana aja.

## Catatan saya

(Diisi pas selesai. Boleh satu kalimat aja.)
