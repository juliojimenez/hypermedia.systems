from app import app
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
