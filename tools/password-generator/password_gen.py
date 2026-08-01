#!/usr/bin/env python3
"""
Secure Password Generator
Pakai module 'secrets' (cryptographically secure), bukan 'random'.
"""
import argparse
import secrets
import string
import math

def generate_password(length=16, use_symbols=True, use_digits=True, use_uppercase=True):
    alphabet = string.ascii_lowercase
    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+"

    return "".join(secrets.choice(alphabet) for _ in range(length)), len(alphabet)

def estimate_entropy_bits(length, charset_size):
    """Entropy (bits) = length * log2(charset_size). Estimasi kekuatan brute-force."""
    return length * math.log2(charset_size)

def strength_label(bits):
    if bits < 40:
        return "Lemah"
    elif bits < 60:
        return "Sedang"
    elif bits < 80:
        return "Kuat"
    else:
        return "Sangat Kuat"

def main():
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("--length", type=int, default=16, help="Panjang password (default: 16)")
    parser.add_argument("--count", type=int, default=1, help="Jumlah password yang di-generate")
    parser.add_argument("--no-symbols", action="store_true", help="Tanpa simbol")
    parser.add_argument("--no-digits", action="store_true", help="Tanpa angka")
    parser.add_argument("--no-uppercase", action="store_true", help="Tanpa huruf besar")
    args = parser.parse_args()

    if args.length < 8:
        print("[!] Panjang minimal disarankan 8 karakter (12+ lebih baik).")

    for _ in range(args.count):
        password, charset_size = generate_password(
            length=args.length,
            use_symbols=not args.no_symbols,
            use_digits=not args.no_digits,
            use_uppercase=not args.no_uppercase,
        )
        bits = estimate_entropy_bits(args.length, charset_size)
        print(f"{password}   (entropy: ~{bits:.0f} bit, {strength_label(bits)})")

if __name__ == "__main__":
    main()
