# Cross-Site Scripting (XSS) Demo

Demo comment box yang rentan Stored XSS, plus versi yang aman.

## 📂 Isi

- `vulnerable.html` — Comment box yang render input user langsung sebagai HTML (rentan)
- `fixed.html` — Versi aman dengan escaping/sanitization
- `EXPLOIT.md` — Penjelasan payload dan tipe-tipe XSS

## 🚀 Cara Coba

Buka `vulnerable.html` langsung di browser. Masukkan komentar:

```html
<script>alert('XSS!')</script>
```

Komentar akan langsung ter-eksekusi sebagai JavaScript begitu di-submit — inilah **Stored/Reflected XSS**.

Bandingkan dengan `fixed.html`, di mana input yang sama hanya tampil sebagai teks biasa (escaped).
