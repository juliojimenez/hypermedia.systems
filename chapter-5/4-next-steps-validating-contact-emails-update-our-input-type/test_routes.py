from app import app
import uuid
from werkzeug.test import TestResponse


def test_index() -> None:
    response: TestResponse = app.test_client().get("/")
    assert response.status_code == 302


def test_contacts_all() -> None:
    response: TestResponse = app.test_client().get("/contacts")
    assert b"<td>Carson</td>" in response.data


def test_contacts_search() -> None:
    response: TestResponse = app.test_client().get("/contacts?q=carson")
    assert b"<td>Carson</td>" in response.data


def test_contacts_new_get() -> None:
    response: TestResponse = app.test_client().get("/contacts/new")
    assert b"<legend>Contact Values</legend>" in response.data


def test_contacts_new_post() -> None:
    response: TestResponse = app.test_client().post(
        "/contacts/new",
        data={
            "first_name": "Test",
            "last_name": "Contact",
            "phone": "555-555-5555",
            "email": f"{str(uuid.uuid4())[:8]}@example.com",
        },
    )
    assert response.status_code == 302


def test_contacts_view() -> None:
    response: TestResponse = app.test_client().get("/contacts/2")
    assert b"<h1>Carson Gross</h1>" in response.data


def test_contact_view_not_exist() -> None:
    response: TestResponse = app.test_client().get("/contacts/200")
    assert b"<h1> </h1>" in response.data


def test_contacts_edit() -> None:
    response: TestResponse = app.test_client().get("/contacts/2/edit")
    assert (
        b'<input name="email" id="email" type="email" placeholder="Email" value="carson@example.comz">'
        in response.data
    )


def test_contacts_edit_not_exists() -> None:
    response: TestResponse = app.test_client().get("/contacts/200/edit")
    assert response.status_code == 500


def test_contacts_edit_post() -> None:
    response: TestResponse = app.test_client().post(
        "/contacts/20/edit",
        data={
            "first_name": "Test",
            "last_name": "Contact",
            "phone": "666-666-6666",
            "email": f"{str(uuid.uuid4())[:8]}@example.com",
        },
    )
    assert response.status_code == 302


def test_contacts_delete_post() -> None:
    response: TestResponse = app.test_client().delete("/contacts/21")
    assert response.status_code == 303
