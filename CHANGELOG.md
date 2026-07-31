# Changelog

Semua perubahan penting pada repo ini dicatat di file ini.
Format berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Planned
- File Upload & Command Injection demo (`web-security/`)
- YARA Rules dasar (`malware-analysis/`)
- Password Generator & standalone Hash Generator (`tools/`)
- Writeup CTF kategori Reverse Engineering, Cryptography, OSINT, Binary Exploitation, Forensics
- Notes: Linux, Networking, Python, Active Directory, Reverse Engineering, Digital Forensics

---

## [0.3.0] — Certification Roadmap

### Added
- `notes/certification-roadmap.md` — rencana sertifikasi (eJPT sebagai prioritas pertama, Security+ opsional, OSCP jangka panjang, CEH dilewati dulu) lengkap dengan rencana persiapan dan sumber belajar
- Update `README.md`: link ke roadmap sertifikasi

---

## [0.2.0] — Network Enumeration, Malware Analysis, First CTF

### Added
- `network-security/enumeration/service_enum.py` — banner grabbing + catatan kerentanan berbasis versi servis
- `network-security/enumeration/subdomain_enum.py` — subdomain enumeration via DNS resolution
- `malware-analysis/static_analysis.py` — static analysis tool (hashing, entropy, string extraction, indicator matching)
- `malware-analysis/sample_harmless.py` + `NOTES.md` — sample file demo + konsep static vs dynamic analysis
- `ctf-writeups/mini-ctf-web-auth-bypass/` — CTF pertama: self-hosted SQL injection login bypass challenge + writeup lengkap

### Changed
- `README.md` — roadmap diupdate (network scanning & enumeration, CTF pertama, malware analysis dasar dicentang)
- `ctf-writeups/README.md` — tabel daftar writeup diupdate

---

## [0.1.0] — Initial Portfolio

### Added
- `web-security/sql-injection/` — vulnerable + fixed Flask app, penjelasan exploit
- `web-security/xss/` — vulnerable + fixed HTML demo, penjelasan exploit
- `web-security/csrf/` — vulnerable + fixed Flask app, contoh attacker page, penjelasan exploit
- `web-security/auth-vulnerabilities/` — vulnerable + fixed JWT implementation, penjelasan exploit
- `network-security/port-scanner/` — multi-threaded TCP port scanner
- `network-security/packet-sniffer/` — packet sniffer berbasis scapy
- `tools/password-cracker/` — dictionary attack tool + demo MD5/SHA vs bcrypt
- `tools/vuln-scanner/` — scanner misconfigurasi (security headers, cookie flags, info leakage)
- `ctf-writeups/example-writeup/` — template writeup
- `notes/owasp-top10.md` — catatan OWASP Top 10 dengan referensi ke demo di repo
- `notes/learning-log.md` — template log belajar
- `README.md`, `.gitignore`, `LICENSE` (MIT)
