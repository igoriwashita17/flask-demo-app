from marshmallow import Schema, fields
from flask import Request


class Validators:
    class GetAddressValidator(Schema):
        cep = fields.String(required=True)

    @staticmethod
    def validateParams(schema: Schema, request: Request):
        schema(many=False).load(request.args.to_dict())
        return request.args.to_dict()

    @staticmethod
    def validateBody(schema: Schema, request: Request):
        schema(many=False).load(request.data)
        return request.data
