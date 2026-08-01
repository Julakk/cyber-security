#!/usr/bin/env python3
"""
Simple IAM Policy Auditor
Menganalisis file IAM policy (JSON, format AWS-style) untuk mencari
pattern permission yang terlalu longgar (overly permissive).

Tidak butuh koneksi ke AWS/cloud manapun — murni analisis file policy JSON lokal.
Cocok dipakai sebelum apply policy ke production, sebagai sanity check cepat.

Cara pakai:
    python3 iam_audit.py policy_example.json
"""
import json
import argparse
import sys

def normalize_to_list(value):
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return value

def audit_statement(statement, index):
    findings = []
    effect = statement.get("Effect", "")
    actions = normalize_to_list(statement.get("Action"))
    resources = normalize_to_list(statement.get("Resource"))
    principal = statement.get("Principal")

    if effect != "Allow":
        return findings  # cuma audit statement yang Allow

    # Cek wildcard action penuh
    if "*" in actions:
        findings.append(f"[Statement {index}] ⚠️ Action '*' — mengizinkan SEMUA action, sangat longgar")

    # Cek wildcard action per-service (misal 's3:*')
    for action in actions:
        if isinstance(action, str) and action.endswith(":*") and action != "*":
            findings.append(f"[Statement {index}] ⚠️ Action '{action}' — mengizinkan semua action di service ini")

    # Cek wildcard resource
    if "*" in resources:
        findings.append(f"[Statement {index}] ⚠️ Resource '*' — berlaku ke SEMUA resource, sebaiknya dibatasi ke ARN spesifik")

    # Cek principal wildcard (biasanya di resource-based policy, misal S3 bucket policy)
    if principal == "*" or principal == {"AWS": "*"}:
        findings.append(f"[Statement {index}] 🚨 Principal '*' — policy ini bisa diakses SIAPA SAJA (termasuk publik internet)!")

    # Kombinasi paling berbahaya: Action:*, Resource:*, Principal:*
    if "*" in actions and "*" in resources and (principal == "*" or principal == {"AWS": "*"}):
        findings.append(f"[Statement {index}] 🚨🚨 KRITIKAL: Action, Resource, dan Principal semuanya wildcard — setara akses admin publik!")

    return findings

def main():
    parser = argparse.ArgumentParser(description="Simple IAM policy JSON auditor")
    parser.add_argument("policy_file", help="Path ke file IAM policy JSON")
    args = parser.parse_args()

    try:
        with open(args.policy_file) as f:
            policy = json.load(f)
    except json.JSONDecodeError as e:
        print(f"[!] File bukan JSON valid: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"[!] File tidak ditemukan: {args.policy_file}")
        sys.exit(1)

    statements = policy.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]

    print(f"[*] Mengaudit {args.policy_file} — {len(statements)} statement ditemukan\n")

    all_findings = []
    for i, statement in enumerate(statements, start=1):
        all_findings.extend(audit_statement(statement, i))

    if not all_findings:
        print("[+] Tidak ada pattern overly-permissive yang terdeteksi dari pengecekan dasar ini.")
    else:
        for finding in all_findings:
            print(finding)

    print(f"\n[*] Selesai. {len(all_findings)} temuan.")
    print("[i] Ini pengecekan dasar, bukan pengganti review manual/tools resmi seperti AWS IAM Access Analyzer.")

if __name__ == "__main__":
    main()
