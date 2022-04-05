from entity.student import Student


class StudentInMem():
    def __init__(self, db_):
        self.db_ = db_

    def get(self, id_):
        try:
            return self.db_.students[id_]
        except Exception as e:  # pylint:disable=C0103
            raise e

    def create(self, student: Student):
        try:
            self.db_.students[student.id_] = {
                        "name": student.name,
                        "grad_year": student.grad_year,
                        "major": student.major
                    }
        except Exception as e:  # pylint:disable=C0103
            raise e

        return student

    def delete(self, id_):
        try:
            del self.db_.students[id_]
        except Exception as e:  # pylint:disable=C0103
            raise e
