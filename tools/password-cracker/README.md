# Educational Hash Cracker

Dictionary attack sederhana untuk belajar kenapa password lemah berbahaya, dan kenapa hashing yang benar (bcrypt/argon2) itu penting.

> ⚠️ Hanya gunakan pada hash milik sendiri untuk keperluan belajar (misal cek kekuatan password sendiri). Jangan gunakan untuk membobol akun orang lain.

## 📂 Isi

- `cracker.py` — Dictionary attack terhadap hash MD5/SHA1/SHA256
- `wordlist_sample.txt` — Contoh wordlist kecil (password umum)
- `hash_demo.py` — Demo kenapa MD5/SHA polos rentan, dan kenapa bcrypt lebih aman

## 🚀 Cara Pakai

```bash
python cracker.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --algo md5 --wordlist wordlist_sample.txt
```

## 🎓 Pelajaran Utama

MD5/SHA1/SHA256 itu **cepat** — dirancang untuk checksum/integrity, bukan password hashing. Ini artinya attacker bisa coba jutaan kombinasi per detik (brute-force). Password hashing yang benar (bcrypt, scrypt, argon2) sengaja dibuat **lambat** dan pakai **salt**, supaya brute-force jadi tidak praktis.
