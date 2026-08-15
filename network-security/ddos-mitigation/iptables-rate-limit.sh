#!/bin/bash
#
# Contoh rule rate limiting iptables untuk mitigasi DDoS dasar.
# Termasuk rule khusus untuk game server (SA-MP/Open.MP).
#
# ⚠️ CATATAN PENTING:
# - Script ini CONTOH/TEMPLATE, sesuaikan port dan angka limit dengan kebutuhan server kamu.
# - Jalankan dengan sudo/root.
# - Test dulu di environment non-production, rule firewall yang salah bisa mengunci diri sendiri
#   keluar dari server (selalu punya akses console/backup selain SSH sebelum apply rule baru).
# - Rule ini melengkapi (bukan menggantikan) proteksi di level provider/network.
#
# Cara pakai:
#   chmod +x iptables-rate-limit.sh
#   sudo ./iptables-rate-limit.sh

set -e

echo "[*] Menerapkan rule rate limiting dasar..."

# --- 1. Rate limit koneksi baru secara umum (mitigasi SYN flood dasar) ---
# Maksimal 25 koneksi baru per detik per IP ke port 22 (SSH) -- ganti sesuai kebutuhan
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m limit --limit 25/second --limit-burst 50 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j DROP

# --- 2. Rate limit ICMP (mitigasi ping flood) ---
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 10/second --limit-burst 20 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

# --- 3. Drop paket invalid/malformed (sering dipakai di serangan volumetric) ---
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

# --- 4. Batasi SYN flood umum ---
iptables -A INPUT -p tcp --syn -m limit --limit 30/second --limit-burst 60 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP

# --- 5. Rate limit khusus GAME SERVER PORT (SA-MP/Open.MP) ---
# GANTI 7777 dengan port game server kamu yang sebenarnya.
GAME_PORT=7777
iptables -A INPUT -p udp --dport "$GAME_PORT" -m limit --limit 50/second --limit-burst 100 -j ACCEPT
iptables -A INPUT -p udp --dport "$GAME_PORT" -j DROP

# --- 6. Rate limit khusus QUERY PORT (biasanya port game + 1, cek dokumentasi server kamu) ---
QUERY_PORT=7778
iptables -A INPUT -p udp --dport "$QUERY_PORT" -m limit --limit 20/second --limit-burst 40 -j ACCEPT
iptables -A INPUT -p udp --dport "$QUERY_PORT" -j DROP

echo "[*] Rule diterapkan. Cek dengan: sudo iptables -L -n -v"
echo "[!] PENTING: rule ini TIDAK persistent setelah reboot."
echo "    Simpan permanen pakai 'iptables-save' + 'netfilter-persistent',"
echo "    atau tambahkan script ini ke systemd service yang jalan saat boot."
