from json import dumps
from flask import Response


def create_json_response(response, status=200):
    response = Response(response=dumps(response), status=status, mimetype='application/json')
    return response