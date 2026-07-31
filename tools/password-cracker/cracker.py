#!/usr/bin/env python3
"""
Educational Dictionary Attack Tool
Untuk belajar tentang kelemahan hashing cepat (MD5/SHA1/SHA256) tanpa salt.

⚠️ Hanya gunakan pada hash milik sendiri untuk tujuan edukasi.
"""
import argparse
import hashlib
import time

ALGOS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
}

def crack(target_hash, wordlist_path, algo):
    hash_func = ALGOS[algo]
    target_hash = target_hash.lower().strip()

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        words = [w.strip() for w in f if w.strip()]

    print(f"[*] Mencoba {len(words)} kata dari wordlist menggunakan algoritma {algo.upper()}...\n")
    start = time.time()

    for word in words:
        computed = hash_func(word.encode()).hexdigest()
        if computed == target_hash:
            elapsed = time.time() - start
            print(f"[+] DITEMUKAN! Password: '{word}'  (dalam {elapsed:.4f} detik)")
            return word

    elapsed = time.time() - start
    print(f"[-] Tidak ditemukan di wordlist ini. ({elapsed:.4f} detik, {len(words)} percobaan)")
    return None

def main():
    parser = argparse.ArgumentParser(description="Educational hash dictionary cracker")
    parser.add_argument("--hash", required=True, help="Target hash yang ingin dicocokkan")
    parser.add_argument("--algo", choices=ALGOS.keys(), default="md5", help="Algoritma hash")
    parser.add_argument("--wordlist", default="wordlist_sample.txt", help="Path ke wordlist")
    args = parser.parse_args()

    crack(args.hash, args.wordlist, args.algo)

if __name__ == "__main__":
    main()
