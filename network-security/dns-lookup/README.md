# DNS Lookup Tool

Tool DNS reconnaissance dasar — cek berbagai record type (A, MX, NS, TXT, CNAME) buat domain target. Langkah awal yang umum di fase recon pentest/CTF.

## 🚀 Cara Pakai

```bash
pip install dnspython --break-system-packages
python3 dns_lookup.py example.com
python3 dns_lookup.py example.com --record MX
```

## 🎓 Kenapa DNS Recon Penting

- **A/AAAA record** — IP address asli di balik domain (kadang beda dari yang di-serve CDN)
- **MX record** — server email, bisa kasih clue provider email yang dipakai (relevan buat phishing simulation/assessment)
- **TXT record** — sering berisi info verifikasi (SPF, DKIM, verifikasi Google/lainnya) — kadang bocorin info infrastruktur
- **NS record** — siapa yang jadi authoritative DNS server, bisa nunjukin provider hosting/DNS yang dipakai
