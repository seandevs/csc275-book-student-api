from entity.book import Book


class BookInMem():
    def __init__(self, db_):
        self.db_ = db_

    def get(self, id_):
        try:
            return self.db_.books[id_]
        except Exception as e:  # pylint:disable=C0103
            raise e

    def create(self, book: Book):
        try:
            self.db_.books[book.id_] = {
                    "title": book.title,
                    "author": book.author,
                    "pages": book.pages
                }
        except Exception as e:  # pylint:disable=C0103
            raise e

        return book

    def delete(self, id_):
        try:
            del self.db_.books[id_]
        except Exception as e:  # pylint:disable=C0103
            raise e
