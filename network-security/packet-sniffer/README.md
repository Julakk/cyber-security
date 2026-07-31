# Simple Packet Sniffer

Network traffic analyzer sederhana pakai `scapy`, buat belajar cara kerja packet capture.

> ⚠️ Hanya jalankan di jaringan milik sendiri. Menyadap traffic jaringan orang lain tanpa izin melanggar hukum. Butuh hak akses root/administrator untuk capture raw packet.

## 🚀 Cara Pakai

```bash
pip install scapy --break-system-packages
sudo python3 sniffer.py                  # capture semua interface
sudo python3 sniffer.py --iface eth0      # capture interface tertentu
sudo python3 sniffer.py --filter "tcp port 80"   # BPF filter, misal HTTP saja
```

## 🛠️ Fitur

- Menampilkan source/destination IP, protokol, dan port
- Filter BPF (Berkeley Packet Filter) syntax standar
- Highlight paket HTTP (plaintext) sebagai contoh kenapa HTTPS penting
