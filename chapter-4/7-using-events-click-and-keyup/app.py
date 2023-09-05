from flask import Flask, render_template

app: Flask = Flask(__name__)

app.secret_key = b"it is over"


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/contacts-partial")
def contacts_partial() -> str:
    return render_template("partial.html")


@app.route("/contacts-demo")
def contacts_demo() -> str:
    return "You got contacts!"


if __name__ == "__main__":
    app.run(port=5016)
