from django.db import models
from common.baseModel import BaseModel
from common.helpers.passwordHelper import hash_password, verify_password

class user(models.Model, BaseModel):

    SKIPPED_ATTRIBTES = ['id', 'password_hash']

    firstname = models.CharField(max_length = 500)
    lastname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length = 500)
    phone = models.CharField(max_length=200)
    otp = models.CharField(max_length=10, null=True)
    password_hash = models.CharField(max_length=500)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=100, null=True)

    #virtual fields
    password = None
    password_again = None

    def toDic(self):
        return {
            "id" : self.id,
            "firstname" : self.firstname,
        }
    def save(self, *args, **kwargs):
        try :
            if(self.password is None):
                self.error_message = 'empty passwords'
                return False
            if(self.id is None ):
                self.password_hash = hash_password(self.password)
            return super(user, self).save(*args, **kwargs)
        except Exception as e:
            self.error_message = str(e)
            return False    

    def signup(self):
        if(self.password != self.password_again):
            self.error_message = 'passwords are not matching'
            return False
        if(False != user.getUserByEmail(self.email)):
            self.error_message = 'user already exists with this email'
            return False
        return self.save()
    
    def verifyPassword(self, password):
        return verify_password(self.password_hash, password)

    @staticmethod
    def getUserByEmail(email):
        try:
            return user.objects.get(email=email)
        except user.DoesNotExist:
            return False
        except user.MultipleObjectsReturned:
            return False

    @staticmethod 
    def getUserOnAuthenticate(email, password, passowrd_again):
        if( password != passowrd_again):
            return False
        filtered_user = user.getUserByEmail(email)
        if(False == filtered_user):
            return False
        if(False != filtered_user.verifyPassword(password)):
            return filtered_user
        return False
        