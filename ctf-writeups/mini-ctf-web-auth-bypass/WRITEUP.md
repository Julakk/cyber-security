# Mini CTF: Login Bypass — Writeup

**Platform**: Self-hosted (dibuat sendiri buat repo ini)
**Kategori**: Web
**Difficulty**: Easy
**Tanggal**: 2026-08-01

## 📝 Deskripsi Challenge

Ada form login sederhana. Password admin di-generate random tiap kali server start (`os.urandom(8).hex()`), jadi mustahil ditebak lewat brute-force biasa. Tujuannya: login sebagai admin **tanpa tahu password aslinya** untuk dapetin flag.

## 🔍 Reconnaissance

Buka source code `challenge.py` (dalam CTF nyata, biasanya kita coba lihat behavior aplikasi dulu lewat black-box testing, tapi karena ini kode sendiri, langsung baca sourcenya).

Bagian pentingnya:

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cur.execute(query)
```

Ini pola **string interpolation langsung ke query SQL** — sinyal kuat kerentanan SQL Injection.

## 🎯 Exploitation

Karena input `username` dan `password` masuk mentah ke query tanpa sanitasi, kita bisa "mematahkan" struktur query dengan payload SQL.

**Payload yang dipakai:**

- Username: `admin' --`
- Password: (boleh diisi apa saja, misal `x`)

**Query yang terbentuk di server:**

```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'x'
```

`--` adalah comment SQL, jadi semua setelah itu diabaikan. Query efektif jadi:

```sql
SELECT * FROM users WHERE username = 'admin'
```

Server ambil row pertama yang username-nya `admin`, tanpa pernah mencocokkan password. Login berhasil sebagai admin.

## 🏁 Flag

```
flag{sql_1nj3ct10n_l0g1n_byp4ss_c0ngr4ts}
```

## 💡 Pelajaran

- Ini variasi dari demo di [`web-security/sql-injection/`](../../web-security/sql-injection) — nunjukin kalau konsep yang sama (SQLi comment-based bypass) berlaku di berbagai konteks, gak cuma satu skenario
- Random password TIDAK melindungi dari SQL Injection — attacker gak perlu tahu password kalau bisa manipulasi query-nya langsung
- Fix-nya sama kayak demo sebelumnya: **parameterized query**
- Pola belajar yang bagus: baca source code (kalau ada akses/whitebox), cari tempat input user masuk ke query/command, cek apakah ada sanitasi

## 🔗 Referensi

- [`web-security/sql-injection/EXPLOIT.md`](../../web-security/sql-injection/EXPLOIT.md) — penjelasan lebih detail tentang SQLi comment-based bypass
