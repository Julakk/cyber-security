# Command Injection Demo

Demo fitur "ping host" yang rentan Command Injection — input user masuk ke shell command tanpa sanitasi. Plus versi aman.

> ⚠️ Jalankan hanya di localhost/sandbox sendiri.

## 📂 Isi

- `vulnerable_app.py` — Fitur ping yang jalanin shell command langsung dari input user
- `fixed_app.py` — Versi aman tanpa shell, pakai validasi input ketat
- `EXPLOIT.md` — Penjelasan payload

## 🚀 Cara Coba

```bash
pip install flask --break-system-packages
python vulnerable_app.py   # localhost:5008
```

Coba masukkan host: `127.0.0.1; whoami` — command tambahan `whoami` akan ikut ke-eksekusi di server.
