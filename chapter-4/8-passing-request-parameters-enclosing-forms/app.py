from contacts_model import Contact
from flask import Flask, render_template, request

Contact.load_db()

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


@app.route("/contacts", methods=["GET", "POST"])
def contacts() -> str:
    search: str | None = request.form.get("q")
    if search is not None:
        contacts_set: list = Contact.search(search)
    else:
        contacts_set = Contact.all()
    return render_template("partial.html", contacts=contacts_set)


if __name__ == "__main__":
    app.run(port=5017)
