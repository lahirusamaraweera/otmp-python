from django.db import models
from common.baseModel import BaseModel

class item(models.Model, BaseModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length = 500)
    item_code = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.CharField(max_length=10)

    def toDic(self):
        return {
            "name" : self.name,
            "price" : float(self.price),
            "currency" : self.currency,
            "description" : self.description
        }