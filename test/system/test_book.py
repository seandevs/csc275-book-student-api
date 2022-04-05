import unittest
import json

from api import app


class TestBook(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.fixture_data = (
            (
                {"title": None, "author": "Raya Johnson", "pages": 20},
                {"message": "Title is required", "status": 400},
            ),
            (
                {"title": "Python for Experts", "author": None, "pages": 20},
                {"message": "Author is required", "status": 400},
            ),
            (
                {"title": "Python for Experts", "author": "Raya Johnson", "pages": "not_an_int"},
                {"message": "Pages is required", "status" :400},
            ),
            (
                {"title": "Python for Experts", "author": "Raya Johnson", "pages": None},
                {"message": "Pages is required", "status": 400},
            ),
            (
                {"title": "Python for Experts", "author": "Raya Johnson", "pages": 0},
                {"message": "Param is missing", "status": 400},
            ),
        )

    def test_create_book_failed(self):
        for context, expected in self.fixture_data:
            res = self.app.post("/books", data=context)
            data = json.loads(res.data)
            self.assertIn(expected.get("message"), str(data.get("message")))
            self.assertEqual(res.status_code, expected.get("status"))

    def test_create_book_successfully(self):
        res = self.app.post(
                "/books",
                data={
                    "title": "Python for Experts",
                    "author": "Raya Johnson",
                    "pages": 20
                }
            )

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertIsNotNone(data.get("id"))
        self.assertEqual(data.get("title"), "Python for Experts")
        self.assertEqual(data.get("author"), "Raya Johnson")
        self.assertEqual(data.get("pages"), 20)

    def test_book_not_existant(self):
        res = self.app.get("/books/1234")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data.get("message"), "Book 1234 doesn't exist")

    def test_book_existant(self):
        app.db.books["abc"] = {
                "title": "Python for Experts",
                "author": "Raya Johnson",
                "pages": 20
            }

        res = self.app.get("/books/abc")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data.get("id"), "abc")
        self.assertEqual(data.get("title"), "Python for Experts")
        self.assertEqual(data.get("author"), "Raya Johnson")
        self.assertEqual(data.get("pages"), 20)

    def test_delete_book_non_existant(self):
        res = self.app.delete("/books/1234")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data.get("message"), "Book 1234 doesn't exist")

    def test_delete_book_existant(self):
        app.db.books["abc"] = {
                "title": "Python for Experts",
                "author": "Raya Johnson",
                "pages": 20
            }

        res = self.app.delete("/books/abc")
        self.assertEqual(res.status_code, 200)
