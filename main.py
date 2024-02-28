from flask import Flask, render_template, redirect
import random

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')


@app.route("/")
def root():
    return render_template("profile.html", random_number=random.random())


@app.route("/profile")
def profile():
    return redirect("/")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
