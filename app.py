from flask import Flask
from flask_restful import Api
from Response import TestResponse

app = Flask(__name__)
api = Api(app)
api.add_resource(TestResponse, '/test')
if __name__ == "__main__":
    # start up api
    app.run(port=5000, debug=True)
