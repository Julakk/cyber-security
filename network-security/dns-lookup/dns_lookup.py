#!/usr/bin/env python3
"""
DNS Lookup / Reconnaissance Tool
Cek berbagai record type untuk sebuah domain.
"""
import argparse
import socket

try:
    import dns.resolver
    HAS_DNSPYTHON = True
except ImportError:
    HAS_DNSPYTHON = False

RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"]

def lookup_with_dnspython(domain, record_types):
    resolver = dns.resolver.Resolver()
    for rtype in record_types:
        print(f"--- {rtype} ---")
        try:
            answers = resolver.resolve(domain, rtype)
            for rdata in answers:
                print(f"  {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            print("  (tidak ada record)")
        except dns.resolver.NXDOMAIN:
            print(f"  [!] Domain '{domain}' tidak ditemukan (NXDOMAIN)")
            return
        except Exception as e:
            print(f"  [!] Error: {e}")
        print()

def lookup_fallback(domain):
    """Fallback pakai socket kalau dnspython gak ada — cuma bisa A record."""
    print("[i] dnspython tidak terinstall, fallback ke socket (cuma bisa A record)")
    print("--- A ---")
    try:
        ip = socket.gethostbyname(domain)
        print(f"  {ip}")
    except socket.gaierror as e:
        print(f"  [!] Gagal resolve: {e}")

def main():
    parser = argparse.ArgumentParser(description="DNS lookup / reconnaissance tool")
    parser.add_argument("domain", help="Domain target, misal example.com")
    parser.add_argument("--record", choices=RECORD_TYPES, help="Cek 1 record type spesifik saja")
    args = parser.parse_args()

    print(f"[*] DNS lookup untuk: {args.domain}\n")

    if not HAS_DNSPYTHON:
        lookup_fallback(args.domain)
        print("\n[i] Install 'dnspython' untuk cek record type lain (MX, TXT, NS, dll):")
        print("    pip install dnspython --break-system-packages")
        return

    record_types = [args.record] if args.record else RECORD_TYPES
    lookup_with_dnspython(args.domain, record_types)

if __name__ == "__main__":
    main()
