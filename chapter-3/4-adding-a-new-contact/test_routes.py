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
