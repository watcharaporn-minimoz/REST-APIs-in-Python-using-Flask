from flask_restful import Resource, request
import json

class TestResponse(Resource):
    def post(self):
        req_data = request.get_json()
        req_json = json.dumps(req_data)
        return json.loads(req_json)