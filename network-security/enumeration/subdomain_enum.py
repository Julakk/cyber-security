#!/usr/bin/env python3
"""
Simple Subdomain Enumeration Tool
Cek subdomain yang aktif berdasarkan wordlist, pakai DNS resolution.

⚠️ Hanya gunakan pada domain milik sendiri atau yang sudah diberi izin eksplisit.
"""
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_subdomain(subdomain, domain):
    full_domain = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        return (full_domain, ip)
    except socket.gaierror:
        return None

def main():
    parser = argparse.ArgumentParser(description="Simple subdomain enumeration")
    parser.add_argument("domain", help="Domain target, misal example.com")
    parser.add_argument("--wordlist", default="subdomains_sample.txt", help="Path wordlist subdomain")
    parser.add_argument("--threads", type=int, default=30, help="Jumlah thread paralel")
    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        subdomains = [line.strip() for line in f if line.strip()]

    print(f"[*] Mencoba {len(subdomains)} subdomain untuk {args.domain}\n")

    found = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(check_subdomain, sub, args.domain) for sub in subdomains]
        for future in as_completed(futures):
            result = future.result()
            if result:
                full_domain, ip = result
                found.append(full_domain)
                print(f"[+] {full_domain} -> {ip}")

    print(f"\n[*] Selesai. {len(found)} subdomain aktif ditemukan.")

if __name__ == "__main__":
    main()
