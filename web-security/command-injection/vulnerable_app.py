"""
CONTOH VULNERABLE APP - Command Injection
Fitur "ping host" yang menjalankan shell command langsung dari input user.
Jalankan hanya di localhost/sandbox.
"""
import subprocess
from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<h2>Ping Tool (Vulnerable)</h2>
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
        host = request.form.get("host", "")

        # ⚠️ VULNERABLE: input user langsung dimasukkan ke shell command string.
        # shell=True + string concatenation = classic command injection.
        command = f"ping -c 1 {host}"
        try:
            output = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)
            result = output.stdout + output.stderr
        except Exception as e:
            result = str(e)

    return render_template_string(PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5008)
