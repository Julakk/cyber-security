"""
VERSI YANG SUDAH DIPERBAIKI - Ping tool tanpa shell injection risk
"""
import subprocess
import re
from flask import Flask, request, render_template_string, abort

app = Flask(__name__)

# ✅ FIXED #1: whitelist ketat format host yang diizinkan (IPv4 atau hostname sederhana)
HOST_PATTERN = re.compile(r"^[a-zA-Z0-9.\-]+$")

PAGE = """
<h2>Ping Tool (Fixed)</h2>
<form method="post">
    Host: <input name="host" placeholder="127.0.0.1">
    <input type="submit" value="Ping">
</form>
<pre>{{ result }}</pre>
"""

@app.route("/", methods=["GET", "POST"])
def ping():
    result = ""
    if request.method == "POST":
        host = request.form.get("host", "").strip()

        # ✅ FIXED #2: validasi ketat sebelum diproses sama sekali
        if not host or not HOST_PATTERN.match(host) or len(host) > 255:
            abort(400, description="Format host tidak valid. Hanya huruf, angka, titik, dan strip yang diizinkan.")

        # ✅ FIXED #3: TIDAK PAKAI shell=True, dan command dipecah jadi list argumen.
        # Ini artinya input user diperlakukan sebagai SATU argumen tunggal ke 'ping',
        # tidak pernah bisa diinterpretasikan ulang sebagai shell syntax (';', '&&', '|', dll).
        try:
            output = subprocess.run(
                ["ping", "-c", "1", host],
                shell=False,
                capture_output=True,
                text=True,
                timeout=5,
            )
            result = output.stdout + output.stderr
        except Exception as e:
            result = str(e)

    return render_template_string(PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5009)
