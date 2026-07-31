#!/usr/bin/env python3
"""
Demo: kenapa MD5/SHA polos buruk untuk password, dan kenapa bcrypt lebih aman.
"""
import hashlib
import time

def demo_speed_comparison():
    print("=" * 60)
    print("DEMO 1: Kecepatan hashing (kenapa MD5/SHA rentan brute-force)")
    print("=" * 60)

    password = "password123"
    n = 100_000

    start = time.time()
    for _ in range(n):
        hashlib.md5(password.encode()).hexdigest()
    md5_time = time.time() - start
    print(f"MD5:    {n:,} hash dalam {md5_time:.3f} detik  (~{n/md5_time:,.0f} hash/detik)")

    start = time.time()
    for _ in range(n):
        hashlib.sha256(password.encode()).hexdigest()
    sha_time = time.time() - start
    print(f"SHA256: {n:,} hash dalam {sha_time:.3f} detik  (~{n/sha_time:,.0f} hash/detik)")

    print("\n[!] Attacker dengan GPU modern bisa coba MILIARAN hash MD5 per detik.")
    print("    Ini kenapa MD5/SHA polos TIDAK COCOK untuk hashing password.\n")

def demo_no_salt_problem():
    print("=" * 60)
    print("DEMO 2: Masalah tanpa salt (rainbow table attack)")
    print("=" * 60)

    password = "password123"
    hash1 = hashlib.sha256(password.encode()).hexdigest()
    hash2 = hashlib.sha256(password.encode()).hexdigest()

    print(f"Password: '{password}'")
    print(f"Hash #1:  {hash1}")
    print(f"Hash #2:  {hash2}")
    print(f"Sama persis? {hash1 == hash2}")
    print("\n[!] Tanpa salt, 2 user dengan password sama akan punya hash yang SAMA.")
    print("    Attacker cukup punya 1 tabel hash umum (rainbow table) untuk")
    print("    membobol SEMUA user yang pakai password itu sekaligus.\n")

def demo_bcrypt_concept():
    print("=" * 60)
    print("DEMO 3: Kenapa bcrypt/argon2 lebih baik (konsep)")
    print("=" * 60)
    print("""
bcrypt/argon2 punya 2 karakteristik penting yang tidak dimiliki MD5/SHA:

1. SALT otomatis & unik per password
   -> 2 user dengan password sama akan hasilkan hash BERBEDA
   -> rainbow table jadi tidak berguna

2. SENGAJA DIBUAT LAMBAT (cost factor / work factor bisa diatur)
   -> MD5: jutaan-miliaran hash/detik
   -> bcrypt (cost=12): cuma puluhan hash/detik
   -> Ini bikin brute-force jadi tidak praktis secara waktu/biaya

Contoh pakai bcrypt (butuh: pip install bcrypt --break-system-packages):

    import bcrypt
    hashed = bcrypt.hashpw(b"password123", bcrypt.gensalt(rounds=12))
    bcrypt.checkpw(b"password123", hashed)  # True kalau cocok
""")

if __name__ == "__main__":
    demo_speed_comparison()
    demo_no_salt_problem()
    demo_bcrypt_concept()
