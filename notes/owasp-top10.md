# Catatan Belajar: OWASP Top 10 (2021)

Ringkasan 10 kerentanan web paling kritis menurut OWASP, dengan contoh di repo ini kalau ada.

## A01: Broken Access Control
User bisa mengakses data/fungsi yang seharusnya tidak boleh diakses (misal ubah `user_id` di URL untuk lihat data user lain).
- **Contoh nyata**: `/api/orders/123` bisa diakses user manapun tanpa cek kepemilikan
- **Fix**: selalu validasi kepemilikan resource di server-side, jangan percaya ID dari client

## A02: Cryptographic Failures
Data sensitif tidak dienkripsi dengan benar (atau tidak dienkripsi sama sekali).
- **Contoh nyata**: password disimpan plaintext atau pakai MD5 tanpa salt
- **Demo di repo ini**: [`tools/password-cracker/hash_demo.py`](../tools/password-cracker/hash_demo.py)
- **Fix**: gunakan bcrypt/argon2 untuk password, TLS untuk data in-transit

## A03: Injection
Input user masuk ke interpreter (SQL, OS command, dll) tanpa sanitasi.
- **Demo di repo ini**: [`web-security/sql-injection/`](../web-security/sql-injection)
- **Fix**: parameterized query, input validation, least privilege

## A04: Insecure Design
Kelemahan yang tertanam di desain arsitektur, bukan sekadar bug implementasi.
- **Contoh**: sistem reset password yang tidak ada rate limiting, jadi bisa di-brute-force

## A05: Security Misconfiguration
Konfigurasi default/salah yang membuka celah — header keamanan tidak diset, debug mode aktif di production, dll.
- **Demo di repo ini**: [`tools/vuln-scanner/`](../tools/vuln-scanner)

## A06: Vulnerable and Outdated Components
Menggunakan library/framework dengan CVE yang sudah diketahui.
- **Fix**: rutin update dependency, pakai tools seperti `npm audit` / `pip-audit` / Dependabot

## A07: Identification and Authentication Failures
Kelemahan di proses login, session management, atau token.
- **Demo di repo ini**: [`web-security/auth-vulnerabilities/`](../web-security/auth-vulnerabilities)

## A08: Software and Data Integrity Failures
Aplikasi mempercayai update/plugin/dependency tanpa verifikasi integritas (misal tidak cek checksum/signature).

## A09: Security Logging and Monitoring Failures
Serangan tidak terdeteksi karena log tidak cukup atau tidak ada monitoring/alert.

## A10: Server-Side Request Forgery (SSRF)
Aplikasi bisa dipaksa membuat request ke lokasi yang tidak diinginkan (misal ke internal network) berdasarkan input user.
- **Contoh nyata**: fitur "fetch URL preview" yang bisa dipakai untuk akses `http://169.254.169.254/` (metadata cloud internal)

---

_Referensi: [owasp.org/Top10](https://owasp.org/Top10/) — catatan ini ditulis ulang dengan kata sendiri untuk keperluan belajar._
