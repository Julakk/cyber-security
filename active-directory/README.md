# Active Directory Security — Catatan Belajar

Pengenalan konsep serangan & pertahanan di lingkungan Active Directory (AD) — infrastruktur yang dipakai hampir semua perusahaan enterprise berbasis Windows untuk manajemen user, komputer, dan permission.

> ℹ️ Topik ini murni konseptual/notes. AD butuh lab Windows Server + domain controller yang gak bisa disimulasikan di environment sandbox Linux biasa. Untuk praktik hands-on, gunakan lab khusus seperti **TryHackMe "Attacktive Directory"** atau **HackTheBox Active Directory labs**.

## 🏢 Konsep Dasar

- **Domain Controller (DC)** — server pusat yang nyimpen semua akun user, komputer, dan policy di jaringan
- **Domain** — kumpulan user/komputer yang dikelola bareng di bawah satu DC
- **Kerberos** — protokol autentikasi default AD (pakai tiket, bukan password langsung dikirim ulang tiap request)
- **Group Policy Object (GPO)** — aturan yang di-push ke semua komputer/user di domain (misal: password policy, software yang diizinkan)

## 🎯 Teknik Serangan Umum (untuk dipahami, bukan untuk dieksekusi tanpa izin)

### 1. Enumeration
Sebelum menyerang, attacker mapping dulu: siapa saja user, grup mana yang admin, komputer apa saja yang ada.
- Tools: `BloodHound` (visualisasi relasi permission), `PowerView`, `ldapsearch`
- Tujuan: cari jalur privilege escalation (misal: user biasa → member grup tertentu → bisa akses DC)

### 2. Kerberoasting
Setiap service account di AD punya "Service Principal Name" (SPN). Attacker yang punya akses user biasa bisa minta tiket Kerberos untuk service account itu, tiketnya di-enkripsi pakai hash password service account tsb — lalu di-**crack offline**.
- Kenapa berbahaya: service account sering punya password lemah/gak pernah diganti, dan permission tinggi
- Mitigasi: password panjang & random untuk service account, monitoring request TGS yang tidak wajar

### 3. Pass-the-Hash (PtH)
Di Windows, autentikasi NTLM bisa pakai **hash password** langsung tanpa perlu tahu plaintext password. Kalau attacker berhasil dapetin hash NTLM (misal dari memory lewat `mimikatz`), dia bisa "pass" hash itu buat auth ke sistem lain tanpa crack password-nya dulu.
- Mitigasi: disable NTLM kalau memungkinkan (pakai Kerberos aja), local admin password unik per mesin (LAPS), network segmentation

### 4. Golden Ticket / Silver Ticket
Kalau attacker berhasil dapetin hash akun `krbtgt` (akun spesial yang nandatangan semua tiket Kerberos di domain), dia bisa bikin tiket Kerberos palsu ("Golden Ticket") yang keliatan valid untuk **akses apapun, kapanpun**, bahkan setelah password direset.
- Ini kenapa kompromi DC itu sangat kritikal — begitu attacker dapet `krbtgt` hash, cleanup-nya harus reset hash itu **dua kali** (bukan cuma sekali)

### 5. AS-REP Roasting
Kalau ada user yang settingan "Do not require Kerberos preauthentication" aktif, attacker bisa minta data terenkripsi user itu **tanpa perlu password sama sekali**, lalu crack offline mirip Kerberoasting.
- Mitigasi: pastikan preauthentication tetap aktif untuk semua user (default-nya emang aktif, cuma sering ke-disable gak sengaja)

## 🛡️ Prinsip Pertahanan Umum

- **Least privilege** — jangan kasih user permission lebih dari yang dibutuhkan
- **Tiering model** — pisahkan akun admin domain dari akun kerja sehari-hari
- **Monitoring & logging** — Kerberoasting/Golden Ticket sering ninggalin jejak log yang bisa dideteksi kalau ada monitoring yang bener
- **Patch & password hygiene** — service account sering jadi titik lemah karena passwordnya jarang diganti

## 📚 Sumber Belajar Lanjutan

- TryHackMe: room "Attacktive Directory", jalur "Active Directory Basics"
- HackTheBox Academy: modul "Active Directory Enumeration & Attacks"
- Tool: BloodHound (untuk visualisasi attack path)

## 🔗 Referensi

- Konsep ini melengkapi [`web-security/auth-vulnerabilities/`](../web-security/auth-vulnerabilities) — sama-sama soal broken authentication, tapi di konteks enterprise Windows environment
