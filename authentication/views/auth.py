from authentication.models.user import user
from authentication.models.authToken import authToken 
from common.helpers.responseHelper import responseHelper
from common.helpers.validationHelper import validateStructure
import json

def handleLogin(request):
    
    if( ("POST" != request.method ) or ( not request.body ) or ('' == request.body)):
        return responseHelper.getUnauthorizedResponse()

    payload = json.loads(request.body)
    if( not validateStructure(payload,["email","password","password_again"])):
        return responseHelper.getUnauthorizedResponse()


def handleSignup(request):
    if("POST" != request.method):
        return responseHelper.getUnauthorizedResponse()
    payload = json.loads(request.body)
    return responseHelper.getUnauthorizedResponse()