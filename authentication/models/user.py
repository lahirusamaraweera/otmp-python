from django.db import models
from common.baseModel import BaseModel
from common.helpers.passwordHelper import hash_password, verify_password

class user(models.Model, BaseModel):
    firstname = models.CharField(max_length = 500)
    lastname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length = 500)
    phone = models.CharField(max_length=200)
    otp = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=200)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=100, null=True)

    raw_password = None

    def toDic(self):
        return {
            "id" : self.id,
            "firstname" : self.firstname,
        }
    def save(self, *args, **kwargs):
        if(self.id is None ):
            self.password = hash_password(self.raw_password)
        return super(user, self).save(*args, **kwargs)
    
    def verifyPassword(self, password):
        return verify_password(self.password, password)

    @staticmethod
    def getUserByEmail(email):
        try:
            user = user.objects.get(email=email)
        except Employee.DoesNotExist:
            return False
        except Employee.MultipleObjectsReturned:
            return False

    @staticmethod 
    def verifyUser(email, password, passowrd_again):
        if( password != passowrd_again):
            return False
        filtered_user = user.getUserByEmail(email)
        if(False == filtered_user):
            return False
        return filtered_user.verifyPassword(password)
        