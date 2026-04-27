# Git Cheatsheet — Daily Commands

Cuma 5 perintah ini yang dipakai 95% waktu. Hafalin pelan-pelan.

## Daily flow (yang paling sering)

```powershell
# Lihat file mana saja yang berubah
git status

# Tambahkan SEMUA perubahan ke "staging" (siap di-commit)
git add .

# Commit dengan pesan
git commit -m "Day 5: add CSV reader for motor temp"

# Push ke GitHub
git push
```

> **Shortcut**: pakai script kita — `python automation\save.py "pesan commit"` melakukan semua di atas sekaligus.

---

## Kalau lupa commit beberapa hari

Tetap commit aja, gak masalah. GitHub graph akan tetap show commit di tanggal kamu commit, bukan tanggal kamu coding. Jadi:
- Coding hari Senin tapi commit Kamis → square Kamis yang ijo, bukan Senin.
- **Lesson**: commit setiap hari kerja, walaupun cuma 5 baris.

---

## Beberapa perintah lain yang berguna

```powershell
# Lihat history commit (q untuk keluar)
git log --oneline -20

# Lihat detail commit terakhir
git show

# Batalkan perubahan di file (sebelum di-add)
git checkout -- nama_file.py

# Batalkan add (tapi pertahankan perubahan)
git reset nama_file.py

# Lihat siapa yang edit baris berapa
git blame nama_file.py
```

---

## Branching (skip dulu sampai Level 3)

Belum perlu sampai project mulai banyak. Untuk sekarang: kerja di `main` aja.

---

## Kalau salah commit — JANGAN PANIK

```powershell
# Belum push? Edit pesan commit terakhir:
git commit --amend -m "pesan baru"

# Sudah commit tapi mau batalin (tapi pertahankan perubahan kode):
git reset --soft HEAD~1

# Sudah commit dan mau hapus total perubahan:
git reset --hard HEAD~1   # HATI-HATI: hilang permanen
```

---

## Kalau git push error "rejected"

Artinya ada commit di GitHub yang belum kamu pull. Solusinya:

```powershell
git pull --rebase
git push
```

---

## Naming convention untuk commit message

Pakai format ini di portfolio kita biar konsisten dan terbaca recruiter:

```
Day NN: <kata kerja> <apa yang dikerjakan>

Contoh:
Day 03: add mean/max/min calculation
Day 12: refactor sensor classes for type hints
Day 21: write tests for anomaly detector
Week 5 capstone: complete Modbus RTU parser
```

Kata kerja yang bagus: `add`, `fix`, `refactor`, `document`, `test`, `cleanup`, `complete`.

---

## Yang JANGAN dilakukan

- **Jangan commit password / API key** — kalau terlanjur, ganti password dulu, baru fix git history.
- **Jangan commit file besar (> 50 MB)** — pakai Git LFS atau .gitignore.
- **Jangan force-push** ke main (`git push -f`) — bisa hilang riwayat.
- **Jangan commit `__pycache__`, `.venv`, `.vscode`** — sudah di-ignore di `.gitignore` kita.
