# Student / Book API
This is a basic API that has endpoints for Students and Books. This API is based off of a golang project at <https://github.com/eminetto/clean-architecture-go-v2>.

## General Architecture
The **handler** accepts a request and then calls the **usecase service** which calls the **entity** if creating a new object but ultimately calls the **repository** which calls the **db** eventually bubbling results back to the **handler** which presents the results (where appropriate) using the **presenter**.  

## Installation
```
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## Running
```
$ python api.py
```

### Calling Endpoints
#### Hello World
```
# Get
$ curl --request GET \
  --url http://localhost:5000/
```

#### Student
```
# Post
$ curl --request POST \
  --url http://localhost:5000/students \
  --header 'Content-Type: application/json' \
  --data '{"name": "Mike Jones", "grad_year": 2020, "major": "Computer Science"}'

# Get
$ curl --request GET \
  --url http://localhost:5000/students/{student_id}

# Delete
$ curl --request DELETE \
  --url http://localhost:5000/students/{student_id}
```

#### Book
```
# Post
$ curl --request POST \
  --url http://localhost:5000/books \
  --header 'Content-Type: application/json' \
  --data '{"title": "Python for Experts", "author": "Dev Nobody", "pages": 20}'

# Get
$ curl --request GET \
  --url http://localhost:5000/students/{book_id}

# Delete
$ curl --request DELETE \
  --url http://localhost:5000/books/{book_id}
```

## Running Tests
```
$ python -m unittest discover -s test
```
