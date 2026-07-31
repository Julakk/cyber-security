# Service Enumeration

Lanjutan dari port scanner — begitu port terbuka ketemu, langkah berikutnya adalah **enumeration**: cari tahu servis apa, versi berapa, dan kemungkinan kerentanan apa yang relevan.

> ⚠️ Hanya gunakan pada host milik sendiri atau yang sudah diberi izin eksplisit.

## 📂 Isi

- `service_enum.py` — Enumerasi servis umum (HTTP, SSH, FTP) + cek versi & saran kerentanan yang relevan
- `subdomain_enum.py` — Subdomain enumeration sederhana pakai wordlist + DNS resolution

## 🚀 Cara Pakai

```bash
pip install requests --break-system-packages

# Enumerasi servis di target (pakai hasil port scanner sebelumnya)
python3 service_enum.py 127.0.0.1 --ports 21,22,80,443

# Enumerasi subdomain
python3 subdomain_enum.py example.com --wordlist subdomains_sample.txt
```

## 🎯 Alur Kerja Tipikal (Recon Workflow)

```
1. Port scan          → network-security/port-scanner/scanner.py
2. Service enum        → network-security/enumeration/service_enum.py
3. Vuln check spesifik → cari CVE sesuai versi servis yang ketemu
4. Exploitation        → sesuai kerentanan yang ditemukan
```

Ini alur dasar yang dipakai di hampir semua CTF kategori network/pentest.
