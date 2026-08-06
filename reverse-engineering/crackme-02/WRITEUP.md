# Crackme #02 — Writeup

## 🔍 Step 1: `strings` Dulu (dan Kenapa Ini Jebakan)

```bash
strings crackme | grep -iE "pass|letmein|flag"
```

Output:
```
letmein123
Masukkan password:
Password benar! Flag:
Password salah. Coba lagi!
DECOY_PASSWORD
check_real_password
```

Ada string `letmein123` dengan nama variabel `DECOY_PASSWORD` di dekatnya — **kalau langsung dicoba tanpa dianalisis lebih lanjut, ini akan selalu gagal**. Ini pelajaran penting: jangan asumsikan string pertama yang "keliatan kayak password" itu beneran password-nya.

Untungnya di binary ini nama fungsi masih ada (`check_real_password`) — kasih clue jelas kalau ada fungsi lain yang perlu dianalisis. Di real-world crackme/malware, symbol biasanya udah di-strip (dihapus), jadi analis harus rely ke logic aja tanpa nama fungsi yang membantu.

## 🔍 Step 2: Baca Fungsi `check_decoy`

```bash
objdump -d crackme | awk '/<check_decoy>:/,/ret/'
```

Kalau dibaca, fungsi ini selalu return 0 apapun inputnya — dikonfirmasi juga lewat testing manual:

```bash
echo "letmein123" | ./crackme
# Output: Password salah. Coba lagi!
```

Confirmed: ini jebakan.

## 🔍 Step 3: Baca Fungsi `check_real_password`

```bash
objdump -d crackme | awk '/<check_real_password>:/,/ret/'
```

Beberapa instruksi kunci yang ditemukan:

```asm
cmp    $0xb,%rax          ; cek panjang input == 11 (0xb)
movabs $0x24a0605da069a0fd,%rax   ; 8 byte pertama dari target array
movl   $0x6aa0ee24,-0x9(%rbp)     ; 4 byte terakhir (overlap 3 byte)

; di dalam loop per-karakter:
movzbl (%rax),%eax        ; ambil 1 byte karakter input
add    %eax,%eax          ; eax = eax + eax        -> char*2
add    %edx,%eax          ; eax = eax + edx(=char)  -> char*3
lea    0x7(%rax),%edx     ; edx = (char*3) + 7
...                        ; instruksi sar/shr/sub setelahnya = implementasi modulo 256
                            ; dari compiler (walau %256 harusnya trivial, GCC tetap generate
                            ; pengecekan overflow/sign yang eksplisit di -O0)
```

Dari sini kelihatan compiler mengimplementasikan `char * 3` bukan pakai instruksi `imul`, tapi pakai **dua kali `add`** (`char + char = char*2`, lalu `+ char lagi = char*3`) — ini optimisasi umum karena `add` lebih cepat dari `imul` di banyak arsitektur, bahkan di level `-O0`.

Kesimpulan logic: `transformed = (input[i] * 3 + 7) % 256`, dibandingkan ke target byte array.

## 🔍 Step 4: Ambil Target Bytes

Dari immediate value `movabs $0x24a0605da069a0fd`, ingat ini **little-endian**, jadi urutan byte aslinya dibalik:

```
0x24a0605da069a0fd
-> byte order asli: fd a0 69 a0 5d 60 a0 24
```

Ditambah 3 byte terakhir dari `movl $0x6aa0ee24,-0x9(%rbp)` (juga little-endian, ambil 3 byte low): `ee a0 6a`

Target lengkap (11 byte): `fd a0 69 a0 5d 60 a0 24 ee a0 6a`

## 🎯 Step 5: Reverse Transformasi buat Cari Password

Formula: `transformed = (c * 3 + 7) % 256`, jadi buat cari `c` dari `transformed`, kita brute-force tiap kemungkinan byte (0-255) karena modulo bikin operasi ini gak trivial dibalik langsung:

```python
target = [0xfd, 0xa0, 0x69, 0xa0, 0x5d, 0x60, 0xa0, 0x24, 0xee, 0xa0, 0x6a]

password = ""
for t in target:
    for c in range(256):
        if (c * 3 + 7) % 256 == t:
            password += chr(c)
            break

print(password)  # R3v3rs3_M3!
```

## 🏁 Step 6: Jalankan

```bash
echo "R3v3rs3_M3!" | ./crackme
```

Output:
```
Password benar! Flag: flag{m4th_tr4nsf0rm_ch4ll3ng3_d0n3}
```

## 💡 Pelajaran

- **Jangan percaya string pertama yang "keliatan benar"** — selalu verifikasi lewat logic program, bukan asumsi
- Compiler bisa mengoptimalkan operasi matematika sederhana (`* 3`) jadi kombinasi instruksi lain (`add+add`) — penting buat kenal pola-pola umum ini biar gak bingung pas baca disassembly
- Immediate value besar (`movabs`) sering nyimpen beberapa byte data sekaligus — perlu diinget urutannya **little-endian**, jadi harus dibalik buat dapetin urutan byte yang benar
- Kalau transformasi gak reversible secara langsung (karena modulo), **brute-force per-karakter** (256 kemungkinan) tetap praktis karena search space-nya kecil

## 🔗 Referensi

- [`crackme-01/`](../crackme-01) — dasar-dasar XOR encoding, mulai dari sini kalau belum pernah coba
