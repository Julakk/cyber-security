# Cyber Security Portfolio

Kumpulan demo, tools, dan catatan belajar seputar cybersecurity — fokus di web security, network security, dan defensive tooling. Semua demo dibuat untuk tujuan edukasi dan dijalankan di environment lokal/sandbox sendiri.

> ⚠️ **Disclaimer**: Semua kode di repo ini dibuat untuk keperluan belajar dan riset keamanan. Jangan digunakan untuk menyerang sistem yang bukan milik sendiri atau tanpa izin. Penulis tidak bertanggung jawab atas penyalahgunaan.

## 📁 Struktur

| Folder | Isi |
|---|---|
| [`web-security/`](./web-security) | Demo kerentanan web (SQLi, XSS, CSRF, broken auth) lengkap dengan versi vulnerable & fixed |
| [`network-security/`](./network-security) | Port scanner, service/subdomain enumeration |
| [`tools/`](./tools) | Tools security umum (password cracker edukasi, vuln scanner sederhana) |
| [`malware-analysis/`](./malware-analysis) | Konsep static analysis (hashing, entropy, string extraction) |
| [`ctf-writeups/`](./ctf-writeups) | Dokumentasi penyelesaian CTF / lab hacking |
| [`notes/`](./notes) | Catatan belajar (OWASP Top 10, learning log, roadmap sertifikasi) |

## 🎯 Roadmap Belajar

- [x] Dasar web vulnerabilities (SQLi, XSS, CSRF)
- [x] Broken authentication & session management
- [x] Network scanning & enumeration
- [x] CTF pertama (self-hosted mini CTF)
- [x] Malware analysis dasar
- [ ] Sertifikasi — lihat rencana lengkap di [`notes/certification-roadmap.md`](./notes/certification-roadmap.md) (target: eJPT dulu, lalu OSCP jangka panjang)

## 🛠️ Tech yang dipakai

Python, Node.js, Flask/Express (untuk demo vulnerable app), Bash.

## 📬 Kontak

Punya masukan atau nemu bug di salah satu demo? Buka issue atau PR.
