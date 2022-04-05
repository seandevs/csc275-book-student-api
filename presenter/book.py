from dataclasses import dataclass


@dataclass
class BookView:
    id_: str
    title: str
    author: str
    pages: int

    def json(self):
        return {
                'id': self.id_,
                'title': self.title,
                'author': self.author,
                'pages': self.pages
            }
