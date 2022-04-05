from entity.student import Student


class StudentService():
    def __init__(self, repository):
        self.repository = repository

    def get(self, id_):
        try:
            return self.repository.get(id_)
        except Exception as e:  # pylint:disable=C0103
            raise e

    def create(self, name, grad_year, major):
        try:
            student = Student.new_enrollment(name, grad_year, major)
            new_student = self.repository.create(student)
        except Exception as e:  # pylint:disable=C0103
            raise e

        return new_student

    def delete(self, id_):
        try:
            self.get(id_)
            self.repository.delete(id_)
        except Exception as e:  # pylint:disable=C0103
            raise e
