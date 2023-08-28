from app import app
from werkzeug.test import TestResponse


def test_request_example():
    response: TestResponse = app.test_client().get("/")
    assert response.data == b"Hello World!"
