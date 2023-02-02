from flask import request

from app import app
from base.request import RequestHandler
from v1.adapter import Adapter
from v1.schema import Validators

a = Adapter()
req_handler = RequestHandler()


@app.route("/address", methods=['GET'])
def getAddress():
    try:
        payload = Validators.validateParams(Validators.GetAddressValidator, request)
        return req_handler.build_success_response(a.getAddress(payload))
    except Exception as e:
        return req_handler.build_error_response(e)

