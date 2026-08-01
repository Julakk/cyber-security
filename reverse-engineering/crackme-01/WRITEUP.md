# Crackme #01 — Writeup

## 🔍 Step 1: Kenali Binary

```bash
file crackme
```

Output nunjukin ini ELF 64-bit executable, dynamically linked — binary Linux biasa, gak ada packing/obfuscation aneh.

## 🔍 Step 2: Coba `strings` Dulu

```bash
strings crackme | grep -i pass
```

Ketemu string kayak `"Masukkan password: "`, `"Password benar!"`, `"Password salah."` — tapi **gak ada flag plaintext**. Ini nunjukin flag-nya di-encode, gak bisa langsung diambil dari strings doang.

## 🔍 Step 3: Disassembly dengan `objdump`

```bash
objdump -d crackme | less
```

Cari fungsi `main`, scroll ke bagian yang ngebandingin input user. Bakal ketemu pattern kayak:

```asm
xor    $0x13,%eax
```

Instruksi `xor $0x13` ini muncul **dua kali** — sekali buat cek password, sekali lagi buat decode flag. Ini kunci pentingnya: **XOR key = 0x13**.

Kalau diliat lebih detail, ada loop yang:
1. Ambil tiap karakter input
2. XOR sama `0x13`
3. Bandingin sama byte target yang udah di-hardcode di binary

## 🔍 Step 4: Ambil Target Bytes

Dari disassembly (atau baca `.rodata`/stack setup di awal fungsi `main`), ketemu array 8 byte yang jadi target perbandingan. Bisa juga diambil pakai `objdump -s -j .rodata crackme` atau debug pakai `gdb` buat dump memory-nya langsung.

Target bytes (hasil observasi): `5b 27 70 78 20 61 32 32`

## 🎯 Step 5: Hitung Password

Karena logikanya `input[i] XOR 0x13 == target[i]`, maka `input[i] = target[i] XOR 0x13`:

```python
key = 0x13
target = [0x5b, 0x27, 0x70, 0x78, 0x20, 0x61, 0x32, 0x32]
password = "".join(chr(t ^ key) for t in target)
print(password)  # H4ck3r!!
```

## 🏁 Step 6: Jalankan dengan Password yang Benar

```bash
echo "H4ck3r!!" | ./crackme
```

Output:

```
Password benar! Flag: flag{r3v3rs1ng_1s_fun_2026}
```

## 💡 Pelajaran

- `strings` itu langkah pertama yang cepat, tapi jangan berhenti di situ kalau data penting sengaja di-encode
- **XOR encoding** adalah teknik obfuscation paling dasar — gampang dikenali dari instruksi `xor` dengan konstanta yang sama dipakai berulang kali
- Begitu tahu key-nya, decode balik itu simetris: `A XOR K XOR K = A`
- Di reverse engineering nyata (malware analysis), teknik ini sering dikombinasi dengan enkripsi yang lebih kuat atau packing (UPX, dll) yang butuh langkah tambahan sebelum bisa sampai ke tahap analisis logic seperti ini

## 🔗 Referensi

- [`malware-analysis/`](../../malware-analysis) — konsep string extraction & entropy analysis yang relevan buat langkah awal analisis binary
