from http import HTTPStatus
from json import dumps as jsonstring
from flask import Response
from marshmallow import ValidationError

from base.model.ResponseData import ResponseData


class RequestHandler:
    def __init__(self):
        self.http_status = HTTPStatus

    def build_success_response(self, data, http_status: HTTPStatus = HTTPStatus.OK):
        data = ResponseData(data, 'Sucesso', http_status.value).__dict__

        resp = Response()

        resp.data = jsonstring(data)
        resp.status_code = http_status.value
        resp.mimetype = 'application/json'

        return resp

    def build_error_response(self, e: Exception, http_status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR):
        resp = Response()

        if isinstance(e, ValidationError):
            data = ResponseData(None, str(e), HTTPStatus.BAD_REQUEST.value).__dict__
            resp.data = jsonstring(data)
            resp.status_code = HTTPStatus.BAD_REQUEST.value
        else:
            data = ResponseData(None, 'Ocorreu um erro ao processar sua solicitação', http_status.value).__dict__
            resp.data = jsonstring(data)
            resp.status_code = http_status.value
        resp.mimetype = 'application/json'

        print(e)

        return resp
