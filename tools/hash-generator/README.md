# Hash Generator

Generate hash file/text pakai berbagai algoritma, plus verifikasi checksum file.

## 🚀 Cara Pakai

```bash
# Hash dari teks langsung
python3 hash_gen.py --text "halo dunia"

# Hash dari file
python3 hash_gen.py --file dokumen.pdf

# Verifikasi checksum (misal setelah download file, cek integritas)
python3 hash_gen.py --file dokumen.pdf --verify <hash_yang_diharapkan>
```

## 🎓 Kegunaan Umum Hashing

1. **Integrity checking** — pastikan file gak corrupt/berubah pas transfer/download (bandingkan hash sebelum & sesudah)
2. **Deduplication** — deteksi file duplikat lewat hash-nya, bukan compare isi byte-by-byte
3. **Digital forensics** — identifikasi file dengan "sidik jari" unik (lihat juga [`malware-analysis/static_analysis.py`](../../malware-analysis/static_analysis.py))

> ⚠️ Untuk **password hashing**, jangan pakai MD5/SHA polos — lihat [`tools/password-cracker/hash_demo.py`](../password-cracker/hash_demo.py) buat penjelasan kenapa, dan pakai bcrypt/argon2 sebagai gantinya.
