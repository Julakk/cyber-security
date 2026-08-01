"""
CONTOH VULNERABLE APP - File Upload tanpa validasi
Jalankan hanya di localhost/sandbox.
"""
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)
UPLOAD_DIR = "uploads_vulnerable"
os.makedirs(UPLOAD_DIR, exist_ok=True)

PAGE = """
<h2>Upload File (Vulnerable)</h2>
<form method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>
{% if result %}<p>{{ result }}</p>{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def upload():
    result = None
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            # ⚠️ VULNERABLE: tidak ada validasi ekstensi, MIME type, atau isi file.
            # Filename juga dipakai apa adanya dari input user (bisa path traversal
            # kalau nama filenya mengandung '../').
            save_path = os.path.join(UPLOAD_DIR, file.filename)
            file.save(save_path)
            result = f"File tersimpan di: {save_path}"
            print(f"[!] File diterima tanpa validasi: {file.filename}")

    return render_template_string(PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5006)
