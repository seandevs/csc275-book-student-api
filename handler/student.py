from flask_restful import Resource, reqparse, abort

from presenter.student import StudentView


class StudentHandler(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            'name',
            type=str,
            required=True,
            help='Name is required'
        )
    parser.add_argument(
            'grad_year',
            type=int,
            required=True,
            help='Grad Year is required'
        )
    parser.add_argument(
            'major',
            type=str,
            required=True,
            help='Major is required'
        )

    def __init__(self, **kwargs):
        self.service = kwargs['service']

    def get(self, student_id):
        try:
            student = self.service.get(student_id)
        except Exception:
            return 404

        student_view = StudentView(
                student_id,
                student.get("name"),
                student.get("grad_year"),
                student.get("major")
            )

        return student_view.json()

    def post(self):
        args = StudentHandler.parser.parse_args()

        try:
            student = self.service.create(
                    args.name,
                    args.grad_year,
                    args.major
                )
        except Exception:
            return 500

        student_view = StudentView(
                student.id_,
                student.name,
                student.grad_year,
                student.major
            )

        return student_view.json(), 201

    def delete(self, student_id):
        try:
            self.service.delete(student_id)
        except Exception:
            abort(404, message=f"Student {student_id} doesn't exist")

        return '', 200
