from django.db import models
from common.baseModel import BaseModel

class authToken(models.Model, BaseModel):
    token = models.CharField(max_length=200)
    expire_date = models.DateField()
    user = models.ForeignKey(
        'user',
        on_delete=models.PROTECT,
    )

    def toDic(self):
        return {
            "id" : self.id,
            "token" : self.token,
            "expire_date" : self.expire_date,
            "user" : self.user.toDic()
        }