from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("StateOfMatter.html")


@app.route("/gas")
def gas():
    return render_template("GAS.html")


@app.route("/liquid")
def liquid():
    return render_template("LIQUID.html")


@app.route("/plasma")
def plasma():
    return render_template("PLASMA.html")

@app.route("/solid")
def solid():
    return render_template("SOLID.html")


if __name__ == "__main__":
    app.run(debug=True)