from contacts_model import Contact
from flask import Flask, flash, redirect, render_template, request
from typing import Any
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
    page: int = int(request.args.get("page", 1))
    if search is not None:
        contacts_set: list = Contact.search(search)
        if request.headers.get("HX-Trigger") == "search":
            return render_template("rows.html", contacts=contacts_set)
    else:
        contacts_set = Contact.all(page)
    return render_template("index.html", contacts=contacts_set, page=page)


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
    contact: Any | None = Contact.find(contact_id)
    return render_template("show.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["GET"])
def contacts_edit_get(contact_id: int = 0) -> str:
    contact: Any | None = Contact.find(contact_id)
    return render_template("edit.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["POST"])
def contacts_edit_post(contact_id: int = 0) -> response.Response | str:
    c: Any = Contact.find(contact_id)
    c.update(
        request.form["first_name"],
        request.form["last_name"],
        request.form["phone"],
        request.form["email"],
    )
    if c.save():
        flash("Updated Contact!")
        return redirect("/contacts/" + str(contact_id))
    else:
        return render_template("edit.html", contact=c)


@app.route("/contacts/<contact_id>/email", methods=["GET"])
def contacts_email_get(contact_id=0) -> response.Response | str:
    c: Any = Contact.find(contact_id)
    c.email = request.args.get("email")
    c.validate()
    return c.errors.get("email") or ""


@app.route("/contacts/<contact_id>", methods=["DELETE"])
def contacts_delete(contact_id: int = 0) -> response.Response:
    contact: Any | None = Contact.find(contact_id)
    if contact is not None:
        contact.delete()
    flash("Deleted Contact!")
    return redirect("/contacts", 303)


if __name__ == "__main__":
    app.run(port=5033)
