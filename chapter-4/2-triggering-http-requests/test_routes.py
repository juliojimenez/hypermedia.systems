from app import app
from werkzeug.test import TestResponse


def test_index() -> None:
    response: TestResponse = app.test_client().get("/")
    assert b"<sub-title>The Chapter 4 Demo</sub-title>" in response.data


def test_contacts_demo() -> None:
    response: TestResponse = app.test_client().get("/contacts-demo")
    assert response.data == b"You got contacts!"
