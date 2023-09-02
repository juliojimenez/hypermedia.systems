from contacts_model import Contact
from typing import Any

Contact.load_db()


def test_contacts_all() -> None:
    assert Contact.all()[0].id == 2
    assert Contact.all()[0].first == "Carson"


def test_contacts_search() -> None:
    assert Contact.search("carson")[0].id == 2
    assert Contact.search("carson")[0].first == "Carson"
