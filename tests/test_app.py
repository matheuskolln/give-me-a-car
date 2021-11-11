from unittest.case import TestCase
from app import app
import json


class TestApp(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_server_is_up(self):
        response = self.app.get("/")

        assert json.loads(response.data).get("car") is not None
        assert response.status_code == 200
