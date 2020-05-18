from bottle import HTTPResponse

import datetime
import json


class Response:

    def __init__(self, status=500):
        if type(status) is not int:
            raise ValueError('Invalid status type')
        self._body = None
        self._headers = {
            'Access-Control-Allow-Headers': 'Accept, Accept-Type, Authorization, Content-Type, Origin, X-CSRF-Token, '
                                            'X-Requested-With',
            'Access-Control-Allow-Methods': 'DELETE, GET, OPTIONS, POST, PUT',
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        }
        self._status = status

    def binary(self, data):
        self._body = data
        return self

    def body(self, data):
        _content = data
        if isinstance(_content, dict):
            self._body = json.dumps(_content, default=self.date_converter)
        elif isinstance(_content, list):
            content_json = [vars(d) for d in _content]
            self._body = json.dumps(content_json)
        else:
            self._body = json.dumps(vars(_content), default=str, use_decimal=True)
        return self

    def build(self):
        return HTTPResponse(body=self._body, headers=self._headers, status=self._status)

    def content_type(self, content_type):
        self._headers['Content-Type'] = content_type
        return self

    @staticmethod
    def date_converter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    def headers(self, custom_headers):
        self._headers = dict(**self._headers, **custom_headers)
        return self

    def raise_request(self):
        raise HTTPResponse(body=self._body, headers=self._headers, status=self._status)
