# File Upload Vulnerability Demo

Demo fitur upload file yang rentan — user bisa upload file berbahaya (misal script `.py`/`.php`) yang nantinya bisa dieksekusi di server. Plus versi yang aman.

> ⚠️ Jalankan hanya di localhost/sandbox sendiri.

## 📂 Isi

- `vulnerable_app.py` — Upload tanpa validasi tipe file/isi file
- `fixed_app.py` — Upload dengan validasi ekstensi, MIME type, ukuran, dan rename file
- `EXPLOIT.md` — Penjelasan skenario serangan

## 🚀 Cara Coba

```bash
pip install flask --break-system-packages
python vulnerable_app.py   # localhost:5006
```

Coba upload file dengan ekstensi `.py` yang isinya kode Python — di versi vulnerable, file akan tersimpan apa adanya di folder `uploads/` tanpa validasi.
