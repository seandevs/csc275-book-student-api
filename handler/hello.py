from flask_restful import Resource

from presenter.hello import HelloView

class HelloWorldHandler(Resource):
    def get(self):
        return HelloView().json()
