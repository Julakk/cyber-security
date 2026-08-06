# Networking Fundamentals — Catatan Belajar

Dasar-dasar networking yang relevan buat cybersecurity, jadi fondasi buat semua tools di [`network-security/`](../network-security).

## 🌐 OSI Model (Ringkas)

| Layer | Nama | Contoh Protokol | Relevansi Security |
|---|---|---|---|
| 7 | Application | HTTP, DNS, FTP | Web vulnerabilities (SQLi, XSS, dll) |
| 4 | Transport | TCP, UDP | Port scanning, firewall rules |
| 3 | Network | IP, ICMP | Routing, subnetting, ping |
| 2 | Data Link | Ethernet, ARP | ARP spoofing, MAC filtering |

Sebagian besar tools security (port scanner, packet sniffer di repo ini) beroperasi di layer 3-4 (network/transport), sementara web vulnerability tools beroperasi di layer 7 (application).

## 🔢 TCP vs UDP

- **TCP**: connection-oriented, reliable (ada acknowledgment), dipakai HTTP/HTTPS, SSH, FTP — cocok kalau data harus lengkap & berurutan
- **UDP**: connectionless, lebih cepat tapi gak ada guarantee delivery — dipakai DNS query, streaming, VoIP

**Kenapa penting**: port scanner ([`network-security/port-scanner/`](../network-security/port-scanner)) di repo ini scan TCP karena three-way handshake TCP (`SYN` → `SYN-ACK` → `ACK`) bisa dipakai buat deteksi port terbuka secara reliable.

## 🔀 Subnetting Dasar

```
192.168.1.0/24  -> subnet mask 255.255.255.0 -> 254 usable host (192.168.1.1 - 192.168.1.254)
192.168.1.0/28  -> subnet mask 255.255.255.240 -> 14 usable host
```

Notasi `/24` = 24 bit pertama dipakai buat network address, sisanya (8 bit) buat host address (`2^8 - 2 = 254`, dikurangi network address & broadcast address).

**Kenapa penting**: waktu recon jaringan internal, paham subnetting bantu nentuin range IP yang perlu di-scan (misal `/24` = scan 254 host).

## 📡 Protokol Penting

### DNS
Translate domain name ke IP address. Lihat [`network-security/dns-lookup/`](../network-security/dns-lookup) buat tools query DNS record.

### ARP (Address Resolution Protocol)
Translate IP address ke MAC address di local network. Rentan **ARP spoofing** — attacker kirim ARP reply palsu supaya traffic korban di-redirect lewat mesin attacker (man-in-the-middle).

### ICMP
Dipakai `ping` buat cek konektivitas. Beberapa firewall block ICMP, jadi host bisa "invisible" ke ping scan meski port-nya kebuka — makanya port scanner biasanya pakai TCP connect scan, bukan cuma ping.

## 🔥 Firewall & NAT Dasar

- **Firewall**: filter traffic berdasarkan rule (source/dest IP, port, protokol)
- **NAT (Network Address Translation)**: translate IP private (`192.168.x.x`, `10.x.x.x`) ke IP public — ini kenapa banyak device di jaringan rumah bisa share 1 IP public

## 🎯 Kaitan ke Tools di Repo Ini

| Konsep | Tools Terkait |
|---|---|
| TCP three-way handshake | [`network-security/port-scanner/`](../network-security/port-scanner) |
| DNS record types | [`network-security/dns-lookup/`](../network-security/dns-lookup) |
| Packet capture di layer 2-4 | [`network-security/packet-sniffer/`](../network-security/packet-sniffer) |
| Subnetting buat scope recon | [`network-security/RECON-CHECKLIST.md`](../network-security/RECON-CHECKLIST.md) |

## 📚 Sumber Belajar Lanjutan

- TryHackMe: jalur "Network Fundamentals"
- Buku: "Computer Networking: A Top-Down Approach" (buat yang mau lebih mendalam)
