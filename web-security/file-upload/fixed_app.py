"""
VERSI YANG SUDAH DIPERBAIKI - File Upload dengan validasi berlapis
"""
import os
import uuid
from flask import Flask, request, render_template_string, abort

app = Flask(__name__)
UPLOAD_DIR = "uploads_fixed"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ✅ FIXED #1: whitelist ekstensi yang diizinkan (bukan blacklist!)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# ✅ FIXED #2: cek magic bytes (file signature), bukan cuma percaya ekstensi
MAGIC_BYTES = {
    b"\xff\xd8\xff": "jpg",
    b"\x89PNG": "png",
    b"GIF8": "gif",
    b"%PDF": "pdf",
}

PAGE = """
<h2>Upload File (Fixed)</h2>
<form method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>
{% if result %}<p>{{ result }}</p>{% endif %}
<p>Hanya menerima: {{ allowed }}, maks 5MB</p>
"""

def get_extension(filename):
    return filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

def check_magic_bytes(file_bytes):
    for signature, ext in MAGIC_BYTES.items():
        if file_bytes.startswith(signature):
            return ext
    return None

@app.route("/", methods=["GET", "POST"])
def upload():
    result = None
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            result = "Tidak ada file dipilih."
            return render_template_string(PAGE, result=result, allowed=", ".join(ALLOWED_EXTENSIONS))

        # ✅ FIXED #3: cek ukuran file
        file.seek(0, os.SEEK_END)
        size = file.tell()
        file.seek(0)
        if size > MAX_FILE_SIZE:
            abort(413, description="File terlalu besar (maks 5MB)")

        # ✅ FIXED: validasi ekstensi (whitelist)
        ext = get_extension(file.filename)
        if ext not in ALLOWED_EXTENSIONS:
            abort(400, description=f"Ekstensi '.{ext}' tidak diizinkan")

        # ✅ FIXED: validasi isi file (magic bytes), bukan cuma percaya ekstensi
        # -> mencegah attacker rename shell.php jadi shell.jpg
        file_bytes = file.read(16)
        file.seek(0)
        detected_type = check_magic_bytes(file_bytes)
        if detected_type is None or (detected_type != ext and not (detected_type == "jpg" and ext == "jpeg")):
            abort(400, description="Isi file tidak cocok dengan ekstensinya (kemungkinan file dipalsukan)")

        # ✅ FIXED #4: rename file pakai UUID random, JANGAN pakai nama asli dari user
        # -> mencegah path traversal DAN mencegah overwrite/collision
        safe_filename = f"{uuid.uuid4().hex}.{ext}"
        save_path = os.path.join(UPLOAD_DIR, safe_filename)
        file.save(save_path)
        result = f"File berhasil diupload dengan nama aman: {safe_filename}"

    return render_template_string(PAGE, result=result, allowed=", ".join(ALLOWED_EXTENSIONS))

if __name__ == "__main__":
    app.run(debug=True, port=5007)
