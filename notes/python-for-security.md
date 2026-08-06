# Python for Security — Catatan Belajar

Library dan pattern Python yang sering dipakai buat bikin security tools — rangkuman dari apa yang udah dipraktikkan di tools lain di repo ini.

## 📦 Library yang Sering Dipakai

| Library | Fungsi | Contoh Pemakaian di Repo Ini |
|---|---|---|
| `socket` | Low-level network operations (TCP/UDP connect, DNS resolve) | [`port-scanner/scanner.py`](../network-security/port-scanner/scanner.py) |
| `requests` | HTTP client, buat interact sama web app | [`vuln-scanner/vuln_scanner.py`](../tools/vuln-scanner/vuln_scanner.py) |
| `hashlib` | Hashing (MD5, SHA1, SHA256, dll) | [`hash-generator/hash_gen.py`](../tools/hash-generator/hash_gen.py) |
| `secrets` | Cryptographically secure random (BUKAN `random`!) | [`password-generator/password_gen.py`](../tools/password-generator/password_gen.py) |
| `subprocess` | Jalanin command eksternal (hati-hati kalau input user masuk ke sini!) | [`command-injection/fixed_app.py`](../web-security/command-injection/fixed_app.py) |
| `scapy` | Packet crafting & sniffing level rendah | [`packet-sniffer/sniffer.py`](../network-security/packet-sniffer/sniffer.py) |
| `dns.resolver` (dnspython) | Query DNS record | [`dns-lookup/dns_lookup.py`](../network-security/dns-lookup/dns_lookup.py) |
| `yara` (yara-python) | Pattern matching buat malware analysis | [`yara-rules/run_yara.py`](../malware-analysis/yara-rules/run_yara.py) |
| `concurrent.futures` | Multi-threading (bikin scanning jauh lebih cepat) | [`port-scanner/scanner.py`](../network-security/port-scanner/scanner.py) |

## ⚠️ Pattern Berbahaya yang Harus Dihindari

### 1. `random` buat keperluan security

```python
import random
token = ''.join(random.choice(string.ascii_letters) for _ in range(16))  # ❌ SALAH
```

`random` itu PRNG predictable, cocok buat game/simulasi tapi **bukan** buat token/password/session ID. Pakai `secrets` sebagai gantinya.

### 2. `subprocess` dengan `shell=True` + input user

```python
subprocess.run(f"ping {user_input}", shell=True)  # ❌ RENTAN COMMAND INJECTION
```

Lihat [`web-security/command-injection/EXPLOIT.md`](../web-security/command-injection/EXPLOIT.md) buat penjelasan lengkap.

### 3. String formatting langsung ke SQL query

```python
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # ❌ RENTAN SQL INJECTION
```

Selalu pakai parameterized query — lihat [`web-security/sql-injection/`](../web-security/sql-injection).

### 4. `eval()`/`exec()` terhadap input user

```python
result = eval(user_input)  # ❌ SANGAT BERBAHAYA — bisa eksekusi kode arbitrer apapun
```

## 🧰 Pattern yang Bagus buat Bikin Security Tools

### Multi-threading buat scanning cepat

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(scan_func, target) for target in targets]
    for future in as_completed(futures):
        result = future.result()
```

### Selalu pakai `argparse` buat CLI tools

Semua tools di repo ini pakai `argparse` — bikin tool jadi self-documenting (`--help` otomatis ada) dan gampang dipakai orang lain.

### Error handling yang informatif, tapi gak bocorin detail sensitif

```python
try:
    result = risky_operation()
except SpecificException as e:
    print(f"[!] Error: {e}")  # OK buat tool internal
    # Tapi di web app production, jangan tampilkan stack trace lengkap ke user!
```

## 📚 Sumber Belajar Lanjutan

- Dokumentasi resmi tiap library (`hashlib`, `secrets`, `socket` — semua bagian dari Python standard library, dokumentasinya lengkap)
- [Black Hat Python](https://nostarch.com/black-hat-python2E) (buku) — buat belajar bikin tools security lebih advanced (custom C2, network tools, dll)
