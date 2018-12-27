import sys
import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)



class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


class Serve(Resource):

    def get(self):

        return "Hello Service!"

    def post(self):

        if 'data' in request.json.keys():
            print(request.json['data'])
        else:
            raise InvalidUsage("Invalid format. No data given")


api.add_resource(Serve, '/v1/serve')

if __name__ == "__main__":
    # Only for debugging while developing
    print("Server is running ...")
    app.run(host='0.0.0.0', debug=True, port=5000)
