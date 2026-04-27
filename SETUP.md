# SETUP — Baca ini DULU

Setup pertama kali. Ikuti urutannya. Sekali jalan, sisa hari tinggal coding.

Estimasi waktu: **30-45 menit**.

---

## 0. Cek prasyarat (5 menit)

Buka **PowerShell** (Win+X → Terminal / Windows PowerShell), jalankan:

```powershell
python --version    # harus >= 3.9
git --version       # harus muncul versi git
```

Kalau salah satu error / tidak ada:
- **Python**: install dari https://www.python.org/downloads/ → centang "Add Python to PATH"
- **Git**: install dari https://git-scm.com/download/win → next-next-finish (default oke)

Restart PowerShell setelah install, lalu tes lagi.

---

## 1. Konfigurasi Git pertama kali (3 menit)

```powershell
git config --global user.name "Rizqia Rahman"
git config --global user.email "rizqia.rahman@yahoo.com"
git config --global init.defaultBranch main
```

> Catatan: email ini akan **publik** di setiap commit di GitHub. Kalau mau lebih privat, pakai email noreply GitHub (cara: Settings → Emails di GitHub).

---

## 2. Bikin akun GitHub + Personal Access Token (10 menit)

Kalau belum punya:
1. Daftar di https://github.com → pakai username profesional (contoh: `rizqia-rahman`, `rizqia-eng`).
2. Setelah login: **Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token (classic)**.
   - Note: `Soft portfolio laptop`
   - Expiration: 90 days (boleh lebih lama)
   - Scopes: centang `repo` dan `workflow`
3. **Copy token-nya**, simpan di Notepad sementara. Token ini cuma muncul sekali!

---

## 3. Bikin repository di GitHub (3 menit)

1. Di GitHub, klik **+ → New repository**.
2. Repository name: **`soft-portfolio`** (atau bebas, tapi konsisten)
3. Description: `Daily embedded & firmware practice — building public engineering portfolio`
4. **Public** (penting — biar jadi portfolio)
5. Checkbox "Add a README file" → **biarkan kosong / unchecked** (kita sudah punya README sendiri di laptop, kalau dicentang nanti konflik pas push)
   - Checkbox "Add .gitignore" → biarkan kosong juga
   - Checkbox "Choose a license" → biarkan kosong (boleh tambahkan nanti)
6. Klik **Create repository**

---

## 4. Sambungkan folder ini ke GitHub (3 menit)

Buka PowerShell di folder ini:

```powershell
cd C:\Users\rizqi\Desktop\Soft
git init
git add .
git commit -m "Day 0: portfolio scaffolding"
git branch -M main
git remote add origin https://github.com/USERNAME/soft-portfolio.git
git push -u origin main
```

> Ganti `USERNAME` dengan username GitHub kamu.

Pas push pertama, akan minta login:
- Username: username GitHub kamu
- Password: **paste Personal Access Token** dari step 2 (bukan password GitHub)

Cek di GitHub — file-file harusnya sudah muncul.

---

## 5. Install Python deps (2 menit)

```powershell
cd C:\Users\rizqi\Desktop\Soft
python -m pip install -r automation\requirements.txt
```

---

## 6. Tes dulu sebelum scheduling (3 menit)

Coba script-nya jalan manual dulu:

```powershell
python automation\daily_template.py
```

Harusnya muncul folder hari ini di `projects/level-1-foundations/` dengan README + starter file.

```powershell
python automation\update_readme.py
```

Cek `README.md` di root — sudah ke-update otomatis dengan status hari ini.

---

## 7. Setup Windows Task Scheduler (10 menit)

Buka **PowerShell sebagai Administrator** (klik kanan → Run as administrator), lalu:

```powershell
cd C:\Users\rizqi\Desktop\Soft
PowerShell -ExecutionPolicy Bypass -File automation\setup_windows_tasks.ps1
```

Script ini akan setup 3 scheduled task:
- **Soft-Daily-Template** — tiap pagi jam 08:00, generate template hari ini
- **Soft-Hourly-Push** — tiap jam, push commit yang belum naik ke GitHub
- **Soft-Weekly-Report** — tiap Minggu jam 20:00, generate weekly report

Cek hasilnya: buka **Task Scheduler** (Start → ketik "Task Scheduler") → harusnya 3 task itu ada di sana.

---

## 8. Selesai. Daily flow kamu sekarang

Setiap hari:

1. **Jam 08:00** — laptop otomatis bikin folder hari ini di `projects/level-1-foundations/day-XX-...`
2. **Pagi/siang/malam** — buka folder hari itu, baca `README.md`-nya (ada task), kerjain di `main.py`
3. **Sebelum tidur** — buka PowerShell di folder Soft, jalankan:

   ```powershell
   python automation\save.py
   ```

   Script ini commit + push semuanya dengan message yang masuk akal.
4. **Minggu malam** — laptop otomatis bikin weekly report di `reports/`

Setiap commit muncul di GitHub graph → konsistensi nyata, bukan fake.

---

## Troubleshooting cepat

**"git push" minta login terus-terusan** → install GitHub CLI lalu `gh auth login`, atau pakai Git Credential Manager (biasanya sudah ke-install dari Git for Windows).

**Task Scheduler nggak jalan** → cek di Task Scheduler, klik task yang gagal, lihat tab History. Biasanya path Python salah. Edit task-nya, ganti path Python.

**Mau pause beberapa hari (sakit/sibuk)** → di Task Scheduler, klik kanan task → Disable. Aktifkan lagi pas siap.

---

Lanjut baca `ROADMAP.md` buat lihat plan 6 bulan ke depan.
