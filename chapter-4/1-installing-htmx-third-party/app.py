from flask import Flask, render_template

app: Flask = Flask(__name__)

app.secret_key = b"it is over"


@app.route("/")
def index() -> str:
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
