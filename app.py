from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # ===== ЗАДАНИЕ 1: Среднее число =====
    result1 = None

    if request.method == "POST" and "task1" in request.form:
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            c = float(request.form.get("c"))

            # Находим среднее число
            if (a <= b <= c) or (c <= b <= a):
                result1 = b
            elif (b <= a <= c) or (c <= a <= b):
                result1 = a
            else:
                result1 = c
        except ValueError:
            result1 = "Ошибка ввода"

    # ===== ЗАДАНИЕ 2: Калькулятор через форму =====
    result2 = None
    error = None

    if request.method == "POST" and "task2" in request.form:
        try:
            num1 = float(request.form.get("num1"))
            operator = request.form.get("operator")
            num2 = float(request.form.get("num2"))

            if operator == "+":
                result2 = num1 + num2
            elif operator == "-":
                result2 = num1 - num2
            elif operator == "*":
                result2 = num1 * num2
            elif operator == ":":
                if num2 == 0:
                    error = "Ошибка: деление на ноль!"
                else:
                    result2 = num1 / num2
            elif operator == "**":
                result2 = num1 ** num2
            else:
                error = "Ошибка: неизвестная операция!"
        except ValueError:
            error = "Ошибка: введите числа!"

    return render_template("index.html",
                           result1=result1,
                           result2=result2,
                           error=error)


# ===== ЗАДАНИЕ 2: Калькулятор через URL =====
@app.route("/<num1>/<operator>/<num2>/")
def calculate(num1, operator, num2):
    result = None
    error = None

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        error = "Ошибка"
        return render_template("index.html", result=result, error=error, num1=num1, operator=operator, num2=num2)

    # Преобразуем URL-кодированные символы
    if operator == "%2A":
        operator = "*"

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == ":":
        if num2 == 0:
            error = "Ошибка"
        else:
            result = num1 / num2
    elif operator == "**":
        result = num1 ** num2
    else:
        error = "Ошибка"

    return render_template("index.html",
                           result=result,
                           error=error,
                           num1=num1,
                           operator=operator,
                           num2=num2)


if __name__ == "__main__":
    app.run(debug=True)