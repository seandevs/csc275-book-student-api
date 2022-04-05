from dataclasses import dataclass


@dataclass
class StudentView:
    id_: str
    name: str
    grad_year: int
    major: str

    def json(self):
        return {
                'id': self.id_,
                'name': self.name,
                'grad_year': self.grad_year,
                'major': self.major
            }
