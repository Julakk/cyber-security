#!/usr/bin/env python3
"""
Simple Web Vulnerability Scanner
Mengecek misconfigurasi umum: security headers, cookie flags, info leakage.

⚠️ Hanya gunakan pada website milik sendiri atau yang sudah diberi izin.
"""
import argparse
import sys

try:
    import requests
except ImportError:
    print("[!] Butuh library requests. Jalankan: pip install requests --break-system-packages")
    sys.exit(1)

SECURITY_HEADERS = {
    "Content-Security-Policy": "Mencegah XSS dengan membatasi sumber script/resource",
    "X-Frame-Options": "Mencegah clickjacking (embed di iframe)",
    "X-Content-Type-Options": "Mencegah MIME-sniffing (harus 'nosniff')",
    "Strict-Transport-Security": "Memaksa koneksi HTTPS (HSTS)",
    "Referrer-Policy": "Mengontrol informasi referrer yang dikirim ke situs lain",
}

def check_headers(response):
    print("\n--- Security Headers ---")
    for header, desc in SECURITY_HEADERS.items():
        if header in response.headers:
            print(f"[+] {header}: {response.headers[header]}")
        else:
            print(f"[-] MISSING: {header}  ({desc})")

def check_cookies(response):
    print("\n--- Cookie Flags ---")
    if not response.cookies:
        print("[i] Tidak ada cookie yang diset pada response ini.")
        return

    for cookie in response.cookies:
        flags = []
        if cookie.has_nonstandard_attr("HttpOnly") or cookie._rest.get("HttpOnly"):
            flags.append("HttpOnly")
        if cookie.secure:
            flags.append("Secure")
        samesite = cookie._rest.get("SameSite")
        if samesite:
            flags.append(f"SameSite={samesite}")

        print(f"[i] Cookie '{cookie.name}': flags = {flags if flags else 'TIDAK ADA'}")
        if "HttpOnly" not in flags:
            print(f"    [-] Tidak ada HttpOnly -> bisa diakses lewat JavaScript (risiko kalau ada XSS)")
        if "Secure" not in flags:
            print(f"    [-] Tidak ada Secure -> bisa terkirim lewat koneksi HTTP biasa (tidak terenkripsi)")

def check_server_info_leak(response):
    print("\n--- Information Disclosure ---")
    server = response.headers.get("Server")
    powered_by = response.headers.get("X-Powered-By")

    if server:
        print(f"[-] Header 'Server' bocor: {server}  (sebaiknya disembunyikan/generic)")
    else:
        print("[+] Header 'Server' tidak bocor versi spesifik.")

    if powered_by:
        print(f"[-] Header 'X-Powered-By' bocor: {powered_by}  (sebaiknya dihapus)")

def check_https_redirect(url):
    print("\n--- HTTPS Redirect ---")
    if url.startswith("https://"):
        http_url = url.replace("https://", "http://", 1)
        try:
            r = requests.get(http_url, timeout=5, allow_redirects=True)
            if r.url.startswith("https://"):
                print(f"[+] HTTP otomatis redirect ke HTTPS.")
            else:
                print(f"[-] HTTP TIDAK redirect ke HTTPS! Final URL: {r.url}")
        except requests.RequestException:
            print("[i] Tidak bisa cek versi HTTP (mungkin port 80 ditutup, itu juga OK).")
    else:
        print("[-] URL yang dites bukan HTTPS.")

def main():
    parser = argparse.ArgumentParser(description="Simple web vulnerability/misconfiguration scanner")
    parser.add_argument("url", help="URL target, misal https://example.com")
    args = parser.parse_args()

    url = args.url if args.url.startswith("http") else f"https://{args.url}"

    print(f"[*] Scanning {url} ...")
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"[!] Gagal mengakses {url}: {e}")
        sys.exit(1)

    print(f"[*] Status code: {response.status_code}")
    check_headers(response)
    check_cookies(response)
    check_server_info_leak(response)
    check_https_redirect(url)

    print("\n[*] Scan selesai.")

if __name__ == "__main__":
    main()
