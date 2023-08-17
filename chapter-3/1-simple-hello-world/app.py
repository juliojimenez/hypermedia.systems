from typing import (
    Literal
)
from flask import (
    Flask
)

app: Flask = Flask(__name__)

@app.route("/")
def index() -> Literal["Hello World!"]:
    return "Hello World!"

if __name__ == "__main__":
    app.run()
