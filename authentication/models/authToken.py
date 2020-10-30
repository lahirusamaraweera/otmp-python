from django.db import models
from common.baseModel import BaseModel
import secrets
import datetime


class authToken(models.Model, BaseModel):

    AUTH_TOKEN_VALIDITY_DAYS = 1

    token = models.CharField(max_length=200)
    expire_date = models.DateTimeField()
    user = models.ForeignKey(
        'user',
        on_delete=models.PROTECT,
    )

    #virtual field
    token_raw = None

    def toDic(self):
        return {
            "id" : self.id,
            "token" : self.token,
            "expire_date" : self.expire_date,
            "user" : self.user.toDic()
        }
        
    @staticmethod
    def generateUserToken(target_user):
        new_token = authToken.findTokenByUser(target_user.id)
        if(False == new_token):
            new_token = authToken()
        token_raw = secrets.token_urlsafe(16)
        
        expiry_dt = datetime.datetime.today()
        expiry_dt = expiry_dt + datetime.timedelta(days=authToken.AUTH_TOKEN_VALIDITY_DAYS)

        new_token.token, new_token.token_raw = token_raw, token_raw
        new_token.expire_date = expiry_dt
        new_token.user_id = target_user.id
        new_token.save()
        return new_token

    @staticmethod
    def findTokenByUser(user_id):
        try:
            return authToken.objects.get(user_id=user_id)
        except authToken.DoesNotExist:
            return False
        except authToken.MultipleObjectsReturned:
            return False
    
    @staticmethod
    def validateToken(client_token):
        try:
            return authToken.objects.get(token=client_token)
        except authToken.DoesNotExist:
            return False
        except authToken.MultipleObjectsReturned:
            return False
