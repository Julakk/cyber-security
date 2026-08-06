# Linux Fundamentals — Catatan Belajar

Dasar-dasar Linux yang relevan buat kerjaan cybersecurity — bukan tutorial Linux umum, tapi fokus ke command dan konsep yang sering kepake di pentest/CTF/administrasi sistem aman.

## 📁 Filesystem & Permission

```bash
ls -la                  # lihat permission, owner, hidden files
chmod 750 file           # ubah permission (owner: rwx, group: r-x, other: none)
chown user:group file    # ubah owner/group
find / -perm -4000 2>/dev/null   # cari file dengan SUID bit aktif (potensi privesc)
```

**Kenapa penting**: SUID/SGID binary yang salah konfigurasi adalah salah satu vektor privilege escalation paling umum di CTF/pentest Linux.

## 👤 User & Process Management

```bash
whoami                   # user saat ini
id                        # UID, GID, grup yang diikuti
sudo -l                   # cek command apa yang bisa dijalankan sebagai user lain (privesc vector)
ps aux                    # lihat semua proses yang jalan
netstat -tulnp             # port yang listening + proses yang punya (butuh sudo biasanya)
```

## 🔍 Log & Monitoring

```bash
tail -f /var/log/auth.log      # monitor log autentikasi real-time (Debian/Ubuntu)
journalctl -u nama-service      # log service tertentu (systemd)
last                              # histori login user
```

**Kenapa penting**: analisis log adalah skill inti buat incident response & forensics — tahu di mana log penting disimpan itu langkah pertama.

## 🔐 Permission & Privilege Escalation Basics

Konsep dasar yang sering muncul di CTF Linux privesc:

1. **SUID binaries** — cari binary dengan SUID bit yang bisa dieksploitasi (lihat [GTFOBins](https://gtfobins.github.io/) buat daftar binary yang punya "shell escape" kalau dijalankan dengan privilege tertentu)
2. **Sudo misconfiguration** — `sudo -l` nunjukin command apa yang bisa dijalankan tanpa password, kadang bisa dieksploitasi buat dapat shell root
3. **Cron jobs** — script yang dijalankan otomatis (biasanya sebagai root) kadang punya permission salah, bisa di-modify user biasa
4. **Kernel exploits** — kernel versi lama kadang punya CVE privilege escalation yang public exploit-nya

## 🛠️ Command yang Sering Dipakai di CTF/Pentest

| Command | Fungsi |
|---|---|
| `grep -r "password" /var/www` | Cari string sensitif di codebase |
| `find / -name "*.conf" 2>/dev/null` | Cari file konfigurasi |
| `history` | Lihat command history user (kadang ada credential ketinggalan) |
| `crontab -l` | Lihat scheduled task user saat ini |
| `env` | Lihat environment variable (kadang ada secret ketinggalan) |

## 🔗 Referensi

- Konsep ini relevan buat [`ctf-writeups/`](../ctf-writeups) — banyak CTF Linux privesc pakai teknik-teknik di atas
- [GTFOBins](https://gtfobins.github.io/) — database teknik privilege escalation lewat Unix binary
