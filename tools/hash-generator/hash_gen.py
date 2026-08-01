#!/usr/bin/env python3
"""
Hash Generator & Verifier
Generate hash dari text/file, dan verifikasi checksum.
"""
import argparse
import hashlib
import sys

ALGORITHMS = ["md5", "sha1", "sha256", "sha512"]

def hash_text(text, algo):
    h = hashlib.new(algo)
    h.update(text.encode())
    return h.hexdigest()

def hash_file(filepath, algo, chunk_size=8192):
    h = hashlib.new(algo)
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(chunk_size):
                h.update(chunk)
    except FileNotFoundError:
        print(f"[!] File tidak ditemukan: {filepath}")
        sys.exit(1)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Hash generator & verifier")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Teks yang mau di-hash")
    group.add_argument("--file", help="Path file yang mau di-hash")
    parser.add_argument("--algo", choices=ALGORITHMS, help="Algoritma spesifik (default: tampilkan semua)")
    parser.add_argument("--verify", help="Hash yang diharapkan, buat verifikasi checksum")
    args = parser.parse_args()

    algos = [args.algo] if args.algo else ALGORITHMS

    results = {}
    for algo in algos:
        if args.text is not None:
            results[algo] = hash_text(args.text, algo)
        else:
            results[algo] = hash_file(args.file, algo)

    source = f"text: '{args.text}'" if args.text is not None else f"file: {args.file}"
    print(f"[*] Hash untuk {source}\n")
    for algo, digest in results.items():
        print(f"{algo.upper():8s}: {digest}")

    if args.verify:
        matched_algo = None
        for algo, digest in results.items():
            if digest.lower() == args.verify.lower():
                matched_algo = algo
                break
        print()
        if matched_algo:
            print(f"[+] VERIFIED — cocok dengan hash {matched_algo.upper()} yang diberikan.")
        else:
            print(f"[-] TIDAK COCOK — hash yang diberikan tidak match dengan algoritma manapun yang dihitung.")

if __name__ == "__main__":
    main()
