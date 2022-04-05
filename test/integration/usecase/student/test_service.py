import unittest
from unittest.mock import MagicMock

from usecase.student.service import StudentService
from repository.student_in_mem import StudentInMem


class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.db_ = MagicMock()
        self.db_.students = {
                "abc": {
                    "name": "Maninder Bains",
                    "grad_year": 2020,
                    "major": "Computer Science"
                }
            }
        student_in_mem = StudentInMem(self.db_)
        self.student_service = StudentService(student_in_mem)

    def test_get_student_not_existant(self):
        self.assertRaises(
            Exception, self.student_service.get, "not_found_id"
        )

    def test_get_student_existant(self):
        student = self.student_service.get("abc")
        self.assertEqual(student.get("name"), "Maninder Bains")
        self.assertEqual(student.get("grad_year"), 2020)
        self.assertEqual(student.get("major"), "Computer Science")

    def test_create_student_successfully(self):
        student = self.student_service.create("Maninder Bains", 2020, "Computer Science")
        self.assertIsNotNone(student.id_)
        self.assertEqual(student.name, "Maninder Bains")
        self.assertEqual(student.grad_year, 2020)
        self.assertEqual(student.major, "Computer Science")

    def test_create_student_failed(self):
        fixture_data = (
            (
                {"name": None, "grad_year": 2020, "major": "Computer Science"},
                "Name must have a value",
            ),
            (
                {"name": "Maninder Bains", "grad_year": None, "major": "Computer Science"},
                "Grad Year must be an integer",
            ),
            (
                {"name": "Maninder Bains", "grad_year": "not_an_integer", "major": "Computer Science"},
                "Grad Year must be an integer",
            ),
            (
                {"name": "Maninder Bains", "grad_year": 1999, "major": "Computer Science"},
                "Grad Year must be > 2000",
            ),
            (
                {"name": "Maninder Bains", "grad_year": 2020, "major": None},
                "Major must have a value",
            ),
        )

        for context, expected in fixture_data:
            with self.assertRaises(Exception) as exception:
                name = context.get("name")
                grad_year = context.get("grad_year")
                major = context.get("major")
                self.student_service.create(name, grad_year, major)

            self.assertTrue(expected in str(exception.exception))

    def test_delete_student_non_existant(self):
        self.assertRaises(
            Exception, self.student_service.delete, "not_found_id"
        )

    def test_delete_student_existant(self):
        self.assertIn("abc", self.db_.students)
        self.student_service.delete("abc")
        self.assertNotIn("abc", self.db_.students)
