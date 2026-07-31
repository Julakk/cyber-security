# Roadmap Sertifikasi Cybersecurity

Catatan riset & rencana buat item roadmap terakhir: **Sertifikasi**.

## 🎯 Rekomendasi Urutan

### 1. eJPT (eLearnSecurity Junior Penetration Tester) — MULAI DARI SINI

- **Biaya**: ~$249
- **Format**: 48 jam, open book, lab live via VPN, 35 pertanyaan berdasarkan apa yang berhasil di-exploit
- **Kenapa cocok**: murni hands-on — exploit mesin beneran, bukan hafalan teori. Tidak ada prasyarat, tidak pernah expired
- **Persiapan**: materi INE (ada free tier), plus practice di TryHackMe/HackTheBox

### 2. (Opsional) Security+ — kalau butuh lolos filter HR

- Lebih dikenal HR/rekruter karena vendor-neutral dan sering jadi syarat wajib di lowongan
- Kombinasi eJPT (bukti skill) + Security+ (bukti "keyword" di CV) sering direkomendasikan bareng

### 3. OSCP — target jangka panjang (setelah eJPT + pengalaman)

- **Biaya**: ~$1,699 (self-guided) atau ~$2,699 (dengan akses lab setahun)
- **Format**: 24 jam ujian praktikal (compromise sebanyak mungkin mesin target) + 24 jam bikin laporan pentest profesional
- **Kenapa nunggu**: mahal & berat sebagai sertifikasi pertama — lebih make sense setelah eJPT dan beberapa bulan pengalaman hands-on

### ❌ CEH — Skip (untuk sekarang)

- Biaya jauh lebih mahal dari eJPT, tapi format-nya 125 soal pilihan ganda (ujian praktikal cuma opsional tambahan)
- Lebih dianggap sebagai "keyword di resume" daripada bukti kemampuan teknis
- Baru worth dipertimbangkan kalau ada lowongan spesifik yang mensyaratkan CEH (banyak di role compliance/government)

## 📅 Rencana Persiapan eJPT (perkiraan 2-4 bulan)

| Fase | Fokus | Terhubung ke repo ini |
|---|---|---|
| 1. Networking dasar | TCP/IP, subnetting, protokol umum | - |
| 2. Web app pentest | SQLi, XSS, CSRF, auth bypass | [`web-security/`](../web-security) |
| 3. Network scanning & enum | Port scan, service/subdomain enum | [`network-security/`](../network-security) |
| 4. Practice lab | TryHackMe "Pre Security" → "Jr Penetration Tester" path | [`ctf-writeups/`](../ctf-writeups) — dokumentasikan tiap room di sini |
| 5. Ambil ujian eJPT | Daftar di ine.com, siapkan 48 jam kosong | - |

## 📚 Sumber Belajar

- TryHackMe — jalur "Pre Security" & "Jr Penetration Tester" (cocok buat pemanasan sebelum eJPT)
- INE Security — penyedia resmi materi eJPT
- HackTheBox — practice tambahan setelah dasar kuat

## ✅ Cara Update Status

Setiap ada progress (mulai belajar materi, selesai practice lab, ambil ujian), update di [`notes/learning-log.md`](./learning-log.md) dan centang di README utama kalau sudah lulus.
