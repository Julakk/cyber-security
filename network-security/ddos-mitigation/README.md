# DDoS Mitigation

Strategi & tools untuk mendeteksi dan mengurangi dampak serangan DDoS (Distributed Denial of Service) — termasuk pertimbangan khusus untuk **game server** (SA-MP/Open.MP), bukan cuma web server biasa.

> ⚠️ Konten ini fokus ke **defensive/mitigasi**, bukan cara menyerang. Melakukan DDoS ke sistem yang bukan milik sendiri atau tanpa izin adalah tindak pidana (di Indonesia diatur di UU ITE).

## 📂 Isi

- `iptables-rate-limit.sh` — Contoh rule rate limiting di level firewall (Linux `iptables`), termasuk rule khusus untuk port game server
- `connection_rate_analyzer.py` — Tool analisis log koneksi untuk deteksi pola serangan (IP mana yang connection rate-nya mencurigakan)
- `sample_connection_log.csv` — Contoh log (traffic normal + 1 IP yang melakukan flood) untuk testing tool di atas

---

## 🎯 Jenis-Jenis Serangan DDoS

| Layer | Tipe | Contoh |
|---|---|---|
| Network (L3/L4) | Volumetric | UDP flood, ICMP flood, amplification (DNS/NTP reflection) |
| Network (L3/L4) | Protocol attack | SYN flood, ACK flood |
| Application (L7) | App-layer | HTTP flood, Slowloris, query flood ke database |
| Game-specific | Query/packet flood | Flood ke port query SA-MP/Open.MP, fake player connect |

---

## 🛡️ Strategi Mitigasi (4 Lapis)

### 1. Network-level Protection

Filter traffic sebelum sampai ke server — paling efektif untuk volumetric attack.

- **DDoS protection provider** (Cloudflare Spectrum, OVH Anti-DDoS, atau provider lokal) — untuk game server, pastikan provider-nya support UDP/custom protocol, karena banyak provider anti-DDoS cuma fokus HTTP/HTTPS
- **Rate limiting di firewall** (`iptables`/`nftables`) — batasi jumlah koneksi per IP per detik, lihat contoh di [`iptables-rate-limit.sh`](./iptables-rate-limit.sh)
- **Blackhole routing** — buang traffic dari IP/subnet yang jelas-jelas attacker di level routing, sebelum masuk ke server sama sekali
- **Anycast network** (kalau budget memungkinkan) — sebar traffic ke banyak lokasi server, jadi attacker harus membagi kekuatan serangannya

### 2. Application-level Protection

Lindungi layer aplikasi dari flood yang lolos dari filter network.

- **Connection rate limiting per IP di level aplikasi** — jangan cuma andalkan firewall, aplikasi sendiri juga perlu validasi
- **Validasi packet/query sebelum diproses** — reject packet yang malformed secepat mungkin, sebelum masuk logic yang berat
- **Timeout agresif** untuk koneksi yang gak menyelesaikan handshake (mitigasi SYN flood / slow connection attack)
- **Load balancer** di depan server untuk distribusi beban

### 3. Server & Infrastructure Hardening

Persiapan supaya server tahan banting kalau kena serangan.

- **Pisahkan panel admin dari game server** — kalau panel dan game server jadi satu titik gagal, serangan ke salah satunya bisa melumpuhkan keduanya
- **Monitoring bandwidth real-time**, set alert kalau traffic naik drastis dari baseline normal
- **Auto-scaling / failover** ke server backup kalau memungkinkan
- **Backup config** biar bisa cepat restore kalau server down/perlu rebuild

### 4. Incident Response (saat sedang diserang)

- Identifikasi pola serangan dulu — cek log, capture traffic (lihat [`network-security/packet-sniffer/`](../packet-sniffer)), atau analisis pakai [`connection_rate_analyzer.py`](./connection_rate_analyzer.py)
- Aktifkan rate limiting lebih ketat sementara
- Kontak provider/upstream untuk null-route kalau serangan volumetric-nya besar (di luar kapasitas mitigasi sendiri)
- Dokumentasikan buat post-mortem — update rule mitigasi berdasarkan pola serangan yang benar-benar terjadi

---

## 🎮 Pertimbangan Khusus: SA-MP / Open.MP Game Server

Game server beda dari web server biasa — ada beberapa hal spesifik yang perlu diperhatikan:

### Query Port Flood

SA-MP/Open.MP punya **query protocol** terpisah dari port game utama, yang sering jadi target flood karena biasanya kurang diperhatikan proteksinya dibanding port utama.

### Fake Player Connect Flood

Attacker bisa spam fake connection request buat menghabiskan resource server (CPU/memory buat proses tiap "pemain" palsu yang connect). Mitigasi:
- Connection queue dengan limit
- Verifikasi/handshake sebelum benar-benar assign slot player

### Contoh Rate Limiting untuk Port Game (iptables)

```bash
# Batasi 50 paket/detik per IP ke port game (ganti 7777 sesuai port server kamu)
iptables -A INPUT -p udp --dport 7777 -m limit --limit 50/s --limit-burst 100 -j ACCEPT
iptables -A INPUT -p udp --dport 7777 -j DROP
```

Lihat [`iptables-rate-limit.sh`](./iptables-rate-limit.sh) untuk contoh lebih lengkap termasuk port query terpisah.

### Arsitektur yang Disarankan

Kalau panel admin/monitoring dan game server ada di VPS terpisah (seperti kasus DDoS protection panel yang sempat dikerjakan), pastikan:
- Komunikasi antar VPS pakai koneksi terenkripsi (VPN/SSH tunnel), bukan expose API langsung ke publik
- Rate limiting diterapkan di **kedua sisi** (panel dan game server), bukan cuma salah satu

---

## 🚀 Cara Coba Tool Analisis Log

```bash
python3 connection_rate_analyzer.py sample_connection_log.csv --threshold 20 --window 10
```

Sample log ini berisi traffic normal dari 4 IP + 1 IP yang melakukan flood (50 koneksi dalam beberapa detik) — tool akan otomatis mendeteksi IP yang mencurigakan.

---

## 📚 Sumber Belajar Lanjutan

- Cloudflare Learning Center — [What is a DDoS attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) (penjelasan konsep dari salah satu provider mitigasi terbesar)
- OWASP — [Denial of Service Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html)

## 🔗 Referensi Terkait di Repo Ini

- [`network-security/packet-sniffer/`](../packet-sniffer) — buat capture & analisis traffic mencurigakan
- [`network-security/RECON-CHECKLIST.md`](../RECON-CHECKLIST.md) — konteks recon yang relevan sebelum insiden terjadi
