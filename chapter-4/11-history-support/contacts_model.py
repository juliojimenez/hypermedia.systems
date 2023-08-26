from typing import Any
import json

PAGE_SIZE: int = 100


class Contact:
    db: dict = {}

    def __init__(
        self,
        id_=None,
        first=None,
        last=None,
        phone=None,
        email=None,
    ) -> None:
        self.id = id_
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.errors: dict = {}

    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)

    @classmethod
    def all(cls, page: int = 1) -> list:
        start: int = (page - 1) * PAGE_SIZE
        end: int = start + PAGE_SIZE
        return list(cls.db.values())[start:end]

    @classmethod
    def search(cls, text: str) -> list:
        result: list = []
        for c in cls.db.values():
            match_first: bool = c.first is not None and text in c.first
            match_last: bool = c.last is not None and text in c.last
            match_email: bool = c.email is not None and text in c.email
            match_phone: bool = c.phone is not None and text in c.phone
            if match_first or match_last or match_email or match_phone:
                result.append(c)
        return result

    @classmethod
    def load_db(cls) -> None:
        with open("contacts.json", "r") as contacts_file:
            contacts: Any = json.load(contacts_file)
            cls.db.clear()
            for c in contacts:
                cls.db[c["id"]] = Contact(
                    c["id"], c["first"], c["last"], c["phone"], c["email"]
                )
