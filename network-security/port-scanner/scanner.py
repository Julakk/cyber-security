#!/usr/bin/env python3
"""
Simple TCP Port Scanner
Untuk keperluan edukasi & audit keamanan pada sistem milik sendiri.

⚠️ Hanya scan host yang kamu miliki atau punya izin eksplisit untuk di-scan.
"""
import socket
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def parse_ports(port_str):
    """Parse '1-1000' atau '22,80,443' jadi list of int."""
    ports = set()
    for part in port_str.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)

def grab_banner(sock):
    try:
        sock.settimeout(1)
        banner = sock.recv(1024).decode(errors="ignore").strip()
        return banner if banner else None
    except Exception:
        return None

def scan_port(target, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            if result == 0:
                banner = grab_banner(sock)
                return (port, True, banner)
    except socket.error:
        pass
    return (port, False, None)

def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("target", help="IP address atau hostname target")
    parser.add_argument("--ports", default="1-1024", help="Range/list port, misal '1-1000' atau '22,80,443'")
    parser.add_argument("--threads", type=int, default=100, help="Jumlah thread paralel")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout per koneksi (detik)")
    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"[!] Tidak bisa resolve hostname: {args.target}")
        sys.exit(1)

    ports = parse_ports(args.ports)
    print(f"[*] Scanning {args.target} ({target_ip}) — {len(ports)} port, {args.threads} threads\n")

    open_ports = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(scan_port, target_ip, p, args.timeout) for p in ports]
        for future in as_completed(futures):
            port, is_open, banner = future.result()
            if is_open:
                open_ports.append(port)
                banner_info = f" — {banner}" if banner else ""
                print(f"[+] Port {port} OPEN{banner_info}")

    print(f"\n[*] Scan selesai. {len(open_ports)} port terbuka: {sorted(open_ports)}")

if __name__ == "__main__":
    main()
