import unittest
import json

from api import app


class TestBook(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_book_not_existant(self):
        res = self.app.get("/")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data.get("hello"), "world")
