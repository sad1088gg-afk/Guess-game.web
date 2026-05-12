from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "1234"

@app.route("/")
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0

    return render_template("index.html", message="ابدأ التخمين!")

@app.route("/guess", methods=["POST"])
def guess():
    user_guess = int(request.form["guess"])
    number = session["number"]
    session["attempts"] += 1

    if user_guess < number:
        msg = "📉 أعلى"
    elif user_guess > number:
        msg = "📈 أقل"
    else:
        msg = f"🎉 صح! خلال {session['attempts']} محاولات"

    return render_template("index.html", message=msg)

@app.route("/reset")
def reset():
    session.clear()
    return render_template("index.html", message="تمت إعادة اللعبة!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    