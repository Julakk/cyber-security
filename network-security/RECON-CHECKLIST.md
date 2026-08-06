# Network Reconnaissance Checklist

Alur kerja sistematis buat fase recon di pentest/CTF kategori network — nyambungin semua tools yang udah ada di [`network-security/`](.).

> ⚠️ Hanya lakukan di target milik sendiri atau yang sudah diberi izin eksplisit.

## 📋 Alur Recon Lengkap

### 1. Passive Recon (tanpa nyentuh target langsung)

- [ ] **WHOIS lookup** — cari info registrasi domain (pemilik, tanggal registrasi, nameserver)
- [ ] **DNS reconnaissance** — cek record A, MX, NS, TXT, SOA
  ```bash
  python3 dns-lookup/dns_lookup.py target.com
  ```
- [ ] **Subdomain enumeration** — cari subdomain yang mungkin punya attack surface lebih luas
  ```bash
  python3 enumeration/subdomain_enum.py target.com --wordlist enumeration/subdomains_sample.txt
  ```
- [ ] **Search engine recon (Google dorking)** — cari file/halaman yang gak sengaja ke-index (`site:target.com filetype:pdf`, dll)
- [ ] **Certificate transparency logs** — cek [crt.sh](https://crt.sh) buat nemu subdomain dari histori SSL certificate

### 2. Active Recon (mulai nyentuh target — pastikan udah ada izin)

- [ ] **Port scanning** — cari port/servis yang terbuka
  ```bash
  python3 port-scanner/scanner.py target_ip --ports 1-1000
  ```
- [ ] **Service enumeration** — identifikasi versi servis di port yang terbuka
  ```bash
  python3 enumeration/service_enum.py target_ip --ports 21,22,80,443
  ```
- [ ] **Banner grabbing** — udah otomatis kebawa di step port scanning & service enum di atas
- [ ] **Web technology fingerprinting** — cek header response, cari clue framework/CMS yang dipakai (lihat juga [`tools/vuln-scanner/`](../tools/vuln-scanner))

### 3. Dokumentasi Temuan

Format catatan yang disarankan buat tiap target:

```
Target: target.com (IP: x.x.x.x)
Subdomain aktif: [daftar]
Port terbuka: [daftar + versi servis]
DNS records penting: [MX, TXT, dll]
Potential attack surface: [catatan awal, misal "port 21 FTP versi lama" dll]
```

## 🎯 Kenapa Urutan Ini Penting

Passive recon dilakukan dulu karena **tidak meninggalkan jejak di sisi target** — semua informasi didapat dari sumber pihak ketiga (DNS registrar, search engine, certificate log). Active recon baru dilakukan setelah punya gambaran awal, karena ini **langsung berinteraksi dengan sistem target** dan bisa terdeteksi oleh IDS/monitoring mereka.

## 🔗 Tools Terkait di Repo Ini

| Tools | Lokasi |
|---|---|
| Port scanner | [`port-scanner/`](./port-scanner) |
| Service & subdomain enum | [`enumeration/`](./enumeration) |
| DNS lookup | [`dns-lookup/`](./dns-lookup) |
| Packet sniffer (buat analisis traffic pas testing) | [`packet-sniffer/`](./packet-sniffer) |
