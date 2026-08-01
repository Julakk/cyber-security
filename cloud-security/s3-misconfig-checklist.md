# S3 (Cloud Storage) Misconfiguration Checklist

Checklist kerentanan storage bucket paling umum — berlaku konsepnya untuk AWS S3, Google Cloud Storage, maupun Azure Blob Storage.

## ✅ Checklist

- [ ] **Public access diblokir secara default** — pastikan "Block Public Access" aktif kecuali memang butuh publik (misal bucket buat static website assets)
- [ ] **Bucket policy di-review** — jangan ada `"Principal": "*"` dengan permission `PutObject`/`DeleteObject` tanpa kondisi tambahan
- [ ] **Encryption at rest aktif** — data tersimpan terenkripsi (SSE-S3 atau SSE-KMS)
- [ ] **Versioning aktif** — supaya ada recovery kalau ada penghapusan/overwrite tidak sengaja (juga membantu deteksi ransomware-style attack)
- [ ] **Logging & monitoring aktif** — akses ke bucket sensitif harus tercatat (CloudTrail / Access Logs)
- [ ] **Least privilege di IAM policy** — jangan kasih `s3:*` kalau cuma butuh `s3:GetObject`
- [ ] **Tidak ada credential hardcoded** — cek kode/config gak ada access key/secret key ketinggalan (banyak breach besar berawal dari sini)
- [ ] **MFA Delete diaktifkan** untuk bucket kritis — mencegah penghapusan tidak sengaja/tidak sah meski credential bocor

## 🔍 Cara Cek Cepat (AWS CLI, kalau punya akses)

```bash
# Cek apakah bucket public
aws s3api get-bucket-acl --bucket nama-bucket

# Cek block public access setting
aws s3api get-public-access-block --bucket nama-bucket

# Cek encryption
aws s3api get-bucket-encryption --bucket nama-bucket
```

## 🎓 Kasus Nyata yang Terkenal

Banyak data breach besar (data pelanggan, kredensial, dokumen internal) yang penyebabnya sesederhana: **S3 bucket di-set public tanpa sengaja**, biasanya karena default setting di-override atau developer lupa mengembalikan setting "testing" ke private sebelum production.

## 🛡️ Prinsip Umum

Anggap semua storage bucket **private by default**, dan setiap kali butuh akses publik, tanya: "Apakah ini benar-benar perlu publik, atau cukup pakai signed URL dengan expiry?"
