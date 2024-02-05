import json
from operator import attrgetter
from random import random
from threading import Thread
import time
from typing import Any


PAGE_SIZE: int = 10


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

    def update(self, first: str, last: str, phone: str, email: str) -> None:
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def validate(self) -> bool:
        if not self.email:
            self.errors["email"] = "Email Required"
        existing_contact = next(
            filter(
                lambda c: c.id != self.id and c.email == self.email, Contact.db.values()
            ),
            None,
        )
        if existing_contact:
            self.errors["email"] = "Email Must Be Unique"
        return len(self.errors) == 0

    def save(self) -> bool:
        if not self.validate():
            return False
        if self.id is None:
            if len(Contact.db) == 0:
                max_id: int = 1
            else:
                max_id = max(contact.id for contact in Contact.db.values())
            self.id = max_id + 1
            Contact.db[self.id] = self
        Contact.save_db()
        return True

    def delete(self) -> bool:
        del Contact.db[self.id]
        Contact.save_db()
        return True

    @classmethod
    def count(cls) -> int:
        time.sleep(2)
        return len(cls.db)

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

    @staticmethod
    def save_db() -> None:
        out_arr: list = [c.__dict__ for c in Contact.db.values()]
        with open("contacts.json", "w") as f:
            json.dump(out_arr, f, indent=2)

    @classmethod
    def find(cls, id_: int) -> Any | None:
        id_ = int(id_)
        c: Any | None = cls.db.get(id_)
        if c is not None:
            c.errors = {}
        return c


class Archiver:
    archive_status: str = "Waiting"
    archive_progress: float = 0
    thread: Thread | None = None

    def status(self) -> str:
        return Archiver.archive_status

    def progress(self) -> float:
        return Archiver.archive_progress

    def run(self) -> None:
        if Archiver.archive_status == "Waiting":
            Archiver.archive_status = "Running"
            Archiver.archive_progress = 0
            Archiver.thread = Thread(target=self.run_impl)
            Archiver.thread.start()

    def run_impl(self) -> None:
        for i in range(10):
            time.sleep(1 * random())
            if Archiver.archive_status != "Running":
                return
            Archiver.archive_progress = (i + 1) / 10
            print("Here... " + str(Archiver.archive_progress))
        time.sleep(1)
        if Archiver.archive_status != "Running":
            return
        Archiver.archive_status = "Complete"

    def archive_file(self) -> str:
        return "contacts.json"

    def reset(self) -> None:
        Archiver.archive_status = "Waiting"

    @classmethod
    def get(cls):
        return Archiver()
