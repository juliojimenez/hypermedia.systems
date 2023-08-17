from contacts_model import Contact
from flask import Flask, flash, redirect, render_template, request
from typing_extensions import LiteralString
from werkzeug.wrappers import response

Contact.load_db()

app: Flask = Flask(__name__)

app.secret_key = b"it is over"


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


@app.route("/contacts/new", methods=["GET"])
def contacts_new_get() -> str:
    return render_template("new.html", contact=Contact())


@app.route("/contacts/new", methods=["POST"])
def contacts_new() -> response.Response | str:
    c: Contact = Contact(
        None,
        request.form["first_name"],
        request.form["last_name"],
        request.form["phone"],
        request.form["email"],
    )
    if c.save():
        flash("Created New Contact!")
        return redirect("/contacts")
    else:
        return render_template("new.html", contact=c)
    
@app.route("/contacts/<contact_id>")
def contacts_view(contact_id: int = 0) -> str:
    contact = Contact.find(contact_id)
    return render_template("show.html", contact=contact)


if __name__ == "__main__":
    app.run()
