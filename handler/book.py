from flask_restful import Resource, reqparse, abort

from presenter.book import BookView


class BookHandler(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            'title',
            type=str,
            required=True,
            help='Title is required'
        )
    parser.add_argument(
            'author',
            type=str,
            required=True,
            help='Author is required'
        )
    parser.add_argument(
            'pages',
            type=int,
            required=True,
            help='Pages is required'
        )

    def __init__(self, **kwargs):
        self.service = kwargs['service']

    def get(self, book_id):
        try:
            book = self.service.get(book_id)
        except Exception:
            abort(404, message=f"Book {book_id} doesn't exist")

        book_view = BookView(
                book_id,
                book.get("title"),
                book.get("author"),
                book.get("pages")
            )

        return book_view.json()

    def post(self):
        args = BookHandler.parser.parse_args()

        try:
            book = self.service.create(args.title, args.author, args.pages)
        except Exception:
            abort(400, message="Param is missing")

        book_view = BookView(
                book.id_,
                book.title,
                book.author,
                book.pages
            )

        return book_view.json(), 201

    def delete(self, book_id):
        try:
            self.service.delete(book_id)
        except Exception:
            abort(404, message=f"Book {book_id} doesn't exist")

        return '', 200
