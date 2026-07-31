#!/usr/bin/env python3
"""
Service Enumeration Tool
Ambil banner/versi dari servis umum (HTTP, SSH, FTP) dan kasih catatan
kerentanan yang relevan berdasarkan versi (untuk edukasi, bukan database CVE lengkap).

⚠️ Hanya gunakan pada host milik sendiri atau yang sudah diberi izin eksplisit.
"""
import socket
import argparse
import re

try:
    import requests
except ImportError:
    requests = None

# Catatan edukasi: contoh kerentanan versi lama yang terkenal (bukan daftar CVE lengkap,
# cuma buat nunjukin KONSEP kenapa versi servis penting diketahui)
KNOWN_ISSUES = {
    "vsftpd 2.3.4": "Punya backdoor terkenal (CVE-2011-2523) di versi ini.",
    "OpenSSH 7.2": "Ada beberapa CVE user enumeration timing attack di versi lama.",
    "Apache/2.4.49": "Rentan path traversal / RCE (CVE-2021-41773) jika belum di-patch.",
}

def check_known_issues(banner):
    for sig, note in KNOWN_ISSUES.items():
        if sig.lower() in banner.lower():
            return note
    return None

def grab_banner(target, port, timeout=2.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((target, port))
            try:
                banner = s.recv(1024).decode(errors="ignore").strip()
            except socket.timeout:
                banner = ""
            return banner
    except Exception:
        return None

def enum_http(target, port, timeout=2.0):
    scheme = "https" if port == 443 else "http"
    url = f"{scheme}://{target}:{port}"
    if requests is None:
        return "requests belum terinstall, skip enum HTTP detail"
    try:
        r = requests.get(url, timeout=timeout, verify=False)
        server = r.headers.get("Server", "tidak diketahui")
        powered_by = r.headers.get("X-Powered-By", "")
        info = f"Server: {server}"
        if powered_by:
            info += f", X-Powered-By: {powered_by}"
        return info
    except Exception as e:
        return f"Gagal request HTTP: {e}"

def main():
    parser = argparse.ArgumentParser(description="Simple service enumeration tool")
    parser.add_argument("target", help="IP/hostname target")
    parser.add_argument("--ports", default="21,22,80,443", help="Daftar port dipisah koma")
    args = parser.parse_args()

    ports = [int(p.strip()) for p in args.ports.split(",")]
    target_ip = socket.gethostbyname(args.target)

    print(f"[*] Enumerasi servis di {args.target} ({target_ip})\n")

    for port in ports:
        print(f"--- Port {port} ---")
        if port in (80, 443):
            info = enum_http(target_ip, port)
            print(f"[i] {info}")
        else:
            banner = grab_banner(target_ip, port)
            if banner is None:
                print("[-] Tidak bisa konek (port kemungkinan tertutup)")
                continue
            print(f"[i] Banner: {banner if banner else '(kosong)'}")

            note = check_known_issues(banner)
            if note:
                print(f"[!] Catatan: {note}")
        print()

if __name__ == "__main__":
    main()
