# SQL Injection Demo

Demo login form yang rentan SQL Injection, lengkap dengan penjelasan exploit dan versi yang sudah diperbaiki.

## 📂 Isi

- `vulnerable_app.py` — Flask app dengan query SQL yang rentan (string concatenation langsung)
- `fixed_app.py` — Versi aman menggunakan parameterized query
- `setup_db.py` — Script untuk membuat database SQLite contoh
- `EXPLOIT.md` — Penjelasan cara exploit dan payload yang digunakan

## 🚀 Cara Menjalankan

```bash
pip install flask --break-system-packages
python setup_db.py
python vulnerable_app.py   # jalan di http://localhost:5000
```

Buka `http://localhost:5000`, coba login dengan:
- Username: `admin' --`
- Password: `apa saja`

Lihat `EXPLOIT.md` untuk detail lengkap kenapa ini bisa bypass login.

## 🛡️ Fix

Bandingkan `vulnerable_app.py` dengan `fixed_app.py` — perbedaan utamanya ada di penggunaan **parameterized query** (`?` placeholder) alih-alih string formatting langsung ke query SQL.
