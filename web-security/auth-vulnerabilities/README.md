# Broken Authentication Demo

Demo beberapa kesalahan umum dalam implementasi autentikasi JWT/session, plus versi yang diperbaiki.

## 📂 Isi

- `vulnerable_jwt.py` — JWT dengan kesalahan umum (alg:none bypass, secret lemah, no expiry)
- `fixed_jwt.py` — JWT yang aman (algoritma dipaksa, secret kuat, expiry, refresh token)
- `EXPLOIT.md` — Penjelasan tiap kerentanan dan cara exploitnya

## 🎯 Kerentanan yang didemokan

1. **Algorithm confusion / `alg: none`** — token dipalsukan tanpa signature
2. **Weak secret** — secret JWT bisa di-brute-force
3. **No expiry** — token berlaku selamanya walau sudah logout
4. **Sensitive data di payload** — password/data sensitif ikut ditaruh di JWT (yang cuma base64, bukan enkripsi!)

## 🚀 Cara Coba

```bash
pip install pyjwt flask --break-system-packages
python vulnerable_jwt.py
```

Lihat `EXPLOIT.md` untuk payload exploit tiap kerentanan.
