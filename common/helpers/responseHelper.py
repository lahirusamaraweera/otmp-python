from django.http import HttpResponse
from http import HTTPStatus
from authTokenHelper import authTokenHelper
import json

class responseHelper:

    headers = {
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Headers" : "*",
        "Access-Control-Allow-Methods" : "*",
    }
    content_type = 'text/plain'

    def __init__(self, content_type):
        self.content_type = content_type

    def setHeaders(self, headers):
        return
        self.headers = headers
    
    def setHeader(self, key, value):
        self.headers[key] = value

    def setContentType(self, type):
        self.content_type = type

    def success(self, message):
        return self.respond(200, message)

    def conflict(self, message):
        return self.respond(409, message)

    def unauthorized(self):
        return self.respond(403, 'You not allowed to acesss this resource')

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
    
    @staticmethod
    def isTokenInvalid(request){
        return authTokenHelper.validateToken(request)
    }



