from http import HTTPStatus
from flask import make_response

def ok(data):
    return make_response(data), HTTPStatus.OK.value

def badRequest(data):
    return make_response(data), HTTPStatus.BAD_REQUEST.value
