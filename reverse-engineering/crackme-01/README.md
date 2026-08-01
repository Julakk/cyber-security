# Crackme #01 — "Simple Serial Check"

**Difficulty**: Easy
**Arsitektur**: x86-64 Linux ELF

## 🎯 Tujuan

Cari password yang benar supaya program print pesan sukses + flag. Flag **tidak** disimpan sebagai plaintext di binary (di-XOR dulu), jadi gak bisa langsung ketemu cuma pake `strings` — harus beneran nyari passwordnya dulu.

## 📂 Isi

- `crackme.c` — Source code (buat referensi setelah nyoba solve; jangan diintip dulu kalau mau latihan beneran!)
- `crackme` — Binary hasil kompilasi, siap dianalisis
- `build.sh` — Script buat compile ulang dari source
- `WRITEUP.md` — Solusi lengkap step-by-step

## 🚀 Cara Coba

```bash
chmod +x crackme
./crackme
# masukin password waktu diminta
```

Coba dulu analisis pakai `strings crackme` dan `objdump -d crackme` sebelum baca `WRITEUP.md`. Selamat mencoba! 🕵️
