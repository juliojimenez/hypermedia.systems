from flask import Flask, redirect
from werkzeug.wrappers import response

app: Flask = Flask(__name__)

# This route will produce a Not Found error
# But that's ok! What we want to see is the
# redirect to /contacts in the address bar.


@app.route("/")
def index() -> response.Response:
    return redirect("/contacts")


if __name__ == "__main__":
    app.run(port=5002)
