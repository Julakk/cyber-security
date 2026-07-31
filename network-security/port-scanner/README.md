# Simple Port Scanner

TCP port scanner sederhana pakai Python socket, tanpa dependency eksternal.

> ⚠️ Hanya gunakan untuk scan host milik sendiri atau yang sudah diberi izin eksplisit. Scanning tanpa izin bisa melanggar hukum di banyak negara (termasuk Indonesia — UU ITE).

## 🚀 Cara Pakai

```bash
python scanner.py 127.0.0.1
python scanner.py 127.0.0.1 --ports 1-1000
python scanner.py scanme.nmap.org --ports 20-100 --threads 50
```

## 🛠️ Fitur

- Multi-threaded scanning (cepat untuk range port besar)
- Banner grabbing sederhana (coba baca respons awal dari port terbuka)
- Bisa scan single port, range, atau daftar port spesifik
