# 🛡️ Cyber Security Portfolio

> A collection of cybersecurity projects, learning notes, tools, and write-ups created for educational and research purposes.

![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 About

Repository ini berisi kumpulan project, catatan belajar, demo keamanan, dan tools sederhana yang dibuat untuk meningkatkan pemahaman di bidang Cyber Security.

Seluruh konten ditujukan **hanya untuk edukasi, penelitian, dan pengujian pada lingkungan yang memiliki izin**.

> ⚠️ **Disclaimer**
>
> Jangan gunakan project atau script dalam repository ini untuk aktivitas ilegal.
> Penulis tidak bertanggung jawab atas penyalahgunaan informasi yang tersedia.

---

## 📂 Repository Structure

```
cyber-security/
│
├── 📁 web-security/
├── 📁 network-security/
├── 📁 malware-analysis/
├── 📁 reverse-engineering/
├── 📁 active-directory/
├── 📁 cloud-security/
├── 📁 tools/
├── 📁 ctf-writeups/
├── 📁 notes/
│
├── CHANGELOG.md
├── LICENSE
└── README.md
```

---

## 🌐 Web Security

Sudah ada (vulnerable + fixed version + penjelasan exploit):
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Broken Authentication (JWT vulnerabilities)
- File Upload Vulnerabilities
- Command Injection

---

## 🌍 Network Security

Sudah ada:
- Port Scanner (multi-threaded, banner grabbing)
- Service Enumeration (banner grab + version-based vuln notes)
- Subdomain Enumeration
- DNS Lookup / Reconnaissance (A, MX, NS, TXT, CNAME, SOA record)
- Packet Sniffer
- Recon Checklist (alur kerja lengkap dari passive sampai active recon)
- DDoS Mitigation (strategi 4 lapis + rate limiting rules + tool deteksi pola flood, termasuk pertimbangan khusus game server SA-MP/Open.MP)

---

## 🦠 Malware Analysis

Sudah ada:
- Static Analysis tool (hashing, string extraction, entropy analysis)
- Notes konsep static vs dynamic analysis
- YARA Rules dasar (pattern matching, tested terhadap sample file)

---

## 🔬 Reverse Engineering

Sudah ada:
- Crackme #01 (C binary, XOR-encoded flag) lengkap dengan writeup solve step-by-step
- Crackme #02 (math transformation + decoy string, medium difficulty) lengkap dengan writeup
- Pengenalan tools: `strings`, `objdump`, `gdb`, `file`

---

## 🏢 Active Directory

Sudah ada:
- Notes konsep serangan AD: enumeration, Kerberoasting, Pass-the-Hash, Golden Ticket, AS-REP Roasting
- Prinsip pertahanan & sumber belajar lanjutan

> Catatan: ini murni conceptual notes karena butuh lab Windows domain controller yang di luar scope environment repo ini. Praktik hands-on direkomendasikan lewat TryHackMe/HackTheBox AD labs.

---

## ☁️ Cloud Security

Sudah ada:
- S3/cloud storage misconfiguration checklist
- IAM policy auditor (deteksi wildcard action/resource/principal yang overly permissive)
- Container/Kubernetes security basics (checklist + contoh konfigurasi aman)

---

## ⚙️ Security Tools

Sudah ada:
- Educational Hash Cracker (dictionary attack + hash speed/salt demo)
- Simple Web Vulnerability Scanner (security headers, cookie flags, info leakage)
- Password Generator (cryptographically secure, entropy estimation)
- Hash Generator & Verifier (text/file, multi-algoritma, checksum verification)

---

## 🏴 CTF Writeups

Sudah ada:
- Web Exploitation (self-hosted mini CTF: SQLi login bypass)

> Catatan: writeup Reverse Engineering ada di folder terpisah [`reverse-engineering/crackme-01/`](./reverse-engineering/crackme-01) karena formatnya crackme, bukan CTF platform biasa.

Planned (kategori yang belum ada writeup-nya):
- Cryptography
- OSINT
- Binary Exploitation
- Forensics

---

## 📚 Learning Notes

Sudah ada:
- OWASP Top 10
- Linux Fundamentals
- Networking Fundamentals
- Python for Security
- Digital Forensics
- Learning Log
- Certification Roadmap

---

## 🎯 Learning Roadmap

### Web Security
- [x] SQL Injection
- [x] Cross-Site Scripting (XSS)
- [x] Cross-Site Request Forgery (CSRF)
- [x] Broken Authentication & Session Management (JWT)
- [x] File Upload Vulnerabilities
- [x] Command Injection

### Network Security
- [x] Port Scanning
- [x] Service Enumeration & Banner Grabbing
- [x] Subdomain Enumeration
- [x] DNS Reconnaissance
- [x] Packet Sniffing
- [x] Network Reconnaissance writeup/checklist
- [x] DDoS Mitigation

### Malware Analysis
- [x] Static Analysis (hashing, entropy, string extraction)
- [x] YARA Rules

### Reverse Engineering
- [x] Crackme dasar (XOR-encoded flag + writeup)
- [x] Crackme tingkat lanjut

### Security Tools
- [x] Password Cracker (edukasi)
- [x] Web Vulnerability Scanner
- [x] Password Generator
- [x] Hash Generator & Verifier

### Active Directory
- [x] Konsep & notes (enumeration, Kerberoasting, Pass-the-Hash, Golden Ticket)
- [ ] Praktik hands-on di lab (TryHackMe/HackTheBox)

### Cloud Security
- [x] S3/Storage Misconfiguration Checklist
- [x] IAM Policy Auditor
- [x] Container/Kubernetes Security Basics

### CTF
- [x] CTF pertama (self-hosted: SQLi login bypass)
- [ ] CTF di platform publik (TryHackMe/HackTheBox) — kategori Cryptography, OSINT, Binary Exploitation, Forensics

### Learning Notes
- [x] OWASP Top 10
- [x] Linux Fundamentals
- [x] Networking Fundamentals
- [x] Python for Security
- [x] Digital Forensics

### Sertifikasi
- [ ] eJPT → lihat rencana lengkap di [`notes/certification-roadmap.md`](./notes/certification-roadmap.md)
- [ ] PNPT / OSCP (jangka panjang)

> Lihat [`CHANGELOG.md`](./CHANGELOG.md) untuk histori lengkap perubahan repo ini.

---

## 🛠️ Technologies

- Python
- C (untuk crackme reverse engineering)
- Flask
- Bash

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

Jika repository ini bermanfaat, jangan lupa berikan ⭐ pada repository ini.

Terima kasih!
