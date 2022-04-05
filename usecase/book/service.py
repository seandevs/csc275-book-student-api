from entity.book import Book


class BookService():
    def __init__(self, repository):
        self.repository = repository

    def get(self, id_):
        try:
            return self.repository.get(id_)
        except Exception as e:  # pylint:disable=C0103
            raise e

    def create(self, title, author, pages):
        try:
            book = Book.new_edition(title, author, pages)
            new_book = self.repository.create(book)
        except Exception as e:  # pylint:disable=C0103
            raise e

        return new_book

    def delete(self, id_):
        try:
            self.get(id_)
            self.repository.delete(id_)
        except Exception as e:  # pylint:disable=C0103
            raise e
