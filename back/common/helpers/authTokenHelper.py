from django.http import HttpResponse
from http import HTTPStatus
import json
from authentication.models.authToken import authToken

class authTokenHelper:

    @staticmethod
    def validateToken(request, user_id = None ):
        if ( not 'Authorization' in request.headers ):
            return False
        
        token = request.headers['Authorization']
        existing_token = authToken.validateToken(token)
        if(False == existing_token):
            return False

        is_valid_token = True
        if(not user_id is None):
            is_valid_token =  existing_token.user_id == user_id
        return is_valid_token
        

    @staticmethod
    def getUserIdFromToken(request):
        if ( not 'Authorization' in request.headers ):
            return False
        
        token = request.headers['Authorization']
        existing_token = authToken.validateToken(token)
        if(False == existing_token):
            return False

        return existing_token.user_id



