# CSRF (Cross-Site Request Forgery) Demo

Demo form ganti email yang rentan CSRF, plus versi aman dengan CSRF token.

## 📂 Isi

- `vulnerable_app.py` — Flask app: ganti email tanpa CSRF protection
- `fixed_app.py` — Versi aman dengan CSRF token
- `attacker_page.html` — Contoh halaman jahat yang mengeksploitasi CSRF
- `EXPLOIT.md` — Penjelasan cara kerja serangan

## 🚀 Cara Coba

```bash
pip install flask --break-system-packages
python vulnerable_app.py   # localhost:5002
```

1. Login dulu di `http://localhost:5002` (session otomatis dibuat)
2. Buka `attacker_page.html` di tab baru (simulasi korban mengunjungi web jahat)
3. Email korban otomatis berubah tanpa korban sadar — inilah CSRF

Bandingkan dengan `fixed_app.py` yang menolak request tanpa token CSRF yang valid.
