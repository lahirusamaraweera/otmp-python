from django.http import HttpResponse
from http import HTTPStatus
import json

class authTokenHelper:

    @staticmethod
    def validateToken(request):
        if not 'Authorization' in request.headers:
            return False
        
        token = request.headers['Authorization']
        is_valid_token = True
        return is_valid_token
        




