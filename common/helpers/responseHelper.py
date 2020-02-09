from django.http import HttpResponse
from http import HTTPStatus
import json

class responseHelper:

    headers = {}
    content_type = 'text/plain'

    def __init__(self, content_type):
        self.content_type = content_type

    def setHeaders(self, headers):
        self.headers = headers

    def setContentType(self, type):
        self.content_type = type

    def success(self, message):
        return self.respond(200, message)

    def conflict(self, message):
        return self.respond(409, message)

    def respond(self, status_code, content):
        response = HttpResponse(content_type=self.content_type)
        if('application/json' == self.content_type):
            response.content = json.dumps(content)
        else:
            response.content = content
        response.status_code = status_code
        if(bool(self.headers)):
            for key, value in self.headers.items():
                response[key] = value
        
        return response



