# Cloud Security

Pengenalan dasar kerentanan & best practice keamanan di lingkungan cloud (fokus AWS sebagai contoh, konsepnya berlaku umum ke Azure/GCP juga).

## 📂 Isi

- `s3-misconfig-checklist.md` — Checklist kerentanan bucket storage yang paling umum
- `iam_audit.py` — Tool audit sederhana buat cek IAM policy lokal (config file), cari pattern permission yang terlalu longgar

## 🎯 Kenapa Cloud Security Beda dari Security Tradisional

Di infrastruktur on-premise, keamanan banyak ditentukan firewall/network perimeter. Di cloud, kesalahan **konfigurasi** (bukan cuma kerentanan kode) jadi penyebab breach paling umum — misal bucket storage yang ke-expose publik, IAM policy yang kebablasan permission-nya, atau credential yang ke-hardcode di kode/config.

## 🔗 Referensi

- [OWASP Cloud-Native Application Security Top 10](https://owasp.org/www-project-cloud-native-application-security-top-10/)
- AWS Well-Architected Framework — Security Pillar
