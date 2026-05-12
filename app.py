from flask import Flask, render_template, request
import random

app = Flask(__name__)
secret = random.randint(1, 10)

@app.route("/", methods=["GET", "POST"])
def home():
    msg = "خمن رقم بين 1 و 10"

    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess == secret:
            msg = "🎉 صح! فزت"
        elif guess > secret:
            msg = "أصغر"
        else:
            msg = "أكبر"

    return render_template("index.html", message=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
