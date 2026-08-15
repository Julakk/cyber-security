#!/usr/bin/env python3
"""
Connection Rate Analyzer
Analisis log koneksi (format CSV: timestamp,ip) untuk mendeteksi IP dengan
connection rate mencurigakan — indikasi awal serangan DDoS/flood.

Format log yang diharapkan (CSV, tanpa header):
    2026-08-01T10:00:00,192.168.1.10
    2026-08-01T10:00:01,192.168.1.10
    2026-08-01T10:00:01,10.0.0.5
    ...

Cara pakai:
    python3 connection_rate_analyzer.py connection_log.csv --threshold 20 --window 10
"""
import argparse
import csv
from datetime import datetime
from collections import defaultdict

def parse_log(filepath):
    entries = []
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue
            timestamp_str, ip = row[0].strip(), row[1].strip()
            try:
                timestamp = datetime.fromisoformat(timestamp_str)
            except ValueError:
                continue
            entries.append((timestamp, ip))
    return sorted(entries, key=lambda x: x[0])

def analyze(entries, window_seconds, threshold):
    """
    Sliding window sederhana: untuk tiap entry, hitung berapa banyak koneksi
    dari IP yang sama dalam window_seconds sebelumnya. Kalau melebihi threshold,
    tandai sebagai suspicious.
    """
    ip_timestamps = defaultdict(list)
    suspicious_events = []

    for timestamp, ip in entries:
        ip_timestamps[ip].append(timestamp)
        # buang timestamp yang udah di luar window
        window_start = timestamp.timestamp() - window_seconds
        ip_timestamps[ip] = [t for t in ip_timestamps[ip] if t.timestamp() >= window_start]

        count_in_window = len(ip_timestamps[ip])
        if count_in_window > threshold:
            suspicious_events.append((timestamp, ip, count_in_window))

    return suspicious_events

def summarize(entries, suspicious_events):
    total_connections = len(entries)
    unique_ips = len(set(ip for _, ip in entries))

    # ambil IP unik yang pernah suspicious, beserta count tertinggi yang tercatat
    worst_per_ip = {}
    for timestamp, ip, count in suspicious_events:
        if ip not in worst_per_ip or count > worst_per_ip[ip][1]:
            worst_per_ip[ip] = (timestamp, count)

    return total_connections, unique_ips, worst_per_ip

def main():
    parser = argparse.ArgumentParser(description="Analisis log koneksi untuk deteksi pola DDoS/flood")
    parser.add_argument("logfile", help="Path ke file log CSV (format: timestamp,ip)")
    parser.add_argument("--window", type=int, default=10, help="Ukuran sliding window dalam detik (default: 10)")
    parser.add_argument("--threshold", type=int, default=20, help="Jumlah koneksi dalam window yang dianggap mencurigakan (default: 20)")
    args = parser.parse_args()

    entries = parse_log(args.logfile)
    if not entries:
        print("[!] Tidak ada entry valid yang bisa diparse dari log ini.")
        return

    print(f"[*] {len(entries)} koneksi diparse dari {args.logfile}")
    print(f"[*] Window: {args.window} detik, threshold: {args.threshold} koneksi\n")

    suspicious_events = analyze(entries, args.window, args.threshold)
    total, unique_ips, worst_per_ip = summarize(entries, suspicious_events)

    print(f"[i] Total koneksi: {total}")
    print(f"[i] IP unik: {unique_ips}\n")

    if not worst_per_ip:
        print("[+] Tidak ada IP dengan connection rate mencurigakan yang terdeteksi.")
    else:
        print(f"[!] {len(worst_per_ip)} IP dengan pola mencurigakan terdeteksi:\n")
        # urutkan dari yang paling parah
        for ip, (timestamp, count) in sorted(worst_per_ip.items(), key=lambda x: -x[1][1]):
            print(f"    {ip:20s} -> {count} koneksi dalam {args.window} detik (puncak pada {timestamp.isoformat()})")

    print("\n[i] Ini deteksi pola dasar berbasis rate. Untuk analisis lebih dalam,")
    print("    kombinasikan dengan packet capture (lihat network-security/packet-sniffer/).")

if __name__ == "__main__":
    main()
