import uuid


class Student():
    def __init__(self, id_, name, grad_year, major):
        self._id = id_
        self.name = name
        self.grad_year = grad_year
        self.major = major

    @property
    def id_(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            raise TypeError("Name must have a value")
        self._name = value

    @property
    def grad_year(self):
        return self._grad_year

    @grad_year.setter
    def grad_year(self, value):
        if not isinstance(value, int):
            raise TypeError("Grad Year must be an integer")
        if value < 2000:
            raise ValueError("Grad Year must be > 2000")
        self._grad_year = value

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        if value is None:
            raise TypeError("Major must have a value")
        self._major = value

    @classmethod
    def new_enrollment(cls, name, grad_year, major):
        id_ = str(uuid.uuid4())
        return cls(id_, name, grad_year, major)
