#!/usr/bin/env python3
"""
Simple Packet Sniffer menggunakan Scapy.
Untuk keperluan edukasi tentang cara kerja network traffic capture.

⚠️ Hanya jalankan di jaringan milik sendiri. Butuh hak akses root/administrator.
Legalitas: menyadap jaringan orang lain tanpa izin adalah pelanggaran hukum.
"""
import argparse
from datetime import datetime

try:
    from scapy.all import sniff, IP, TCP, UDP, Raw
except ImportError:
    print("[!] Scapy belum terinstall. Jalankan: pip install scapy --break-system-packages")
    exit(1)

def process_packet(packet):
    if not packet.haslayer(IP):
        return

    ip_layer = packet[IP]
    timestamp = datetime.now().strftime("%H:%M:%S")
    proto = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "OTHER"

    src_port = dst_port = "-"
    if packet.haslayer(TCP):
        src_port, dst_port = packet[TCP].sport, packet[TCP].dport
    elif packet.haslayer(UDP):
        src_port, dst_port = packet[UDP].sport, packet[UDP].dport

    line = f"[{timestamp}] {proto} {ip_layer.src}:{src_port} -> {ip_layer.dst}:{dst_port}"

    # Contoh edukasi: highlight plaintext HTTP traffic (port 80) untuk nunjukin
    # kenapa HTTPS penting -- data bisa dibaca siapa saja yang sniff traffic ini.
    if packet.haslayer(Raw) and (dst_port == 80 or src_port == 80):
        payload = packet[Raw].load
        try:
            text = payload.decode(errors="ignore")
            if any(k in text for k in ("HTTP", "GET", "POST", "Host:")):
                line += "  [!] Plaintext HTTP traffic terdeteksi (tidak terenkripsi)"
        except Exception:
            pass

    print(line)

def main():
    parser = argparse.ArgumentParser(description="Simple Packet Sniffer (educational)")
    parser.add_argument("--iface", default=None, help="Network interface (default: semua interface)")
    parser.add_argument("--filter", default="ip", help="BPF filter, misal 'tcp port 80'")
    parser.add_argument("--count", type=int, default=0, help="Jumlah paket ditangkap (0 = tanpa batas)")
    args = parser.parse_args()

    print(f"[*] Mulai sniffing... (filter: '{args.filter}', interface: {args.iface or 'semua'})")
    print("[*] Tekan Ctrl+C untuk berhenti.\n")

    try:
        sniff(iface=args.iface, filter=args.filter, prn=process_packet, count=args.count, store=False)
    except PermissionError:
        print("[!] Butuh hak akses root/administrator untuk capture packet. Coba jalankan dengan 'sudo'.")
    except KeyboardInterrupt:
        print("\n[*] Sniffing dihentikan.")

if __name__ == "__main__":
    main()
