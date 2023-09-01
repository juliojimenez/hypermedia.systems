from app import app
from werkzeug.test import TestResponse


def test_index() -> None:
    response: TestResponse = app.test_client().get("/")
    assert response.status_code == 302
