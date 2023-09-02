from contacts_model import Contact
from flask import Flask, redirect, render_template, request
from werkzeug.wrappers import response

Contact.load_db()

app: Flask = Flask(__name__)


@app.route("/")
def index() -> response.Response:
    return redirect("/contacts")


@app.route("/contacts")
def contacts() -> str:
    search: str | None = request.args.get("q")
    if search is not None:
        contacts_set: list = Contact.search(search)
    else:
        contacts_set = Contact.all()
    return render_template("index.html", contacts=contacts_set)


if __name__ == "__main__":
    app.run(port=5003)
