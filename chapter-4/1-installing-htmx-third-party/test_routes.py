from app import app
import json
from typing import Any
from werkzeug.test import TestResponse


def get_last_contact_id() -> int:
    with open("contacts.json", "r") as contacts_file:
        contacts: Any = json.load(contacts_file)
        sorted_contacts: Any = sorted(contacts, key=lambda x: x["id"])
        return sorted_contacts[-1]["id"]


def test_index() -> None:
    response: TestResponse = app.test_client().get("/")
    assert b"<sub-title>The Chapter 4 Demo</sub-title>" in response.data
