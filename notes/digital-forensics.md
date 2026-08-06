# Digital Forensics — Catatan Belajar

Pengenalan dasar digital forensics: proses mengumpulkan, menganalisis, dan mempresentasikan bukti digital — biasanya dipakai setelah insiden keamanan terjadi (incident response) atau buat keperluan investigasi hukum.

## 🎯 Prinsip Dasar Forensics

1. **Chain of Custody** — dokumentasi lengkap siapa yang pegang bukti, kapan, dan apa yang dilakukan ke bukti itu. Kalau chain of custody putus, bukti bisa dianggap gak valid secara hukum.
2. **Jangan modifikasi bukti asli** — selalu kerja di atas **copy/image** dari bukti asli, bukan data aslinya langsung. Ini kenapa ada istilah "forensic image" — bit-by-bit copy yang exact.
3. **Reproducibility** — proses analisis harus bisa direproduksi orang lain dan menghasilkan kesimpulan yang sama.

## 📂 Kategori Forensics

### 1. Disk Forensics
Analisis storage (HDD/SSD) — recover deleted files, analisis file system, timeline aktivitas file.
- Tools: `Autopsy`, `FTK Imager`, `dd` (buat bikin disk image)

### 2. Memory Forensics
Analisis RAM dump — bisa nemuin proses yang berjalan, koneksi network aktif, bahkan malware yang cuma ada di memory (fileless malware) yang gak ninggalin jejak di disk.
- Tools: `Volatility` (paling populer, open source)

### 3. Network Forensics
Analisis traffic jaringan yang udah di-capture — lihat [`network-security/packet-sniffer/`](../network-security/packet-sniffer) buat konsep dasar packet capture.
- Tools: `Wireshark`, `tcpdump`, `NetworkMiner`

### 4. Log Analysis
Analisis log sistem/aplikasi buat rekonstruksi timeline kejadian — lihat juga [`notes/linux-fundamentals.md`](./linux-fundamentals.md) bagian log & monitoring.

## 🔍 Proses Investigasi Umum (Incident Response)

```
1. Identification    → ada insiden apa? sistem mana yang kena?
2. Preservation       → bikin forensic image, jangan sentuh sistem asli lebih jauh
3. Collection          → kumpulkan log, memory dump, network capture yang relevan
4. Examination          → analisis detail (timeline, artefak, indicator of compromise)
5. Analysis              → hubungkan temuan jadi narasi lengkap kejadian
6. Presentation            → laporan (buat tim internal, manajemen, atau pengadilan)
```

## 🎓 Konsep Terkait dari Repo Ini

- **File hashing** — bukti forensik biasanya di-hash (SHA256) begitu dikumpulkan, buat prove integritasnya gak berubah selama proses investigasi. Lihat [`tools/hash-generator/`](../tools/hash-generator)
- **Static analysis** — analisis file mencurigakan tanpa eksekusi, bagian penting dari forensik malware. Lihat [`malware-analysis/`](../malware-analysis)
- **Log analysis pattern** — sama seperti mencari indicator di [`malware-analysis/static_analysis.py`](../malware-analysis/static_analysis.py) (string matching, pattern), forensik log juga sering pakai pendekatan serupa buat cari IOC (Indicator of Compromise)

## 📚 Sumber Belajar Lanjutan

- TryHackMe: jalur "Digital Forensics and Incident Response (DFIR)"
- SANS FOR508 (kursus, berbayar tapi materinya gold standard buat memory forensics)
- Practice: [CyberDefenders](https://cyberdefenders.org/) — platform CTF khusus blue team/forensics
