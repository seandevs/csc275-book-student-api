from flask import Flask
from flask_restful import Api, Resource

from handler.book import BookHandler
from handler.student import StudentHandler
from handler.hello import HelloWorldHandler
from usecase.book.service import BookService
from usecase.student.service import StudentService
from repository.book_in_mem import BookInMem
from repository.student_in_mem import StudentInMem
from db.in_memory import InMemory

app = Flask(__name__)
api = Api(app)

# instantiate a database
db = InMemory()
app.db = db

"""
Instantiate Books
"""
# instantiate book repository
book_in_mem = BookInMem(db)

# instantiate book service
book_service = BookService(book_in_mem)

"""
Instantiate Students
"""
# instantiate student repository
student_in_mem = StudentInMem(db)

# instantiate student service
student_service = StudentService(student_in_mem)

"""
API Endpoints
"""
# api endpoints
api.add_resource(
        BookHandler,
        '/books',
        '/books/<string:book_id>',
        resource_class_kwargs={'service': book_service}
    )

api.add_resource(
        StudentHandler,
        '/students',
        '/students/<string:student_id>',
        resource_class_kwargs={'service': student_service}
    )

api.add_resource(HelloWorldHandler, '/')


if __name__ == '__main__':
    app.run(debug=True)
