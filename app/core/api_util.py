from json import dumps
from flask import Response


def create_json_response(response, status=200):
    response = Response(response=dumps(response), status=status, mimetype='application/json')
    return response


def unauthorized():
    return 'Unauthorized', 401


def forbidden():
    return 'Forbidden', 403


def not_found():
    return 'Not Found', 404


def ok():
    return 'OK', 200