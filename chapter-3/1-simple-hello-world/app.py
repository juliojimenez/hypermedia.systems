from flask import Flask
from typing import Literal

app: Flask = Flask(__name__)


@app.route("/")
def index() -> Literal["Hello World!"]:
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=5001)
