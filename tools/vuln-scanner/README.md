# Simple Web Vulnerability Scanner

Scanner sederhana yang mengecek misconfigurasi umum pada sebuah website: security headers yang hilang, cookie tanpa flag aman, dan informasi server yang bocor.

> ⚠️ Hanya scan website milik sendiri atau yang sudah diberi izin eksplisit untuk di-scan.

## 🚀 Cara Pakai

```bash
pip install requests --break-system-packages
python vuln_scanner.py https://example.com
```

## 🛠️ Yang Dicek

- Security headers: `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Referrer-Policy`
- Cookie flags: `HttpOnly`, `Secure`, `SameSite`
- Server header yang bocor versi (misal `Apache/2.4.41`)
- Apakah situs redirect HTTP → HTTPS
