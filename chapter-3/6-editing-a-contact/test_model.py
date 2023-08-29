from contacts_model import Contact

Contact.load_db()


def test_contacts_all() -> None:
    assert Contact.all()[0].id == 2
    assert Contact.all()[0].first == "Carson"


def test_contacts_search() -> None:
    assert Contact.search("carson")[0].id == 2
    assert Contact.search("carson")[0].first == "Carson"


def test_contacts_validate_pass() -> None:
    c: Contact = Contact(None, "Jane", "Doe", "555-555-5555", "jane.doe@example.com")
    assert c.validate()


def test_contacts_validate_email_missing() -> None:
    c: Contact = Contact(None, "Jane", "Doe", "555-555-5555")
    assert not c.validate()


def test_contacts_validate_email_not_unique() -> None:
    c: Contact = Contact(None, "Jane", "Doe", "555-555-5555" "carson@example.comz")
    assert not c.validate()


def test_contacts_find() -> None:
    assert Contact.find(2)
    assert not Contact.find(200)
