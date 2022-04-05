import unittest
from unittest.mock import MagicMock

from usecase.book.service import BookService
from repository.book_in_mem import BookInMem


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.db_ = MagicMock()
        self.db_.books = {
                "abc": {
                    "title": "Python for Experts",
                    "author": "Raya Johnson",
                    "pages": 20
                }
            }
        book_in_mem = BookInMem(self.db_)
        self.book_service = BookService(book_in_mem)

    def test_get_book_not_existant(self):
        self.assertRaises(
            Exception, self.book_service.get, "not_found_id"
        )

    def test_get_book_existant(self):
        book = self.book_service.get("abc")
        self.assertEqual(book.get("title"), "Python for Experts")
        self.assertEqual(book.get("author"), "Raya Johnson")
        self.assertEqual(book.get("pages"), 20)

    def test_create_book_successfully(self):
        book = self.book_service.create("Python for Experts", "Raya Johnson", 20)
        self.assertIsNotNone(book.id_)
        self.assertEqual(book.title, "Python for Experts")
        self.assertEqual(book.author, "Raya Johnson")
        self.assertEqual(book.pages, 20)

    def test_create_book_failed(self):
        fixture_data = (
            (
                {"title": None, "author": "Raya Johnson", "pages": 20},
                "Title must have a value",
            ),
            (
                {"title": "Python for Experts", "author": None, "pages": 20},
                "Author must have a value",
            ),
            (
                {"title": "Python for Experts", "author": "Raya Johnson", "pages": "not_an_int"},
                "Pages must be an integer",
            ),
            (
                {"title": "Python for Experts", "author": "Raya Johnson", "pages": None},
                "Pages must be an integer",
            ),
            (
                {"title": "Python for Experts", "author": "Raya Johnson", "pages": 0},
                "Pages must be > 1",
            ),
        )

        for context, expected in fixture_data:
            with self.assertRaises(Exception) as exception:
                title = context.get("title")
                author = context.get("author")
                pages = context.get("pages")
                self.book_service.create(title, author, pages)

            self.assertTrue(expected in str(exception.exception))

    def test_delete_book_non_existant(self):
        self.assertRaises(
            Exception, self.book_service.delete, "not_found_id"
        )

    def test_delete_book_existant(self):
        self.assertIn("abc", self.db_.books)
        self.book_service.delete("abc")
        self.assertNotIn("abc", self.db_.books)
