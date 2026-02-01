from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h2>Simple Calculator</h2>
<form method="post">
<input type="number" name="a" required>
<input type="number" name="b" required><br><br>
<button name="op" value="+">+</button>
<button name="op" value="-">-</button>
<button name="op" value="*">*</button>
<button name="op" value="/">/</button>
</form>

{% if result is not none %}
<h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def calc():
    result = None
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        op = request.form["op"]
        result = eval(f"{a}{op}{b}")
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
