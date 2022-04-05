import uuid


class Book():
    def __init__(self, id_, title, author, pages):
        self._id = id_
        self.title = title
        self.author = author
        self.pages = pages

    @property
    def id_(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value is None:
            raise TypeError("Title must have a value")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if value is None:
            raise TypeError("Author must have a value")
        self._author = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Pages must be an integer")
        if value < 1:
            raise ValueError("Pages must be > 1")
        self._pages = value

    @classmethod
    def new_edition(cls, title, author, pages):
        id_ = str(uuid.uuid4())
        return cls(id_, title, author, pages)
