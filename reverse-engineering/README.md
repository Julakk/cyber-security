# Reverse Engineering

Pengenalan dasar reverse engineering: menganalisis binary/program untuk memahami cara kerjanya tanpa punya source code aslinya.

> ⚠️ Semua binary di sini dibuat sendiri untuk keperluan latihan (crackme). Tidak ada software pihak ketiga yang di-reverse engineer di repo ini.

## 📂 Isi

- [`crackme-01/`](./crackme-01) — Crackme pertama (C binary sederhana), lengkap dengan source code, cara analisis pakai `strings`/`objdump`, dan writeup solve-nya

## 🧰 Tools yang Dipakai

| Tool | Fungsi |
|---|---|
| `strings` | Ekstrak string printable dari binary — sering langsung bocorin flag/logic |
| `objdump -d` | Disassemble binary jadi assembly x86, buat baca logic program |
| `gdb` | Debugger — jalanin program step-by-step, cek register/memory |
| `file` | Identifikasi jenis binary (ELF, PE, arsitektur, dll) |

## 🎯 Alur Belajar

```
1. file <binary>         → kenali jenis & arsitektur binary
2. strings <binary>       → cari clue cepat (kadang flag langsung kebaca)
3. objdump -d <binary>    → baca disassembly, cari logic percabangan (if/else)
4. gdb <binary>            → kalau perlu, jalanin & debug step-by-step
```

Ini level paling dasar (crackme tanpa obfuscation/packing). Reverse engineering malware asli jauh lebih kompleks (ada anti-debug, packing, obfuscation) — itu di luar scope repo edukasi ini.
