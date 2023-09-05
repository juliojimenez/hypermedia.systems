from app import app
import json
from typing import Any
from werkzeug.test import TestResponse


def get_last_contact_id() -> int:
    with open("contacts.json", "r") as contacts_file:
        contacts: Any = json.load(contacts_file)
        return contacts[-1]["id"]


def test_index() -> None:
    response: TestResponse = app.test_client().get("/")
    assert b"<sub-title>The Chapter 4 Demo</sub-title>" in response.data


def test_contacts_demo() -> None:
    response: TestResponse = app.test_client().get("/contacts-demo")
    assert response.data == b"You got contacts!"


def test_contacts_state() -> None:
    response: TestResponse = app.test_client().get("/contacts-state?state=NC")
    assert b"The state is NC" in response.data


def test_contacts_partial() -> None:
    response: TestResponse = app.test_client().get("/contacts-partial")
    assert (
        b"<th>First</th> <th>Last</th> <th>Phone</th> <th>Email</th>" in response.data
    )


def test_contacts_get() -> None:
    response: TestResponse = app.test_client().get("/contacts")
    assert b"<td>carson@example.comz</td>" in response.data


def test_contacts_post() -> None:
    response: TestResponse = app.test_client().post("/contacts", data={"q": "Gross"})
    assert b"<td>Gross</td>" in response.data
