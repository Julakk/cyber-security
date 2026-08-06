# Crackme #02 — "Math Transform + Decoy"

**Difficulty**: Medium
**Arsitektur**: x86-64 Linux ELF

## 🎯 Tujuan

Lanjutan dari [`crackme-01`](../crackme-01). Kali ini ada 2 twist tambahan:

1. Password check pakai **transformasi matematika** (bukan XOR simple)
2. Ada **decoy check** (jebakan) — string yang keliatan kayak "password langsung" tapi sebenernya salah arah

## 📂 Isi

- `crackme.c` — Source code (jangan diintip dulu kalau mau latihan!)
- `crackme` — Binary hasil kompilasi
- `build.sh` — Script compile ulang
- `WRITEUP.md` — Solusi lengkap

## 🚀 Cara Coba

```bash
chmod +x crackme
./crackme
```

Hint: `strings` bakal nunjukin sesuatu yang KELIATAN kayak password. Coba itu dulu — terus perhatiin apa yang sebenarnya terjadi. 😉
