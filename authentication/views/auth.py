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

    existing_user = user.getUserOnAuthenticate(payload['email'], payload['password'], payload['password_again'])
    if ( False == existing_user ):
        return responseHelper.getUnauthorizedResponse()

def handleSignup(request):
    if("POST" != request.method):
        return responseHelper.getUnauthorizedResponse()

    payload = json.loads(request.body)
    if( not validateStructure(payload,["email","password","password_again"])):
        return responseHelper.conflict("Invalid payload")
    
    user_model = user()
    user_model.setAll(payload)
    if(False ==  user_model.signup()):
        return responseHelper.getConflictResponse(user_model.error_message)
    return responseHelper.getSuccessResponse(user_model.toDic())