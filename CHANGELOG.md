# Changelog

Semua perubahan penting pada repo ini dicatat di file ini.
Format berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Planned
- Writeup CTF kategori Cryptography, OSINT, Binary Exploitation, Forensics (butuh platform publik seperti TryHackMe/HackTheBox)
- Praktik hands-on Active Directory lab

---

## [0.6.0] — Network Recon Checklist, Crackme #02, Kubernetes Security, Full Learning Notes

### Added
- `network-security/RECON-CHECKLIST.md` — alur kerja recon lengkap (passive → active), menghubungkan semua tools network-security yang sudah ada
- `reverse-engineering/crackme-02/` — crackme medium difficulty (math transformation + decoy string), lengkap dengan writeup yang menjelaskan compiler optimization (`add+add` untuk `*3`) dan cara reverse transformasi lewat brute-force
- `cloud-security/kubernetes-basics/README.md` — checklist Docker & Kubernetes security, contoh Dockerfile dan Pod Security Context yang aman vs tidak
- `notes/linux-fundamentals.md` — command & konsep Linux relevan untuk pentest/CTF (SUID, privesc, log analysis)
- `notes/networking-fundamentals.md` — OSI model, TCP/UDP, subnetting, dikaitkan ke tools network-security yang sudah ada
- `notes/python-for-security.md` — rangkuman library & pattern Python yang dipakai di seluruh tools repo ini, termasuk anti-pattern yang harus dihindari
- `notes/digital-forensics.md` — prinsip dasar forensics, chain of custody, kategori forensics, dikaitkan ke tools hashing & static analysis yang sudah ada

### Changed
- `README.md` — roadmap per-kategori diupdate; sisa item yang belum selesai sekarang murni yang butuh aksi langsung dari user (praktik lab, CTF platform publik, sertifikasi)

---

## [0.5.0] — Complete Planned Items

### Added
- `web-security/file-upload/` — vulnerable + fixed upload demo (whitelist ekstensi, magic bytes check, UUID rename), EXPLOIT.md
- `web-security/command-injection/` — vulnerable + fixed ping tool demo (shell=False, input validation), EXPLOIT.md
- `malware-analysis/yara-rules/` — 5 rule contoh, tested terhadap sample file (positive/negative case + ELF binary), `run_yara.py`
- `tools/password-generator/` — secure password generator (`secrets` module) + entropy estimation
- `tools/hash-generator/` — hash generator & checksum verifier, multi-algoritma
- `network-security/dns-lookup/` — DNS reconnaissance tool (A, MX, NS, TXT, CNAME, SOA)

### Changed
- `README.md` — semua item "Planned" di section web-security, network-security, malware-analysis, dan tools dipindah ke "Sudah ada"

---

## [0.4.0] — Reverse Engineering, Active Directory, Cloud Security

### Added
- `reverse-engineering/crackme-01/` — crackme C binary dengan XOR-encoded flag, build script, dan writeup solve lengkap (strings → objdump → decode logic)
- `active-directory/README.md` — notes konsep serangan AD (enumeration, Kerberoasting, Pass-the-Hash, Golden Ticket, AS-REP Roasting) dan prinsip pertahanan
- `cloud-security/s3-misconfig-checklist.md` — checklist kerentanan storage bucket
- `cloud-security/iam_audit.py` — tool audit IAM policy JSON, deteksi wildcard action/resource/principal
- `cloud-security/policy_example_bad.json` & `policy_example_good.json` — contoh policy buat testing tool audit

### Changed
- `README.md` — struktur repo, section tiap kategori, dan roadmap diupdate untuk mencerminkan 3 area baru
- Roadmap: Reverse Engineering, Active Directory, dan Cloud Security dicentang

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
