from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    number = None
    text = None

    r = None
    area = None

    if request.method == "POST":
        if "multiply" in request.form:
            try:
                num = float(request.form.get("number"))
                doubled = num * 2
                number = doubled
                text = f"Ваше число {num}, умноженное на 2: {doubled}"
            except ValueError:
                text = "❌ Пожалуйста, введите корректное число!"

        elif "circle" in request.form:
            try:
                r = float(request.form.get("radius"))
            except ValueError:
                r = None

    return render_template("index.html", number=number, text=text, r=r, pi=3.14)


if __name__ == "__main__":
    app.run(debug=True)