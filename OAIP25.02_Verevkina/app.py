from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

VALID_LOGIN = "diana"
VALID_PASSWORD = "12345"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        if login == VALID_LOGIN and password == VALID_PASSWORD:
            return redirect(url_for("me"))
        else:
            return render_template("index.html", error="❌ Неверный логин или пароль!")

    return render_template("index.html", error=None)


@app.route("/me")
def me():
    return render_template("me.html", name="Диана")


@app.route("/about")
def about():
    facts = [
        "📚 Учусь на программиста",
        "🐱 Люблю кошек",
        "💅 Занимаюсь профессиональным маникюром уже четыре года"
    ]
    return render_template("about.html", facts=facts)


if __name__ == "__main__":
    app.run(debug=True)